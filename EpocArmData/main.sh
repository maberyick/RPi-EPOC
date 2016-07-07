#!/usr/bin/env python

from __future__ import division
import sys
import math
from PyQt4.QtGui import QApplication, QDialog, QTabWidget, QMainWindow
from PyQt4.QtGui import QColor, QPainter, QPen, QBrush, QGraphicsScene
from PyQt4.QtGui import QGraphicsRectItem, QGraphicsLineItem
from PyQt4.QtCore import QObject, pyqtSignal, pyqtSlot, QCoreApplication
import numpy as np
from emokit.emotiv import Emotiv
from gevent import spawn
from threading import Thread
import collections
from pylab import mlab, arange
from time import sleep
import matplotlib.pyplot as plt
from sklearn import preprocessing
from scipy.io import savemat
""" Import from within the files """
from GUI import GUI
from GUI.GUI import Ui_MainWindow
from ColorChanger.changecolors import ColorBatt, ColorChannelQuality
from ColorChanger.changecolors import ColorAdjust, ChckFolders
from Alert.soundy import finito, savinginfo, donothing, standard_re
from Alert.soundy import offline_re
from Alert.soundy import emg_wright, emg_wleft, mu_onright, mu_onleft
from Alert.soundy import beta_rest, alfa_closede, _eog
from Profile.save_profile import save_prof, check_prof
from Features.feat_extraction import feat_extract_
from Features.ch_plot import plt_ch,plt_ch_beta,plt_ch_emg

"""Function to detect type of excepts
except Exception as ex:
	template = "An exception of type {0} occured. Arguments:\n{1!r}"
	message = template.format(type(ex).__name__, ex.args)
	print message
"""

""" Class for linking processes from one function to another """
class LinkingPath(QObject):
	patcher_Battery = pyqtSignal(int)
	patcher_Trial = pyqtSignal(int)
	patcher_Quality = pyqtSignal(int,int,int,int,int,int,int,int,int,
	int,int,int,int,int)
	patcher_Gyros = pyqtSignal(int)
	def __init__(self):
		QObject.__init__(self)
	def patch_Battery(self, data):
		self.patcher_Battery.emit(data)  
	def patch_Trial(self, data):
		self.patcher_Trial.emit(data)  
	def patch_Quality(self,data1,data2,data3,data4,data5,data6,data7,
	data8,data9,data10,data11,data12,data13,data14):
		self.patcher_Quality.emit(data1,data2,data3,data4,data5,data6,
		data7,data8,data9,data10,data11,data12,data13,data14)
	def patch_Gyros(self, data1):
		self.patcher_Gyros.emit(data1)
