import time
import board
import mfrc522

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
        if status == rfid.OK:
            rfid_data = "{:02x}{:02x}{:02x}{:02x}".format(raw_uid[0], raw_uid[1], raw_uid[2], raw_uid[3])

            if rfid_data != prev_data:
                prev_data = rfid_data

                print("Card detected! UID: {}".format(rfid_data))
            prev_time = time.monotonic()

    else:
        if time.monotonic() - prev_time > timeout:
            prev_data = ""
