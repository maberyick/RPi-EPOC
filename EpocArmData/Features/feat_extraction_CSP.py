from scipy import mean
from copy import copy
import matplotlib.mlab as mlab
from pylab import psd
import csv
import os.path
from itertools import islice
import time
from sklearn import preprocessing
import numpy as np
from scipy.fftpack import fft, rfftfreq, ifft, rfft, irfft
from scipy.signal import hanning, hann, hamming, blackman
from scipy.signal import butter, lfilter, filtfilt, welch, resample
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from scipy import signal
from numpy.linalg import inv
import time as timpo
from os import getcwd as getdir
from os import path as pth
from Library.pyeeg import pfd,hjorth_com,hjorth_mob,hurst
from scipy.io import savemat
import sys
from PyQt4 import QtCore, QtGui
from os.path import exists
from matplotlib.patches import Polygon
import matplotlib.patches as mpatches
from scipy.io import savemat, whosmat, loadmat
from Library import loadmat_new
import random as rndm
from itertools import chain
import collections
from matplotlib.colors import Normalize
from sklearn.preprocessing import StandardScaler
from sklearn.cross_validation import StratifiedShuffleSplit
from sklearn.cross_validation import train_test_split
from sklearn.grid_search import GridSearchCV
from sklearn.metrics import classification_report
from sklearn.svm import SVC
from sklearn.externals import joblib

"""---------------------------------------------------------------------
					Alpha
|EEG|-|remove_DC|-|uV_convert|-|Filter|-|epoching|-|Scale|-|Extract Features|-|Save|
Alpha Ratio			[Active(High) vs Standard(Low)]
Hjorth complexity 	[Active(High) vs Standard(Low)]
					Beta
|EEG|-|remove_DC|-|uV_convert|-|Filter|-|epoching|-|Scale|-|Extract Features|-|Save|
Beta+Gamma Ratio				[Active(High) vs Standard(Low)]
Petrosian Fractal Dimension 	[Active(High) vs Standard(Low)]
					EMG
|EMG|-|remove_DC|-|uV_convert|-|Filter|-|epoching|-|Extract Features|-|Save|
Frobenius Norm		[Active(High) vs Standard(Low)]
Hjorth complexity 	[Active(High) vs Standard(Low)]
---------------------------------------------------------------------"""
#-------------------------- Constants ----------------------------------
dir_wrk = getdir()
dir_fol = ['1','2','3','4','5','6','7','8','9','10']
dir_fol_emg = ['1','2','3','4','5']
cs0 = [0,3,4,7,8,11,12,15,16,19,20,23,24,27,28]
cs1 = [1,2,5,6,9,10,13,14,17,18,21,22,25,26,29]
cs0_b = [0,1,4,5,8,9,12,13,16,17,20,21,24,25,28,29]
cs1_b = [2,3,6,7,10,11,14,15,18,19,22,23,26,27,30,31]
emg_channel = ['AF3','AF4'];emg_folder = ['Left_Wink','Right_Wink']
classes = {'active','nonactive','standard','offline'}
classes_emg = {'active','standard','offline','eog'}
classes_ext = {'eog','emg'}
train_n = 100; total_n = 150;data_n = 100; test_n = 50
train_n_alfa = 50; total_n_alfa = 75;data_n_alfa = 50; test_n_alfa = 25
train_n_emg = 50; total_n_emg = 75;data_n_emg = 50; test_n_emg = 25
train_n_beta = 128; total_n_beta = 192;data_n_beta = 128; test_n_beta = 64
numClss = 4;
Dists = ['Active',' non-Active', 'Standard', 'Offline']
Dists_b = ['Active',' non-Active', 'Standard', 'Offline', 'EOG', 'EMG-Wink']
Dists_emg = ['Active', 'Standard', 'Offline', 'EOG']
seq_ = [];seq_b = []; seq_m = []
for x in range(total_n):exec "seq_.append('part_%s')" % (x)
for x in range(total_n_beta):exec "seq_b.append('part_%s')" % (x)
for x in range(total_n_emg):exec "seq_m.append('part_%s')" % (x)
#---------------------------- Plot Normalizer --------------------------
class MidpointNormalize(Normalize):

    def __init__(self, vmin=None, vmax=None, midpoint=None, clip=False):
        self.midpoint = midpoint
        Normalize.__init__(self, vmin, vmax, clip)

    def __call__(self, value, clip=None):
        x, y = [self.vmin, self.midpoint, self.vmax], [0, 0.5, 1]
        return np.ma.masked_array(np.interp(value, x, y))
#--------------------------- HPF ---------------------------------------
def filtering(data):
	samprate = 128
	cutlow = 2.0
	nyq = samprate/2.0
	low = cutlow / nyq
	b,a = butter(5,low,btype='highpass',analog=0)
	data_f = filtfilt(b,a,data)
	return data_f
#--------------------------- Alpha Parameters --------------------------
def parametrs_alpha(val_):
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
	vaf_hjorth_com = (hjorth_com(val_))/100.0
	vaf_tt = {'a1_ratio':vaf_r,'hjr_com':vaf_hjorth_com}
	return vaf_tt
#--------------------------- Beta Parameters --------------------------
def parametrs_beta(val_):
	temp_val1 = []; temp_val2 = []
	fq_, px_ = welch(val_, nperseg=256, nfft=1023, fs = 128,
					noverlap=100, scaling='density'
					)
	# BETA 3 + GAMMA
	fq1_up = 38.0;  fq1_dwn = 20.0
	# DIV RANGE
	fq2_up = 42.0;  fq2_dwn = 14.0
	for i in range(len(px_)):
		if   fq_[i]<=fq1_up and fq_[i]>=fq1_dwn:temp_val1.append(px_[i])
		elif fq_[i]<=fq2_up and fq_[i]>=fq2_dwn:temp_val2.append(px_[i])
	vaf_eng1 = sum(temp_val1)
	vaf_eng2 = sum(temp_val2)
	vaf_r = vaf_eng1 / vaf_eng2
	vaf_pfd = pfd(val_)
	vaf_hjorth_mob = (hjorth_mob(val_))*10.0
#	vaf_hjorth_com = (hjorth_com(val_))/100.0
#	vaf_tt = {'a1_ratio':vaf_r,'pfd':vaf_pfd}
	vaf_tt = {'a1_ratio':vaf_r,'pfd':vaf_pfd, 'vaf_hjorth_mob': vaf_hjorth_mob}
	return vaf_tt
#--------------------------- EMG Parameters ----------------------------
def parametrs_emg(val_):
	vaf_froben = np.linalg.norm(val_)
	vaf_hjorth_com = hjorth_com(val_)
	vaf_tt = {'a1_froben':vaf_froben, 'a2_hjorth':vaf_hjorth_com}
	return vaf_tt
#--------------------------- Prepros (no DC level (uV) )----------------
def dc2uV(val_):
	vaf_ = ( val_ - np.average(val_) )*0.51
	return vaf_
#--------------------------- Normalization -----------------------------
def normalz(val_):
	vaf_ = preprocessing.scale(val_)
	return vaf_
