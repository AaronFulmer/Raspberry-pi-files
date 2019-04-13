import board
import digitalio
import busio
import adafruit_bme280
import adafruit_tsl2561
import datetime

i2c = busio.I2C(board.SCL, board.SDA)
sensor = adafruit_tsl2561.TSL2561(i2c)
spi = busio.SPI(board.SCK, MOSI = board.MOSI, MISO = board.MISO)
cs = digitalio.DigitalInOut(board.D5)
bme280 = adafruit_bme280.Adafruit_BME280_SPI(spi, cs)

file = open(datetime.datetime.now().strftime("%m-%d-%y") + ".txt", "a")

file.write(datetime.datetime.now().strftime("%H:%M:%S") + "\n")
file.write("\tTemp: %0.1f C" % bme280.temperature + "\n")
file.write("\tHumidity: %0.1f %%" % bme280.humidity + "\n")
file.write("\tPressure: %0.1f hPa" % bme280.pressure + "\n")

file.write("\tLux: {}".format(sensor.lux) + "\n")
file.write("\tBroadband: {}".format(sensor.broadband) + "\n")
file.write("\tInfrared: {}".format(sensor.infrared) + "\n")
file.write("\tLuminosity: {}".format(sensor.luminosity) + "\n")