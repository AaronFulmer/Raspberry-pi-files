import board
import digitalio
import busio
import time
import adafruit_tsl2591
import adafruit_bme280

# Create the objects needed to instantiate the sensors
i2c = busio.I2C(board.SCL, board.SDA)
spi = busio.SPI(board.SCK, MOSI = board.MOSI, MISO = board.MISO)
cs = digitalio.DigitalInOut(board.D5)

# Create sensor objects for use in polling for data
sensor = adafruit_tsl2591.TSL2591(i2c)
bme280 = adafruit_bme280.Adafruit_BME280_SPI(spi, cs)

# Example infinite loop to demonstrate simple use of sensors
while True:
	# Read from the TSL2591 sensor
	# Note: There are also methods such as infrared, visible, and
	#       full_spectrum in the TSL2591 library
	print("Lux: %0.1f lux" % sensor.lux)

	# Read from the BME280 sensor
	print("Temp: %0.1f C" % bme280.temperature)
	print("Humidity: %0.1f %%" % bme280.humidity)
	print("Pressure: %0.1f hPa" % bme280.pressure)

	# Moderate how quickly the script repeats
	time.sleep(1)
