#!/usr/bin/env python

from __future__ import division
import sys
import math
import collections
import math
import scipy as scp
from time import sleep
from threading import Thread
import numpy as np
import gevent
from emokit.emotiv import Emotiv
from multiprocessing import Process, Pipe
"""Import from Graphic libraries"""
from PyQt4.QtGui import QApplication, QDialog, QTabWidget, QMainWindow
from PyQt4.QtGui import QColor
from PyQt4.QtCore import QObject, pyqtSignal, pyqtSlot
from pyqtgraph.Qt import QtGui, QtCore
"""Import from within the files"""
from GUI.GUI import Ui_MainWindow
from ColorChanger.changecolors import ColorBatt, ColorChannelQuality
from ColorChanger.changecolors import ColorAdjust

class LinkingPath(QObject):
	patcher_Battery = pyqtSignal(int)
	patcher_Quality = pyqtSignal(int, int, int, int, int)
	patcher_PlotGyros = pyqtSignal(int)
	patcher_emg = pyqtSignal(int, int)
	patcher_eeg = pyqtSignal(int, int, int, int)
	def __init__(self):
		QObject.__init__(self)
	def patch_Battery(self, data):
		self.patcher_Battery.emit(data)
	def patch_Quality(self, data1, data2, data3, data4, data5):
		self.patcher_Quality.emit(data1, data2, data3, data4, data5)
	def patch_PlotGyros(self, data1):
		self.patcher_PlotGyros.emit(data1)
	def patch_emg(self, data1, data2):
		self.patcher_emg.emit(data1, data2)
	def patch_eeg(self, data1, data2, data3, data4):
		self.patcher_eeg.emit(data1, data2, data3, data4)

