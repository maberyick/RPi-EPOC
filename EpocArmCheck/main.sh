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
"""Import from within the files"""
from GUI.GUI import Ui_MainWindow
from Library.changecolors import ColorBatt, ColorChannelQuality
from Library.changecolors import ColorAdjust

class LinkingPath(QObject):
	patcher_Gyros = pyqtSignal(int)
	patcher_Battery = pyqtSignal(int)
	patcher_Quality = pyqtSignal(int,int,int)
	def __init__(self):
		QObject.__init__(self)
	def patch_Gyros(self, data1):
		self.patcher_Gyros.emit(data1)
	def patch_Battery(self, data1):
		self.patcher_Battery.emit(data1)
	def patch_Quality(self, data1,data2,data3):
		self.patcher_Quality.emit(data1,data2,data3)

class MainWindow(QMainWindow, Ui_MainWindow):
	def __init__(self):
		super(MainWindow, self).__init__()
		QTabWidget.__init__(self)
		self.setupUi(self)
		""" Seccion de links y botones """
		sld1 = self.push_Iniciar
		sld3 = self.push_Salir
		sld1.clicked.connect(self._Iniciar)
		sld3.clicked.connect(self._Salida)
		self.linking = LinkingPath()
		self.linking.patcher_Gyros.connect(self.print_Gyros)
		self.linking.patcher_Battery.connect(self.print_Battery)
		self.linking.patcher_Quality.connect(self.print_Quality)

	def _Salida(self):
		self.continuidad = False
		QtCore.QCoreApplication.instance().quit()

	def print_Gyros(self, GyroX):
		self.label_GyroX.setNum(GyroX)

	def print_Battery(self, BattValue):
		if 0 < BattValue < 100:
			self.progressBar_Bat.setValue(BattValue)
			ColorBatt(self, BattValue)

	def print_Quality(self,CH1,CH2,CH3):
		for x, CH_S in enumerate([CH1,CH2,CH3],start=1):
			exec "tmp%s=ColorAdjust(self, CH_S)" % (x)
		ColorChannelQuality(self,tmp1,tmp2,tmp3)

	def update_Value(self):
		headset = Emotiv(display_output=False)
		gevent.spawn(headset.setup)
		try:
			while self.continuidad:
				packet = headset.dequeue()
				self.linking.patch_Quality(
				packet.sensors['O2']['quality'],
				packet.sensors['AF3']['quality'],
				packet.sensors['F8']['quality'])
				self.linking.patch_Gyros(packet.gyro_x)
				self.linking.patch_Battery(packet.battery)
		finally:
			headset.close()

	def _Iniciar(self):
		try:
			self.continuidad = True
			cycle1 = Thread(target = self.update_Value)
			cycle1.daemon=True
			cycle1.start()
		except self.continuidad == False:
			pass

def main():
	app = QApplication(sys.argv)
	window = MainWindow()
	window.show()
	sys.exit(app.exec_())

if __name__ == '__main__':
	main()
