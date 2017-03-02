from Rover import Rover
import time

r = Rover() # Default I2C Address

r.move(-255,255) # Rotate left
time.sleep(1) # Wait 1 second
r.move(255,-255) # Rotate Right
time.sleep(1) # Wait 1 second

r.stop() # Release all motor tension (REQUIRED AT THE END OF EVERY PROGRAM!)