from sklearn import preprocessing
import matplotlib.pyplot as plt
import numpy as np
from pylab import mlab
from scipy.signal import butter, lfilter, filtfilt, welch, resample
from os import getcwd as getdir
from Library import loadmat_new
#-----------------------------------------------------------------------
dir_wrk = getdir();fs = 128
noverlap=100; nfft=128
noverlap_b=1000; nfft_b=1024
noverlap_m=250; nfft_m=256
#-----------------------------------------------------------------------
def highpass(data,samprate=128,cutlow=0.05):
	nyq = samprate/2.0
	low = cutlow / nyq
	b,a = butter(5,low,btype='highpass',analog=0)
#	data_f = lfilter(b,a,data)
	data_f = filtfilt(b,a,data)
	return data_f

def plt_ch_beta(self,_dir,_type,_chann):
	exec "sign_0 = loadmat_new.loadmat('%s/channels/%s/%s/%s.mat')['%s']"  %(dir_wrk,_type,_dir,_chann[0],_chann[0])
	exec "sign_1 = loadmat_new.loadmat('%s/channels/%s/%s/%s.mat')['%s']"  %(dir_wrk,_type,_dir,_chann[1],_chann[1])
	exec "sign_2 = loadmat_new.loadmat('%s/channels/%s/%s/%s.mat')['%s']"  %(dir_wrk,_type,_dir,_chann[2],_chann[2])
	exec "sign_3 = loadmat_new.loadmat('%s/channels/%s/%s/%s.mat')['%s']"  %(dir_wrk,_type,_dir,_chann[3],_chann[3])
	exec "sign_4 = loadmat_new.loadmat('%s/channels/%s/%s/%s.mat')['%s']"  %(dir_wrk,_type,_dir,_chann[4],_chann[4])
	exec "sign_5 = loadmat_new.loadmat('%s/channels/%s/%s/%s.mat')['%s']"  %(dir_wrk,_type,_dir,_chann[5],_chann[5])
	exec "sign_6 = loadmat_new.loadmat('%s/channels/%s/%s/%s.mat')['%s']"  %(dir_wrk,_type,_dir,_chann[6],_chann[6])
	exec "sign_7 = loadmat_new.loadmat('%s/channels/%s/%s/%s.mat')['%s']"  %(dir_wrk,_type,_dir,_chann[7],_chann[7])
	exec "sign_8 = loadmat_new.loadmat('%s/channels/%s/%s/%s.mat')['%s']"  %(dir_wrk,_type,_dir,_chann[8],_chann[8])
	exec "sign_9 = loadmat_new.loadmat('%s/channels/%s/%s/%s.mat')['%s']"  %(dir_wrk,_type,_dir,_chann[9],_chann[9])
	plt.ion()
	fig =  plt.figure()
	fig2 = plt.figure()
	fig3 = plt.figure()
	fig.subplots_adjust(hspace=0.5)
	fig2.subplots_adjust(hspace=0.5)
	fig3.subplots_adjust(hspace=0.5)
	ax0 = fig.add_subplot(411)
	ax1 = fig.add_subplot(412)
	ax2 = fig.add_subplot(413)
	ax3 = fig.add_subplot(414)
	ax4 = fig2.add_subplot(411)
	ax5 = fig2.add_subplot(412)
	ax6 = fig2.add_subplot(413)
	ax7 = fig2.add_subplot(414)
	ax8 = fig3.add_subplot(411)
	ax9 = fig3.add_subplot(412)
	for x in range (10):
		exec "ax%s.set_title('channel %s')" % (x,_chann[x])
	fig.suptitle('spectograms channels')
	fig2.suptitle('spectograms channels')
	fig3.suptitle('spectograms channels')
	ax0.grid(); ax1.grid(); ax2.grid(); ax3.grid(); ax4.grid()
	ax5.grid(); ax6.grid(); ax7.grid(); ax8.grid(); ax9.grid()
	ax0.specgram(highpass(sign_0), Fs = fs, noverlap=noverlap_b,
	NFFT=nfft_b, window=mlab.window_hanning)
	ax1.specgram(highpass(sign_1), Fs = fs, noverlap=noverlap_b,
	NFFT=nfft_b, window=mlab.window_hanning)
	ax2.specgram(highpass(sign_2), Fs = fs, noverlap=noverlap_b,
	NFFT=nfft_b, window=mlab.window_hanning)
	ax3.specgram(highpass(sign_3), Fs = fs, noverlap=noverlap_b,
	NFFT=nfft_b, window=mlab.window_hanning)
	ax4.specgram(highpass(sign_4), Fs = fs, noverlap=noverlap_b,
	NFFT=nfft_b, window=mlab.window_hanning)
	ax5.specgram(highpass(sign_5), Fs = fs, noverlap=noverlap_b,
	NFFT=nfft_b, window=mlab.window_hanning)
	ax6.specgram(highpass(sign_6), Fs = fs, noverlap=noverlap_b,
	NFFT=nfft_b, window=mlab.window_hanning)
	ax7.specgram(highpass(sign_7), Fs = fs, noverlap=noverlap_b,
	NFFT=nfft_b, window=mlab.window_hanning)
	ax8.specgram(highpass(sign_8), Fs = fs, noverlap=noverlap_b,
	NFFT=nfft_b, window=mlab.window_hanning)
	ax9.specgram(highpass(sign_9), Fs = fs, noverlap=noverlap_b,
	NFFT=nfft_b, window=mlab.window_hanning)
	for i in range(10):
		# Active epoch
		exec "ax%s.plot([50, 50], [50, 64], 'black', lw=0.5)" %(i)
		exec "ax%s.plot([250, 250], [50, 64], 'black', lw=0.5)" %(i)
		exec "ax%s.plot([450, 450], [50, 64], 'black', lw=0.5)" %(i)
		exec "ax%s.plot([650, 650], [50, 64], 'black', lw=0.5)" %(i)
		exec "ax%s.plot([850, 850], [50, 64], 'black', lw=0.5)" %(i)
		exec "ax%s.plot([1050, 1050], [50, 64], 'black', lw=0.5)" %(i)
		exec "ax%s.plot([1250, 1250], [50,64], 'black', lw=0.5)" %(i)
		exec "ax%s.plot([1450, 1450], [50,64], 'black', lw=0.5)" %(i)
		# Divisory Line
		exec "ax%s.plot([100, 100], [0, 64], 'black', lw=0.5)" %(i)
		exec "ax%s.plot([200, 200], [0, 64], 'black', lw=0.5)" %(i)
		exec "ax%s.plot([300, 300], [0, 64], 'black', lw=0.5)" %(i)
		exec "ax%s.plot([400, 400], [0, 64], 'black', lw=0.5)" %(i)
		exec "ax%s.plot([500, 500], [0, 64], 'black', lw=0.5)" %(i)
		exec "ax%s.plot([600, 600], [0, 64], 'black', lw=0.5)" %(i)
		exec "ax%s.plot([700, 700], [0, 64], 'black', lw=0.5)" %(i)
		exec "ax%s.plot([800, 800], [0, 64], 'black', lw=0.5)" %(i)
		exec "ax%s.plot([900, 900], [0, 64], 'black', lw=0.5)" %(i)
		exec "ax%s.plot([1000, 1000], [0, 64], 'black', lw=0.5)" %(i)
		exec "ax%s.plot([1100, 1100], [0, 64], 'black', lw=0.5)" %(i)
		exec "ax%s.plot([1200, 1200], [0, 64], 'black', lw=0.5)" %(i)
		exec "ax%s.plot([1300, 1300], [0, 64], 'black', lw=0.5)" %(i)
		exec "ax%s.plot([1400, 1400], [0, 64], 'black', lw=0.5)" %(i)
		exec "ax%s.plot([1500, 1500], [0, 64], 'black', lw=0.5)" %(i)
	ax0.axis('tight')
	ax1.axis('tight')
	ax2.axis('tight')
	ax3.axis('tight')
	ax4.axis('tight')
	ax5.axis('tight')
	ax6.axis('tight')
	ax7.axis('tight')
	ax8.axis('tight')
	ax9.axis('tight')
	plt.tight_layout

