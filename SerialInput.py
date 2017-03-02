from Rover import Rover
import time
import serial

def map(x, in_min, in_max, out_min, out_max):
	return (x - in_min) * (out_max - out_min) // (in_max - in_min) + out_min

ser = serial.Serial('/dev/ttyUSB0')
r = Rover()
r.stop()

while True:
	# Pull in our command
	command = ser.read() # Read in one byte
	if command=='J': # Left Joystick
		x = ser.read()
		y = ser.read()
		if 'a'<x<'z' and 'a'<y<'z':
			j1x = map(x,'a','z',100,0)
			j1y = map(x,'a','z',0,100)
			r.Joy2Mot(j1x,j1y)


r = Rover() # Default I2C Address

r.move(-255,255) # Rotate left
time.sleep(1) # Wait 1 second
r.move(255,-255) # Rotate Right
time.sleep(1) # Wait 1 second

r.stop() # Release all motor tension (REQUIRED AT THE END OF EVERY PROGRAM!)