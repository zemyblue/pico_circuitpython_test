import time
import board
import mfrc522

from decode_TLV import parseTLVBlocks
from decode_ndef import decode_ndef

'''
VCC  - 3V3
RST  - GP22
GND  - GND
IRQ  - x
MISO - GP4
MOSI - GP7
SCK  - GP6
SDA  - GP5
'''

nfc_rst = board.GP22
nfc_miso = board.GP4
nfc_mosi = board.GP7
nfc_sck = board.GP6
nfc_sda = board.GP5 # cs


rfid = mfrc522.MFRC522(sck=nfc_sck, 
                       mosi=nfc_mosi, 
                       miso=nfc_miso, 
                       rst=nfc_rst, 
                       cs=nfc_sda)
rfid.set_antenna_gain(0x07 << 4)

print("*** Scan RFid tag/card ***\n")

prev_data = ""
prev_time = 0
timeout = 1

while True:
    (status, tag_type) = rfid.request(rfid.REQALL)
    if status == rfid.OK:
        (status, raw_uid) = rfid.anticoll()
        # (status, raw_uid) = rfid.select_tag
        if status == rfid.OK:
            rfid_data = "{:02x}{:02x}{:02x}{:02x}".format(raw_uid[0], raw_uid[1], raw_uid[2], raw_uid[3])

            if rfid_data != prev_data:
                prev_data = rfid_data

                print("Card detected! UID: {}".format(rfid_data))

                # check If Mifare1K or Mifare ultralight
                static_block = rfid.read(0)
                if static_block != None:
                    ccs = static_block[-4:]
                    # get NFC data memory size
                    num_block = ccs[2] / 2
                    print("numBlock:%d" % num_block)

                    # load data blocks
                    datas = []
                    for i in range(1, num_block):
                        data_block = rfid.read(i * 4)
                        if status != None:
                            datas += data_block
                        else:
                            print("Failed to read data block[%d]" % i)
                            break

                    if len(datas) < (num_block - 1) * 8:
                        print("Failed to read all datas.")
                        break

                    # parse TLV block
                    nfc_blocks = parseTLVBlocks(datas)
                    if nfc_blocks != None:
                        for type, value in nfc_blocks:
                            if type == 0x03:    # if NDEF
                                ndef_value = decode_ndef(value)
                                if ndef_value != None:
                                    print("NDEF value: %s" % ndef_value)
                                else:
                                    print(ndef_value)
            # else:
            #     prev_data = ""

            prev_time = time.monotonic()

    else:
        if time.monotonic() - prev_time > timeout:
            prev_data = ""
