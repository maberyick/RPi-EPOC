#!/usr/bin/env python

import sys
from PyQt4.QtGui import QApplication, QTabWidget, QMainWindow
from pyqtgraph.Qt import QtCore
import numpy as np
from emokit.emotiv import Emotiv
import gevent
from threading import Thread
from multiprocessing import Process, Pipe
from PyQt4.QtCore import QObject, pyqtSignal
import collections
"""Import from within the files"""
from GUI.GUI import Ui_MainWindow
from Library.alpha_work import alpha_work
from Library.beta_work import beta_work
from Library.wink_work import wink_work
from Library.gyro_work import gyro_work

class LinkingPath(QObject):
	patcher_Gyros = pyqtSignal(int)
	def __init__(self):
		QObject.__init__(self)
	def patch_Gyros(self, data1):
		self.patcher_Gyros.emit(data1)

class MainWindow(QMainWindow, Ui_MainWindow):
	def __init__(self):
		super(MainWindow, self).__init__()
		QTabWidget.__init__(self)
		self.setupUi(self)
		""" Constants and Buffers """
#--------------------------- Buff size for each function window --------
		""" Relax {O2 -> 2 secs}	Conc {AF3 -> 3 secs}	Wink {AF3,AF4 -> 2 secs} '"""
		self._bufsize1 = 256; self._bufsize2 = 256
		self._bufsize3 = 256; self._bufsize4 = 512
#----------------------------------------------------------------------
		for x, val in enumerate([self._bufsize1,self._bufsize2,
		self._bufsize3,self._bufsize4],start=1):
			exec "self.databuffer%s=collections.deque([0.0]*%s, %s)" % (x,val,val)
#----------------------------------------------------------------------
		""" Seccion de links y botones """
		sld1 = self.push_Iniciar
		sld2 = self.push_Finalizar
		sld3 = self.push_Salir
		sld1.clicked.connect(self._Iniciar)
		sld2.clicked.connect(self._Pausado)
		sld3.clicked.connect(self._Salida)
		self.linking = LinkingPath()
		self.linking.patcher_Gyros.connect(self.pros_Gyro)
		self.alpha_work = alpha_work(self)
		self.beta_work = beta_work(self)
		self.wink_work = wink_work(self)
		self.gyro_work = gyro_work(self)

	def _Pausado(self):
		self.continuidad = False

	def _Salida(self):
		self.continuidad = False
		QtCore.QCoreApplication.instance().quit()

	def pros_Gyro(self, GyroX):
		self.gyro_work.GyroDeflection(GyroX,self.continuidad)

	def alpha_sensors_svm(self,q):
		while self.continuidad:
			self.alpha_work.svm_alphaPro(q.recv())

	def wleft_sensors_svm(self,q):
		while self.continuidad:
			self.beta_work.svm_betaPro(q.recv())

	def wright_sensors_svm(self,q):
		while self.continuidad:
			self.wink_work.svm_winkPro(q.recv())

	def update_Gyros(self):
		headset = Emotiv(display_output=False)
		gevent.spawn(headset.setup)
		try:
			while self.continuidad:
				packet = headset.dequeue()
				GyroX = packet.gyro_x
				self.linking.patch_Gyros(GyroX)
		finally:
			headset.close()

	def update_Value(self,q1,q2,q3):
		headset = Emotiv(display_output=False)
		gevent.spawn(headset.setup)
		try:
			while self.continuidad:
				for i in range(64):
					packet = headset.dequeue()
					for x, name_val in enumerate(['O2','AF3','F8'],start=1):
						exec "self.databuffer%s.append(packet.sensors[name_val]['value'])" % (x)
				for x in range(1,4):
					exec "q%s.send(np.array(self.databuffer%s))" % (x,x)
		finally:
			headset.close()

	def _Iniciar(self):
		try:
			self.continuidad = True
			q_reci_1, q_send_1 = Pipe()
			q_reci_2, q_send_2 = Pipe()
			q_reci_3, q_send_3 = Pipe()
			cycle1 = Process(target = self.update_Value,args=(q_send_1,q_send_2,q_send_3))
			cycle2 = Thread(target = self.update_Gyros)
			cycle3 = Thread(target = self.alpha_sensors_svm,args=(q_reci_1,))
			cycle4 = Thread(target = self.wleft_sensors_svm,args=(q_reci_2,))
			cycle5 = Thread(target = self.wright_sensors_svm,args=(q_reci_3,))
			cycle1.daemon=True
			cycle2.daemon=True
			cycle3.daemon=True
			cycle4.daemon=True
			cycle5.daemon=True
			cycle1.start()
			cycle2.start()
			cycle3.start()
			cycle4.start()
			cycle5.start()
		except self.continuidad == False:
			pass

def main():
	app = QApplication(sys.argv)
	window = MainWindow()
	window.show()
	sys.exit(app.exec_())

if __name__ == '__main__':
	main()