def plt_ch_emg(self,_dir,_type,_chann):
	exec "sign_0 = loadmat_new.loadmat('%s/channels/%s/%s/%s.mat')['%s']"  %(dir_wrk,_type,_dir,_chann[0],_chann[0])
	exec "sign_1 = loadmat_new.loadmat('%s/channels/%s/%s/%s.mat')['%s']"  %(dir_wrk,_type,_dir,_chann[1],_chann[1])
	exec "sign_2 = loadmat_new.loadmat('%s/channels/%s/%s/%s.mat')['%s']"  %(dir_wrk,_type,_dir,_chann[2],_chann[2])
	exec "sign_3 = loadmat_new.loadmat('%s/channels/%s/%s/%s.mat')['%s']"  %(dir_wrk,_type,_dir,_chann[3],_chann[3])
	exec "sign_4 = loadmat_new.loadmat('%s/channels/%s/%s/%s.mat')['%s']"  %(dir_wrk,_type,_dir,_chann[4],_chann[4])
	exec "sign_5 = loadmat_new.loadmat('%s/channels/%s/%s/%s.mat')['%s']"  %(dir_wrk,_type,_dir,_chann[5],_chann[5])
	exec "sign_6 = loadmat_new.loadmat('%s/channels/%s/%s/%s.mat')['%s']"  %(dir_wrk,_type,_dir,_chann[6],_chann[6])
	exec "sign_7 = loadmat_new.loadmat('%s/channels/%s/%s/%s.mat')['%s']"  %(dir_wrk,_type,_dir,_chann[7],_chann[7])
	exec "sign_8 = loadmat_new.loadmat('%s/channels/%s/%s/%s.mat')['%s']"  %(dir_wrk,_type,_dir,_chann[8],_chann[8])
	exec "sign_9 = loadmat_new.loadmat('%s/channels/%s/%s/%s.mat')['%s']"  %(dir_wrk,_type,_dir,_chann[9],_chann[9])
	plt.ion()
	fig =  plt.figure()
	fig2 = plt.figure()
	fig3 = plt.figure()
	fig.subplots_adjust(hspace=0.5)
	fig2.subplots_adjust(hspace=0.5)
	fig3.subplots_adjust(hspace=0.5)
	ax0 = fig.add_subplot(411)
	ax1 = fig.add_subplot(412)
	ax2 = fig.add_subplot(413)
	ax3 = fig.add_subplot(414)
	ax4 = fig2.add_subplot(411)
	ax5 = fig2.add_subplot(412)
	ax6 = fig2.add_subplot(413)
	ax7 = fig2.add_subplot(414)
	ax8 = fig3.add_subplot(411)
	ax9 = fig3.add_subplot(412)
	for x in range (10):
		exec "ax%s.set_title('channel %s')" % (x,_chann[x])
	fig.suptitle('spectograms channels')
	fig2.suptitle('spectograms channels')
	fig3.suptitle('spectograms channels')
	ax0.grid(); ax1.grid(); ax2.grid(); ax3.grid(); ax4.grid()
	ax5.grid(); ax6.grid(); ax7.grid(); ax8.grid(); ax9.grid()
	ax0.specgram(highpass(sign_0), Fs = fs, noverlap=noverlap_m,
	NFFT=nfft_m, window=mlab.window_hanning)
	ax1.specgram(highpass(sign_1), Fs = fs, noverlap=noverlap_m,
	NFFT=nfft_m, window=mlab.window_hanning)
	ax2.specgram(highpass(sign_2), Fs = fs, noverlap=noverlap_m,
	NFFT=nfft_m, window=mlab.window_hanning)
	ax3.specgram(highpass(sign_3), Fs = fs, noverlap=noverlap_m,
	NFFT=nfft_m, window=mlab.window_hanning)
	ax4.specgram(highpass(sign_4), Fs = fs, noverlap=noverlap_m,
	NFFT=nfft_m, window=mlab.window_hanning)
	ax5.specgram(highpass(sign_5), Fs = fs, noverlap=noverlap_m,
	NFFT=nfft_m, window=mlab.window_hanning)
	ax6.specgram(highpass(sign_6), Fs = fs, noverlap=noverlap_m,
	NFFT=nfft_m, window=mlab.window_hanning)
	ax7.specgram(highpass(sign_7), Fs = fs, noverlap=noverlap_m,
	NFFT=nfft_m, window=mlab.window_hanning)
	ax8.specgram(highpass(sign_8), Fs = fs, noverlap=noverlap_m,
	NFFT=nfft_m, window=mlab.window_hanning)
	ax9.specgram(highpass(sign_9), Fs = fs, noverlap=noverlap_m,
	NFFT=nfft_m, window=mlab.window_hanning)
	for i in range(10):
		""" Divisory Line """
		for x in range(4,300,4):
			exec "ax%s.plot([%s, %s], [0, 20], 'black', lw=0.5)" %(i,x,x)
	ax0.axis('tight')
	ax1.axis('tight')
	ax2.axis('tight')
	ax3.axis('tight')
	ax4.axis('tight')
	ax5.axis('tight')
	ax6.axis('tight')
	ax7.axis('tight')
	ax8.axis('tight')
	ax9.axis('tight')
	plt.tight_layout

