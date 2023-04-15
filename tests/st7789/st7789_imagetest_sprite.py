import os
import time
import board
import displayio
from adafruit_st7789 import ST7789
import adafruit_imageload

import busio

print("==============================")
print(os.uname())
print("Hello Raspberry Pi Pico/CircuitPython ST7789 SPI IPS Display")
print()

# Release any resources currently in use for the displays
displayio.release_displays()

tft_cs = board.GP1
tft_dc = board.GP0
tft_res = board.GP4
spi_sda_mosi = board.GP3
spi_scl_clk = board.GP2

spi = busio.SPI(spi_scl_clk, MOSI=spi_sda_mosi)

display_bus = displayio.FourWire(
    spi, command=tft_dc, chip_select=tft_cs, reset=tft_res
)

display = ST7789(display_bus, width=280, height=240, rowstart=20, rotation=270)

# Load the sprite sheet (bitmap)
sprite_sheet, palette = adafruit_imageload.load("/cp_sprite_sheet.bmp", 
                                          bitmap=displayio.Bitmap, 
                                          palette=displayio.Palette)

# Create a sprite (tilegrid)
sprite = displayio.TileGrid(sprite_sheet, pixel_shader=palette, 
                               width = 1, 
                               height = 1, 
                               tile_width = 16, 
                               tile_height = 16)

# Create a Group to hold the sprite
group = displayio.Group(scale = 10)

# Add the TileGrid to the Group
group.append(sprite)

# Add the Group to the Display
display.show(group)

# Set sprite location
group.x = 60
group.y = 40

# Loop through each sprite in the sprite sheet
source_index = 0
while True:
    sprite[0] = source_index % 6
    source_index += 1
    time.sleep(2)

