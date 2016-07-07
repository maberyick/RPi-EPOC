from PyQt4.QtGui import QPalette, QColor
from PyQt4.QtCore import Qt, QObject, pyqtSignal, pyqtSlot
from sklearn import preprocessing
import numpy as np
from scipy.signal import butter, lfilter, welch
from os import getcwd as getdir
from sklearn.externals import joblib
from collections import deque
"""Import from within the files"""
from pyeeg import hjorth_mob
import armbot

class LinkingPath(QObject):
	patcher_Alpha = pyqtSignal(int,int)
	def __init__(self):
		QObject.__init__(self)
	def patch_Alpha(self,data1,data2):
		self.patcher_Alpha.emit(data1,data2)
class alpha_work():
	def __init__(self,obj):
		self.epoc_samp = 128.0
		self.y = 6500
		self.dbuff3=deque([1]*8, 8)
		self.dir_user = str(getdir()+'/Profile/')
		self.clf_alpha = joblib.load(self.dir_user+'/alphaSVM.pkl')
		self.scaler_alpha = joblib.load(self.dir_user+'/alphaScaler.pkl')
		self.obj = obj
		self.linking = LinkingPath()
		self.linking.patcher_Alpha.connect(self.alpha)
		self.obj = obj
		self.highlght = QPalette.Highlight
		self.greeny = QColor(Qt.green)
		self.bluey = QColor(Qt.blue)
		self.redy = QColor(Qt.red)
		self.armb = armbot.arm_bot()

	def dc2uV(self,val_):
		vaf_ = ( val_ - np.average(val_) )*0.51
		return vaf_

	def normalz(self,val_):
		vaf_ = preprocessing.scale(val_)
		return vaf_

	def alpha_parametrs(self,val_):
		temp_val1 = []; temp_val2 = []
		fq_, px_ = welch(val_, nperseg=256, nfft=1023, fs = 128,
						noverlap=100, scaling='density'
						)
		fq1_up = 12.0;  fq1_dwn = 8.0
		fq2_up = 30.0;  fq2_dwn = 4.0
		for i in range(len(px_)):
			if   fq_[i]<=fq1_up and fq_[i]>=fq1_dwn:temp_val1.append(px_[i])
			elif fq_[i]<=fq2_up and fq_[i]>=fq2_dwn:temp_val2.append(px_[i])
		vaf_eng1 = sum(temp_val1)
		vaf_eng2 = sum(temp_val2)
		vaf_r = vaf_eng1 / vaf_eng2
		vaf_hjorth_mob = (hjorth_mob(val_))*10.0
		"""Value = ['Alpha Ratio','Hjorth mobility']"""
		vaf_tt = np.array([vaf_r,vaf_hjorth_mob])
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
	def alpha(self,val,status):
		palette = QPalette()
		self.dbuff3.append(val)
		acumm = int(self.dbuff3.count(0))
		self.obj.pB_Alpha.setValue(acumm)
		if status:
			palette.setColor(self.highlght, self.greeny)
			self.obj.pB_Alpha.setPalette(palette)
			if acumm >= 8:
				palette.setColor(self.highlght, self.redy)
				self.obj.pB_Alpha.setPalette(palette)
				self.armb.Alp(True)
		else:
			palette.setColor(self.highlght, self.bluey)
			self.obj.pB_Alpha.setPalette(palette)

	def AlphaAction(self,Alpha_val):
		if Alpha_val == 0:
			self.linking.patch_Alpha(Alpha_val,True)
		else:
			self.linking.patch_Alpha(Alpha_val,False)

	def alpha_processing(self,ch_):
		ch_ = self.dc2uV(ch_)
		ch_ = self.filtering(ch_)
		ch_ = self.normalz(ch_)
		param_val = self.alpha_parametrs(ch_)
		return param_val

	def svm_alphaPro(self,val_):
		ch_scl = self.scaler_alpha.transform(self.alpha_processing(val_))
		curr_val = self.clf_alpha.predict(ch_scl)
		self.AlphaAction(curr_val[0])
