import maestro
import time
"""
		-- Pololu Reference --
No.servo		Type		min (us)/(ns)		max(us)/(ns)		mid(us)/(ns)
	0		Waist			448	 / 1792			2464 / 9856			1328 / 5312
	1		Shoulder		1600 / 6400			2000 / 8000			1800 / 7200
	2		Elbow			1056 / 4224			2000 / 8000			1528 / 6112
	3		Wrist			800  / 3200			2000 / 8000			1400 / 5600
	4		Tool			496  / 1984			2400 / 9600			1448 / 5792
	5		Grabber			1296 / 5184			2000 / 8000			1648 / 6592
(us) -> (quarter us unit) 	-> target = value(us) / (250 ns)
"""
class arm_bot():
	def __init__(self):
		self.servo = maestro.Controller()
		'''		Gyro_X		'''
		self.waist = 5312
		self.tool = 5792
		'''		Wink		'''
		self.shoulder = 7200
		self.elbow = 6112
		self.wrist = 5600
		'''		Alpha/Beta	'''
		self.grabber = 6592

	def servo_end(self,en):
		if en:
			self.servo = maestro.Controller()
		else:
			self.servo.close

	def WinL(self,val_):
		if val_:
			self.servo.setTarget(4,5792)

	def WinR(self,val_):
		if val_:
			self.servo.setTarget(4,9600)

	def GyrR(self,val_):
		if val_:
			self.waist -= 250
			if self.waist < 1792:
				self.waist = 1792
			self.servo.setTarget(0,self.waist)

	def GyrL(self,val_):
		if val_:
			self.waist += 100
			if self.waist > 9856:
				self.waist = 9856
			self.servo.setTarget(0,self.waist)

	def Alp(self,val_):
		if val_:
			self.servo.setTarget(5,8000)

	def Bet(self,val_):
		if val_:
			self.servo.setTarget(5,5500)