#-------------------------- Dictionar ----------------------------------
def dic_values_alfa():
	dic_fol={'folder_1':0,'folder_2':0,'folder_3':0,'folder_4':0,
	'folder_5':0}
	dic_fol_st = {'folder_1':0,'folder_2':0,'folder_3':0,'folder_4':0,
	'folder_5':0}
	dic_fol_of = {'folder_1':0,'folder_2':0,'folder_3':0,'folder_4':0,
	'folder_5':0}
	seq_ = []
	for x in range(75):exec "seq_.append('part_%s')" % (x)
	dic_active = dict.fromkeys(seq_,0)
	dic_nonactive = dict.fromkeys(seq_,0)
	dic_standard = dict.fromkeys(seq_,0)
	dic_offline = dict.fromkeys(seq_,0)
	return dic_fol,dic_fol_st,dic_fol_of,dic_active,dic_nonactive,dic_standard,dic_offline
def dic_values_emg():
	seq_ = []
	for x in range(75):exec "seq_.append('part_%s')" % (x)
	dic_active = dict.fromkeys(seq_,0)
	dic_standard = dict.fromkeys(seq_,0)
	dic_offline = dict.fromkeys(seq_,0)
	dic_eog = dict.fromkeys(seq_,0)
	return dic_active,dic_standard,dic_offline,dic_eog
def dic_values_beta():
	seq_ = [];seq_a = []
	for x in range(192):exec "seq_.append('part_%s')" % (x)
	for x in range(75):exec "seq_a.append('part_%s')" % (x)
	dic_active = dict.fromkeys(seq_,0)
	dic_nonactive = dict.fromkeys(seq_,0)
	dic_standard = dict.fromkeys(seq_,0)
	dic_offline = dict.fromkeys(seq_,0)
	dic_eog = dict.fromkeys(seq_a,0)
	dic_emg = dict.fromkeys(seq_a,0)
	return dic_active,dic_nonactive,dic_standard,dic_offline,dic_eog,dic_emg
#-------------------------- Save alpha parameters ----------------------
def alpha_extra_():
	active_ch=[];active_st=[];active_of=[];non_active_ch=[]
	dic_fol,dic_fol_st,dic_fol_of,dic_active,dic_nonactive,dic_standard,dic_offline = dic_values_alfa()
	for j, dir_name in enumerate(dic_fol):
		exec "ch_ = np.load('%s/channels/Alpha/Test_1_A/%s/O2.py')" %(dir_wrk,dir_fol_emg[j])
		len_st = [0,len(ch_),2*len(ch_),3*len(ch_),4*len(ch_),5*len(ch_)]
		exec "st_ = np.load('%s/channels/Beta/Standard/O2.py')" %(dir_wrk)
		st_ = st_[len_st[j]:len_st[j+1]]
		exec "of_ = np.load('%s/channels/Beta/Offline/O2.py')" %(dir_wrk)
		of_ = of_[len_st[j]:len_st[j+1]]
		#standard --
		st_ = dc2uV(st_)
		st_ = filtering(st_)
		st_ = np.split(st_,32)
		st_ = np.delete(st_,[0,31],0)
		#Offline --
		of_ = dc2uV(of_)
		of_ = filtering(of_)
		of_ = np.split(of_,32)
		of_ = np.delete(of_,[0,31],0)
		#channel --
		ch_ = dc2uV(ch_)
		ch_ = filtering(ch_)
		ch_ = np.split(ch_,32)
		ch_ = np.delete(ch_,[0,31],0)
		#-- normalize --
		for i in range(len(ch_)):
			ch_[i] = normalz(ch_[i])
			st_[i] = normalz(st_[i])
			of_[i] = normalz(of_[i])
		dic_fol[dir_name] = ch_
		dic_fol_st[dir_name] = st_
		dic_fol_of[dir_name] = of_
		#-- parameters --
	for k,dir_name in enumerate(dic_fol):
		for l in range(len(dic_fol[dir_name])):
			temp_val1 = parametrs_alpha(dic_fol[dir_name][l])
			temp_val2 = parametrs_alpha(dic_fol_st[dir_name][l])
			temp_val3 = parametrs_alpha(dic_fol_of[dir_name][l])
			if l in cs0:
				active_ch.append(temp_val1)
				active_st.append(temp_val2)
				active_of.append(temp_val3)
			elif l in cs1:
				non_active_ch.append(temp_val1)
	#-- archives --
	for x,seq_name in enumerate(dic_active):
		dic_active[seq_name] = active_ch[x]
		dic_nonactive[seq_name] = non_active_ch[x]
		dic_standard[seq_name] = active_st[x]
		dic_offline[seq_name] = active_of[x]
	exec "savemat('%s/Features/Parameters_files/Test_1_A.mat', {'active':dic_active,'nonactive':dic_nonactive,'standard':dic_standard,'offline':dic_offline}, do_compression=1)"  %(dir_wrk)
#-------------------------- Save Beta parameters -----------------------
def beta_extra_():
	active_ch=[];active_st=[];active_of=[];active_eo=[];active_em=[];non_active_ch=[]
	active_tmp=[];non_active_tmp=[];active_tmp_st=[];active_tmp_of=[]
	active_tmp_eo=[];active_tmp_em=[]
	dic_active,dic_nonactive,dic_standard,dic_offline,dic_eog,dic_emg = dic_values_beta()
	exec "ch_ = np.load('%s/channels/Beta/Test_1_B/AF3.py')" %(dir_wrk)
	exec "st_ = np.load('%s/channels/Beta/Standard/AF3.py')" %(dir_wrk)
	exec "of_ = np.load('%s/channels/Beta/Offline/AF3.py')" %(dir_wrk)
	exec "eo_ = np.load('%s/channels/EMG/EOG/AF3.py')" %(dir_wrk)
	exec "em_ = np.load('%s/channels/EMG/Left_Wink/AF3.py')" %(dir_wrk)
	#channel --
	ch_ = dc2uV(ch_)
	ch_ = filtering(ch_)
	ch_ = np.split(ch_,32)
	for i in range(len(ch_)):
		ch_n = np.delete(ch_[i],range(6143,6399),0)
		ch_n = np.split(ch_n,12)
		if i in cs0_b:
			for x in range(len(ch_n)):
				active_tmp.append(ch_n[x])
		elif i in cs1_b:
			for x in range(len(ch_n)):
				non_active_tmp.append(ch_n[x])
	#standard --
	st_ = dc2uV(st_)
	st_ = filtering(st_)
	st_ = np.split(st_,32)
	for i in range(len(st_)):
		st_n = np.delete(st_[i],range(6143,6399),0)
		st_n = np.split(st_n,12)
		if i in cs0_b:
			for x in range(len(st_n)):
				active_tmp_st.append(st_n[x])
	#Offline --
	of_ = dc2uV(of_)
	of_ = filtering(of_)
	of_ = np.split(of_,32)
	for i in range(len(of_)):
		of_n = np.delete(of_[i],range(6143,6399),0)
		of_n = np.split(of_n,12)
		if i in cs0_b:
			for x in range(len(of_n)):
				active_tmp_of.append(of_n[x])
	#EOG --
	eo_ = dc2uV(eo_)
	eo_ = filtering(eo_)
	eo_ = np.split(eo_,75)
	#EMG --
	em_ = dc2uV(em_)
	em_ = filtering(em_)
	em_ = np.split(em_,75)
		#-- normalize --
	for i in range(len(active_tmp)):
		active_tmp[i] = normalz(active_tmp[i])
		non_active_tmp[i] = normalz(non_active_tmp[i])
		active_tmp_st[i] = normalz(active_tmp_st[i])
		active_tmp_of[i] = normalz(active_tmp_of[i])
	for i in range(len(eo_)):
		eo_[i] = normalz(eo_[i])
		em_[i] = normalz(em_[i])
	#-- parameters --
	for l in range(len(active_tmp)):
		active_ch.append(parametrs_beta(active_tmp[l]))
		non_active_ch.append(parametrs_beta(non_active_tmp[l]))
		active_st.append(parametrs_beta(active_tmp_st[l]))
		active_of.append(parametrs_beta(active_tmp_of[l]))
	for l in range(len(eo_)):
		active_eo.append(parametrs_beta(eo_[l]))
		active_em.append(parametrs_beta(em_[l]))
	#-- archives --
	for x,seq_name in enumerate(dic_active):
		dic_active[seq_name] = active_ch[x]
		dic_nonactive[seq_name] = non_active_ch[x]
		dic_standard[seq_name] = active_st[x]
		dic_offline[seq_name] = active_of[x]
	for x,seq_name in enumerate(dic_eog):
		dic_eog[seq_name] = active_eo[x]
		dic_emg[seq_name] = active_em[x]
	exec "savemat('%s/Features/Parameters_files/Test_1_B.mat', {'active':dic_active,'nonactive':dic_nonactive,'standard':dic_standard,'offline':dic_offline,'eog':dic_eog,'emg':dic_emg}, do_compression=1)"  %(dir_wrk)
