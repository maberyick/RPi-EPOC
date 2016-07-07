from PyQt4 import QtCore, QtGui
from scipy.io import savemat
from os import getcwd as getdir
from os import path as pth

dir_wrk = getdir()
final_folder = {}

def ColorAdjust(self, value):
	quality_color = {"0": 0,"1": 10,"2": 20,"3": 30,"4": 40,"5": 80,
	"6": 90,"7": 100,}
	temp = quality_color[str(value)]
	return temp

def ColorBatt(self, BattValue):
    palette = QtGui.QPalette()
    pal = self.progressBar_Bat
    if BattValue <= 20:
       palette.setColor(QtGui.QPalette.Highlight,
       QtGui.QColor(QtCore.Qt.red))
       pal.setPalette(palette)
    elif 21 <= BattValue <= 49:
       palette.setColor(QtGui.QPalette.Highlight,
       QtGui.QColor(QtCore.Qt.yellow))
       pal.setPalette(palette)
    elif 50 <= BattValue <= 89:
       palette.setColor(QtGui.QPalette.Highlight,
       QtGui.QColor(QtCore.Qt.blue))
       pal.setPalette(palette)
    elif BattValue >= 90:
       palette.setColor(QtGui.QPalette.Highlight,
       QtGui.QColor(QtCore.Qt.green))
       pal.setPalette(palette)

def ChckFolders(self, temp_dir, F_value):
	dir_bar_values = {'Test_1_A':self.prB_meditar,
	'Test_1_B':self.prB_restar,'Left_Movement':self.prB_Imgleft,
	'Right_Movement':self.prB_Imgright,'Left_Wink':self.prB_Wleft,
	'Right_Wink':self.prB_Wright,'Standard':self.prB_Estandar,
	'Offline':self.prB_Offline,'EOG':self.prB_EOG}
	if F_value == 5:
		palette = QtGui.QPalette()
		pal = dir_bar_values[temp_dir]
		palette.setColor(QtGui.QPalette.Highlight,
		QtGui.QColor(QtCore.Qt.green))
		pal.setPalette(palette)

def ColorChannelQuality(self, QualityCH1, QualityCH2, QualityCH3, 
QualityCH4, QualityCH5, QualityCH6, QualityCH7, QualityCH8, QualityCH9,
QualityCH10,QualityCH11,QualityCH12, QualityCH13,QualityCH14):
    palette = QtGui.QPalette()
    CH1 = self.progressBar_CH1
    CH2 = self.progressBar_CH2
    CH3 = self.progressBar_CH3
    CH4 = self.progressBar_CH4
    CH5 = self.progressBar_CH5
    CH6 = self.progressBar_CH6
    CH7 = self.progressBar_CH7
    CH8 = self.progressBar_CH8
    CH9 = self.progressBar_CH9
    CH10= self.progressBar_CH10
    CH11= self.progressBar_CH11
    CH12= self.progressBar_CH12
    CH13= self.progressBar_CH13
    CH14= self.progressBar_CH14
# Channel No. 1
    if QualityCH1 <= 20:
       palette.setColor(QtGui.QPalette.Highlight,
       QtGui.QColor(QtCore.Qt.red))
       CH1.setPalette(palette)
    elif 21 <= QualityCH1 <= 49:
       palette.setColor(QtGui.QPalette.Highlight,
       QtGui.QColor(QtCore.Qt.yellow))
       CH1.setPalette(palette)
    elif 50 <= QualityCH1 <= 89:
       palette.setColor(QtGui.QPalette.Highlight,
       QtGui.QColor(QtCore.Qt.blue))
       CH1.setPalette(palette)
    elif QualityCH1 >= 90:
       palette.setColor(QtGui.QPalette.Highlight,
       QtGui.QColor(QtCore.Qt.green))
       CH1.setPalette(palette)
# Channel No. 2
    if QualityCH2 <= 20:
       palette.setColor(QtGui.QPalette.Highlight,
       QtGui.QColor(QtCore.Qt.red))
       CH2.setPalette(palette)
    elif 21 <= QualityCH2 <= 49:
       palette.setColor(QtGui.QPalette.Highlight,
       QtGui.QColor(QtCore.Qt.yellow))
       CH2.setPalette(palette)
    elif 50 <= QualityCH2 <= 89:
       palette.setColor(QtGui.QPalette.Highlight,
       QtGui.QColor(QtCore.Qt.blue))
       CH2.setPalette(palette)
    elif QualityCH2 >= 90:
       palette.setColor(QtGui.QPalette.Highlight,
       QtGui.QColor(QtCore.Qt.green))
       CH2.setPalette(palette)
# Channel No. 3
    if QualityCH3 <= 20:
       palette.setColor(QtGui.QPalette.Highlight,
       QtGui.QColor(QtCore.Qt.red))
       CH3.setPalette(palette)
    elif 21 <= QualityCH3 <= 49:
       palette.setColor(QtGui.QPalette.Highlight,
       QtGui.QColor(QtCore.Qt.yellow))
       CH3.setPalette(palette)
    elif 50 <= QualityCH3 <= 89:
       palette.setColor(QtGui.QPalette.Highlight,
       QtGui.QColor(QtCore.Qt.blue))
       CH3.setPalette(palette)
    elif QualityCH3 >= 90:
       palette.setColor(QtGui.QPalette.Highlight,
       QtGui.QColor(QtCore.Qt.green))
       CH3.setPalette(palette)