class MainWindow(QMainWindow, Ui_MainWindow):
	def __init__(self):
		super(MainWindow, self).__init__()
		QTabWidget.__init__(self)
		self.setupUi(self)
		# Set Basics of Plotting
		win_gyro = self.graphicsView_gyro
		win_emg = self.graphicsView_emg
		win_eeg = self.graphicsView_eeg
		self.f_samp = 128;
		self.sampleinterval=1/self.f_samp
		self.timewindow=4
		self._interval = int(self.sampleinterval)
		self._bufsize = int(self.timewindow/self.sampleinterval)
		# Set Gyro Plotting
		self.p_gyro = win_gyro.addPlot(row=0, col=0,
		title="Giroscopio X")
		self.p_gyro.setYRange(-60,60)
		self.p_gyro.setXRange(0,self.timewindow)
		self.p_gyro.showGrid(x=True, y=True)
		self.p_gyro.setLabel('left', 'Rad*F', 'Theta*N bits')
		self.p_gyro.setLabel('bottom', 'Tiempo', 's') 
		self.databuffer_gyro = collections.deque([0.0]*self._bufsize,
		self._bufsize)
		self.x_gyro = np.linspace(0.0, self.timewindow, self._bufsize)
		self.y_gyro = np.zeros(self._bufsize, dtype=np.float)
		self.curve_gyro = self.p_gyro.plot(self.x_gyro, self.y_gyro,
		pen='b')
		# Set EMG  Plotting
		self.p1_emg = win_emg.addPlot(row=0, col=0, title="Canales EMG")
		self.p1_emg.setYRange(0,0.00015)
		self.p1_emg.setXRange(0,self.timewindow)
		self.p1_emg.showGrid(x=True, y=True)
		self.p1_emg.setLabel('left', 'Voltios', 'V')
		self.p1_emg.setLabel('bottom', 'Tiempo', 's')
		self.x_emg = np.linspace(0.0, self.timewindow, self._bufsize)
		for x in range(1, 3):
			exec "self.databuffer%s_emg=collections.deque([0.0]*self._bufsize, self._bufsize)" % (x)
			exec "self.y%s_emg=np.zeros(self._bufsize, dtype=np.float)" % (x)
		for x, colr in enumerate(['b','r'],start=1):
			exec "self.curve%s_emg=self.p1_emg.plot(self.x_emg, self.y%s_emg, pen=colr)" % (x,x)
		# Set EEG  Plotting   
		self.p1_eeg = win_eeg.addPlot(row=0, col=0, title="Canales EEG")
		self.p1_eeg.setYRange(0,0.00015)
		self.p1_eeg.setXRange(0,self.timewindow)
		self.p1_eeg.showGrid(x=True, y=True)
		self.p1_eeg.setLabel('left', 'Voltios', 'V')
		self.p1_eeg.setLabel('bottom', 'Tiempo', 's')
		self.x_eeg = np.linspace(0.0, self.timewindow, self._bufsize)
		for x in range(1, 5):
			exec "self.databuffer%s_eeg=collections.deque([0.0]*self._bufsize, self._bufsize)" % (x)
			exec "self.y%s_eeg=np.zeros(self._bufsize, dtype=np.float)" % (x)
		for x, colr in enumerate(['b','r','y','g'],start=1):
			exec "self.curve%s_eeg=self.p1_eeg.plot(self.x_eeg, self.y%s_eeg, pen=colr)" % (x,x)     
		# Seccion de links y botones
		for x, val_name in enumerate(["Iniciar","Finalizar","Salir",
								 "Gyroend","Gyroini","emgend",
								 "emgini","eegend","eegini"],start=1):
			exec "sld%s=self.push_%s" % (x,val_name)
		# Seccion de links y botones
		for x, val_name in enumerate(["Iniciar","Pausado","Salida",
								 "PausadoGyro","IniciadoGyro","PausadoEmg",
								 "IniciadoEmg","PausadoEeg","IniciadoEeg"],start=1):
			exec "sld%s.clicked.connect(self._%s)" % (x,val_name)
		self.linking = LinkingPath()
		self.linking.patcher_Battery.connect(self.print_Battery)
		self.linking.patcher_Quality.connect(self.print_Quality)
		self.linking.patcher_PlotGyros.connect(self.plot_Gyro)
		self.linking.patcher_emg.connect(self.plot_Emg)
		self.linking.patcher_eeg.connect(self.plot_Eeg)
		self.tabWidget.currentChanged.connect(self.tabclick)
		# Set Legend Mains
		# Set Gyro Legend
		self.list = self.treeWidget_gyro
		self.list.setRootIsDecorated(False)
		self.list.setUniformRowHeights(True)
		self.list.setAllColumnsShowFocus(True)
		self.list.setItemsExpandable(False)
		self.list.header().hide()
		self.list.setColumnCount(2)
		for label, color in (
		('Giroscopio X', 'Blue'),):
			item = QtGui.QTreeWidgetItem([label, '------------'])
			item.setForeground(1, QtGui.QColor(color))
			self.list.addTopLevelItem(item)
		# Set EMG Legend
		self.list = self.treeWidget_emg
		self.list.setRootIsDecorated(False)
		self.list.setUniformRowHeights(True)
		self.list.setAllColumnsShowFocus(True)
		self.list.setItemsExpandable(False)
		self.list.header().hide()
		self.list.setColumnCount(2)
		for label, color in (
		('CH2   AF3', 'Blue'),
		('CH3   F8', 'Red')
		):
			item = QtGui.QTreeWidgetItem([label, '------------'])
			item.setForeground(1, QtGui.QColor(color))
			self.list.addTopLevelItem(item)
		# Set EEG Legend
		self.list = self.treeWidget_eeg
		self.list.setRootIsDecorated(False)
		self.list.setUniformRowHeights(True)
		self.list.setAllColumnsShowFocus(True)
		self.list.setItemsExpandable(False)
		self.list.header().hide()
		self.list.setColumnCount(2)
		for label, color in (
		('CH1   O2', 'blue'),
		('CH2   AF3', 'red'),
		('CH4   F3', 'yellow'),
		('CH5   F4', 'green')
		):
			item = QtGui.QTreeWidgetItem([label, '------------'])
			item.setForeground(1, QtGui.QColor(color))
			self.list.addTopLevelItem(item)

	def tabclick(self, temp):
		if temp == 0:
			self.continuidad_gyro= False
			self.continuidad_eeg = False
		elif temp == 1:
			self.continuidad_emg = False
			self.continuidad_gyro= False
		elif temp == 2:
			self.continuidad_eeg = False
			self.continuidad_emg = False

	def _IniciadoGyro(self):
		self.continuidad_gyro = True

	def _PausadoGyro(self):
		self.continuidad_gyro = False

	def _IniciadoEmg(self):
		self.continuidad_emg = True

	def _PausadoEmg(self):
		self.continuidad_emg = False
		
	def _IniciadoEeg(self):
		self.continuidad_eeg = True
				
	def _PausadoEeg(self):
		self.continuidad_eeg = False

	def _Pausado(self):
		self.continuidad	  = False
		self.continuidad_gyro = False
		self.continuidad_emg  = False
		self.continuidad_eeg  = False

	def _Salida(self):
		self.continuidad_gyro = False
		self.continuidad_emg  = False
		self.continuidad_eeg  = False
		self.continuidad      = False
		QtCore.QCoreApplication.instance().quit()

	def plot_Emg(self, CH1, CH2):
		self.databuffer1_emg.append(CH1)
		self.databuffer2_emg.append(CH2)
		self.y1_emg[:] = self.databuffer1_emg
		self.y2_emg[:] = self.databuffer2_emg
		self.curve1_emg.setData(self.x_emg,
		(self.y1_emg-np.average(self.y1_emg))*0.51e-6 + 100*0.51e-6)
		self.curve2_emg.setData(self.x_emg,
		(self.y2_emg-np.average(self.y2_emg))*0.51e-6 + 200*0.51e-6)
	def plot_Eeg(self, CH1, CH2, CH3,CH4):
		self.databuffer1_eeg.append(CH1)
		self.databuffer2_eeg.append(CH2)
		self.databuffer3_eeg.append(CH3)
		self.databuffer4_eeg.append(CH4)
		self.y1_eeg[:] = self.databuffer1_eeg
		self.y2_eeg[:] = self.databuffer2_eeg
		self.y3_eeg[:] = self.databuffer3_eeg
		self.y4_eeg[:] = self.databuffer4_eeg
		self.curve1_eeg.setData(self.x_eeg,
		(self.y1_eeg-np.average(self.y1_eeg))*0.51e-6 + 50*0.51e-6)
		self.curve2_eeg.setData(self.x_eeg,
		(self.y2_eeg-np.average(self.y2_eeg))*0.51e-6 + 100*0.51e-6)
		self.curve3_eeg.setData(self.x_eeg,
		(self.y3_eeg-np.average(self.y3_eeg))*0.51e-6 + 150*0.51e-6)
		self.curve4_eeg.setData(self.x_eeg,
		(self.y4_eeg-np.average(self.y4_eeg))*0.51e-6 + 200*0.51e-6)

	def plot_Gyro(self, GyroX):
		self.databuffer_gyro.append(GyroX)
		self.y_gyro[:] = self.databuffer_gyro
		self.curve_gyro.setData(self.x_gyro, self.y_gyro)

	def print_Battery(self, BattValue):
		if 0 < BattValue < 100:
			self.progressBar_Bat.setValue(BattValue)
			ColorBatt(self, BattValue)

	def print_Quality(self, CH1, CH2, CH3, CH4, CH5):
		for x in range(1, 6):
			exec "tmp%s = ColorAdjust(self, CH%s)" % (x,x)
		ColorChannelQuality(self, tmp1, tmp2, tmp3, tmp4, tmp5)

	def update_battery(self):
		headset = Emotiv(display_output=False)
		gevent.spawn(headset.setup)
		try:
			while self.continuidad:
				packet = headset.dequeue()
				BattValue = packet.battery
				self.linking.patch_Battery(BattValue)
		finally:
			headset.close()

	def update_Quality(self):
		headset = Emotiv(display_output=False)
		gevent.spawn(headset.setup)
		try:
			while self.continuidad:
				packet = headset.dequeue()
				self.linking.patch_Quality(
				packet.sensors['O2']['quality'],
				packet.sensors['AF3']['quality'],
				packet.sensors['F8']['quality'],
				packet.sensors['F3']['quality'],
				packet.sensors['F4']['quality'])
				if self.continuidad_emg:
					self.linking.patch_emg(
					packet.sensors['AF3']['value'],
					packet.sensors['F8']['value'])
				if self.continuidad_eeg:
					self.linking.patch_eeg(
					packet.sensors['O2']['value'],
					packet.sensors['AF3']['value'],
					packet.sensors['F3']['value'],
					packet.sensors['F4']['value'])
				if self.continuidad_gyro:
					packet = headset.dequeue()
					GyroX = packet.gyro_x
					self.linking.patch_PlotGyros(GyroX)
		finally:
			headset.close()

	def _Iniciar(self):
		try:
			self.continuidad_gyro	= False
			self.continuidad_emg	= False
			self.continuidad_eeg	= False
			self.continuidad		= True
			cycle3 = Thread(target = self.update_Quality)
			cycle4 = Thread(target = self.update_battery)
			cycle3.daemon=True
			cycle4.daemon=True
			cycle3.start()
			cycle4.start()
		except self.continuidad == False:
			pass
def main():
	app = QApplication(sys.argv)
	window = MainWindow()
	window.show()
	sys.exit(app.exec_())

if __name__ == '__main__':
	main()