#-------------------------- Save EMG parameters ------------------------
def emg_extra_():
	for xx,yy in enumerate(emg_folder):
		active_ch=[];active_st=[];active_of=[];active_eo=[]
		dic_active,dic_standard,dic_offline,dic_eog = dic_values_emg()
		exec "ch_ = np.load('%s/channels/EMG/%s/%s.py')" %(dir_wrk,emg_folder[xx],emg_channel[xx])
		exec "eo_ = np.load('%s/channels/EMG/EOG/%s.py')" %(dir_wrk,emg_channel[xx])
		exec "st_ = np.load('%s/channels/Beta/Standard/%s.py')" %(dir_wrk,emg_channel[xx])
		exec "of_ = np.load('%s/channels/Beta/Offline/%s.py')" %(dir_wrk,emg_channel[xx])
		st_ = st_[0:len(ch_)]
		of_ = of_[0:len(ch_)]
		#standard --
		st_ = dc2uV(st_)
		st_ = filtering(st_)
		st_ = np.split(st_,75)
		#offline --
		of_ = dc2uV(of_)
		of_ = filtering(of_)
		of_ = np.split(of_,75)
		#eog --
		eo_ = dc2uV(eo_)
		eo_ = filtering(eo_)
		eo_ = np.split(eo_,75)
		#channel --
		ch_ = dc2uV(ch_)
		ch_ = filtering(ch_)
		ch_ = np.split(ch_,75)
		#-- parameters --
		for l in range(len(ch_)):
			temp_val1 = parametrs_emg(ch_[l])
			temp_val2 = parametrs_emg(st_[l])
			temp_val3 = parametrs_emg(of_[l])
			temp_val4 = parametrs_emg(eo_[l])
#			if l % 2 == 0:
			active_ch.append(temp_val1)
			active_st.append(temp_val2)
			active_of.append(temp_val3)
			active_eo.append(temp_val4)
#			else:
#				non_active_ch.append(temp_val1)
		#-- archives --
		for x,seq_name in enumerate(dic_active):
			dic_active[seq_name] = active_ch[x]
			dic_standard[seq_name] = active_st[x]
			dic_offline[seq_name] = active_of[x]
			dic_eog[seq_name] = active_eo[x]
		exec "savemat('%s/Features/Parameters_files/%s.mat', {'active':dic_active,'standard':dic_standard,'offline':dic_offline,'eog':dic_eog}, do_compression=1)"  %(dir_wrk,emg_folder[xx])
#-------------------------- Plotting of Alpha --------------------------
def plot_alpha_():
	for x,cls in enumerate(classes):
		exec "%s_ratio = []" % (cls)
		exec "%s_hjr = []" % (cls)
	#-------------------------------------------------------------------
	exec "mat_contents = loadmat_new.loadmat('%s/Features/Parameters_files/Test_1_A.mat')" %(dir_wrk)
	# 4 classes
	active = mat_contents['active'];
	nonactive = mat_contents['nonactive']
	standard = mat_contents['standard']
	offline = mat_contents['offline']
	#-------------------------------------------------------------------
	for y,cls in enumerate(classes):
		for x in range(total_n_alfa):
			exec "%s_ratio.append(%s[seq_[%s]]['a1_ratio'])" % (cls,cls,x)
			exec "%s_hjr.append(%s[seq_[%s]]['hjr_com'])" % (cls,cls,x)
	#-------------------------------------------------------------------
	data1 = [active_ratio, nonactive_ratio, standard_ratio, offline_ratio]
	data2 = [active_hjr, nonactive_hjr, standard_hjr, offline_hjr]
	#-------------------------------------------------------------------
	fig1, (ax1,ax2) = plt.subplots(2)
	for x in range(1,3):
		exec "bp%s = ax%s.boxplot(data%s, notch=1, sym='k+', vert=1)" %(x,x,x)
	#-------------------------------------------------------------------
	for x in range(1,3):
		exec "ax%s.yaxis.grid(True, linestyle='-', which='major', color='lightgrey',alpha=0.5)" %(x)
		exec "ax%s.xaxis.grid(True, linestyle='-', which='major', color='lightgrey',alpha=0.5)" %(x)
	fig1.canvas.set_window_title('Parametros de Alpha')
	ax1.set_axisbelow(True)
	ax1.set_xlabel('Class')
	ax1.set_title('Alpha Ratio')
	ax2.set_title('Hjorth complexity')
	for x in range(1,3):
		exec "ax%s.set_ylabel('Value')" %(x)
	plt.setp((ax1,ax2), xticklabels=Dists)
	#-------------------------------------------------------------------
	fig1.tight_layout()
