# TSC34725 test
This is color sensor.

**warning**: TCS3472X colour sensor recommends using 5V as VIN. If not, the color data is darkter.


## Connected Pins
TCS34725 use I2C interface.
```
VIN - 3V3
GND - GND
SCL - GP19
SDA - GP18
```

## Copy adafruit library
Copy below libraries of [circuitpython library](https://circuitpython.org/libraries) to `CIRCUITPY/lib/`
* `lib/adafruit_tcs34725.mpy`
* `lib/adafruit_bus_device`


# References
* https://learn.adafruit.com/adafruit-color-sensors/python-circuitpython
## for support TCS34727
* https://blog.csdn.net/qq_16519885/article/details/119580644
* https://raspberrypi.stackexchange.com/questions/135976/im-running-raspbian-on-my-pi-3-model-b-and-trying-to-get-the-i2c-tcs3472-colour
