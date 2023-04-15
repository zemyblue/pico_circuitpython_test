import os
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

# Setup the file as the bitmap data source
# `OnDiskBitmap` source the bitmap image directly from flash memory storage. So slow.
# bitmap = displayio.OnDiskBitmap("/purple.bmp")
bitmap, palette = adafruit_imageload.load("/purple.bmp", bitmap=displayio.Bitmap, palette=displayio.Palette)

# Create a TileGrid to hold the bitmap
tile_grid = displayio.TileGrid(bitmap, pixel_shader=palette)

# Create a Group to hold the TileGrid
group = displayio.Group()

# Add the TileGrid to the Group
group.append(tile_grid)

# Add the Group to the Display
display.show(group)

while True:
    pass
