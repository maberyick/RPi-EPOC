# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI.ui'
#
# Created: Wed Apr  6 22:40:52 2016
#      by: PyQt4 UI code generator 4.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1112, 586)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout_10 = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout_10.setObjectName(_fromUtf8("gridLayout_10"))
        self.groupBox_2 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_2.setTitle(_fromUtf8(""))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.gridLayout_5 = QtGui.QGridLayout(self.groupBox_2)
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.push_Iniciar = QtGui.QPushButton(self.groupBox_2)
        self.push_Iniciar.setObjectName(_fromUtf8("push_Iniciar"))
        self.gridLayout_5.addWidget(self.push_Iniciar, 0, 0, 1, 1)
        self.push_Finalizar = QtGui.QPushButton(self.groupBox_2)
        self.push_Finalizar.setObjectName(_fromUtf8("push_Finalizar"))
        self.gridLayout_5.addWidget(self.push_Finalizar, 1, 0, 1, 1)
        self.push_Salir = QtGui.QPushButton(self.groupBox_2)
        self.push_Salir.setObjectName(_fromUtf8("push_Salir"))
        self.gridLayout_5.addWidget(self.push_Salir, 2, 0, 1, 1)
        self.gridLayout_10.addWidget(self.groupBox_2, 0, 0, 1, 1)
        self.gridLayout_14 = QtGui.QGridLayout()
        self.gridLayout_14.setObjectName(_fromUtf8("gridLayout_14"))
        spacerItem = QtGui.QSpacerItem(900, 1, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.gridLayout_14.addItem(spacerItem, 1, 0, 1, 1)
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.gridLayoutWidget_6 = QtGui.QWidget(self.tab_2)
        self.gridLayoutWidget_6.setGeometry(QtCore.QRect(280, 10, 591, 431))
        self.gridLayoutWidget_6.setObjectName(_fromUtf8("gridLayoutWidget_6"))
        self.gridLayout_25 = QtGui.QGridLayout(self.gridLayoutWidget_6)
        self.gridLayout_25.setMargin(0)
        self.gridLayout_25.setObjectName(_fromUtf8("gridLayout_25"))
        self.graphicsView_eeg = GraphicsLayoutWidget(self.gridLayoutWidget_6)
        self.graphicsView_eeg.setObjectName(_fromUtf8("graphicsView_eeg"))
        self.gridLayout_25.addWidget(self.graphicsView_eeg, 0, 0, 1, 1)
        self.push_eegini = QtGui.QPushButton(self.tab_2)
        self.push_eegini.setGeometry(QtCore.QRect(700, 470, 93, 29))
        self.push_eegini.setObjectName(_fromUtf8("push_eegini"))
        self.push_eegend = QtGui.QPushButton(self.tab_2)
        self.push_eegend.setGeometry(QtCore.QRect(800, 470, 93, 29))
        self.push_eegend.setObjectName(_fromUtf8("push_eegend"))
        self.gridLayoutWidget_4 = QtGui.QWidget(self.tab_2)
        self.gridLayoutWidget_4.setGeometry(QtCore.QRect(10, 10, 261, 91))
        self.gridLayoutWidget_4.setObjectName(_fromUtf8("gridLayoutWidget_4"))
        self.gridLayout_4 = QtGui.QGridLayout(self.gridLayoutWidget_4)
        self.gridLayout_4.setMargin(0)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.treeWidget_eeg = QtGui.QTreeWidget(self.gridLayoutWidget_4)
        self.treeWidget_eeg.setObjectName(_fromUtf8("treeWidget_eeg"))
        self.treeWidget_eeg.headerItem().setText(0, _fromUtf8("1"))
        self.treeWidget_eeg.header().setVisible(False)
        self.gridLayout_4.addWidget(self.treeWidget_eeg, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.gridLayoutWidget_5 = QtGui.QWidget(self.tab)
        self.gridLayoutWidget_5.setGeometry(QtCore.QRect(280, 10, 591, 431))
        self.gridLayoutWidget_5.setObjectName(_fromUtf8("gridLayoutWidget_5"))
        self.gridLayout_21 = QtGui.QGridLayout(self.gridLayoutWidget_5)
        self.gridLayout_21.setMargin(0)
        self.gridLayout_21.setObjectName(_fromUtf8("gridLayout_21"))
        self.graphicsView_emg = GraphicsLayoutWidget(self.gridLayoutWidget_5)
        self.graphicsView_emg.setObjectName(_fromUtf8("graphicsView_emg"))
        self.gridLayout_21.addWidget(self.graphicsView_emg, 0, 0, 1, 1)
        self.push_emgend = QtGui.QPushButton(self.tab)
        self.push_emgend.setGeometry(QtCore.QRect(800, 470, 93, 29))
        self.push_emgend.setObjectName(_fromUtf8("push_emgend"))
        self.push_emgini = QtGui.QPushButton(self.tab)
        self.push_emgini.setGeometry(QtCore.QRect(700, 470, 93, 29))
        self.push_emgini.setObjectName(_fromUtf8("push_emgini"))
        self.gridLayoutWidget_3 = QtGui.QWidget(self.tab)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(10, 10, 261, 91))
        self.gridLayoutWidget_3.setObjectName(_fromUtf8("gridLayoutWidget_3"))
        self.gridLayout_3 = QtGui.QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_3.setMargin(0)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.treeWidget_emg = QtGui.QTreeWidget(self.gridLayoutWidget_3)
        self.treeWidget_emg.setObjectName(_fromUtf8("treeWidget_emg"))
        self.treeWidget_emg.headerItem().setText(0, _fromUtf8("1"))
        self.treeWidget_emg.header().setVisible(False)
        self.gridLayout_3.addWidget(self.treeWidget_emg, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.gridLayoutWidget_13 = QtGui.QWidget(self.tab_3)
        self.gridLayoutWidget_13.setGeometry(QtCore.QRect(280, 10, 591, 431))
        self.gridLayoutWidget_13.setObjectName(_fromUtf8("gridLayoutWidget_13"))
        self.gridLayout_29 = QtGui.QGridLayout(self.gridLayoutWidget_13)
        self.gridLayout_29.setMargin(0)
        self.gridLayout_29.setObjectName(_fromUtf8("gridLayout_29"))
        self.graphicsView_gyro = GraphicsLayoutWidget(self.gridLayoutWidget_13)
        self.graphicsView_gyro.setObjectName(_fromUtf8("graphicsView_gyro"))
        self.gridLayout_29.addWidget(self.graphicsView_gyro, 0, 1, 1, 1)
        self.push_Gyroini = QtGui.QPushButton(self.tab_3)
        self.push_Gyroini.setGeometry(QtCore.QRect(700, 470, 93, 29))
        self.push_Gyroini.setObjectName(_fromUtf8("push_Gyroini"))
        self.push_Gyroend = QtGui.QPushButton(self.tab_3)
        self.push_Gyroend.setGeometry(QtCore.QRect(800, 470, 93, 29))
        self.push_Gyroend.setObjectName(_fromUtf8("push_Gyroend"))
        self.gridLayoutWidget_2 = QtGui.QWidget(self.tab_3)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(10, 10, 261, 91))
        self.gridLayoutWidget_2.setObjectName(_fromUtf8("gridLayoutWidget_2"))
        self.gridLayout_2 = QtGui.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setMargin(0)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.treeWidget_gyro = QtGui.QTreeWidget(self.gridLayoutWidget_2)
        self.treeWidget_gyro.setProperty("showDropIndicator", True)
        self.treeWidget_gyro.setExpandsOnDoubleClick(True)
        self.treeWidget_gyro.setColumnCount(1)
        self.treeWidget_gyro.setObjectName(_fromUtf8("treeWidget_gyro"))
        self.treeWidget_gyro.headerItem().setText(0, _fromUtf8("1"))
        self.treeWidget_gyro.header().setVisible(False)
        self.treeWidget_gyro.header().setStretchLastSection(True)
        self.gridLayout_2.addWidget(self.treeWidget_gyro, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_3, _fromUtf8(""))
        self.gridLayout_14.addWidget(self.tabWidget, 0, 0, 1, 1)
        self.gridLayout_10.addLayout(self.gridLayout_14, 0, 1, 5, 1)
        self.gridLayout_6 = QtGui.QGridLayout()
        self.gridLayout_6.setObjectName(_fromUtf8("gridLayout_6"))
        self.gB_bateria = QtGui.QGroupBox(self.centralwidget)
        self.gB_bateria.setMaximumSize(QtCore.QSize(184, 117))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.gB_bateria.setFont(font)
        self.gB_bateria.setObjectName(_fromUtf8("gB_bateria"))
        self.gridLayout_13 = QtGui.QGridLayout(self.gB_bateria)
        self.gridLayout_13.setObjectName(_fromUtf8("gridLayout_13"))
        self.progressBar_Bat = QtGui.QProgressBar(self.gB_bateria)
        self.progressBar_Bat.setProperty("value", 0)
        self.progressBar_Bat.setObjectName(_fromUtf8("progressBar_Bat"))
        self.gridLayout_13.addWidget(self.progressBar_Bat, 0, 0, 1, 1)
        self.gridLayout_6.addWidget(self.gB_bateria, 0, 0, 1, 1)
        self.gridLayout_10.addLayout(self.gridLayout_6, 1, 0, 1, 1)
        self.gL_calidad = QtGui.QGridLayout()
        self.gL_calidad.setObjectName(_fromUtf8("gL_calidad"))
        self.gB_calidad = QtGui.QGroupBox(self.centralwidget)
        self.gB_calidad.setMaximumSize(QtCore.QSize(184, 312))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.gB_calidad.setFont(font)
        self.gB_calidad.setObjectName(_fromUtf8("gB_calidad"))
        self.gridLayout_12 = QtGui.QGridLayout(self.gB_calidad)
        self.gridLayout_12.setObjectName(_fromUtf8("gridLayout_12"))
        self.gridLayout_11 = QtGui.QGridLayout()
        self.gridLayout_11.setObjectName(_fromUtf8("gridLayout_11"))
        spacerItem1 = QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.gridLayout_11.addItem(spacerItem1, 1, 0, 1, 1)
        self.progressBar_CH3 = QtGui.QProgressBar(self.gB_calidad)
        self.progressBar_CH3.setProperty("value", 100)
        self.progressBar_CH3.setTextVisible(False)
        self.progressBar_CH3.setObjectName(_fromUtf8("progressBar_CH3"))
        self.gridLayout_11.addWidget(self.progressBar_CH3, 2, 1, 1, 1)
        self.progressBar_CH4 = QtGui.QProgressBar(self.gB_calidad)
        self.progressBar_CH4.setProperty("value", 100)
        self.progressBar_CH4.setTextVisible(False)
        self.progressBar_CH4.setObjectName(_fromUtf8("progressBar_CH4"))
        self.gridLayout_11.addWidget(self.progressBar_CH4, 3, 1, 1, 1)
        self.progressBar_CH5 = QtGui.QProgressBar(self.gB_calidad)
        self.progressBar_CH5.setProperty("value", 100)
        self.progressBar_CH5.setTextVisible(False)
        self.progressBar_CH5.setObjectName(_fromUtf8("progressBar_CH5"))
        self.gridLayout_11.addWidget(self.progressBar_CH5, 4, 1, 1, 1)
        self.progressBar_CH1 = QtGui.QProgressBar(self.gB_calidad)
        self.progressBar_CH1.setProperty("value", 100)
        self.progressBar_CH1.setTextVisible(False)
        self.progressBar_CH1.setObjectName(_fromUtf8("progressBar_CH1"))
        self.gridLayout_11.addWidget(self.progressBar_CH1, 0, 1, 1, 1)
        self.progressBar_CH2 = QtGui.QProgressBar(self.gB_calidad)
        self.progressBar_CH2.setProperty("value", 100)
        self.progressBar_CH2.setTextVisible(False)
        self.progressBar_CH2.setObjectName(_fromUtf8("progressBar_CH2"))
        self.gridLayout_11.addWidget(self.progressBar_CH2, 1, 1, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(120, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.gridLayout_11.addItem(spacerItem2, 2, 2, 1, 1)
        self.gridLayout_12.addLayout(self.gridLayout_11, 0, 1, 1, 1)
        self.vL_epoc = QtGui.QVBoxLayout()
        self.vL_epoc.setObjectName(_fromUtf8("vL_epoc"))
        self.label_3 = QtGui.QLabel(self.gB_calidad)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.vL_epoc.addWidget(self.label_3)
        self.label_4 = QtGui.QLabel(self.gB_calidad)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.vL_epoc.addWidget(self.label_4)
        self.label_5 = QtGui.QLabel(self.gB_calidad)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.vL_epoc.addWidget(self.label_5)
        self.label_6 = QtGui.QLabel(self.gB_calidad)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.vL_epoc.addWidget(self.label_6)
        self.label_7 = QtGui.QLabel(self.gB_calidad)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.vL_epoc.addWidget(self.label_7)
        self.gridLayout_12.addLayout(self.vL_epoc, 0, 0, 1, 1)
        self.gL_calidad.addWidget(self.gB_calidad, 0, 0, 1, 1)
        self.gridLayout_10.addLayout(self.gL_calidad, 2, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1112, 27))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "EPOC Visualizer", None))
        self.push_Iniciar.setText(_translate("MainWindow", "Iniciar", None))
        self.push_Finalizar.setText(_translate("MainWindow", "Pausar", None))
        self.push_Salir.setText(_translate("MainWindow", "Salir", None))
        self.push_eegini.setText(_translate("MainWindow", "Iniciar", None))
        self.push_eegend.setText(_translate("MainWindow", "Pausar", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "EEG", None))
        self.push_emgend.setText(_translate("MainWindow", "Pausar", None))
        self.push_emgini.setText(_translate("MainWindow", "Iniciar", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "EMG", None))
        self.push_Gyroini.setText(_translate("MainWindow", "Iniciar", None))
        self.push_Gyroend.setText(_translate("MainWindow", "Pausar", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Gyro", None))
        self.gB_bateria.setTitle(_translate("MainWindow", "Nivel de Bateria", None))
        self.gB_calidad.setTitle(_translate("MainWindow", "Calidad de Canales", None))
        self.label_3.setText(_translate("MainWindow", "CH1  O2", None))
        self.label_4.setText(_translate("MainWindow", "CH2  AF3", None))
        self.label_5.setText(_translate("MainWindow", "CH3  F8", None))
        self.label_6.setText(_translate("MainWindow", "CH4  F3", None))
        self.label_7.setText(_translate("MainWindow", "CH5  F4", None))

from pyqtgraph import GraphicsLayoutWidget