#-------------------------- Plotting of Beta --------------------------
def plot_beta_():
	for x,cls in enumerate(classes):
		exec "%s_ratio = []" % (cls)
		exec "%s_pfd = []" % (cls)
		exec "%s_mob = []" % (cls)
	for x,cls in enumerate(classes_ext):
		exec "%s_ratio = []" % (cls)
		exec "%s_pfd = []" % (cls)
		exec "%s_mob = []" % (cls)
	#-------------------------------------------------------------------
	exec "mat_contents = loadmat_new.loadmat('%s/Features/Parameters_files/Test_1_B.mat')" %(dir_wrk)
	# 4 classes
	active = mat_contents['active'];
	nonactive = mat_contents['nonactive']
	standard = mat_contents['standard']
	offline = mat_contents['offline']
	eog = mat_contents['eog']
	emg = mat_contents['emg']
	#-------------------------------------------------------------------
 	for y,cls in enumerate(classes):
		for x in range(total_n_beta):
			exec "%s_ratio.append(%s[seq_b[%s]]['a1_ratio'])" % (cls,cls,x)
			exec "%s_pfd.append(%s[seq_b[%s]]['pfd'])" % (cls,cls,x)
			exec "%s_mob.append(%s[seq_b[%s]]['vaf_hjorth_mob'])" % (cls,cls,x)
	for y,cls in enumerate(classes_ext):
		for x in range(total_n_emg):
			exec "%s_ratio.append(%s[seq_b[%s]]['a1_ratio'])" % (cls,cls,x)
			exec "%s_pfd.append(%s[seq_b[%s]]['pfd'])" % (cls,cls,x)
			exec "%s_mob.append(%s[seq_b[%s]]['vaf_hjorth_mob'])" % (cls,cls,x)
	#-------------------------------------------------------------------
	data1 = [active_ratio, nonactive_ratio, standard_ratio, offline_ratio, eog_ratio, emg_ratio]
	data2 = [active_pfd, nonactive_pfd, standard_pfd, offline_pfd, eog_pfd, emg_pfd]
	data3 = [active_mob, nonactive_mob, standard_mob, offline_mob, eog_mob, emg_mob]
	#-------------------------------------------------------------------
	fig1, (ax1,ax2,ax3) = plt.subplots(3)
	for x in range(1,4):
		exec "bp%s = ax%s.boxplot(data%s, notch=1, sym='k+', vert=1)" %(x,x,x)
	#-------------------------------------------------------------------
	for x in range(1,4):
		exec "ax%s.yaxis.grid(True, linestyle='-', which='major', color='lightgrey',alpha=0.5)" %(x)
		exec "ax%s.xaxis.grid(True, linestyle='-', which='major', color='lightgrey',alpha=0.5)" %(x)
	fig1.canvas.set_window_title('Parametros de Beta')
	ax1.set_axisbelow(True)
	ax1.set_xlabel('Class')
	ax1.set_title('Beta Ratio')
	ax2.set_title('Petrosian Fractal Dimension')
	ax3.set_title('Hjorth Mobility')
	for x in range(1,4):
		exec "ax%s.set_ylabel('Value')" %(x)
	plt.setp((ax1,ax2,ax3), xticklabels=Dists_b)
	#-------------------------------------------------------------------
	fig1.tight_layout()
#-------------------------- Plotting of Wleft --------------------------
def plot_wleft_():
	for x,cls in enumerate(classes_emg):
		exec "%s_froben = []" % (cls)
		exec "%s_hjorth = []" % (cls)
	#-------------------------------------------------------------------
	exec "mat_contents = loadmat_new.loadmat('%s/Features/Parameters_files/Left_Wink.mat')" %(dir_wrk)
	# 4 classes
	active = mat_contents['active']
	standard = mat_contents['standard']
	offline = mat_contents['offline']
	eog = mat_contents['eog']
	#-------------------------------------------------------------------
	for y,cls in enumerate(classes_emg):
		for x in range(total_n_emg):
			exec "%s_froben.append(%s[seq_[%s]]['a1_froben'])" % (cls,cls,x)
			exec "%s_hjorth.append(%s[seq_[%s]]['a2_hjorth'])" % (cls,cls,x)
	#-------------------------------------------------------------------
	data1 = [active_froben, standard_froben, offline_froben, eog_froben]
	data2 = [active_hjorth, standard_hjorth, offline_hjorth, eog_hjorth]
	#-------------------------------------------------------------------
	fig1, (ax1,ax2) = plt.subplots(2)
	for x in range(1,3):
		exec "bp%s = ax%s.boxplot(data%s, notch=1, sym='k+', vert=1)" %(x,x,x)
	#-------------------------------------------------------------------
	for x in range(1,3):
		exec "ax%s.yaxis.grid(True, linestyle='-', which='major', color='lightgrey',alpha=0.5)" %(x)
		exec "ax%s.xaxis.grid(True, linestyle='-', which='major', color='lightgrey',alpha=0.5)" %(x)
	fig1.canvas.set_window_title('Parametros de Parpadeo Izq.')
	ax1.set_axisbelow(True)
	ax1.set_xlabel('Class')
	ax1.set_title('Frobenius Norm')
	ax2.set_title('Hjorth complexity')
	for x in range(1,3):
		exec "ax%s.set_ylabel('Value')" %(x)
	plt.setp((ax1,ax2), xticklabels=Dists_emg)
	#-------------------------------------------------------------------
	fig1.tight_layout()
#-------------------------- Plotting of Wright -------------------------
def plot_wright_():
	for x,cls in enumerate(classes_emg):
		exec "%s_froben = []" % (cls)
		exec "%s_hjorth = []" % (cls)
	#-------------------------------------------------------------------
	exec "mat_contents = loadmat_new.loadmat('%s/Features/Parameters_files/Right_Wink.mat')" %(dir_wrk)
	# 4 classes
	active = mat_contents['active'];
	standard = mat_contents['standard']
	offline = mat_contents['offline']
	eog = mat_contents['eog']
	#-------------------------------------------------------------------
	for y,cls in enumerate(classes_emg):
		for x in range(total_n_emg):
			exec "%s_froben.append(%s[seq_[%s]]['a1_froben'])" % (cls,cls,x)
			exec "%s_hjorth.append(%s[seq_[%s]]['a2_hjorth'])" % (cls,cls,x)
	#-------------------------------------------------------------------
	data1 = [active_froben, standard_froben, offline_froben, eog_froben]
	data2 = [active_hjorth, standard_hjorth, offline_hjorth, eog_hjorth]
	#-------------------------------------------------------------------
	fig1, (ax1,ax2) = plt.subplots(2)
	for x in range(1,3):
		exec "bp%s = ax%s.boxplot(data%s, notch=1, sym='k+', vert=1)" %(x,x,x)
	#-------------------------------------------------------------------
	for x in range(1,3):
		exec "ax%s.yaxis.grid(True, linestyle='-', which='major', color='lightgrey',alpha=0.5)" %(x)
		exec "ax%s.xaxis.grid(True, linestyle='-', which='major', color='lightgrey',alpha=0.5)" %(x)
	fig1.canvas.set_window_title('Parametros de Parpadeo Der.')
	ax1.set_axisbelow(True)
	ax1.set_xlabel('Class')
	ax1.set_title('Frobenius Norm')
	ax2.set_title('Hjorth complexity')
	for x in range(1,3):
		exec "ax%s.set_ylabel('Value')" %(x)
	plt.setp((ax1,ax2), xticklabels=Dists_emg)
	#-------------------------------------------------------------------
	fig1.tight_layout()
