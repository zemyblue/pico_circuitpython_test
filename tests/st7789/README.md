# ST7789 test

This test use 1.69 inch(280x240) TFT display.
You need to download [circuitpython libraries](https://circuitpython.org/libraries) and unzip for testing.

**Connected Pins**
```
3v3 - BLK (blacklight, always on)
GP1 - CS
GP0 - DC
GP4 - RES
GP2 - SDA
GP3 - SCL
3V3 - VCC
GND - GND
```


# Display Simple text test
1. copy `lib/adafruit_display_text` folder and `lib/adafruit_st7789.mpy` of [circuitpython libraries](https://circuitpython.org/libraries) to `CIRCUITPY/lib/` folder.
2. connects pins
3. run `./st7789_simpletest.py`


# Display image test
1. copy `lib/adafruit_imageload/` folder
2. connects pins
3. run `./st7789_imagetest.py` or `./st7789_imagetest_imageload.py`

* `./st7789_imagetest.py` use `OnDiskBitmap`, it source the bitmap image directly from flash memory storage. So slow.
* `./st7789_imagetest_imageload.py` use `adafruit_imageload`. It is more faster then using `OnDiskBitmap`.


## Tests
* `./st7789_imagetest.py`: display image throught OnDiskBitmap
* `./st7789_imagetest_imageload.py`: display image after loading
* `./st7789_imagetest_sprite.py`: display sprite images using one bitmap file.
* `./st7789_imagetest_sprite_autorefreshOff.py`: refresh off test.

# References
* https://docs.circuitpython.org/projects/st7789/en/latest/index.html
* https://helloraspberrypi.blogspot.com/2021/01/raspberry-pi-picocircuitpython-st7789.html
* https://learn.adafruit.com/circuitpython-display-support-using-displayio
