from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import QObject, pyqtSignal, pyqtSlot
from collections import deque
from sklearn import preprocessing
import numpy as np
from scipy.signal import butter, lfilter
from os import getcwd as getdir
from sklearn.externals import joblib
"""Import from within the files"""
from pyeeg import pfd,hjorth_mob
import armbot

class LinkingPath(QObject):
	patcher_WinkR = pyqtSignal(int,int)
	def __init__(self):
		QObject.__init__(self)
	def patch_WinkR(self,data1,data2):
		self.patcher_WinkR.emit(data1,data2)
class wink_work():
	def __init__(self,obj):
		self.epoc_samp = 128.0
		self.y = 6500
		self.dbuff2=deque([1]*7, 7)
		self.dir_user = str(getdir()+'/Profile/')
		self.clf_wright = joblib.load(self.dir_user+'/wrightSVM.pkl')
		self.scaler_wright = joblib.load(self.dir_user+'/wrightScaler.pkl')
		self.obj = obj
		self.linking = LinkingPath()
		self.linking.patcher_WinkR.connect(self.winkR)
		self.obj = obj
		self.highlght = QtGui.QPalette.Highlight
		self.greeny = QtGui.QColor(QtCore.Qt.green)
		self.bluey = QtGui.QColor(QtCore.Qt.blue)
		self.redy = QtGui.QColor(QtCore.Qt.red)
		self.armb = armbot.arm_bot()

	def dc2uV(self,val_):
		vaf_ = ( val_ - average(val_) )*0.51
		return vaf_

	def normalz(self,val_):
		vaf_ = preprocessing.scale(val_)
		return vaf_

	def emg_parametrs(self,val_):
		vaf_froben = linalg.norm(val_)/1000.0
		vaf_hjorth_mob = (hjorth_mob(val_))*10.0
		vaf_tt = array([vaf_froben,vaf_hjorth_mob])
		"""Value = ['Frobenius Norm','Hjorth Mobility']"""
		return vaf_tt

	def filtering(self,data):
		samprate = 128
		cutlow = 2.0
		nyq = samprate/2.0
		low = cutlow / nyq
		b,a = butter(5,low,btype='highpass',analog=0)
		data_f = lfilter(b,a,data)
		return data_f

	@pyqtSlot()
	def winkR(self,val,status):
		palette = QtGui.QPalette()
		self.dbuff2.append(val)
		acumm = int(self.dbuff2.count(0))
		self.obj.pB_WRight.setValue(acumm)
		if status and acumm >= 3:
			palette.setColor(self.highlght, self.redy)
			self.obj.pB_WRight.setPalette(palette)
			self.armb.WinR(True)
		else:
			palette.setColor(self.highlght, self.bluey)
			self.obj.pB_WRight.setPalette(palette)

	def WinkAction_R(self,Wink_val):
		if Wink_val == 0:
			self.linking.patch_WinkR(Wink_val,True)
		else:
			self.linking.patch_WinkR(Wink_val,False)
	def emg_processing(self,ch_):
		ch_ = self.dc2uV(ch_)
		ch_ = self.filtering(ch_)
		param_val = self.emg_parametrs(ch_)
		return param_val

	def svm_winkPro(self,val_):
		ch_scl = self.scaler_wright.transform(self.emg_processing(val_))
		curr_val = self.clf_wright.predict(ch_scl)
		self.WinkAction_R(curr_val[0])