#-------------------------- SVM Alpha ----------------------------------
def svm_alpha_():
	#------------------------------ labels -----------------------------
	# data full
	target_names = np.array(['active','nonactive','standard','offline'])
	# data 2D
	target_names_2d = np.array(['active','standard'])
	feature_names_2d = ['a1_ratio','hjr_com']
	#------------------------------ Variables ------------------------------
	seq_ = []
	for x in range(total_n_emg):exec "seq_.append('part_%s')" % (x)
	svm_data = [];svm_target = [];svm_target_test = [];svm_test = []
	for x,cls in enumerate(target_names):
		exec "%s_ratio = []" % (cls)
		exec "%s_hjr = []" % (cls)
	#------------------------------ Extract Feats ----------------------
	exec "mat_contents = loadmat_new.loadmat('%s/Features/Parameters_files/Test_1_A.mat')" %(dir_wrk)
	active = mat_contents['active'];
	nonactive = mat_contents['nonactive']
	standard = mat_contents['standard']
	offline = mat_contents['offline']
	for y,cls in enumerate(target_names):
		exec "%s_class = []" %(cls)
		exec "%s_class_data = []" %(cls)
		exec "%s_class_test = []" %(cls)
		exec "%s_class_target = []" %(cls)
	#------------------------------ Create classes ---------------------
	for y,cls in enumerate(target_names):
		for x in range(total_n_emg):
			exec "%s_class.append(np.asarray(collections.OrderedDict(sorted(%s[seq_[%s]].items())).values()))" % (cls,cls,x)
		exec "rndm.shuffle(%s_class)" %(cls)
	#------------------------------ test and data extract --------------
	for y,cls in enumerate(target_names):
		for x in range(total_n_emg):
			exec "if %s < test_n_emg:%s_class_test.append(%s_class[x])" %(x,cls,cls)
			exec "if %s >= test_n_emg:%s_class_data.append(%s_class[x])" %(x,cls,cls)
	for y,cls in enumerate(target_names):
		exec "%s_class_test = np.asarray(%s_class_test)" %(cls,cls)
		exec "%s_class_data = np.asarray(%s_class_data)" %(cls,cls)
	#------------------------------ Create targets ---------------------
	for x in range(numClss):
		exec "class_%s = [x]*50" %(x)
		exec "class_test_%s = [x]*25" %(x)
		exec "svm_target.append(class_%s)" %(x)
		exec "svm_target_test.append(class_test_%s)" %(x)
	#------------------------------ test and data file ---------------------
	for y,cls in enumerate(target_names):
		exec "svm_data.append(%s_class_data)" %(cls)
		exec "svm_test.append(%s_class_test)" %(cls)
	for y,cls in enumerate(['target_test','target','data','test']):
		exec "svm_%s = list(chain.from_iterable(svm_%s))" %(cls,cls)
		exec "svm_%s = np.asarray(svm_%s)" %(cls,cls)
	#------------------------------ Train SVM --------------------------
	X = svm_data; y = svm_target; T = svm_test;yy = svm_target_test
	#------------------------------ Data Binary Class and Feats --------
	# Train part
	X_2d = np.delete(X,range(50,85)+range(100,130)+range(150,185),axis=0)
	y_2d = y[y < 2]
	# Test part
	T_2d = np.delete(T,range(25,43)+range(50,64)+range(75,93),axis=0)
	yy_2d = yy[yy < 2]
	#------------------------------ Standardize data ------------
	scaler = StandardScaler()
	X_2d = scaler.fit_transform(X_2d)
	T_2d_scaled = scaler.transform(T_2d)
	#------------------------------ Create Classifier ------------------
	manual_param = {'C':100,'gamma':0.1}
	clf = SVC(gamma=manual_param['gamma'], C=manual_param['C'])
	clf.fit(X_2d, y_2d)
	#------------------------------ Create Classifier ------------------
	C_range = np.logspace(1, 3, 3)
	gamma_range = np.logspace(-3, -1, 3)
	param_grid = dict(gamma=gamma_range, C=C_range)
	cv = StratifiedShuffleSplit(y_2d, n_iter=100, test_size=0.2, random_state=42)
	grid = GridSearchCV(SVC(), param_grid=param_grid, cv=cv)
	#------------------------------ Best parameter Aprox.---------------
	grid.fit(X_2d, y_2d)
	best_param = grid.best_params_
	best_score = grid.best_score_
	manual_score = clf.score(T_2d_scaled,yy_2d)
	C_2d_range = [1e1, 1e2, 1e3];
	gamma_2d_range = [1e-3, 1e-2, 0.1]
	classifiers = []
	for C in C_2d_range:
	    for gamma in gamma_2d_range:
	        clf_auto = SVC(C=C, gamma=gamma)
	        clf_auto.fit(X_2d, y_2d)
	        classifiers.append((C, gamma, clf_auto))
	#------------------------------ Parameters Visualization -----------
	fig = plt.figure(figsize=(8, 6))
	max_x = max(X_2d[:, 0]); min_x = min(X_2d[:, 0])
	max_y = max(X_2d[:, 1]); min_y = min(X_2d[:, 1])
	xx, yy = np.meshgrid(np.linspace((min_x-abs(min_x*(0.15))), 
			(max_x+max_x*(0.15)), 200), 
			np.linspace((min_y-abs(min_y*(0.15))),
			(max_y+max_y*(0.15)), 200))
	for (k, (C, gamma, clf_auto)) in enumerate(classifiers):
		# evaluate decision function in a grid
		Z = clf_auto.decision_function(np.c_[xx.ravel(), yy.ravel()])
		Z = Z.reshape(xx.shape)
		# visualize decision function for these parameters
		plt.subplot(len(C_2d_range), len(gamma_2d_range), k + 1)
		plt.title("gamma=10^%d, C=10^%d" % (np.log10(gamma), np.log10(C)),
			size='medium')
		# visualize parameter's effect on decision function
		plt.pcolormesh(xx, yy, -Z, cmap=plt.cm.RdBu)
		plt.scatter(X_2d[:, 0], X_2d[:, 1], c=y_2d)
		plt.xticks(())
		plt.yticks(())
		plt.axis('tight')
	#------------------------------ Save SVM and Scaler to a File ------
	joblib.dump(clf, dir_wrk+'/Features/Dump_Files/alphaSVM.pkl',compress=3)
	joblib.dump(scaler,dir_wrk+'/Features/Dump_Files/alphaScaler.pkl',compress=3)
	#------------------------------ Save SVM data files to a File ------
	exec "savemat('%s/Features/SVM_DataFile/Test_1_A_SVM_2D.mat', {'svm data':X_2d,'svm target':y_2d,'svm test':T_2d, 'svm target test':yy_2d, 'features names':feature_names_2d,'target names':target_names_2d}, do_compression=1)"  %(dir_wrk)
	fig.canvas.set_window_title('Parametros RBF de SVM para "Alpha"')
	return manual_param, manual_score, best_param, best_score
#-------------------------- SVM Beta ----------------------------------
def svm_beta_():
	#------------------------------ labels -----------------------------
	# data full
	target_names_all = np.array(['active','nonactive','standard','offline','eog','emg'])
	target_names = np.array(['active','nonactive','standard','offline'])
	target_names_extra = np.array(['eog','emg'])
	# data 2D
	target_names_2d = np.array(['active','standard'])
