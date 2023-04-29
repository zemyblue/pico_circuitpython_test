import time
import board
import busio
import adafruit_tcs34725

# i2c_sda = board.GP18
# i2c_scl = board.GP19
i2c_sda = board.GP20
i2c_scl = board.GP21

i2c = busio.I2C(scl=i2c_scl, sda=i2c_sda)
sensor = adafruit_tcs34725.TCS34725(i2c)

while True:
    # Raw data from the sensor in a 4-tuple of red, green, blue, clear light component values
    # print(sensor.color_raw)

    color = sensor.color
    color_rgb = sensor.color_rgb_bytes
    print("RGB color as 8 bits per channel int: #{0:02X} or as 3-tuple: {1}".format(color, color_rgb))

    # Read the color temperature and lux of the sensor too.
    temp = sensor.color_temperature
    lux = sensor.lux
    print("Temperature: {0}K Lux:{1}\n".format(temp, lux))
    # Delay for a second and repeat.
    time.sleep(1.0)
