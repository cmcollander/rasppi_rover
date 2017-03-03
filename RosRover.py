import roshelper
import rospy
from std_msgs.msg import Int16
from std_msgs.msg import String
from Rover import Rover

n = roshelper.Node("RosRover", anonymous=False)
r = Rover()

left = 0
right = 0

@n.subscriber("/RosRover_Motor_Left", Int16)
def listener(mot_left):
	global left
	global right
	left  = mot_left.data
	r.move(left,right)
	rospy.loginfo("MOVE: %d, %d"%(left,right))

@n.subscriber("/RosRover_Motor_Right", Int16)
def listener(mot_right):
	global left
	global right
	right = mot_right.data
	r.move(left,right)
	rospy.loginfo("MOVE: %d, %d"%(left,right))

@n.subscriber("/RosRover_Stop", String)
def listener(stop_val): # This value gets discarded
	r.stop()
	rospy.loginfo("STOP")

@n.entry_point(frequency=1)
def main():
	pass

if __name__ == "__main__":
	n.start(spin=True)


