import time
import board
import busio
import adafruit_mpu6050

i2c_sda = board.GP16
i2c_scl = board.GP17

i2c = busio.I2C(scl=i2c_scl, sda=i2c_sda)
mpu = adafruit_mpu6050.MPU6050(i2c)

while True:
    print("Acceleration X:%.2f, Y:%.2f, Z:%.2f m/s^2" % (mpu.acceleration))
    print("Gyro X:%.2f, Y:%.2f, Z:%.2f rad/s" % (mpu.gyro))
    print("Temperature: %.2f C" % mpu.temperature)
    print("")
    time.sleep(1)
