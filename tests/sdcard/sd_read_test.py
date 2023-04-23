import os
import busio
import board
import sdcardio
import storage

sd_miso = board.GP12
sd_mosi = board.GP11
sd_sck = board.GP10
sd_cs = board.GP13

# Connect to the card and mount the filesystem.
spi = busio.SPI(sd_sck, MOSI=sd_mosi, MISO=sd_miso)
# RP2040 doesn't need adafruit_sdcard
# cs = digitalio.DigitalInOut(sd_cs)
# sdcard = adafruit_sdcard.SDCard(spi, cs)
sdcard = sdcardio.SDCard(spi, sd_cs)
vfs = storage.VfsFat(sdcard)
storage.mount(vfs, "/sd")

print(os.listdir("/sd/sounds"))
