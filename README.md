# rasppi_rover

This is a ROS-kinetic wrapper to control a custom built treaded rover of the following components.
* Raspberry Pi 3
* Adafruit DC & Stepper Motor HAT for Raspberry Pi
* Sparkfun's Rover 5
* The Official 7" Raspberry Pi Touchscreen Display

There is one custom message definition
* rosrover/MotorControl
* * int16 left   - Controls the left motors, give a value from -256 to 256 representing the PWM duty cycle of the wheel, with negative values indicating opposite direction.
* * int16 right   - Controls the right motors, give a value from -256 to 256 representing the PWM duty cycle of the wheel, with negative values indicating opposite direction.
* * bool stop - If this is anything other than 0, it will override 'left' and 'right' with 0 and release all current from the motors allowing external rotations.

The rover currently only has one subscriber.
* rosrover/rosrover_motor  - Takes a rosrover/MotorControl message to control the motors

Future additions.
* Add support for an outgoing camera stream of some sort
* Add more functions regarding motor control as are needed
* Incorporate the motor encoders of the Rover 5 to provide feedback
* Create some form of GUI on the display to allow status observation
