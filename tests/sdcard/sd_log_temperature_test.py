# SPDX-FileCopyrightText: 2017 Limor Fried for Adafruit Industries
#
# SPDX-License-Identifier: MIT

import time

import adafruit_sdcard
import board
import busio
import digitalio
import microcontroller
import storage

# Use any pin that is not taken by SPI
sd_miso = board.GP12
sd_mosi = board.GP11
sd_sck = board.GP10
sd_cs = board.GP13

led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

# Connect to the card and mount the filesystem.
spi = busio.SPI(sd_sck, MOSI=sd_mosi, MISO=sd_miso)
cs = digitalio.DigitalInOut(sd_cs)
sdcard = adafruit_sdcard.SDCard(spi, cs)
vfs = storage.VfsFat(sdcard)
storage.mount(vfs, "/sd")

# Use the filesystem as normal! Our files are under /sd

print("Logging temperature to filesystem")
# append to the file!
while True:
    # open file for append
    with open("/sd/temperature.txt", "a") as f:
        led.value = True  # turn on LED to indicate we're writing to the file
        t = microcontroller.cpu.temperature
        print("Temperature = %0.1f" % t)
        f.write("%0.1f\n" % t)
        led.value = False  # turn off LED to indicate we're done
    # file is saved
    time.sleep(1)
