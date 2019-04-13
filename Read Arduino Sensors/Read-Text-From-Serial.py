import serial
import time

'''
#################################################################

A couple of important things to note:
	1: I made this to make an Arduino Uno and a Raspberry Pi talk
		to each other, so any other machine may be different

	2: Baudrate between machines MUST be the same, but its value
		is most likely inconsequential (Depends on machines used)

	3: Serial Port name is different on Windows vs. Raspberry Pi
		On Windows, it would be "COM#" where the number can be
			found in the device manager window.
		On Linux, it is "/dev/tty[port]" where port could vary
			depending on how it is connected.
		To get the port on Raspberry Pi, run the command
			"dmesg | grep tty" to see all active ports, the one you'll
			want should be near the bottom labelled "USB device" or
			something similar.

	4: The output filename, port, resulting text, and markers will
			all probably be different between my machines and yours.
		The filename is something easily fixable; it does not
			matter what it is, so make it whatever you want.
		I've already discussed what to do with the port.
		The markers and serial data are sent by my arduino, so
			you can make your own however you see fit. Mine sends
			"hello" "0" where hello is the data and 0 is the line
			end marker.

That should be it. Have fun with it and let me know if you
have any problems with it.

#################################################################
'''

port = "/dev/ttyACM0"  # Serial port for computer this program runs on (this one is what the port was on my Raspberry Pi)
try:
	serial_connection = serial.Serial(port, baudrate=19200, timeout=1) # Establishing a serial connection at 19200 baudrate
	print "Connected!"                                                 # Confirmation
except serial.SerialException:                                         # Catching an invalid port error
	print "Connection Failure!"

serial_connection.close()       # Close the serial connection
time.sleep(0.5)                 # Delay half of a second
serial_connection.open()        # Open the serial connection
time.sleep(0.5)                 # Delay half of a second
file = open("output.txt", "a")  # Open a text file (mine is called output.txt) in the program's source folder in append mode ("a")

out = ""                        # Declaring an empty string variable to use to print out read information   
x = 0                           # Declaring an empty counter variable for use with testing

while not out.endswith('/>'):    # This means that the loop will run until there is nothing to read/the serial connection is terminated

	received_chars = str(serial_connection.read()) # Reading serial information and casting it to a string
	
	# If the current character is my "marker" (used to denote end of a line)...
	if received_chars == '0':                      
		file.write(out + "\n")                     # Write the current line to the file
		out = ""                                   # Empty the line string
		x += 1                                     # Incrementing the counter
		continue                                   # Ignore remaining code in loop and start again
	
	# Otherwise...
	out += received_chars                          # Add the current character to the current line
	
	# If the loop has output 40 times...
	if x == 40:                                    
		file.close()                               # Save changes and close the file
		break                                      # Break out of the loop (finishes the program)
print ""
