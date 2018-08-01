'''#################################################################

	This file is meant to be called by a service in the mesh to
	read the sensors wired to the arduino and log the data in a
	text file. 

'''#################################################################
import serial
import time

port = "COM3"  # Serial port for computer this program runs on (this one is what the port was on my PC)
try:
	serial_connection = serial.Serial(port, baudrate=9600, timeout=1)  # Establishing a serial connection at 9600 baudrate
	print "Connected!"                                                 # Confirmation
except serial.SerialException:                                         # Catching an invalid port error
	print "Connection Failure!"

time.sleep(2)                   # Delay 2 seconds to allow for initialisation time before sending any commands.
file = open("output.txt", "a")  # Open a text file (mine is called output.txt) in the program's source folder in append mode ("a")
serial_connection.write(b'r')   # Sending the command to the arduino to read the sensors and return the data

time.sleep(2)                   # Delay 2 seconds to allow the Arduino to receive the data, make necessary calculations, and
                                # 	send the data over the serial port

'''
The following loop checks that there is something left in the buffer to read.
If there is, it loops over reading each line and writing it to the text file.
'''
while serial_connection.inWaiting():
	file.write(serial_connection.readline())
file.close()
