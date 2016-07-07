from PyQt4.QtCore import Qt, QObject, pyqtSignal, pyqtSlot
from PyQt4.QtGui import QPalette, QColor
"""Import from within the files"""
import armbot

class LinkingPath(QObject):
	patcher_GyroL = pyqtSignal(int,int)
	patcher_GyroR = pyqtSignal(int,int)
	def __init__(self):
		QObject.__init__(self)
	def patch_GyroL(self,data1,data2):
		self.patcher_GyroL.emit(data1,data2)
	def patch_GyroR(self,data1,data2):
		self.patcher_GyroR.emit(data1,data2)
class gyro_work():
	def __init__(self,obj):
		self.y = 6500
		self.obj = obj
		self.linking = LinkingPath()
		self.linking.patcher_GyroL.connect(self.gyroL)
		self.linking.patcher_GyroR.connect(self.gyroR)
		self.obj = obj
		self.highlght = QPalette.Highlight
		self.greeny = QColor(Qt.green)
		self.bluey = QColor(Qt.blue)
		self.redy = QColor(Qt.red)
		self.armb = armbot.arm_bot()

	@pyqtSlot()
	def gyroL(self,val,status):
		palette = QPalette()
		if status:
			palette.setColor(self.highlght, self.greeny)
			self.obj.pB_Gleft.setPalette(palette)
			self.obj.pB_Gleft.setValue(val)
			self.armb.GyrL(True)
		else:
			palette.setColor(self.highlght, self.bluey)
			self.obj.pB_Gleft.setPalette(palette)
	@pyqtSlot()
	def gyroR(self,val,status):
		palette = QPalette()
		if status:
			palette.setColor(self.highlght, self.greeny)
			self.obj.pB_Gright.setPalette(palette)
			self.obj.pB_Gright.setValue(abs(val))
			self.armb.GyrR(True)
		else:
			palette.setColor(self.highlght, self.bluey)
			self.obj.pB_Gright.setPalette(palette)
	@pyqtSlot()

	def GyroDeflection(self,GyroValue_X, en):
		if GyroValue_X > 1:
			self.linking.patch_GyroL(GyroValue_X,True)
		else:
			self.linking.patch_GyroL(GyroValue_X,False)
		if GyroValue_X < -1:
			self.linking.patch_GyroR(GyroValue_X,True)
		else:
			self.linking.patch_GyroR(GyroValue_X,False)
		self.armb.servo_end(en)