""" Main Class """
class MainWindow(QMainWindow, Ui_MainWindow):
	""" initial variables """
	def __init__(self):
		super(MainWindow, self).__init__()
		QTabWidget.__init__(self)
		self.setupUi(self)
		""" Constants """
		self.i = 0
		""" Size of the buffers """
		self._bufsize = 16384
		self._bufsize_a = 16384;self._bufsize_b = 204800
		self._bufsize_m = 38400;self._bufsize_i = 16384
		_sampme = 128; _initst = 1024; _svtime = 5
		""" Test Window size """
		_alfatst=1024; _betatst=12800; _mutst=1024; _emgtst=256
		""" Human reaction delay in seconds """
		_alfahdl = 2; _betahdl = 3; _muhdl = 1; _emghdl = 0.5
		""" values of action and rest for the trials """
		""" Relax """
		self._act_rel = range(_initst,self._bufsize_a + _initst,
		_alfatst*2)
		self._non_rel = range(_initst + _alfatst,
		self._bufsize_a + _initst, _alfatst*2)
		self._hm_rel = self._bufsize_a + _initst + _alfahdl*_sampme
		self._sv_rel = self._hm_rel + _svtime*_sampme
		""" Concentration """
		self._act_con = range(_initst, self._bufsize_b + _initst,
		_betatst*2)
		self._non_con = range(_initst + _betatst,
		self._bufsize_b + _initst, _betatst*2)
		self._hm_con = self._bufsize_b + _initst + _betahdl*_sampme
		self._sv_con = self._hm_con + _svtime*_sampme
		""" Motor Imagery """
		self._act_mu = range(_initst, self._bufsize_i + _initst,
		_mutst*2)
		self._non_mu = range(_initst + _mutst,
		self._bufsize_i + _initst, _mutst*2)
		self._hm_mu = self._bufsize_i + _initst + _muhdl*_sampme
		self._sv_mu = self._hm_mu + _svtime*_sampme
		""" EMG """
		self._act_emg = range(_initst, self._bufsize_m + _initst,
		_emgtst*2)
		self._non_emg = range(_initst + _emgtst,
		self._bufsize_m + _initst, _emgtst*2)
		self._hm_emg = self._bufsize_m + _initst + _emghdl*_sampme
		self._sv_emg = self._hm_emg + _svtime*_sampme
		""" Buffers """
		for x in range(1, 15):
			exec "self.databuffer%s=collections.deque([0.0]*self._bufsize, self._bufsize)" % (x)
			exec "self.CH%s_buf=np.zeros(self._bufsize, dtype=np.float)" % (x)
		""" Alfa """
		for x in range(1, 15):
			exec "self.Adatabuffer%s=collections.deque([0.0]*self._bufsize_a, self._bufsize_a)" % (x)
			exec "self.ACH%s_buf=np.zeros(self._bufsize_a, dtype=np.float)" % (x)
		""" Beta """
		for x in range(1, 15):
			exec "self.Bdatabuffer%s=collections.deque([0.0]*self._bufsize_b, self._bufsize_b)" % (x)
			exec "self.BCH%s_buf=np.zeros(self._bufsize_b, dtype=np.float)" % (x)
		""" Mu """
		for x in range(1, 15):
			exec "self.Idatabuffer%s=collections.deque([0.0]*self._bufsize_i, self._bufsize_i)" % (x)
			exec "self.ICH%s_buf=np.zeros(self._bufsize_i, dtype=np.float)" % (x)
		""" EMG """
		for x in range(1, 15):
			exec "self.Mdatabuffer%s=collections.deque([0.0]*self._bufsize_m, self._bufsize_m)" % (x)
			exec "self.MCH%s_buf=np.zeros(self._bufsize_m, dtype=np.float)" % (x)
		""" linking paths y buttons """
		""" temp profile und Folders dict """
		self.temp_proff = {'name':'NA' , 'age':'NA' , 'gender':'NA'}
		self.temp_foldering = {'Test_1_A':0,'Test_1_B':0,
		'Left_Movement':0,'Right_Movement':0,'Left_Wink':0,
		'Right_Wink':0,'Standard':0,'Offline':0,'EOG':0}
		self.temp_profile   = {'Test_1_A':0,'Test_1_B':0,
		'Left_Movement':0,'Right_Movement':0,'Left_Wink':0,
		'Right_Wink':0,'Standard':0,'Offline':0,'EOG':0}
		for x, val_temp in enumerate(list(self.temp_foldering),start=1):
			self.temp_foldering[val_temp] = {'1':0,'2':0,'3':0,'4':0,
			'5':0}
		sld1 = self.push_Iniciar
		sld2 = self.push_Finalizar
		sld3 = self.push_Salir
		sld4 = self.push_alfa_ini
		sld5 = self.push_beta_ini
		sld6 = self.push_mu_ini
		sld7 = self.push_wink_ini
		sld8 = self.Folder_A
		sld10 = self.Folder_Mu
		sld12 = self.label_proname
		sld13 = self.label_proage
		sld14 = self.label_prosex
		sld15 = self.push_processing
		sld16 = self.push_Ckstatus
		sld17 = self.push_saving
		sld18 = self.push_A_plot
		sld19 = self.push_B_plot
		sld20 = self.push_Mu_plot
		sld21 = self.push_EMG_plot
		sld1.clicked.connect(self._Iniciar)
		sld2.clicked.connect(self._Pausado)
		sld3.clicked.connect(self._Salida)
		sld4.clicked.connect(self._Iniciar_alfa)
		sld5.clicked.connect(self._Iniciar_beta)
		sld6.clicked.connect(self._Iniciar_mu)
		sld7.clicked.connect(self._Iniciar_emg)
		sld8.editingFinished.connect(self._Foldering_A)
		sld10.editingFinished.connect(self._Foldering_Mu)
		sld12.editingFinished.connect(self._input_proname)
		sld13.editingFinished.connect(self._input_proage)
		sld14.editingFinished.connect(self._input_prosex)
		sld15.clicked.connect(self._Iniciar_Processing)
		sld16.clicked.connect(self._Iniciar_Check)
		sld17.clicked.connect(self._Iniciar_Save)
		sld18.clicked.connect(self._plot_A)
		sld19.clicked.connect(self._plot_B)
		sld20.clicked.connect(self._plot_Mu)
		sld21.clicked.connect(self._plot_EMG)
		self.linking = LinkingPath()
		self.linking.patcher_Battery.connect(self.print_Battery)
		self.linking.patcher_Quality.connect(self.print_Quality)
		self.linking.patcher_Gyros.connect(self.print_Gyros)
		self.linking.patcher_Trial.connect(self.print_Trial)
	""" Plotting """
	def _plot_A(self):
		if self.A_selec_ME.isChecked():
			A_dir = 'Test_1_A'
		_A_chann = ['O1','O2','F3','F4','FC5','FC6','AF3','AF4','F7',
		'F8']
		_type = 'Alpha'
		try:plt_ch(self, A_dir, self.folder_of_a,_type,_A_chann)
		except UnboundLocalError: self.label_prompt.setText("Seleccione la opcion de Meditacion")
		except AttributeError: self.label_prompt.setText("Escriba numero de trial de 1 a 5")
	def _plot_B(self):
		if self.B_selec_RS.isChecked():
			B_dir = 'Test_1_B'
		elif self.B_selec_RS_S.isChecked():
			B_dir = 'Standard'
		elif self.B_selec_RS_O.isChecked():
			B_dir = 'Offline'
		_B_chann = ['O1','O2','F3','F4','FC5','FC6','AF3','AF4','F7',
		'F8']
		_type = 'Beta'
		try:plt_ch_beta(self, B_dir,_type,_B_chann)
		except UnboundLocalError: self.label_prompt.setText("Seleccione la opcion de Concentracion")
	def _plot_Mu(self):
		if self.Mu_selec_LH.isChecked():
			Mu_dir = 'Left_Movement'
		elif self.Mu_selec_RH.isChecked():
			Mu_dir = 'Right_Movement'
		_Mu_chann = ['O1','O2','F3','F4','FC5','FC6','AF3','AF4','F7',
		'F8']
		_type = 'Mu'
		try:plt_ch(self, Mu_dir, self.folder_of_mu,_type,_Mu_chann)
		except UnboundLocalError: self.label_prompt.setText("Seleccione la opcion de Motor Imagery")
		except AttributeError: self.label_prompt.setText("Escriba numero de trial de 1 a 5")
	def _plot_EMG(self):
		if self.MG_selec_WL.isChecked():
			EMG_dir = 'Left_Wink'
		elif self.MG_selec_WR.isChecked():
			EMG_dir = 'Right_Wink'
		elif self.MG_selec_EOG.isChecked():
			EMG_dir = 'EOG'
		_EMG_chann = ['O1','O2','F3','F4','FC5','FC6','AF3','AF4','F7',
		'F8']
		_type = 'EMG'
		try:plt_ch_emg(self, EMG_dir,_type,_EMG_chann)
		except UnboundLocalError: self.label_prompt.setText("Seleccione la opcion de Winking")

	""" Foldering """
	def _Foldering_A(self):
		self.folder_of_a = self.Folder_A.text()
	def _Foldering_Mu(self):
		self.folder_of_mu = self.Folder_Mu.text()
	def _input_proname(self):
		self.input_of_name = self.label_proname.text()
		self.temp_proff['name'] = self.input_of_name
	def _input_proage(self):
		self.input_of_age = self.label_proage.text()
		self.temp_proff['age'] = self.input_of_age
	def _input_prosex(self):
		self.input_of_sex = self.label_prosex.text()
		self.temp_proff['gender'] = self.input_of_sex
	""" Init alpha """
	def _Iniciar_alfa(self):
		self.alfa = True
	""" Init beta """
	def _Iniciar_beta(self):
		self.beta = True       
	""" Init Mu """
	def _Iniciar_mu(self):
		self.mu = True
	""" Init EMG """
	def _Iniciar_emg(self):
		self.emg = True
	""" Init Processing """
	def _Iniciar_Processing(self):
		feat_extract_(self, self.temp_proff['name'])
	""" Init Checking """
	def _Iniciar_Check(self):
		self.temp_foldering = check_prof(self,self.temp_proff,
		self.temp_foldering)
	""" Init Saving """
	def _Iniciar_Save(self):
		save_prof(self,self.temp_proff, self.temp_foldering)
	""" Init Pausado """
	def _Pausado(self):
		self.continuidad = False
	""" Exit of the program """
	def _Salida(self):
		self.continuidad = False
		self.alfa = False
		self.beta = False
		self.mu = False
		self.emg = False
		QCoreApplication.instance().quit()
	""" Init of the cicles """
	def _Iniciar(self):
		self.continuidad = True
		self.alfa = False
		self.beta = False
		self.mu = False
		self.emg = False
		threads = []
		cycle1 = Thread(target = self.update_battery)
		cycle2 = Thread(target = self.update_Quality_n_Value)
		cycle3 = Thread(target = self.update_Gyros)
		threads.append(cycle1)
		threads.append(cycle2)
		threads.append(cycle3)
		cycle1.start()
		cycle2.start()
		cycle3.start()
	""" Battery Value """
	def print_Battery(self, BattValue):
		if 0 < BattValue < 100:
			self.progressBar_Bat.setValue(BattValue)
			ColorBatt(self, BattValue)
	""" Progress of trial Value """
	def print_Trial(self, BattValue):
		self.progressBar_Trial.setValue(BattValue)
	""" Gyroscope Value """
	def print_Gyros(self, GyroX):
		self.label_GyroX.setNum(GyroX)
	""" Sensor's Quality """			
	def print_Quality(self,CH1,CH2,CH3,CH4,CH5,CH6,CH7,CH8,CH9,CH10,
	CH11,CH12,CH13,CH14):
		for x, CH_S in enumerate([CH1,CH2,CH3,CH4,CH5,CH6,CH7,CH8,CH9,
		CH10,CH11,CH12,CH13,CH14],start=1):
			exec "tmp%s=ColorAdjust(self, CH_S)" % (x)
		ColorChannelQuality(self,tmp1,tmp2,tmp3,tmp4,tmp5,tmp6,tmp7,
		tmp8,tmp9,tmp10,tmp11,tmp12,tmp13,tmp14)
	""" Cycle of Battery """
	def update_battery(self):
		headset = Emotiv(display_output=False)
		spawn(headset.setup)
		try:
			while self.continuidad:
				packet = headset.dequeue()
				BattValue = packet.battery
				self.linking.patch_Battery(BattValue)
		except Exception:
			self.label_prompt.setText("Inserte la USB del EPOC")
		finally:
			headset.close()
	""" Cycle of Gyros """
	def update_Gyros(self):
		headset = Emotiv(display_output=False)
		spawn(headset.setup)
		try:
			while self.continuidad:
				packet = headset.dequeue()
				GyroX = packet.gyro_x
				self.linking.patch_Gyros(GyroX)
		except Exception:
			self.label_prompt.setText("Inserte la USB del EPOC")
		finally:
			headset.close()
	""" Cycle of Quality and Values """
	def update_Quality_n_Value(self):
		headset = Emotiv(display_output=False)
		spawn(headset.setup)
		try:
			while self.continuidad:
				packet = headset.dequeue()
				for x, name_val in enumerate(['O1','O2','P7','P8','F3',
				'F4','T7','T8','FC5','FC6','F7','F8','AF3',
				'AF4'],start=1):
					exec "CH%s = packet.sensors[name_val]" % (x)
				for x, val_q in enumerate([CH1,CH2,CH3,CH4,CH5,CH6,CH7,
				CH8,CH9,CH10,CH11,CH12,CH13,CH14],start=1):
					exec "CH%s_q = val_q['quality']" % (x)
				self.linking.patch_Quality(CH1_q,CH2_q,CH3_q,CH4_q,
				CH5_q,CH6_q,CH7_q,CH8_q,CH9_q,CH10_q,CH11_q,CH12_q,
				CH13_q,CH14_q)
				""" ---------------Analisis de Alpha --------------- """
				if self.alfa:
					self.i += 1
					self.linking.patch_Trial(self.i)
					for x, val_v in enumerate([CH1,CH2,CH3,CH4,CH5,CH6,
					CH7,CH8,CH9,CH10,CH11,CH12,CH13,CH14],start=1):
						exec "self.Adatabuffer%s.append(val_v['value'])" % (x)
					""" Check the directory """
					if self.A_selec_ME.isChecked():
						A_dir = 'Test_1_A'
						cur_cy_1 = alfa_closede; cur_cy_2 = donothing
					if self.i in self._act_rel:cur_cy_1(self)
					if self.i in self._non_rel:cur_cy_2(self)
					if self.i == self._hm_rel:
