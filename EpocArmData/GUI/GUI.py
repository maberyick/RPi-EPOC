# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI.ui'
#
# Created: Wed Oct 14 18:31:29 2015
#      by: PyQt4 UI code generator 4.9.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(739, 664)
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayoutWidget_7 = QtGui.QWidget(self.centralwidget)
        self.gridLayoutWidget_7.setGeometry(QtCore.QRect(200, 20, 281, 61))
        self.gridLayoutWidget_7.setObjectName(_fromUtf8("gridLayoutWidget_7"))
        self.gridLayout_22 = QtGui.QGridLayout(self.gridLayoutWidget_7)
        self.gridLayout_22.setMargin(0)
        self.gridLayout_22.setObjectName(_fromUtf8("gridLayout_22"))
        self.label_prompt = QtGui.QLabel(self.gridLayoutWidget_7)
        self.label_prompt.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.label_prompt.setText(_fromUtf8(""))
        self.label_prompt.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_prompt.setObjectName(_fromUtf8("label_prompt"))
        self.gridLayout_22.addWidget(self.label_prompt, 0, 0, 1, 1)
        self.progressBar_Trial = QtGui.QProgressBar(self.gridLayoutWidget_7)
        self.progressBar_Trial.setMaximum(17200)
        self.progressBar_Trial.setProperty("value", 0)
        self.progressBar_Trial.setTextVisible(False)
        self.progressBar_Trial.setOrientation(QtCore.Qt.Vertical)
        self.progressBar_Trial.setObjectName(_fromUtf8("progressBar_Trial"))
        self.gridLayout_22.addWidget(self.progressBar_Trial, 0, 1, 1, 1)
        self.gridLayoutWidget_9 = QtGui.QWidget(self.centralwidget)
        self.gridLayoutWidget_9.setGeometry(QtCore.QRect(200, 200, 281, 101))
        self.gridLayoutWidget_9.setObjectName(_fromUtf8("gridLayoutWidget_9"))
        self.gridLayout_24 = QtGui.QGridLayout(self.gridLayoutWidget_9)
        self.gridLayout_24.setMargin(0)
        self.gridLayout_24.setObjectName(_fromUtf8("gridLayout_24"))
        self.groupBox_7 = QtGui.QGroupBox(self.gridLayoutWidget_9)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_7.setFont(font)
        self.groupBox_7.setObjectName(_fromUtf8("groupBox_7"))
        self.push_beta_ini = QtGui.QPushButton(self.groupBox_7)
        self.push_beta_ini.setGeometry(QtCore.QRect(220, 70, 51, 29))
        self.push_beta_ini.setObjectName(_fromUtf8("push_beta_ini"))
        self.B_selec_RS = QtGui.QRadioButton(self.groupBox_7)
        self.B_selec_RS.setGeometry(QtCore.QRect(40, 30, 111, 16))
        self.B_selec_RS.setObjectName(_fromUtf8("B_selec_RS"))
        self.prB_restar = QtGui.QProgressBar(self.groupBox_7)
        self.prB_restar.setGeometry(QtCore.QRect(10, 30, 21, 16))
        self.prB_restar.setProperty("value", 100)
        self.prB_restar.setTextVisible(False)
        self.prB_restar.setObjectName(_fromUtf8("prB_restar"))
        self.push_B_plot = QtGui.QPushButton(self.groupBox_7)
        self.push_B_plot.setGeometry(QtCore.QRect(230, 40, 41, 20))
        self.push_B_plot.setObjectName(_fromUtf8("push_B_plot"))
        self.B_selec_RS_S = QtGui.QRadioButton(self.groupBox_7)
        self.B_selec_RS_S.setGeometry(QtCore.QRect(40, 50, 111, 16))
        self.B_selec_RS_S.setObjectName(_fromUtf8("B_selec_RS_S"))
        self.prB_Estandar = QtGui.QProgressBar(self.groupBox_7)
        self.prB_Estandar.setGeometry(QtCore.QRect(10, 50, 21, 16))
        self.prB_Estandar.setProperty("value", 100)
        self.prB_Estandar.setTextVisible(False)
        self.prB_Estandar.setObjectName(_fromUtf8("prB_Estandar"))
        self.prB_Offline = QtGui.QProgressBar(self.groupBox_7)
        self.prB_Offline.setGeometry(QtCore.QRect(10, 70, 21, 16))
        self.prB_Offline.setProperty("value", 100)
        self.prB_Offline.setTextVisible(False)
        self.prB_Offline.setObjectName(_fromUtf8("prB_Offline"))
        self.B_selec_RS_O = QtGui.QRadioButton(self.groupBox_7)
        self.B_selec_RS_O.setGeometry(QtCore.QRect(40, 70, 111, 16))
        self.B_selec_RS_O.setObjectName(_fromUtf8("B_selec_RS_O"))
        self.gridLayout_24.addWidget(self.groupBox_7, 1, 0, 1, 1)
        self.gridLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(200, 90, 281, 101))
        self.gridLayoutWidget.setObjectName(_fromUtf8("gridLayoutWidget"))
        self.gridLayout = QtGui.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.groupBox = QtGui.QGroupBox(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.push_alfa_ini = QtGui.QPushButton(self.groupBox)
        self.push_alfa_ini.setGeometry(QtCore.QRect(220, 70, 51, 29))
        self.push_alfa_ini.setObjectName(_fromUtf8("push_alfa_ini"))
        self.A_selec_ME = QtGui.QRadioButton(self.groupBox)
        self.A_selec_ME.setGeometry(QtCore.QRect(40, 30, 111, 16))
        self.A_selec_ME.setObjectName(_fromUtf8("A_selec_ME"))
        self.label_11 = QtGui.QLabel(self.groupBox)
        self.label_11.setGeometry(QtCore.QRect(150, 20, 91, 21))
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.Folder_A = QtGui.QLineEdit(self.groupBox)
        self.Folder_A.setGeometry(QtCore.QRect(240, 20, 31, 21))
        self.Folder_A.setObjectName(_fromUtf8("Folder_A"))
        self.prB_meditar = QtGui.QProgressBar(self.groupBox)
        self.prB_meditar.setGeometry(QtCore.QRect(10, 30, 21, 16))
        self.prB_meditar.setProperty("value", 100)
        self.prB_meditar.setTextVisible(False)
        self.prB_meditar.setObjectName(_fromUtf8("prB_meditar"))
        self.push_A_plot = QtGui.QPushButton(self.groupBox)
        self.push_A_plot.setGeometry(QtCore.QRect(230, 40, 41, 20))
        self.push_A_plot.setObjectName(_fromUtf8("push_A_plot"))
        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 1)
        self.layoutWidget = QtGui.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 20, 171, 67))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.gridLayout_6 = QtGui.QGridLayout(self.layoutWidget)
        self.gridLayout_6.setMargin(0)
        self.gridLayout_6.setObjectName(_fromUtf8("gridLayout_6"))
        self.groupBox_3 = QtGui.QGroupBox(self.layoutWidget)
        self.groupBox_3.setMaximumSize(QtCore.QSize(184, 117))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_3.setFont(font)
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.gridLayout_13 = QtGui.QGridLayout(self.groupBox_3)
        self.gridLayout_13.setObjectName(_fromUtf8("gridLayout_13"))
        self.progressBar_Bat = QtGui.QProgressBar(self.groupBox_3)
        self.progressBar_Bat.setProperty("value", 0)
        self.progressBar_Bat.setObjectName(_fromUtf8("progressBar_Bat"))
        self.gridLayout_13.addWidget(self.progressBar_Bat, 0, 0, 1, 1)
        self.gridLayout_6.addWidget(self.groupBox_3, 0, 0, 1, 1)
        self.layoutWidget1 = QtGui.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(10, 90, 186, 401))
        self.layoutWidget1.setObjectName(_fromUtf8("layoutWidget1"))
        self.gridLayout_7 = QtGui.QGridLayout(self.layoutWidget1)
        self.gridLayout_7.setMargin(0)
        self.gridLayout_7.setObjectName(_fromUtf8("gridLayout_7"))
        self.groupBox_2 = QtGui.QGroupBox(self.layoutWidget1)
        self.groupBox_2.setMaximumSize(QtCore.QSize(220, 400))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.progressBar_CH4 = QtGui.QProgressBar(self.groupBox_2)
        self.progressBar_CH4.setGeometry(QtCore.QRect(100, 105, 31, 21))
        self.progressBar_CH4.setProperty("value", 100)
        self.progressBar_CH4.setTextVisible(False)
        self.progressBar_CH4.setObjectName(_fromUtf8("progressBar_CH4"))
        self.progressBar_CH8 = QtGui.QProgressBar(self.groupBox_2)
        self.progressBar_CH8.setGeometry(QtCore.QRect(100, 210, 31, 21))
        self.progressBar_CH8.setProperty("value", 100)
        self.progressBar_CH8.setTextVisible(False)
        self.progressBar_CH8.setObjectName(_fromUtf8("progressBar_CH8"))
        self.progressBar_CH1 = QtGui.QProgressBar(self.groupBox_2)
        self.progressBar_CH1.setGeometry(QtCore.QRect(100, 26, 31, 21))
        self.progressBar_CH1.setProperty("value", 100)
        self.progressBar_CH1.setTextVisible(False)
        self.progressBar_CH1.setObjectName(_fromUtf8("progressBar_CH1"))
        self.progressBar_CH5 = QtGui.QProgressBar(self.groupBox_2)
        self.progressBar_CH5.setGeometry(QtCore.QRect(100, 132, 31, 20))
        self.progressBar_CH5.setProperty("value", 100)
        self.progressBar_CH5.setTextVisible(False)
        self.progressBar_CH5.setObjectName(_fromUtf8("progressBar_CH5"))
        self.progressBar_CH10 = QtGui.QProgressBar(self.groupBox_2)
        self.progressBar_CH10.setGeometry(QtCore.QRect(100, 263, 31, 20))
        self.progressBar_CH10.setProperty("value", 100)
        self.progressBar_CH10.setTextVisible(False)
        self.progressBar_CH10.setObjectName(_fromUtf8("progressBar_CH10"))
        self.progressBar_CH6 = QtGui.QProgressBar(self.groupBox_2)
        self.progressBar_CH6.setGeometry(QtCore.QRect(100, 158, 31, 20))
        self.progressBar_CH6.setProperty("value", 100)
        self.progressBar_CH6.setTextVisible(False)
        self.progressBar_CH6.setObjectName(_fromUtf8("progressBar_CH6"))
        self.progressBar_CH2 = QtGui.QProgressBar(self.groupBox_2)
        self.progressBar_CH2.setGeometry(QtCore.QRect(100, 53, 31, 20))
        self.progressBar_CH2.setProperty("value", 100)
        self.progressBar_CH2.setTextVisible(False)
        self.progressBar_CH2.setObjectName(_fromUtf8("progressBar_CH2"))
        self.progressBar_CH3 = QtGui.QProgressBar(self.groupBox_2)
        self.progressBar_CH3.setGeometry(QtCore.QRect(100, 79, 31, 20))
        self.progressBar_CH3.setProperty("value", 100)
        self.progressBar_CH3.setTextVisible(False)
        self.progressBar_CH3.setObjectName(_fromUtf8("progressBar_CH3"))
        self.progressBar_CH7 = QtGui.QProgressBar(self.groupBox_2)
        self.progressBar_CH7.setGeometry(QtCore.QRect(100, 184, 31, 20))
        self.progressBar_CH7.setProperty("value", 100)
        self.progressBar_CH7.setTextVisible(False)
        self.progressBar_CH7.setObjectName(_fromUtf8("progressBar_CH7"))
        self.progressBar_CH9 = QtGui.QProgressBar(self.groupBox_2)
        self.progressBar_CH9.setGeometry(QtCore.QRect(100, 237, 31, 20))
        self.progressBar_CH9.setProperty("value", 100)
        self.progressBar_CH9.setTextVisible(False)
        self.progressBar_CH9.setObjectName(_fromUtf8("progressBar_CH9"))
        self.progressBar_CH12 = QtGui.QProgressBar(self.groupBox_2)
        self.progressBar_CH12.setGeometry(QtCore.QRect(100, 316, 31, 20))
        self.progressBar_CH12.setProperty("value", 100)
        self.progressBar_CH12.setTextVisible(False)
        self.progressBar_CH12.setObjectName(_fromUtf8("progressBar_CH12"))
        self.progressBar_CH11 = QtGui.QProgressBar(self.groupBox_2)
        self.progressBar_CH11.setGeometry(QtCore.QRect(100, 289, 31, 21))
        self.progressBar_CH11.setProperty("value", 100)
        self.progressBar_CH11.setTextVisible(False)
        self.progressBar_CH11.setObjectName(_fromUtf8("progressBar_CH11"))
        self.progressBar_CH13 = QtGui.QProgressBar(self.groupBox_2)
        self.progressBar_CH13.setGeometry(QtCore.QRect(100, 342, 31, 20))
        self.progressBar_CH13.setProperty("value", 100)
        self.progressBar_CH13.setTextVisible(False)
        self.progressBar_CH13.setObjectName(_fromUtf8("progressBar_CH13"))
        self.progressBar_CH14 = QtGui.QProgressBar(self.groupBox_2)
        self.progressBar_CH14.setGeometry(QtCore.QRect(100, 368, 31, 20))
        self.progressBar_CH14.setProperty("value", 100)
        self.progressBar_CH14.setTextVisible(False)
        self.progressBar_CH14.setObjectName(_fromUtf8("progressBar_CH14"))
        self.label_3 = QtGui.QLabel(self.groupBox_2)
        self.label_3.setGeometry(QtCore.QRect(18, 26, 61, 21))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_6 = QtGui.QLabel(self.groupBox_2)
        self.label_6.setGeometry(QtCore.QRect(18, 105, 61, 21))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.label_4 = QtGui.QLabel(self.groupBox_2)
        self.label_4.setGeometry(QtCore.QRect(18, 53, 61, 20))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(self.groupBox_2)
        self.label_5.setGeometry(QtCore.QRect(18, 79, 61, 20))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_7 = QtGui.QLabel(self.groupBox_2)
        self.label_7.setGeometry(QtCore.QRect(18, 132, 61, 20))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.label_8 = QtGui.QLabel(self.groupBox_2)
        self.label_8.setGeometry(QtCore.QRect(18, 158, 74, 20))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.label_9 = QtGui.QLabel(self.groupBox_2)
        self.label_9.setGeometry(QtCore.QRect(18, 184, 74, 20))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.label_10 = QtGui.QLabel(self.groupBox_2)
        self.label_10.setGeometry(QtCore.QRect(18, 210, 54, 21))
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.label_13 = QtGui.QLabel(self.groupBox_2)
        self.label_13.setGeometry(QtCore.QRect(18, 237, 74, 20))
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.label_14 = QtGui.QLabel(self.groupBox_2)
        self.label_14.setGeometry(QtCore.QRect(18, 263, 74, 20))
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.label_15 = QtGui.QLabel(self.groupBox_2)
        self.label_15.setGeometry(QtCore.QRect(18, 289, 62, 21))
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.label_16 = QtGui.QLabel(self.groupBox_2)
        self.label_16.setGeometry(QtCore.QRect(18, 316, 74, 20))
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.label_17 = QtGui.QLabel(self.groupBox_2)
        self.label_17.setGeometry(QtCore.QRect(18, 342, 74, 20))
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.label_20 = QtGui.QLabel(self.groupBox_2)
        self.label_20.setGeometry(QtCore.QRect(18, 368, 74, 20))
        self.label_20.setObjectName(_fromUtf8("label_20"))
        self.gridLayout_7.addWidget(self.groupBox_2, 0, 0, 1, 1)
        self.push_Iniciar = QtGui.QPushButton(self.centralwidget)
        self.push_Iniciar.setGeometry(QtCore.QRect(540, 570, 51, 29))
        self.push_Iniciar.setObjectName(_fromUtf8("push_Iniciar"))
        self.push_Finalizar = QtGui.QPushButton(self.centralwidget)
        self.push_Finalizar.setGeometry(QtCore.QRect(600, 570, 51, 29))
        self.push_Finalizar.setObjectName(_fromUtf8("push_Finalizar"))
        self.push_Salir = QtGui.QPushButton(self.centralwidget)
        self.push_Salir.setGeometry(QtCore.QRect(660, 570, 51, 29))
        self.push_Salir.setObjectName(_fromUtf8("push_Salir"))
        self.gridLayoutWidget_10 = QtGui.QWidget(self.centralwidget)
        self.gridLayoutWidget_10.setGeometry(QtCore.QRect(200, 310, 281, 101))
        self.gridLayoutWidget_10.setObjectName(_fromUtf8("gridLayoutWidget_10"))
        self.gridLayout_26 = QtGui.QGridLayout(self.gridLayoutWidget_10)
        self.gridLayout_26.setMargin(0)
        self.gridLayout_26.setObjectName(_fromUtf8("gridLayout_26"))
        self.groupBox_8 = QtGui.QGroupBox(self.gridLayoutWidget_10)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_8.setFont(font)
        self.groupBox_8.setObjectName(_fromUtf8("groupBox_8"))
        self.push_mu_ini = QtGui.QPushButton(self.groupBox_8)
        self.push_mu_ini.setGeometry(QtCore.QRect(220, 70, 51, 29))
        self.push_mu_ini.setObjectName(_fromUtf8("push_mu_ini"))
        self.Folder_Mu = QtGui.QLineEdit(self.groupBox_8)
        self.Folder_Mu.setGeometry(QtCore.QRect(240, 20, 31, 21))
        self.Folder_Mu.setObjectName(_fromUtf8("Folder_Mu"))
        self.Mu_selec_LH = QtGui.QRadioButton(self.groupBox_8)
        self.Mu_selec_LH.setGeometry(QtCore.QRect(40, 30, 111, 26))
        self.Mu_selec_LH.setObjectName(_fromUtf8("Mu_selec_LH"))
        self.Mu_selec_RH = QtGui.QRadioButton(self.groupBox_8)
        self.Mu_selec_RH.setGeometry(QtCore.QRect(40, 50, 107, 26))
        self.Mu_selec_RH.setObjectName(_fromUtf8("Mu_selec_RH"))
        self.label = QtGui.QLabel(self.groupBox_8)
        self.label.setGeometry(QtCore.QRect(150, 20, 91, 21))
        self.label.setObjectName(_fromUtf8("label"))
        self.prB_Imgright = QtGui.QProgressBar(self.groupBox_8)
        self.prB_Imgright.setGeometry(QtCore.QRect(10, 56, 21, 16))
        self.prB_Imgright.setProperty("value", 100)
        self.prB_Imgright.setTextVisible(False)
        self.prB_Imgright.setObjectName(_fromUtf8("prB_Imgright"))
        self.prB_Imgleft = QtGui.QProgressBar(self.groupBox_8)
        self.prB_Imgleft.setGeometry(QtCore.QRect(10, 35, 21, 16))
        self.prB_Imgleft.setProperty("value", 100)
        self.prB_Imgleft.setTextVisible(False)
        self.prB_Imgleft.setObjectName(_fromUtf8("prB_Imgleft"))
        self.push_Mu_plot = QtGui.QPushButton(self.groupBox_8)
        self.push_Mu_plot.setGeometry(QtCore.QRect(230, 40, 41, 20))
        self.push_Mu_plot.setObjectName(_fromUtf8("push_Mu_plot"))
        self.gridLayout_26.addWidget(self.groupBox_8, 0, 0, 1, 1)
        self.layoutWidget_2 = QtGui.QWidget(self.centralwidget)
        self.layoutWidget_2.setGeometry(QtCore.QRect(490, 20, 241, 131))
        self.layoutWidget_2.setObjectName(_fromUtf8("layoutWidget_2"))
        self.gridLayout_8 = QtGui.QGridLayout(self.layoutWidget_2)
        self.gridLayout_8.setMargin(0)
        self.gridLayout_8.setObjectName(_fromUtf8("gridLayout_8"))
        self.groupBox_4 = QtGui.QGroupBox(self.layoutWidget_2)
        self.groupBox_4.setMaximumSize(QtCore.QSize(184, 117))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_4.setFont(font)
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
        self.gridLayout_14 = QtGui.QGridLayout(self.groupBox_4)
        self.gridLayout_14.setObjectName(_fromUtf8("gridLayout_14"))
        self.label_prosex = QtGui.QLineEdit(self.groupBox_4)
        self.label_prosex.setObjectName(_fromUtf8("label_prosex"))
        self.gridLayout_14.addWidget(self.label_prosex, 3, 1, 1, 1)
        self.label_proage = QtGui.QLineEdit(self.groupBox_4)
        self.label_proage.setObjectName(_fromUtf8("label_proage"))
        self.gridLayout_14.addWidget(self.label_proage, 2, 1, 1, 1)
        self.label_18 = QtGui.QLabel(self.groupBox_4)
        self.label_18.setObjectName(_fromUtf8("label_18"))
        self.gridLayout_14.addWidget(self.label_18, 2, 0, 1, 1)
        self.label_19 = QtGui.QLabel(self.groupBox_4)
        self.label_19.setObjectName(_fromUtf8("label_19"))
        self.gridLayout_14.addWidget(self.label_19, 3, 0, 1, 1)
        self.label_proname = QtGui.QLineEdit(self.groupBox_4)
        self.label_proname.setObjectName(_fromUtf8("label_proname"))
        self.gridLayout_14.addWidget(self.label_proname, 0, 1, 1, 1)
        self.label_12 = QtGui.QLabel(self.groupBox_4)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.gridLayout_14.addWidget(self.label_12, 0, 0, 1, 1)
        self.gridLayout_8.addWidget(self.groupBox_4, 0, 0, 1, 1)
        self.layoutWidget_3 = QtGui.QWidget(self.centralwidget)
        self.layoutWidget_3.setGeometry(QtCore.QRect(490, 160, 241, 351))
        self.layoutWidget_3.setObjectName(_fromUtf8("layoutWidget_3"))
        self.gridLayout_9 = QtGui.QGridLayout(self.layoutWidget_3)
        self.gridLayout_9.setMargin(0)
        self.gridLayout_9.setObjectName(_fromUtf8("gridLayout_9"))
        self.gridLayout_23 = QtGui.QGridLayout()
        self.gridLayout_23.setObjectName(_fromUtf8("gridLayout_23"))
        self.label_results = QtGui.QLabel(self.layoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(6)
        font.setBold(False)
        font.setWeight(50)
        self.label_results.setFont(font)
        self.label_results.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.label_results.setText(_fromUtf8(""))
        self.label_results.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_results.setObjectName(_fromUtf8("label_results"))
        self.gridLayout_23.addWidget(self.label_results, 0, 0, 1, 1)
        self.gridLayout_9.addLayout(self.gridLayout_23, 1, 0, 1, 1)
        self.groupBox_5 = QtGui.QGroupBox(self.layoutWidget_3)
        self.groupBox_5.setMaximumSize(QtCore.QSize(184, 117))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_5.setFont(font)
        self.groupBox_5.setObjectName(_fromUtf8("groupBox_5"))
        self.gridLayout_15 = QtGui.QGridLayout(self.groupBox_5)
        self.gridLayout_15.setObjectName(_fromUtf8("gridLayout_15"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.label_21 = QtGui.QLabel(self.groupBox_5)
        font = QtGui.QFont()
        font.setPointSize(7)
        self.label_21.setFont(font)
        self.label_21.setTextFormat(QtCore.Qt.AutoText)
        self.label_21.setScaledContents(True)
        self.label_21.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_21.setWordWrap(True)
        self.label_21.setObjectName(_fromUtf8("label_21"))
        self.verticalLayout_2.addWidget(self.label_21)
        self.push_processing = QtGui.QPushButton(self.groupBox_5)
        self.push_processing.setObjectName(_fromUtf8("push_processing"))
        self.verticalLayout_2.addWidget(self.push_processing)
        self.gridLayout_15.addLayout(self.verticalLayout_2, 1, 0, 1, 1)
        self.gridLayout_9.addWidget(self.groupBox_5, 0, 0, 1, 1)
        self.push_saving = QtGui.QPushButton(self.centralwidget)
        self.push_saving.setGeometry(QtCore.QRect(620, 520, 93, 29))
        self.push_saving.setObjectName(_fromUtf8("push_saving"))
        self.push_Ckstatus = QtGui.QPushButton(self.centralwidget)
        self.push_Ckstatus.setGeometry(QtCore.QRect(510, 520, 101, 29))
        self.push_Ckstatus.setObjectName(_fromUtf8("push_Ckstatus"))
        self.gridLayoutWidget_11 = QtGui.QWidget(self.centralwidget)
        self.gridLayoutWidget_11.setGeometry(QtCore.QRect(200, 420, 281, 101))
        self.gridLayoutWidget_11.setObjectName(_fromUtf8("gridLayoutWidget_11"))
        self.gridLayout_27 = QtGui.QGridLayout(self.gridLayoutWidget_11)
        self.gridLayout_27.setMargin(0)
        self.gridLayout_27.setObjectName(_fromUtf8("gridLayout_27"))
        self.groupBox_9 = QtGui.QGroupBox(self.gridLayoutWidget_11)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_9.setFont(font)
        self.groupBox_9.setObjectName(_fromUtf8("groupBox_9"))
        self.push_wink_ini = QtGui.QPushButton(self.groupBox_9)
        self.push_wink_ini.setGeometry(QtCore.QRect(220, 70, 51, 29))
        self.push_wink_ini.setObjectName(_fromUtf8("push_wink_ini"))
        self.MG_selec_WL = QtGui.QRadioButton(self.groupBox_9)
        self.MG_selec_WL.setGeometry(QtCore.QRect(40, 30, 111, 20))
        self.MG_selec_WL.setObjectName(_fromUtf8("MG_selec_WL"))
        self.MG_selec_WR = QtGui.QRadioButton(self.groupBox_9)
        self.MG_selec_WR.setGeometry(QtCore.QRect(40, 50, 107, 16))
        self.MG_selec_WR.setObjectName(_fromUtf8("MG_selec_WR"))
        self.prB_Wright = QtGui.QProgressBar(self.groupBox_9)
        self.prB_Wright.setGeometry(QtCore.QRect(10, 50, 21, 16))
        self.prB_Wright.setProperty("value", 100)
        self.prB_Wright.setTextVisible(False)
        self.prB_Wright.setObjectName(_fromUtf8("prB_Wright"))
        self.prB_Wleft = QtGui.QProgressBar(self.groupBox_9)
        self.prB_Wleft.setGeometry(QtCore.QRect(10, 30, 21, 16))
        self.prB_Wleft.setProperty("value", 100)
        self.prB_Wleft.setTextVisible(False)
        self.prB_Wleft.setObjectName(_fromUtf8("prB_Wleft"))
        self.push_EMG_plot = QtGui.QPushButton(self.groupBox_9)
        self.push_EMG_plot.setGeometry(QtCore.QRect(230, 40, 41, 20))
        self.push_EMG_plot.setObjectName(_fromUtf8("push_EMG_plot"))
        self.prB_EOG = QtGui.QProgressBar(self.groupBox_9)
        self.prB_EOG.setGeometry(QtCore.QRect(10, 70, 21, 16))
        self.prB_EOG.setProperty("value", 100)
        self.prB_EOG.setTextVisible(False)
        self.prB_EOG.setObjectName(_fromUtf8("prB_EOG"))
        self.MG_selec_EOG = QtGui.QRadioButton(self.groupBox_9)
        self.MG_selec_EOG.setGeometry(QtCore.QRect(40, 70, 111, 16))
        self.MG_selec_EOG.setObjectName(_fromUtf8("MG_selec_EOG"))
        self.gridLayout_27.addWidget(self.groupBox_9, 0, 0, 1, 1)
        self.layoutWidget_4 = QtGui.QWidget(self.centralwidget)
        self.layoutWidget_4.setGeometry(QtCore.QRect(10, 500, 181, 94))
        self.layoutWidget_4.setObjectName(_fromUtf8("layoutWidget_4"))
        self.gridLayout_10 = QtGui.QGridLayout(self.layoutWidget_4)
        self.gridLayout_10.setMargin(0)
        self.gridLayout_10.setObjectName(_fromUtf8("gridLayout_10"))
        self.groupBox_6 = QtGui.QGroupBox(self.layoutWidget_4)
        self.groupBox_6.setMaximumSize(QtCore.QSize(184, 116))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_6.setFont(font)
        self.groupBox_6.setObjectName(_fromUtf8("groupBox_6"))
        self.gridLayout_18 = QtGui.QGridLayout(self.groupBox_6)
        self.gridLayout_18.setObjectName(_fromUtf8("gridLayout_18"))
        self.groupBox_10 = QtGui.QGroupBox(self.groupBox_6)
        self.groupBox_10.setMaximumSize(QtCore.QSize(76, 80))
        self.groupBox_10.setTitle(_fromUtf8(""))
        self.groupBox_10.setObjectName(_fromUtf8("groupBox_10"))
        self.gridLayout_19 = QtGui.QGridLayout(self.groupBox_10)
        self.gridLayout_19.setObjectName(_fromUtf8("gridLayout_19"))
        self.label_GyroX = QtGui.QLabel(self.groupBox_10)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_GyroX.setFont(font)
        self.label_GyroX.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.label_GyroX.setText(_fromUtf8(""))
        self.label_GyroX.setAlignment(QtCore.Qt.AlignCenter)
        self.label_GyroX.setObjectName(_fromUtf8("label_GyroX"))
        self.gridLayout_19.addWidget(self.label_GyroX, 0, 0, 1, 1)
        self.gridLayout_18.addWidget(self.groupBox_10, 0, 0, 1, 1)
        self.gridLayout_10.addWidget(self.groupBox_6, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 739, 29))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Interfaz EEG/PC/RobotArm", None, QtGui.QApplication.UnicodeUTF8))
        self.progressBar_Trial.setFormat(QtGui.QApplication.translate("MainWindow", "%v", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_7.setTitle(QtGui.QApplication.translate("MainWindow", "Concentracion", None, QtGui.QApplication.UnicodeUTF8))
        self.push_beta_ini.setText(QtGui.QApplication.translate("MainWindow", "Iniciar", None, QtGui.QApplication.UnicodeUTF8))
        self.B_selec_RS.setText(QtGui.QApplication.translate("MainWindow", "Concentrar", None, QtGui.QApplication.UnicodeUTF8))
        self.push_B_plot.setText(QtGui.QApplication.translate("MainWindow", "Plot", None, QtGui.QApplication.UnicodeUTF8))
        self.B_selec_RS_S.setText(QtGui.QApplication.translate("MainWindow", "Estandar", None, QtGui.QApplication.UnicodeUTF8))
        self.B_selec_RS_O.setText(QtGui.QApplication.translate("MainWindow", "Offline", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("MainWindow", "Meditacion", None, QtGui.QApplication.UnicodeUTF8))
        self.push_alfa_ini.setText(QtGui.QApplication.translate("MainWindow", "Iniciar", None, QtGui.QApplication.UnicodeUTF8))
        self.A_selec_ME.setText(QtGui.QApplication.translate("MainWindow", "Meditar", None, QtGui.QApplication.UnicodeUTF8))
        self.label_11.setText(QtGui.QApplication.translate("MainWindow", "Trial (1-5)", None, QtGui.QApplication.UnicodeUTF8))
        self.push_A_plot.setText(QtGui.QApplication.translate("MainWindow", "Plot", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_3.setTitle(QtGui.QApplication.translate("MainWindow", "Nivel de Bateria", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setTitle(QtGui.QApplication.translate("MainWindow", "Calidad de los Canales", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("MainWindow", "CH1 O1", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("MainWindow", "CH4 P8", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("MainWindow", "CH2 O2", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("MainWindow", "CH3 P7", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("MainWindow", "CH5 F3", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("MainWindow", "CH6 F4", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setText(QtGui.QApplication.translate("MainWindow", "CH7 T7", None, QtGui.QApplication.UnicodeUTF8))
        self.label_10.setText(QtGui.QApplication.translate("MainWindow", "CH8 T8", None, QtGui.QApplication.UnicodeUTF8))
        self.label_13.setText(QtGui.QApplication.translate("MainWindow", "CH9 FC5", None, QtGui.QApplication.UnicodeUTF8))
        self.label_14.setText(QtGui.QApplication.translate("MainWindow", "CH10 FC6", None, QtGui.QApplication.UnicodeUTF8))
        self.label_15.setText(QtGui.QApplication.translate("MainWindow", "CH11 F7", None, QtGui.QApplication.UnicodeUTF8))
        self.label_16.setText(QtGui.QApplication.translate("MainWindow", "CH12 F8", None, QtGui.QApplication.UnicodeUTF8))
        self.label_17.setText(QtGui.QApplication.translate("MainWindow", "CH13 AF3", None, QtGui.QApplication.UnicodeUTF8))
        self.label_20.setText(QtGui.QApplication.translate("MainWindow", "CH14 AF4", None, QtGui.QApplication.UnicodeUTF8))
        self.push_Iniciar.setText(QtGui.QApplication.translate("MainWindow", "Iniciar", None, QtGui.QApplication.UnicodeUTF8))
        self.push_Finalizar.setText(QtGui.QApplication.translate("MainWindow", "Pausar", None, QtGui.QApplication.UnicodeUTF8))
        self.push_Salir.setText(QtGui.QApplication.translate("MainWindow", "Salir", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_8.setTitle(QtGui.QApplication.translate("MainWindow", "Motor Imagery", None, QtGui.QApplication.UnicodeUTF8))
        self.push_mu_ini.setText(QtGui.QApplication.translate("MainWindow", "Iniciar", None, QtGui.QApplication.UnicodeUTF8))
        self.Mu_selec_LH.setText(QtGui.QApplication.translate("MainWindow", "Mano Izq.", None, QtGui.QApplication.UnicodeUTF8))
        self.Mu_selec_RH.setText(QtGui.QApplication.translate("MainWindow", "Mano Der.", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "Trial (1-5)", None, QtGui.QApplication.UnicodeUTF8))
        self.push_Mu_plot.setText(QtGui.QApplication.translate("MainWindow", "Plot", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_4.setTitle(QtGui.QApplication.translate("MainWindow", "Profile", None, QtGui.QApplication.UnicodeUTF8))
        self.label_18.setText(QtGui.QApplication.translate("MainWindow", "Edad", None, QtGui.QApplication.UnicodeUTF8))
        self.label_19.setText(QtGui.QApplication.translate("MainWindow", "Genero", None, QtGui.QApplication.UnicodeUTF8))
        self.label_12.setText(QtGui.QApplication.translate("MainWindow", "Nombre", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_5.setTitle(QtGui.QApplication.translate("MainWindow", "Resultados", None, QtGui.QApplication.UnicodeUTF8))
        self.label_21.setText(QtGui.QApplication.translate("MainWindow", "Ejecutar el calculo de los rangos, filtros espaciales y clasificadores del usuario.", None, QtGui.QApplication.UnicodeUTF8))
        self.push_processing.setText(QtGui.QApplication.translate("MainWindow", "Ejecutar", None, QtGui.QApplication.UnicodeUTF8))
        self.push_saving.setText(QtGui.QApplication.translate("MainWindow", "Guardar", None, QtGui.QApplication.UnicodeUTF8))
        self.push_Ckstatus.setText(QtGui.QApplication.translate("MainWindow", "Check Status", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_9.setTitle(QtGui.QApplication.translate("MainWindow", "Winking", None, QtGui.QApplication.UnicodeUTF8))
        self.push_wink_ini.setText(QtGui.QApplication.translate("MainWindow", "Iniciar", None, QtGui.QApplication.UnicodeUTF8))
        self.MG_selec_WL.setText(QtGui.QApplication.translate("MainWindow", "Wink Izq.", None, QtGui.QApplication.UnicodeUTF8))
        self.MG_selec_WR.setText(QtGui.QApplication.translate("MainWindow", "Wink Der.", None, QtGui.QApplication.UnicodeUTF8))
        self.push_EMG_plot.setText(QtGui.QApplication.translate("MainWindow", "Plot", None, QtGui.QApplication.UnicodeUTF8))
        self.MG_selec_EOG.setText(QtGui.QApplication.translate("MainWindow", "EOG", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_6.setTitle(QtGui.QApplication.translate("MainWindow", "Valor del Gyro (X)", None, QtGui.QApplication.UnicodeUTF8))
