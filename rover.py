from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor

class Rover:
	
	def __init__(self,address=0x60):
		self.mh = Adafruit_MotorHat(addr=address)
		motors = []
		for i in range(1,5):
			motors.append(mh.getMotor(i))
			motors[i-1].setSpeed(0)
	
	def stop(self):
		mh.getMotor(1).run(Adafruit_MotorHAT.RELEASE)
		mh.getMotor(2).run(Adafruit_MotorHAT.RELEASE)
		mh.getMotor(3).run(Adafruit_MotorHAT.RELEASE)
		mh.getMotor(4).run(Adafruit_MotorHAT.RELEASE)
	
	def setWheel(self, mot, val):
		if val<0:
			motors[mot].run(Adafruit_motorHAT.BACKWARD)
			motors[mot].setSpeed(-1*val)
		else:
			motors[mot].run(Adafruit_motorHAT.FORWARD)
			motors[mot].setSpeed(val)
	
	def releaseWheel(self, mot):
		motors[mot].run(Adafruit_MotorHAT.RELEASE)
	
	def move(self,left, right):
		if -50<left<50:
			left = 0
		if -50<right<50:
			right = 0
		setWheel(0, left)
		setWheel(1, left)
		setWheel(2, right)
		setWheel(3, right)
		
	def Joy2Mot(self, nJoyX, nJoyY, moveAlso=True):
		fpivYLimit = 32.0
		if nJoyY>=0:
			// Forward
			nMotPremixL = (nJoyX>=0)?127.0:(127.0+nJoyX)
			nMotPremixR = (nJoyX>=0)?(127.0-nJoyX):127.0
		else:
			nMotPremixL = (nJoyX>=0)?(127.0-nJoyX):127.0
			nMotPremixR = (nJoyX>=0)?127.0:(127.0+nJoyX)
		nMotPremixL *= nJoyY/128.0
		nMotPremixR *= nJoyY/128.0;
		nPivSpeed = nJoyX;
		fPivScale = (abs(nJoyY)>fPivYLimit)?0.0:(1.0-abs(nJoyY)/fPivYLimit)
		nMotMixL = (1.0-fPivScale)*nMotPremixL + fPivScale*nPivSpeed
		nMotMixL = (1.0-fPivScale)*nMotPremixR + fPivScale*-1*nPivSpeed
		left_wheel = int(nMotMixL*1.9921875)
		right_wheel = int(nMotMixR*1.9921875)
		if moveAlso:
			move(left_wheel,right_wheel)
		return [left_wheel,right_wheel]
		