# Channel No. 4
    if QualityCH4 <= 20:
       palette.setColor(QtGui.QPalette.Highlight,
       QtGui.QColor(QtCore.Qt.red))
       CH4.setPalette(palette)
    elif 21 <= QualityCH4 <= 49:
       palette.setColor(QtGui.QPalette.Highlight,
       QtGui.QColor(QtCore.Qt.yellow))
       CH4.setPalette(palette)
    elif 50 <= QualityCH4 <= 89:
       palette.setColor(QtGui.QPalette.Highlight,
       QtGui.QColor(QtCore.Qt.blue))
       CH4.setPalette(palette)
    elif QualityCH4 >= 90:
       palette.setColor(QtGui.QPalette.Highlight,
       QtGui.QColor(QtCore.Qt.green))
       CH4.setPalette(palette)
# Channel No. 5
    if QualityCH5 <= 20:
       palette.setColor(QtGui.QPalette.Highlight,
       QtGui.QColor(QtCore.Qt.red))
       CH5.setPalette(palette)
    elif 21 <= QualityCH5 <= 49:
       palette.setColor(QtGui.QPalette.Highlight,
       QtGui.QColor(QtCore.Qt.yellow))
       CH5.setPalette(palette)
    elif 50 <= QualityCH5 <= 89:
       palette.setColor(QtGui.QPalette.Highlight,
       QtGui.QColor(QtCore.Qt.blue))
       CH5.setPalette(palette)
    elif QualityCH5 >= 90:
       palette.setColor(QtGui.QPalette.Highlight,
       QtGui.QColor(QtCore.Qt.green))
       CH5.setPalette(palette)
# Channel No. 6
    if QualityCH6 <= 20:
       palette.setColor(QtGui.QPalette.Highlight,
       QtGui.QColor(QtCore.Qt.red))
       CH6.setPalette(palette)
    elif 21 <= QualityCH6 <= 49:
       palette.setColor(QtGui.QPalette.Highlight,
       QtGui.QColor(QtCore.Qt.yellow))
       CH6.setPalette(palette)
    elif 50 <= QualityCH6 <= 89:
       palette.setColor(QtGui.QPalette.Highlight,
       QtGui.QColor(QtCore.Qt.blue))
       CH6.setPalette(palette)
    elif QualityCH6 >= 90:
       palette.setColor(QtGui.QPalette.Highlight,
       QtGui.QColor(QtCore.Qt.green))
       CH6.setPalette(palette)
# Channel No. 7
    if QualityCH7 <= 20:
       palette.setColor(QtGui.QPalette.Highlight,
       QtGui.QColor(QtCore.Qt.red))
       CH7.setPalette(palette)
    elif 21 <= QualityCH7 <= 49:
       palette.setColor(QtGui.QPalette.Highlight,
       QtGui.QColor(QtCore.Qt.yellow))
       CH7.setPalette(palette)
    elif 50 <= QualityCH7 <= 89:
       palette.setColor(QtGui.QPalette.Highlight,
       QtGui.QColor(QtCore.Qt.blue))
       CH7.setPalette(palette)
    elif QualityCH7 >= 90:
       palette.setColor(QtGui.QPalette.Highlight,
       QtGui.QColor(QtCore.Qt.green))
       CH7.setPalette(palette)
# Channel No. 8
    if QualityCH8 <= 20:
       palette.setColor(QtGui.QPalette.Highlight,
       QtGui.QColor(QtCore.Qt.red))
       CH8.setPalette(palette)
    elif 21 <= QualityCH8 <= 49:
       palette.setColor(QtGui.QPalette.Highlight,
       QtGui.QColor(QtCore.Qt.yellow))
       CH8.setPalette(palette)
    elif 50 <= QualityCH8 <= 89:
       palette.setColor(QtGui.QPalette.Highlight,
       QtGui.QColor(QtCore.Qt.blue))
       CH8.setPalette(palette)
    elif QualityCH8 >= 90:
       palette.setColor(QtGui.QPalette.Highlight,
       QtGui.QColor(QtCore.Qt.green))
       CH8.setPalette(palette)
# Channel No. 8
    if QualityCH8 <= 20:
       palette.setColor(QtGui.QPalette.Highlight,
       QtGui.QColor(QtCore.Qt.red))
       CH8.setPalette(palette)
    elif 21 <= QualityCH8 <= 49:
       palette.setColor(QtGui.QPalette.Highlight,
       QtGui.QColor(QtCore.Qt.yellow))
       CH8.setPalette(palette)
    elif 50 <= QualityCH8 <= 89:
       palette.setColor(QtGui.QPalette.Highlight,
       QtGui.QColor(QtCore.Qt.blue))
       CH8.setPalette(palette)
    elif QualityCH8 >= 90:
       palette.setColor(QtGui.QPalette.Highlight,
       QtGui.QColor(QtCore.Qt.green))
       CH8.setPalette(palette)