#	feature_names_2d = ['a1_ratio','pfd']
	feature_names_2d = ['a1_ratio','pfd','vaf_hjorth_mob']
	#------------------------------ Variables ------------------------------
	seq_ = []
	for x in range(total_n_beta):exec "seq_.append('part_%s')" % (x)
	for x in range(total_n_emg):exec "seq_b.append('part_%s')" % (x)
	svm_data = [];svm_target = [];svm_target_test = [];svm_test = []
	for x,cls in enumerate(target_names_all):
		exec "%s_ratio = []" % (cls)
		exec "%s_hjr = []" % (cls)
		exec "%s_mob = []" % (cls)
	#------------------------------ Extract Feats ----------------------
	exec "mat_contents = loadmat_new.loadmat('%s/Features/Parameters_files/Test_1_B.mat')" %(dir_wrk)
	active = mat_contents['active'];
	nonactive = mat_contents['nonactive']
	standard = mat_contents['standard']
	offline = mat_contents['offline']
	eog = mat_contents['eog']
	emg = mat_contents['emg']
	for y,cls in enumerate(target_names_all):
		exec "%s_class = []" %(cls)
		exec "%s_class_data = []" %(cls)
		exec "%s_class_test = []" %(cls)
		exec "%s_class_target = []" %(cls)
	#------------------------------ Create classes ---------------------
	for y,cls in enumerate(target_names):
		for x in range(total_n_beta):
			exec "%s_class.append(np.asarray(collections.OrderedDict(sorted(%s[seq_[%s]].items())).values()))" % (cls,cls,x)
		exec "rndm.shuffle(%s_class)" %(cls)
	for y,cls in enumerate(target_names_extra):
		for x in range(total_n_emg):
			exec "%s_class.append(np.asarray(collections.OrderedDict(sorted(%s[seq_[%s]].items())).values()))" % (cls,cls,x)
		exec "rndm.shuffle(%s_class)" %(cls)
	#------------------------------ test and data extract --------------
	for y,cls in enumerate(target_names):
		for x in range(total_n_beta):
			exec "if %s < test_n_beta:%s_class_test.append(%s_class[x])" %(x,cls,cls)
			exec "if %s >= test_n_beta:%s_class_data.append(%s_class[x])" %(x,cls,cls)
	for y,cls in enumerate(target_names):
		exec "%s_class_test = np.asarray(%s_class_test)" %(cls,cls)
		exec "%s_class_data = np.asarray(%s_class_data)" %(cls,cls)
	for y,cls in enumerate(target_names_extra):
		for x in range(total_n_emg):
			exec "if %s < test_n_emg:%s_class_test.append(%s_class[x])" %(x,cls,cls)
			exec "if %s >= test_n_emg:%s_class_data.append(%s_class[x])" %(x,cls,cls)
	for y,cls in enumerate(target_names_extra):
		exec "%s_class_test = np.asarray(%s_class_test)" %(cls,cls)
		exec "%s_class_data = np.asarray(%s_class_data)" %(cls,cls)
	#------------------------------ Create targets ---------------------
	for x in range(numClss):
		exec "class_%s = [x]*128" %(x)
		exec "class_test_%s = [x]*64" %(x)
		exec "svm_target.append(class_%s)" %(x)
		exec "svm_target_test.append(class_test_%s)" %(x)
	#------------------------------ test and data file ---------------------
	for y,cls in enumerate(target_names_all):
		exec "svm_data.append(%s_class_data)" %(cls)
		exec "svm_test.append(%s_class_test)" %(cls)
	for y,cls in enumerate(['target_test','target','data','test']):
		exec "svm_%s = list(chain.from_iterable(svm_%s))" %(cls,cls)
		exec "svm_%s = np.asarray(svm_%s)" %(cls,cls)
	#------------------------------ Train SVM --------------------------
	X = svm_data; y = svm_target; T = svm_test;yy = svm_target_test
	#------------------------------ Data Binary Class and Feats --------

#train_n_emg = 50; total_n_emg = 75;data_n_emg = 50; test_n_emg = 25
#train_n_beta = 128; total_n_beta = 192;data_n_beta = 128; test_n_beta = 64
#['active','nonactive','standard','offline', 'eog',    'emg']
# TRAIN PART
#( [0,127] [128,255]   [256,383]   [384,511] [512,561] [562,611])
#( [128]   [24] 		  [32]   	  [24] 		[24]   	  [24] )
# TEST PART
#( [0,63] [64,127]   [128,191]   [192,255] [256,280] [281,305])
#( [64]   [12] 		  [16]   	  [12] 		[12]   	  [12] )

	# Train part
	X_2d = np.delete(X,range(128,232)+range(256,352)+range(384,488)+range(512,538)+range(562,588),axis=0)
#	X_2d = np.delete(X,range(128,218)+range(256,332)+range(384,474),axis=0)
	y_2d = y[y < 2]
	# Test part
	T_2d = np.delete(T,range(64,116)+range(128,176)+range(192,244)+range(256,269)+range(281,294),axis=0)
#	T_2d = np.delete(T,range(64,109)+range(128,166)+range(192,237),axis=0)
	yy_2d = yy[yy < 2]
	#------------------------------ Standardize data ------------
	scaler = StandardScaler()
	X_2d = scaler.fit_transform(X_2d)
	T_2d_scaled = scaler.transform(T_2d)
	#------------------------------ Create Classifier ------------------
	manual_param = {'C':100,'gamma':0.001}
	clf = SVC(gamma=manual_param['gamma'], C=manual_param['C'])
	clf.fit(X_2d, y_2d)
	#------------------------------ Create Classifier ------------------
	C_range = np.logspace(1, 3, 3)
	gamma_range = np.logspace(-3, -1, 3)
	param_grid = dict(gamma=gamma_range, C=C_range)
	cv = StratifiedShuffleSplit(y_2d, n_iter=100, test_size=0.2, random_state=42)
	grid = GridSearchCV(SVC(), param_grid=param_grid, cv=cv)
	#------------------------------ Best parameter Aprox.---------------
	grid.fit(X_2d, y_2d)
	best_param = grid.best_params_
	best_score = grid.best_score_
	manual_score = clf.score(T_2d_scaled,yy_2d)
	C_2d_range = [1e1, 1e2, 1e3];
	gamma_2d_range = [1e-3, 1e-2, 0.1]
	classifiers = []
	for C in C_2d_range:
	    for gamma in gamma_2d_range:
	        clf_auto = SVC(C=C, gamma=gamma)
	        clf_auto.fit(X_2d, y_2d)
	        classifiers.append((C, gamma, clf_auto))
	#------------------------------ Parameters Visualization -----------
	fig = plt.figure()
	ax = fig.add_subplot(111, projection='3d')
	ax.scatter(X_2d[:, 0], X_2d[:, 1], X_2d[:, 2], c=y_2d, cmap=plt.cm.RdBu_r, marker='o')
	ax.set_xlabel('Beta Ratio')
	ax.set_ylabel('Petrosian Fractal Dimension')
	ax.set_zlabel('Hjorth Complexity')
	#------------------------------ Save SVM and Scaler to a File ------
	joblib.dump(clf, dir_wrk+'/Features/Dump_Files/betaSVM.pkl',compress=3)
	joblib.dump(scaler,dir_wrk+'/Features/Dump_Files/betaScaler.pkl',compress=3)
	#------------------------------ Save SVM data files to a File ------
	exec "savemat('%s/Features/SVM_DataFile/Test_1_B_SVM_2D.mat', {'svm data':X_2d,'svm target':y_2d,'svm test':T_2d, 'svm target test':yy_2d, 'features names':feature_names_2d,'target names':target_names_2d}, do_compression=1)"  %(dir_wrk)
	fig.canvas.set_window_title('Parametros RBF de SVM para "Beta"')
	return manual_param, manual_score, best_param, best_score
