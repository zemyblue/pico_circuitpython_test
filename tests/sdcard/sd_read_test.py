import os
import busio
import digitalio
import board
import storage
import adafruit_sdcard

sd_miso = board.GP12
sd_mosi = board.GP11
sd_sck = board.GP10
sd_cs = board.GP13

# Connect to the card and mount the filesystem.
# spi = busio.SPI(board.SCK, board.MOSI, board.MISO)
spi = busio.SPI(sd_sck, MOSI=sd_mosi, MISO=sd_miso)
cs = digitalio.DigitalInOut(sd_cs)
sdcard = adafruit_sdcard.SDCard(spi, cs)
vfs = storage.VfsFat(sdcard)
storage.mount(vfs, "/sd")

print(os.listdir("/sd/sounds"))
