'''#################################################################

	This file is meant to be called by a service in the mesh to
	read the sensors wired to the arduino and log the data in a
	text file. 

	I have not tested it with the RPi and Arduino yet.

'''#################################################################
import serial
import time

port = "/dev/ttyACM0"  # Serial port for computer this program runs on (this one is what the port was on my Raspberry Pi)
try:
	serial_connection = serial.Serial(port, baudrate=9600, timeout=1)  # Establishing a serial connection at 9600 baudrate
	print "Connected!"                                                 # Confirmation
except serial.SerialException:                                         # Catching an invalid port error
	print "Connection Failure!"

serial_connection.close()       # Close the serial connection
time.sleep(0.5)                 # Delay half of a second
serial_connection.open()        # Open the serial connection
time.sleep(0.5)                 # Delay half of a second
file = open("output.txt", "a")  # Open a text file (mine is called output.txt) in the program's source folder in append mode ("a")

serial_connection.write("read sensors")   # Sending the command to the arduino to read the sensors and return the data

time.sleep(1)

'''
There are 5 outputs from the arduino with sensor data (Lux, temperature, 
estimated altitude, barometric pressure, and humidity) so for now it is
just reading the serial port 5 times. This will be changed later but it
works for now
'''
file.print(serial_connection.readLine())
file.print(serial_connection.readLine())
file.print(serial_connection.readLine())
file.print(serial_connection.readLine())
file.print(serial_connection.readLine())