#-------------------------- SVM Wleft ----------------------------------
def svm_wleft_():
	#------------------------------ labels -----------------------------
	# data full
	target_names = np.array(['active','standard','offline','eog'])
	# data 2D
	target_names_2d = np.array(['active','standard'])
	feature_names_2d = ['a1_froben','a2_hjorth']
	#------------------------------ Variables --------------------------
	seq_ = []
	for x in range(total_n_emg):exec "seq_.append('part_%s')" % (x)
	svm_data = [];svm_target = [];svm_target_test = [];svm_test = []
	for x,cls in enumerate(target_names):
		exec "%s_froben = []" % (cls)
		exec "%s_hjr = []" % (cls)
	#------------------------------ Extract Feats ----------------------
	exec "mat_contents = loadmat_new.loadmat('%s/Features/Parameters_files/Left_Wink.mat')" %(dir_wrk)
	active = mat_contents['active'];
	standard = mat_contents['standard']
	offline = mat_contents['offline']
	eog = mat_contents['eog']
	for y,cls in enumerate(target_names):
		exec "%s_class = []" %(cls)
		exec "%s_class_data = []" %(cls)
		exec "%s_class_test = []" %(cls)
		exec "%s_class_target = []" %(cls)
	#------------------------------ Create classes ---------------------
	for y,cls in enumerate(target_names):
		for x in range(total_n_emg):
			exec "%s_class.append(np.asarray(collections.OrderedDict(sorted(%s[seq_[%s]].items())).values()))" % (cls,cls,x)
		exec "rndm.shuffle(%s_class)" %(cls)
	#------------------------------ test and data extract --------------
	for y,cls in enumerate(target_names):
		for x in range(total_n_emg):
			exec "if %s < test_n_emg:%s_class_test.append(%s_class[x])" %(x,cls,cls)
			exec "if %s >= test_n_emg:%s_class_data.append(%s_class[x])" %(x,cls,cls)
	for y,cls in enumerate(target_names):
		exec "%s_class_test = np.asarray(%s_class_test)" %(cls,cls)
		exec "%s_class_data = np.asarray(%s_class_data)" %(cls,cls)
	#------------------------------ Create targets ---------------------
	for x in range(numClss):
		exec "class_%s = [x]*50" %(x)
		exec "class_test_%s = [x]*25" %(x)
		exec "svm_target.append(class_%s)" %(x)
		exec "svm_target_test.append(class_test_%s)" %(x)
	#------------------------------ test and data file ---------------------
	for y,cls in enumerate(target_names):
		exec "svm_data.append(%s_class_data)" %(cls)
		exec "svm_test.append(%s_class_test)" %(cls)
	for y,cls in enumerate(['target_test','target','data','test']):
		exec "svm_%s = list(chain.from_iterable(svm_%s))" %(cls,cls)
		exec "svm_%s = np.asarray(svm_%s)" %(cls,cls)
	#------------------------------ Train SVM --------------------------
	X = svm_data; y = svm_target; T = svm_test;yy = svm_target_test
	#------------------------------ Data Binary Class and Feats --------
#0,49  50,99  100,149  150,199
#50      20     15         15
#0,24  25,49  50,74  75,99
#25      11     7         7
	# Train part
	X_2d = np.delete(X,range(50,80)+range(100,135)+range(150,185),axis=0)
	y_2d = y[y < 2]
	# Test part
	T_2d = np.delete(T,range(25,39)+range(50,68)+range(75,93),axis=0)
	yy_2d = yy[yy < 2]
	#------------------------------ Standardize data ------------
	scaler = StandardScaler()
	X_2d = scaler.fit_transform(X_2d)
	T_2d_scaled = scaler.transform(T_2d)
	#------------------------------ Create Classifier ------------------
	manual_param = {'C':100,'gamma':0.1}
	clf = SVC(gamma=manual_param['gamma'], C=manual_param['C'])
	clf.fit(X_2d, y_2d)
	#------------------------------ Create Classifier ------------------
	C_range = np.logspace(1, 3, 3)
	gamma_range = np.logspace(-3, -1, 3)
	param_grid = dict(gamma=gamma_range, C=C_range)
	cv = StratifiedShuffleSplit(y_2d, n_iter=100, test_size=0.2, random_state=42)
	grid = GridSearchCV(SVC(), param_grid=param_grid, cv=cv)
	#------------------------------ Best parameter Aprox.---------------
	grid.fit(X_2d, y_2d)
	best_param = grid.best_params_
	best_score = grid.best_score_
	manual_score = clf.score(T_2d_scaled,yy_2d)
	C_2d_range = [1e1, 1e2, 1e3];
	gamma_2d_range = [1e-3, 1e-2, 0.1]
	classifiers = []
	for C in C_2d_range:
	    for gamma in gamma_2d_range:
	        clf_auto = SVC(C=C, gamma=gamma)
	        clf_auto.fit(X_2d, y_2d)
	        classifiers.append((C, gamma, clf_auto))
	#------------------------------ Parameters Visualization -----------
	fig = plt.figure(figsize=(8, 6))
	max_x = max(X_2d[:, 0]); min_x = min(X_2d[:, 0])
	max_y = max(X_2d[:, 1]); min_y = min(X_2d[:, 1])
	xx, yy = np.meshgrid(np.linspace((min_x-abs(min_x*(0.15))), 
			(max_x+max_x*(0.15)), 200), 
			np.linspace((min_y-abs(min_y*(0.15))),
			(max_y+max_y*(0.15)), 200))
	for (k, (C, gamma, clf_auto)) in enumerate(classifiers):
		# evaluate decision function in a grid
		Z = clf_auto.decision_function(np.c_[xx.ravel(), yy.ravel()])
		Z = Z.reshape(xx.shape)
		# visualize decision function for these parameters
		plt.subplot(len(C_2d_range), len(gamma_2d_range), k + 1)
		plt.title("gamma=10^%d, C=10^%d" % (np.log10(gamma), np.log10(C)),
			size='medium')
		# visualize parameter's effect on decision function
		plt.pcolormesh(xx, yy, -Z, cmap=plt.cm.RdBu)
		plt.scatter(X_2d[:, 0], X_2d[:, 1], c=y_2d, cmap=plt.cm.RdBu_r)
		plt.xticks(())
		plt.yticks(())
		plt.axis('tight')
	#------------------------------ Save SVM and Scaler to a File ------
	joblib.dump(clf, dir_wrk+'/Features/Dump_Files/wleftSVM.pkl',compress=3)
	joblib.dump(scaler,dir_wrk+'/Features/Dump_Files/wleftScaler.pkl',compress=3)
	#------------------------------ Save SVM data files to a File ------
	exec "savemat('%s/Features/SVM_DataFile/Wink_Left_SVM_2D.mat', {'svm data':X_2d,'svm target':y_2d,'svm test':T_2d, 'svm target test':yy_2d, 'features names':feature_names_2d,'target names':target_names_2d}, do_compression=1)"  %(dir_wrk)
	fig.canvas.set_window_title('Parametros RBF de SVM para "Parpadeo Izq."')
	return manual_param, manual_score, best_param, best_score