#					if self.i == 10:
						savinginfo(self)
						""" Load the buffers """
						for x, val_v in enumerate([self.Adatabuffer1,
						self.Adatabuffer2,self.Adatabuffer3,
						self.Adatabuffer4,self.Adatabuffer5,
						self.Adatabuffer6,self.Adatabuffer7,
						self.Adatabuffer8,self.Adatabuffer9,
						self.Adatabuffer10,self.Adatabuffer11,
						self.Adatabuffer12,self.Adatabuffer13,
						self.Adatabuffer14],start=1):
							exec "self.ACH%s_buf[:] = val_v" % (x)
							for x, name_val in enumerate(["O1","O2",
							"P7","P8","F3","F4","T7","T8","FC5","FC6",
							"F7","F8","AF3","AF4"],start=1):
								exec "savemat('channels/Alpha/%s/%s/%s.mat',{'%s':self.ACH%s_buf}, do_compression=1)" %(A_dir,self.folder_of_a,name_val,name_val,x)
							""" Finished """
#					if self.i == 20:
					if self.i == self._sv_rel:
						finito(self)
						self.alfa = False
						self.beta = False
						self.mu = False
						self.emg = False
						self.temp_foldering[A_dir][str(self.folder_of_a)]=1
						ChckFolders(self,A_dir,
						sum(self.temp_foldering[A_dir].values()))
						if sum(self.temp_foldering[A_dir].values())==5:
							self.temp_profile[A_dir] = 1
						self.i = 0
						self.linking.patch_Trial(self.i)
				""" ---------------Analisis de Beta --------------- """
				if self.beta:
					self.i += 1
					self.linking.patch_Trial(self.i/12)
					for x, val_v in enumerate([CH1,CH2,CH3,CH4,CH5,CH6,
					CH7,CH8,CH9,CH10,CH11,CH12,CH13,CH14],start=1):
						exec "self.Bdatabuffer%s.append(val_v['value'])" % (x)
					""" Check the directory """
					if self.B_selec_RS.isChecked():
						B_dir = 'Test_1_B'
						cur_cy_1 = beta_rest; cur_cy_2 = donothing
					elif self.B_selec_RS_S.isChecked():
						B_dir = 'Standard'
						cur_cy_1 = standard_re; cur_cy_2 = standard_re
					elif self.B_selec_RS_O.isChecked():
						B_dir = 'Offline'
						cur_cy_1 = offline_re; cur_cy_2 = offline_re
					if self.i in self._act_con:cur_cy_1(self)
					if self.i in self._non_con:cur_cy_2(self)
					if self.i == self._hm_con:
						savinginfo(self)
						""" Load the buffers """
						for x, val_v in enumerate([self.Bdatabuffer1,
						self.Bdatabuffer2,self.Bdatabuffer3,
						self.Bdatabuffer4,self.Bdatabuffer5,
						self.Bdatabuffer6,self.Bdatabuffer7,
						self.Bdatabuffer8,self.Bdatabuffer9,
						self.Bdatabuffer10,self.Bdatabuffer11,
						self.Bdatabuffer12,self.Bdatabuffer13,
						self.Bdatabuffer14],start=1):
							exec "self.BCH%s_buf[:] = val_v" % (x)
						for x, name_val in enumerate(["O1","O2","P7",
						"P8","F3","F4","T7","T8","FC5","FC6","F7",
						"F8","AF3","AF4"],start=1):
							exec "savemat('channels/Beta/%s/%s.mat',{'%s':self.BCH%s_buf}, do_compression=1)" %(B_dir,name_val,name_val,x)
						""" Finished """
					if self.i == self._sv_con:
						finito(self)
						self.alfa = False
						self.beta = False
						self.mu = False
						self.emg = False
						for x in range(1,6):
							self.temp_foldering[B_dir][str(x)] = 1
						ChckFolders(self,B_dir,
						sum(self.temp_foldering[B_dir].values()))
						if sum(self.temp_foldering[B_dir].values())==5:
							self.temp_profile[B_dir] = 1
						self.i = 0
						self.linking.patch_Trial(self.i)
				""" ---------------Analisis de Mu --------------- """
				if self.mu:
					self.i += 1
					self.linking.patch_Trial(self.i)
					for x, val_v in enumerate([CH1,CH2,CH3,CH4,CH5,CH6,
					CH7,CH8,CH9,CH10,CH11,CH12,CH13,CH14],start=1):
						exec "self.Idatabuffer%s.append(val_v['value'])" % (x)
					""" Check the directory """
					if self.Mu_selec_LH.isChecked():
						Mu_dir = 'Left_Movement'
						cur_cy_1=mu_onleft;cur_cy_2=donothing;
						cur_cy_3=mu_onleft;cur_cy_4=donothing
					elif self.Mu_selec_RH.isChecked():
						Mu_dir = 'Right_Movement'
						cur_cy_1=mu_onright;cur_cy_2=donothing;
						cur_cy_3=mu_onright;cur_cy_4=donothing
					if self.i in self._act_con:cur_cy_1(self)
					if self.i in self._non_con:cur_cy_2(self)
					if self.i == self._hm_mu:
						savinginfo(self)
						""" Load the buffers """
						for x, val_v in enumerate([self.Idatabuffer1,
						self.Idatabuffer2,self.Idatabuffer3,
						self.Idatabuffer4,self.Idatabuffer5,
						self.Idatabuffer6,self.Idatabuffer7,
						self.Idatabuffer8,self.Idatabuffer9,
						self.Idatabuffer10,self.Idatabuffer11,
						self.Idatabuffer12,self.Idatabuffer13,
						self.Idatabuffer14],start=1):
							exec "self.ICH%s_buf[:] = val_v" % (x)
						for x, name_val in enumerate(["O1","O2","P7",
						"P8","F3","F4","T7","T8","FC5","FC6","F7","F8",
						"AF3","AF4"],start=1):
							exec "savemat('channels/Mu/%s/%s/%s.mat',{'%s':self.ICH%s_buf}, do_compression=1)" %(Mu_dir,self.folder_of_mu,name_val,name_val,x)
					""" Finished """
					if self.i == self._sv_mu:
						finito(self)
						self.alfa = False
						self.beta = False
						self.mu = False
						self.emg = False
						self.temp_foldering[Mu_dir][str(self.folder_of_mu)]=1
						ChckFolders(self,Mu_dir,
						sum(self.temp_foldering[Mu_dir].values()))
						if sum(self.temp_foldering[Mu_dir].values())==5:
							self.temp_profile[Mu_dir] = 1
						self.i = 0
						self.linking.patch_Trial(self.i)
				""" ---------------Analisis de Arctifacts --------------- """
				if self.emg:
					self.i += 1
					self.linking.patch_Trial(self.i/2)
					for x, val_v in enumerate([CH1,CH2,CH3,CH4,CH5,CH6,
					CH7,CH8,CH9,CH10,CH11,CH12,CH13,CH14],start=1):
						exec "self.Mdatabuffer%s.append(val_v['value'])" % (x)
					""" Check the directory """
					if self.MG_selec_WL.isChecked():
						EMG_dir = 'Left_Wink'
						cur_cy_1 = emg_wleft; cur_cy_2 = standard_re
					elif self.MG_selec_WR.isChecked():
						EMG_dir = 'Right_Wink'
						cur_cy_1 = emg_wright; cur_cy_2 = standard_re
					elif self.MG_selec_EOG.isChecked():
						EMG_dir = 'EOG'
						cur_cy_1 = _eog; cur_cy_2 = standard_re
					if self.i in self._act_emg:cur_cy_1(self)
					if self.i in self._non_emg:cur_cy_2(self)
					if self.i == self._hm_emg:
						savinginfo(self)
						""" Load the buffers """
						for x, val_v in enumerate([self.Mdatabuffer1,
						self.Mdatabuffer2,self.Mdatabuffer3,
						self.Mdatabuffer4,self.Mdatabuffer5,
						self.Mdatabuffer6,self.Mdatabuffer7,
						self.Mdatabuffer8,self.Mdatabuffer9,
						self.Mdatabuffer10,self.Mdatabuffer11,
						self.Mdatabuffer12,self.Mdatabuffer13,
						self.Mdatabuffer14],start=1):
							exec "self.MCH%s_buf[:] = val_v" % (x)
						for x, name_val in enumerate(["O1","O2","P7",
						"P8","F3","F4","T7","T8","FC5","FC6","F7",
						"F8","AF3","AF4"],start=1):
							exec "savemat('channels/EMG/%s/%s.mat',{'%s':self.MCH%s_buf}, do_compression=1)" %(EMG_dir,name_val,name_val,x)
					""" Finished """
					if self.i == self._sv_emg:
						finito(self)
						self.alfa = False
						self.beta = False
						self.mu = False
						self.emg = False
						for x in range(1,6):
							self.temp_foldering[EMG_dir][str(x)] = 1
						ChckFolders(self, EMG_dir, sum(self.temp_foldering[EMG_dir].values()))
						if sum(self.temp_foldering[EMG_dir].values()) == 5:
							self.temp_profile[EMG_dir] = 1
						self.i = 0
						self.linking.patch_Trial(self.i)
		except Exception:
			self.label_prompt.setText("Inserte la USB del EPOC")
		finally:
			headset.close()     

def main():
	app = QApplication(sys.argv)
	window = MainWindow()
	window.show()
	sys.exit(app.exec_())

if __name__ == '__main__':
	main()
