from PyQt4 import QtCore, QtGui

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

def ColorChannelQuality(self, QualityCH1, QualityCH2, QualityCH3):
    palette = QtGui.QPalette()
    CH1 = self.progressBar_CH1
    CH2 = self.progressBar_CH2
    CH3 = self.progressBar_CH3
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