#-------------------------- SVM wright ---------------------------------
def svm_wright_():
	#------------------------------ labels -----------------------------
	# data full
	target_names = np.array(['active','standard','offline','eog'])
	# data 2D
	target_names_2d = np.array(['active','standard'])
	feature_names_2d = ['a1_froben','a2_hjorth']
	#------------------------------ Variables ------------------------------
	seq_ = []
	for x in range(total_n_emg):exec "seq_.append('part_%s')" % (x)
	svm_data = [];svm_target = [];svm_target_test = [];svm_test = []
	for x,cls in enumerate(target_names):
		exec "%s_froben = []" % (cls)
		exec "%s_hjr = []" % (cls)
	#------------------------------ Extract Feats ----------------------
	exec "mat_contents = loadmat_new.loadmat('%s/Features/Parameters_files/Right_Wink.mat')" %(dir_wrk)
	active = mat_contents['active'];
	standard = mat_contents['standard']
	offline = mat_contents['offline']
	eog = mat_contents['eog']
	for y,cls in enumerate(target_names):
		exec "%s_class = []" %(cls)
		exec "%s_class_data = []" %(cls)
		exec "%s_class_test = []" %(cls)
		exec "%s_class_target = []" %(cls)
	#------------------------------ Create classes ---------------------
	for y,cls in enumerate(target_names):
		for x in range(total_n_emg):
			exec "%s_class.append(np.asarray(collections.OrderedDict(sorted(%s[seq_[%s]].items())).values()))" % (cls,cls,x)
		exec "rndm.shuffle(%s_class)" %(cls)
	#------------------------------ test and data extract --------------
	for y,cls in enumerate(target_names):
		for x in range(total_n_emg):
			exec "if %s < test_n_emg:%s_class_test.append(%s_class[x])" %(x,cls,cls)
			exec "if %s >= test_n_emg:%s_class_data.append(%s_class[x])" %(x,cls,cls)
	for y,cls in enumerate(target_names):
		exec "%s_class_test = np.asarray(%s_class_test)" %(cls,cls)
		exec "%s_class_data = np.asarray(%s_class_data)" %(cls,cls)
	#------------------------------ Create targets ---------------------
	for x in range(numClss):
		exec "class_%s = [x]*50" %(x)
		exec "class_test_%s = [x]*25" %(x)
		exec "svm_target.append(class_%s)" %(x)
		exec "svm_target_test.append(class_test_%s)" %(x)
	#------------------------------ test and data file ---------------------
	for y,cls in enumerate(target_names):
		exec "svm_data.append(%s_class_data)" %(cls)
		exec "svm_test.append(%s_class_test)" %(cls)
	for y,cls in enumerate(['target_test','target','data','test']):
		exec "svm_%s = list(chain.from_iterable(svm_%s))" %(cls,cls)
		exec "svm_%s = np.asarray(svm_%s)" %(cls,cls)
	#------------------------------ Train SVM --------------------------
	X = svm_data; y = svm_target; T = svm_test;yy = svm_target_test
	#------------------------------ Data Binary Class and Feats --------
#0,49  50,99  100,149  150,199
#50      20     15         15
#0,24  25,49  50,74  75,99
#25      11     7         7
	# Train part
	X_2d = np.delete(X,range(50,80)+range(100,135)+range(150,185),axis=0)
	y_2d = y[y < 2]
	# Test part
	T_2d = np.delete(T,range(25,39)+range(50,68)+range(75,93),axis=0)
	yy_2d = yy[yy < 2]
	#------------------------------ Standardize data ------------
	scaler = StandardScaler()
	X_2d = scaler.fit_transform(X_2d)
	T_2d_scaled = scaler.transform(T_2d)
	#------------------------------ Create Classifier ------------------
	manual_param = {'C':100,'gamma':0.1}
	clf = SVC(gamma=manual_param['gamma'], C=manual_param['C'])
	clf.fit(X_2d, y_2d)
	#------------------------------ Create Classifier ------------------
	C_range = np.logspace(1, 3, 3)
	gamma_range = np.logspace(-3, -1, 3)
	param_grid = dict(gamma=gamma_range, C=C_range)
	cv = StratifiedShuffleSplit(y_2d, n_iter=100, test_size=0.2, random_state=42)
	grid = GridSearchCV(SVC(), param_grid=param_grid, cv=cv)
	#------------------------------ Best parameter Aprox.---------------
	grid.fit(X_2d, y_2d)
	best_param = grid.best_params_
	best_score = grid.best_score_
	manual_score = clf.score(T_2d_scaled,yy_2d)
	C_2d_range = [1e1, 1e2, 1e3];
	gamma_2d_range = [1e-3, 1e-2, 0.1]
	classifiers = []
	for C in C_2d_range:
	    for gamma in gamma_2d_range:
	        clf_auto = SVC(C=C, gamma=gamma)
	        clf_auto.fit(X_2d, y_2d)
	        classifiers.append((C, gamma, clf_auto))
	#------------------------------ Parameters Visualization -----------
	fig = plt.figure(figsize=(8, 6))
	max_x = max(X_2d[:, 0]); min_x = min(X_2d[:, 0])
	max_y = max(X_2d[:, 1]); min_y = min(X_2d[:, 1])
	xx, yy = np.meshgrid(np.linspace((min_x-abs(min_x*(0.15))), 
			(max_x+max_x*(0.15)), 200), 
			np.linspace((min_y-abs(min_y*(0.15))),
			(max_y+max_y*(0.15)), 200))
	for (k, (C, gamma, clf_auto)) in enumerate(classifiers):
		# evaluate decision function in a grid
		Z = clf_auto.decision_function(np.c_[xx.ravel(), yy.ravel()])
		Z = Z.reshape(xx.shape)
		# visualize decision function for these parameters
		plt.subplot(len(C_2d_range), len(gamma_2d_range), k + 1)
		plt.title("gamma=10^%d, C=10^%d" % (np.log10(gamma), np.log10(C)),
			size='medium')
		# visualize parameter's effect on decision function
		plt.pcolormesh(xx, yy, -Z, cmap=plt.cm.RdBu)
		plt.scatter(X_2d[:, 0], X_2d[:, 1], c=y_2d, cmap=plt.cm.RdBu_r)
		plt.xticks(())
		plt.yticks(())
		plt.axis('tight')
	#------------------------------ Save SVM and Scaler to a File ------
	joblib.dump(clf, dir_wrk+'/Features/Dump_Files/wrightSVM.pkl',compress=3)
	joblib.dump(scaler,dir_wrk+'/Features/Dump_Files/wrightScaler.pkl',compress=3)
	#------------------------------ Save SVM data files to a File ------
	exec "savemat('%s/Features/SVM_DataFile/Wink_Right_SVM_2D.mat', {'svm data':X_2d,'svm target':y_2d,'svm test':T_2d, 'svm target test':yy_2d, 'features names':feature_names_2d,'target names':target_names_2d}, do_compression=1)"  %(dir_wrk)
	fig.canvas.set_window_title('Parametros RBF de SVM para "Parpadeo Der."')
	plt.show()
	return manual_param, manual_score, best_param, best_score
#-------------------------- SVM Main -----------------------------------
def feat_extract_(self,name):
	if exists(dir_wrk+'/User_Data/'+name):
		self.label_results.setText("Procesando...")
		alpha_extra_()
		beta_extra_()
		emg_extra_()
		plot_alpha_()
		plot_beta_()
		plot_wleft_()
		plot_wright_()
		man_param1, man_score1, auto_param1, auto_score1 = svm_alpha_()
		man_param2, man_score2, auto_param2, auto_score2 = svm_beta_()
		man_param3, man_score3, auto_param3, auto_score3 = svm_wleft_()
		man_param4, man_score4, auto_param4, auto_score4 = svm_wright_()
		self.label_results.setText("The best manual parameters for Alpha are\n{:<20}\nwith a score of {:.0%}\nThe best automatic parameters for Alpha are\n{:<20}\nwith a score of {:.0%}\n \nThe best manual parameters for Beta are\n{:<20}\nwith a score of {:.0%}\nThe best automatic parameters for Beta are\n{:<20}\nwith a score of {:.0%}\n \nThe best manual parameters for Parpadeo Izq. are\n{:<20}\nwith a score of {:.0%}\nThe best automatic parameters for Parpadeo Izq. are\n{:<20}\nwith a score of {:.0%}\n \nThe best manual parameters for Parpadeo Der. are\n{:<20}\nwith a score of {:.0%}\nThe best automatic parameters for Parpadeo Der. are\n{:<20}\nwith a score of {:.0%}\n \n".
		format(man_param1, man_score1, auto_param1, auto_score1,man_param2, man_score2, auto_param2, auto_score2, man_param3, man_score3, auto_param3, auto_score3, man_param4, man_score4, auto_param4, auto_score4))
	else:
		self.label_results.setText("Usuario no encontrado")
