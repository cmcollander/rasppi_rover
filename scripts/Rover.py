from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor

class Rover:
	def __init__(self,address=0x60):
		self.mh = Adafruit_MotorHAT(addr=address)
		self.motors = []
		for i in range(1,5):
			self.motors.append(self.mh.getMotor(i))
			self.motors[i-1].setSpeed(0)
	
	def stop(self):
		self.mh.getMotor(1).run(Adafruit_MotorHAT.RELEASE)
		self.mh.getMotor(2).run(Adafruit_MotorHAT.RELEASE)
		self.mh.getMotor(3).run(Adafruit_MotorHAT.RELEASE)
		self.mh.getMotor(4).run(Adafruit_MotorHAT.RELEASE)
	
	def setWheel(self, mot, val):
		if val<0:
			self.motors[mot].run(Adafruit_MotorHAT.BACKWARD)
			self.motors[mot].setSpeed(-1*val)
		else:
			self.motors[mot].run(Adafruit_MotorHAT.FORWARD)
			self.motors[mot].setSpeed(val)
	
	def releaseWheel(self, mot):
		self.motors[mot].run(Adafruit_MotorHAT.RELEASE)
	
	def move(self,left, right):
		if -50<left<50:
			left = 0
		if -50<right<50:
			right = 0
		self.setWheel(0, left)
		self.setWheel(1, left)
		self.setWheel(2, right)
		self.setWheel(3, right)
		
	def Joy2Mot(self, nJoyX, nJoyY, moveAlso=True):
		fPivYLimit = 32.0
		if nJoyY>=0:
			nMotPremixL = 127.0 if (nJoyX>=0) else (127.0+nJoyX)
			nMotPremixR = (127.0-nJoyX) if (nJoyX>=0) else 127.0
		else:
			nMotPremixL = (127.0-nJoyX) if (nJoyX>=0) else 127.0
			nMotPremixR = 127.0 if (nJoyX>=0) else (127.0+nJoyX)
		nMotPremixL *= nJoyY/128.0
		nMotPremixR *= nJoyY/128.0;
		nPivSpeed = nJoyX;
		fPivScale = 0.0 if (abs(nJoyY)>fPivYLimit) else (1.0-abs(nJoyY)/fPivYLimit)
		nMotMixL = (1.0-fPivScale)*nMotPremixL + fPivScale*nPivSpeed
		nMotMixR = (1.0-fPivScale)*nMotPremixR + fPivScale*-1*nPivSpeed
		left_wheel = int(nMotMixL*1.9921875)
		right_wheel = int(nMotMixR*1.9921875)
		if moveAlso:
			self.move(left_wheel,right_wheel)
		return [left_wheel,right_wheel]
		