# Channel No. 9
    if QualityCH9 <= 20:
       palette.setColor(QtGui.QPalette.Highlight,
       QtGui.QColor(QtCore.Qt.red))
       CH9.setPalette(palette)
    elif 21 <= QualityCH9 <= 49:
       palette.setColor(QtGui.QPalette.Highlight,
       QtGui.QColor(QtCore.Qt.yellow))
       CH9.setPalette(palette)
    elif 50 <= QualityCH9 <= 89:
       palette.setColor(QtGui.QPalette.Highlight,
       QtGui.QColor(QtCore.Qt.blue))
       CH9.setPalette(palette)
    elif QualityCH9 >= 90:
       palette.setColor(QtGui.QPalette.Highlight,
       QtGui.QColor(QtCore.Qt.green))
       CH9.setPalette(palette)
# Channel No. 10
    if QualityCH10 <= 20:
       palette.setColor(QtGui.QPalette.Highlight,
       QtGui.QColor(QtCore.Qt.red))
       CH10.setPalette(palette)
    elif 21 <= QualityCH10 <= 49:
       palette.setColor(QtGui.QPalette.Highlight,
       QtGui.QColor(QtCore.Qt.yellow))
       CH10.setPalette(palette)
    elif 50 <= QualityCH10 <= 89:
       palette.setColor(QtGui.QPalette.Highlight,
       QtGui.QColor(QtCore.Qt.blue))
       CH10.setPalette(palette)
    elif QualityCH10 >= 90:
       palette.setColor(QtGui.QPalette.Highlight,
       QtGui.QColor(QtCore.Qt.green))
       CH10.setPalette(palette)
# Channel No. 11
    if QualityCH11 <= 20:
       palette.setColor(QtGui.QPalette.Highlight,
       QtGui.QColor(QtCore.Qt.red))
       CH11.setPalette(palette)
    elif 21 <= QualityCH11 <= 49:
       palette.setColor(QtGui.QPalette.Highlight,
       QtGui.QColor(QtCore.Qt.yellow))
       CH11.setPalette(palette)
    elif 50 <= QualityCH11 <= 89:
       palette.setColor(QtGui.QPalette.Highlight,
       QtGui.QColor(QtCore.Qt.blue))
       CH11.setPalette(palette)
    elif QualityCH11 >= 90:
       palette.setColor(QtGui.QPalette.Highlight,
       QtGui.QColor(QtCore.Qt.green))
       CH11.setPalette(palette)
# Channel No. 12
    if QualityCH12 <= 20:
       palette.setColor(QtGui.QPalette.Highlight,
       QtGui.QColor(QtCore.Qt.red))
       CH12.setPalette(palette)
    elif 21 <= QualityCH12 <= 49:
       palette.setColor(QtGui.QPalette.Highlight,
       QtGui.QColor(QtCore.Qt.yellow))
       CH12.setPalette(palette)
    elif 50 <= QualityCH12 <= 89:
       palette.setColor(QtGui.QPalette.Highlight,
       QtGui.QColor(QtCore.Qt.blue))
       CH12.setPalette(palette)
    elif QualityCH12 >= 90:
       palette.setColor(QtGui.QPalette.Highlight,
       QtGui.QColor(QtCore.Qt.green))
       CH12.setPalette(palette)
# Channel No. 13
    if QualityCH13 <= 20:
       palette.setColor(QtGui.QPalette.Highlight,
       QtGui.QColor(QtCore.Qt.red))
       CH13.setPalette(palette)
    elif 21 <= QualityCH13 <= 49:
       palette.setColor(QtGui.QPalette.Highlight,
       QtGui.QColor(QtCore.Qt.yellow))
       CH13.setPalette(palette)
    elif 50 <= QualityCH13 <= 89:
       palette.setColor(QtGui.QPalette.Highlight,
       QtGui.QColor(QtCore.Qt.blue))
       CH13.setPalette(palette)
    elif QualityCH13 >= 90:
       palette.setColor(QtGui.QPalette.Highlight,
       QtGui.QColor(QtCore.Qt.green))
       CH13.setPalette(palette)
# Channel No. 14
    if QualityCH14 <= 20:
       palette.setColor(QtGui.QPalette.Highlight,
       QtGui.QColor(QtCore.Qt.red))
       CH14.setPalette(palette)
    elif 21 <= QualityCH14 <= 49:
       palette.setColor(QtGui.QPalette.Highlight,
       QtGui.QColor(QtCore.Qt.yellow))
       CH14.setPalette(palette)
    elif 50 <= QualityCH14 <= 89:
       palette.setColor(QtGui.QPalette.Highlight,
       QtGui.QColor(QtCore.Qt.blue))
       CH14.setPalette(palette)
    elif QualityCH14 >= 90:
       palette.setColor(QtGui.QPalette.Highlight,
       QtGui.QColor(QtCore.Qt.green))
       CH14.setPalette(palette)