def plt_ch(self,_dir,_folder,_type,_chann):
	exec "sign_0 = loadmat_new.loadmat('%s/channels/%s/%s/%s/%s.mat')['%s']"  %(dir_wrk,_type,_dir,_folder,_chann[0],_chann[0])
	exec "sign_1 = loadmat_new.loadmat('%s/channels/%s/%s/%s/%s.mat')['%s']"  %(dir_wrk,_type,_dir,_folder,_chann[1],_chann[1])
	exec "sign_2 = loadmat_new.loadmat('%s/channels/%s/%s/%s/%s.mat')['%s']"  %(dir_wrk,_type,_dir,_folder,_chann[2],_chann[2])
	exec "sign_3 = loadmat_new.loadmat('%s/channels/%s/%s/%s/%s.mat')['%s']"  %(dir_wrk,_type,_dir,_folder,_chann[3],_chann[3])
	exec "sign_4 = loadmat_new.loadmat('%s/channels/%s/%s/%s/%s.mat')['%s']"  %(dir_wrk,_type,_dir,_folder,_chann[4],_chann[4])
	exec "sign_5 = loadmat_new.loadmat('%s/channels/%s/%s/%s/%s.mat')['%s']"  %(dir_wrk,_type,_dir,_folder,_chann[5],_chann[5])
	exec "sign_6 = loadmat_new.loadmat('%s/channels/%s/%s/%s/%s.mat')['%s']"  %(dir_wrk,_type,_dir,_folder,_chann[6],_chann[6])
	exec "sign_7 = loadmat_new.loadmat('%s/channels/%s/%s/%s/%s.mat')['%s']"  %(dir_wrk,_type,_dir,_folder,_chann[7],_chann[7])
	exec "sign_8 = loadmat_new.loadmat('%s/channels/%s/%s/%s/%s.mat')['%s']"  %(dir_wrk,_type,_dir,_folder,_chann[8],_chann[8])
	exec "sign_9 = loadmat_new.loadmat('%s/channels/%s/%s/%s/%s.mat')['%s']"  %(dir_wrk,_type,_dir,_folder,_chann[9],_chann[9])
	plt.ion()
	fig =  plt.figure()
	fig2 = plt.figure()
	fig3 = plt.figure()
	fig.subplots_adjust(hspace=0.5)
	fig2.subplots_adjust(hspace=0.5)
	fig3.subplots_adjust(hspace=0.5)
	ax0 = fig.add_subplot(411)
	ax1 = fig.add_subplot(412)
	ax2 = fig.add_subplot(413)
	ax3 = fig.add_subplot(414)
	ax4 = fig2.add_subplot(411)
	ax5 = fig2.add_subplot(412)
	ax6 = fig2.add_subplot(413)
	ax7 = fig2.add_subplot(414)
	ax8 = fig3.add_subplot(411)
	ax9 = fig3.add_subplot(412)
	for x in range (10):
		exec "ax%s.set_title('channel %s')" % (x,_chann[x])
	fig.suptitle('spectograms channels')
	fig2.suptitle('spectograms channels')
	fig3.suptitle('spectograms channels')
	ax0.grid(); ax1.grid(); ax2.grid(); ax3.grid(); ax4.grid()
	ax5.grid(); ax6.grid(); ax7.grid(); ax8.grid(); ax9.grid()
	ax0.specgram(highpass(sign_0), Fs = fs, noverlap=noverlap,
	NFFT=nfft, window=mlab.window_hanning)
	ax1.specgram(highpass(sign_1), Fs = fs, noverlap=noverlap,
	NFFT=nfft, window=mlab.window_hanning)
	ax2.specgram(highpass(sign_2), Fs = fs, noverlap=noverlap,
	NFFT=nfft, window=mlab.window_hanning)
	ax3.specgram(highpass(sign_3), Fs = fs, noverlap=noverlap,
	NFFT=nfft, window=mlab.window_hanning)
	ax4.specgram(highpass(sign_4), Fs = fs, noverlap=noverlap,
	NFFT=nfft, window=mlab.window_hanning)
	ax5.specgram(highpass(sign_5), Fs = fs, noverlap=noverlap,
	NFFT=nfft, window=mlab.window_hanning)
	ax6.specgram(highpass(sign_6), Fs = fs, noverlap=noverlap,
	NFFT=nfft, window=mlab.window_hanning)
	ax7.specgram(highpass(sign_7), Fs = fs, noverlap=noverlap,
	NFFT=nfft, window=mlab.window_hanning)
	ax8.specgram(highpass(sign_8), Fs = fs, noverlap=noverlap,
	NFFT=nfft, window=mlab.window_hanning)
	ax9.specgram(highpass(sign_9), Fs = fs, noverlap=noverlap,
	NFFT=nfft, window=mlab.window_hanning)
	for i in range(10):
		exec "ax%s.plot([4, 4], [50, 60], 'black', lw=0.5)" %(i)
		exec "ax%s.plot([20, 20], [50, 60], 'black', lw=0.5)" %(i)
		exec "ax%s.plot([36, 36], [50, 60], 'black', lw=0.5)" %(i)
		exec "ax%s.plot([52, 52], [50, 60], 'black', lw=0.5)" %(i)
		exec "ax%s.plot([68, 68], [50, 60], 'black', lw=0.5)" %(i)
		exec "ax%s.plot([84, 84], [50, 60], 'black', lw=0.5)" %(i)
		exec "ax%s.plot([100, 100], [50, 60], 'black', lw=0.5)" %(i)
		exec "ax%s.plot([116, 116], [50, 60], 'black', lw=0.5)" %(i)
		exec "ax%s.plot([8, 8], [0, 60], 'black', lw=0.5)" %(i)
		exec "ax%s.plot([16, 16], [0, 60], 'black', lw=0.5)" %(i)
		exec "ax%s.plot([24, 24], [0, 60], 'black', lw=0.5)" %(i)
		exec "ax%s.plot([32, 32], [0, 60], 'black', lw=0.5)" %(i)
		exec "ax%s.plot([40, 40], [0, 60], 'black', lw=0.5)" %(i)
		exec "ax%s.plot([48, 48], [0, 60], 'black', lw=0.5)" %(i)
		exec "ax%s.plot([56, 56], [0, 60], 'black', lw=0.5)" %(i)
		exec "ax%s.plot([64, 64], [0, 60], 'black', lw=0.5)" %(i)
		exec "ax%s.plot([72, 72], [0, 60], 'black', lw=0.5)" %(i)
		exec "ax%s.plot([80, 80], [0, 60], 'black', lw=0.5)" %(i)
		exec "ax%s.plot([88, 88], [0, 60], 'black', lw=0.5)" %(i)
		exec "ax%s.plot([96, 96], [0, 60], 'black', lw=0.5)" %(i)
		exec "ax%s.plot([104, 104], [0, 60], 'black', lw=0.5)" %(i)
		exec "ax%s.plot([112, 112], [0, 60], 'black', lw=0.5)" %(i)
		exec "ax%s.plot([120, 120], [0, 60], 'black', lw=0.5)" %(i)
	ax0.axis('tight')
	ax1.axis('tight')
	ax2.axis('tight')
	ax3.axis('tight')
	ax4.axis('tight')
	ax5.axis('tight')
	ax6.axis('tight')
	ax7.axis('tight')
	ax8.axis('tight')
	ax9.axis('tight')
	plt.tight_layout
#	plt.show()

