from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import QObject, pyqtSignal, pyqtSlot
from scipy import mean
from sklearn import preprocessing
import numpy as np
from scipy.signal import butter, lfilter, welch
from os import getcwd as getdir
from sklearn.externals import joblib
from collections import deque
from pygame import mixer
"""Import from within the files"""
from pyeeg import pfd,hjorth_com,hjorth_mob
import armbot

mixer.init()
alert2 = mixer.Sound('Library/snd2.wav')

class LinkingPath(QObject):
	patcher_WinkL = pyqtSignal(int,int)
	patcher_Beta =  pyqtSignal(int,int)
	def __init__(self):
		QObject.__init__(self)
	def patch_WinkL(self,data1,data2):
		self.patcher_WinkL.emit(data1,data2)
	def patch_Beta(self,data1,data2):
		self.patcher_Beta.emit(data1,data2)
class beta_work():
	def __init__(self,obj):
		self.epoc_samp = 128.0
		self.y = 6500
		self.dbuff1=deque([1]*7, 7)
		self.dbuff4=deque([1]*15, 15)
		self.dir_user = str(getdir()+'/Profile/')
		self.clf_beta=joblib.load(self.dir_user+'/betaSVM.pkl')
		self.scaler_beta=joblib.load(self.dir_user+'/betaScaler.pkl')
		self.clf_wleft=joblib.load(self.dir_user+'/wleftSVM.pkl')
		self.scaler_wleft=joblib.load(self.dir_user+'/wleftScaler.pkl')
		self.obj = obj
		self.linking = LinkingPath()
		self.linking.patcher_Beta.connect(self.beta)
		self.linking.patcher_WinkL.connect(self.winkL)
		self.obj = obj
		self.highlght = QtGui.QPalette.Highlight
		self.greeny = QtGui.QColor(QtCore.Qt.green)
		self.bluey = QtGui.QColor(QtCore.Qt.blue)
		self.redy = QtGui.QColor(QtCore.Qt.red)
		self.armb = armbot.arm_bot()

	def dc2uV(self,val_):
		vaf_ = ( val_ - np.average(val_) )*0.51
		return vaf_

	def normalz(self,val_):
		vaf_ = preprocessing.scale(val_)
		return vaf_

	def emg_parametrs(self,val_):
		vaf_froben = np.linalg.norm(val_)/1000.0
		vaf_hjorth_mob = (hjorth_mob(val_))*10.0
		vaf_tt = np.array([vaf_froben,vaf_hjorth_mob])
		"""Value = ['Frobenius Norm','Hjorth Mobility']"""
		return vaf_tt

	def beta_parametrs(self,val_):
		temp_val1 = []; temp_val2 = []
		fq_, px_ = welch(val_, nperseg=256, nfft=1023, fs = 128,
						noverlap=100, scaling='density'
						)
		fq1_up = 38.0; fq1_dwn = 20.0
		fq2_up = 42.0;  fq2_dwn = 14.0
		for i in range(len(px_)):
			if fq_[i]<=fq1_up and fq_[i]>=fq1_dwn:temp_val1.append(px_[i])
			elif fq_[i]<=fq2_up and fq_[i]>=fq2_dwn:temp_val2.append(px_[i])
		vaf_eng1 = sum(temp_val1)
		vaf_eng2 = sum(temp_val2)
		vaf_r = vaf_eng1 / vaf_eng2
		vaf_pfd = pfd(val_)
		vaf_hjorth_mob = (hjorth_mob(val_))*10.0
		"""Value = ['beta ratio','Petrosian Fractal Dimension','Hjorth Mobility']"""
		vaf_tt = np.array([vaf_r,vaf_pfd,vaf_hjorth_mob])
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
	def winkL(self,val,status):
		palette = QtGui.QPalette()
		self.dbuff1.append(val)
		acumm = int(self.dbuff1.count(0))
		self.obj.pB_WLeft.setValue(acumm)
		if status and acumm >= 3:
			palette.setColor(self.highlght, self.redy)
			self.obj.pB_WLeft.setPalette(palette)
			self.armb.WinL(True)
		else:
			palette.setColor(self.highlght, self.bluey)
			self.obj.pB_WLeft.setPalette(palette)

	@pyqtSlot()
	def beta(self,val,status):
		palette = QtGui.QPalette()
		self.dbuff4.append(val)
		acumm = int(self.dbuff4.count(0))
		self.obj.pB_Beta.setValue(acumm)
		if status:
			palette.setColor(self.highlght, self.greeny)
			self.obj.pB_Beta.setPalette(palette)
			if acumm >= 10:
				alert2.play()
				palette.setColor(self.highlght, self.redy)
				self.obj.pB_Beta.setPalette(palette)
				self.armb.Bet(True)
		else:
			palette.setColor(self.highlght, self.bluey)
			self.obj.pB_Beta.setPalette(palette)

	def BetaAction(self,Beta_val):
		if Beta_val == 0:
			self.linking.patch_Beta(Beta_val,True)
		else:
			self.linking.patch_Beta(Beta_val,False)

	def WinkAction_L(self,Wink_val):
		if Wink_val == 0:
			self.linking.patch_WinkL(Wink_val,True)
		else:
			self.linking.patch_WinkL(Wink_val,False)

	def beta_processing(self,ch_):
		ch_ = self.dc2uV(ch_)
		ch_ = self.filtering(ch_)
		ch_ = self.normalz(ch_)
		param_val = self.beta_parametrs(ch_)
		return param_val

	def emg_processing(self,ch_):
		ch_ = self.dc2uV(ch_)
		ch_ = self.filtering(ch_)
		param_val = self.emg_parametrs(ch_)
		return param_val

	def svm_betaPro(self,val_):
		ch_scl_1=self.scaler_beta.transform(self.beta_processing(val_))
		ch_scl_2=self.scaler_wleft.transform(self.emg_processing(val_))
		curr_val_1 = self.clf_beta.predict(ch_scl_1)
		curr_val_2 = self.clf_wleft.predict(ch_scl_2)
		self.BetaAction(curr_val_1[0])
		self.WinkAction_L(curr_val_2[0])
