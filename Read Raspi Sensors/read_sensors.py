import board
import digitalio
import busio
import adafruit_bme280
import adafruit_tsl2561
import datetime


# The following lines make the necessary objects to allow the Raspberry Pi
# to read the sensors and then write the data to a text file using the current
# date as the filename and the current time as the header for the data.
i2c = busio.I2C(board.SCL, board.SDA)
sensor = adafruit_tsl2561.TSL2561(i2c)
spi = busio.SPI(board.SCK, MOSI = board.MOSI, MISO = board.MISO)
cs = digitalio.DigitalInOut(board.D5)
bme280 = adafruit_bme280.Adafruit_BME280_SPI(spi, cs)

file = open(datetime.datetime.now().strftime("%m-%d-%y") + ".txt", "a") # Open the file in append mode (or create one if it doesn't exist)

file.write(datetime.datetime.now().strftime("%H:%M:%S") + "\n")         # This header is the current time in HH:MM:SS format
file.write("\tTemp: %0.1f C" % bme280.temperature + "\n")               # Using the adafruit_bme280 library, record the current temperature
file.write("\tHumidity: %0.1f %%" % bme280.humidity + "\n")             # Using the adafruit_bme280 library, record the current humidity
file.write("\tPressure: %0.1f hPa" % bme280.pressure + "\n")            # Using the adafruit_bme280 library, record the current pressure

file.write("\tLux: {}".format(sensor.lux) + "\n")                       # Using the adafruit_TSL2561 library, record the current lux
file.write("\tBroadband: {}".format(sensor.broadband) + "\n")           # Using the adafruit_TSL2561 library, record the current broadband
file.write("\tInfrared: {}".format(sensor.infrared) + "\n")             # Using the adafruit_TSL2561 library, record the current infrared
file.write("\tLuminosity: {}".format(sensor.luminosity) + "\n")         # Using the adafruit_TSL2561 library, record the current luminosity

file.close()
