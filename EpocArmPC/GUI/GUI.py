# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI.ui'
#
# Created: Sun Nov  1 23:31:40 2015
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
        MainWindow.resize(388, 222)
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayoutWidget_9 = QtGui.QWidget(self.centralwidget)
        self.gridLayoutWidget_9.setGeometry(QtCore.QRect(10, 70, 314, 61))
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
        self.gridLayout_8 = QtGui.QGridLayout(self.groupBox_7)
        self.gridLayout_8.setObjectName(_fromUtf8("gridLayout_8"))
        self.label_11 = QtGui.QLabel(self.groupBox_7)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.gridLayout_8.addWidget(self.label_11, 0, 0, 1, 1)
        self.pB_WLeft = QtGui.QProgressBar(self.groupBox_7)
        self.pB_WLeft.setMaximumSize(QtCore.QSize(180, 200))
        self.pB_WLeft.setMaximum(7)
        self.pB_WLeft.setProperty("value", 1)
        self.pB_WLeft.setTextVisible(False)
        self.pB_WLeft.setInvertedAppearance(True)
        self.pB_WLeft.setObjectName(_fromUtf8("pB_WLeft"))
        self.gridLayout_8.addWidget(self.pB_WLeft, 0, 1, 1, 1)
        self.pB_WRight = QtGui.QProgressBar(self.groupBox_7)
        self.pB_WRight.setMaximumSize(QtCore.QSize(180, 200))
        self.pB_WRight.setMaximum(7)
        self.pB_WRight.setProperty("value", 1)
        self.pB_WRight.setTextVisible(False)
        self.pB_WRight.setObjectName(_fromUtf8("pB_WRight"))
        self.gridLayout_8.addWidget(self.pB_WRight, 0, 2, 1, 1)
        self.label_12 = QtGui.QLabel(self.groupBox_7)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.gridLayout_8.addWidget(self.label_12, 0, 3, 1, 1)
        self.gridLayout_24.addWidget(self.groupBox_7, 0, 0, 1, 1)
        self.gridLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 10, 314, 61))
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
        self.gridLayout_5 = QtGui.QGridLayout(self.groupBox)
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.label_18 = QtGui.QLabel(self.groupBox)
        self.label_18.setObjectName(_fromUtf8("label_18"))
        self.gridLayout_5.addWidget(self.label_18, 0, 0, 1, 1)
        self.pB_Gleft = QtGui.QProgressBar(self.groupBox)
        self.pB_Gleft.setMaximum(7)
        self.pB_Gleft.setProperty("value", 1)
        self.pB_Gleft.setTextVisible(False)
        self.pB_Gleft.setInvertedAppearance(True)
        self.pB_Gleft.setObjectName(_fromUtf8("pB_Gleft"))
        self.gridLayout_5.addWidget(self.pB_Gleft, 0, 1, 1, 1)
        self.pB_Gright = QtGui.QProgressBar(self.groupBox)
        self.pB_Gright.setMaximum(7)
        self.pB_Gright.setProperty("value", 1)
        self.pB_Gright.setTextVisible(False)
        self.pB_Gright.setObjectName(_fromUtf8("pB_Gright"))
        self.gridLayout_5.addWidget(self.pB_Gright, 0, 2, 1, 1)
        self.label_19 = QtGui.QLabel(self.groupBox)
        self.label_19.setObjectName(_fromUtf8("label_19"))
        self.gridLayout_5.addWidget(self.label_19, 0, 3, 1, 1)
        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 1)
        self.push_Iniciar = QtGui.QPushButton(self.centralwidget)
        self.push_Iniciar.setGeometry(QtCore.QRect(330, 10, 51, 29))
        self.push_Iniciar.setObjectName(_fromUtf8("push_Iniciar"))
        self.push_Finalizar = QtGui.QPushButton(self.centralwidget)
        self.push_Finalizar.setGeometry(QtCore.QRect(330, 50, 51, 29))
        self.push_Finalizar.setObjectName(_fromUtf8("push_Finalizar"))
        self.push_Salir = QtGui.QPushButton(self.centralwidget)
        self.push_Salir.setGeometry(QtCore.QRect(330, 90, 51, 29))
        self.push_Salir.setObjectName(_fromUtf8("push_Salir"))
        self.gridLayoutWidget_3 = QtGui.QWidget(self.centralwidget)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(10, 130, 371, 61))
        self.gridLayoutWidget_3.setObjectName(_fromUtf8("gridLayoutWidget_3"))
        self.gridLayout_4 = QtGui.QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_4.setMargin(0)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.groupBox_5 = QtGui.QGroupBox(self.gridLayoutWidget_3)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_5.setFont(font)
        self.groupBox_5.setObjectName(_fromUtf8("groupBox_5"))
        self.gridLayout_9 = QtGui.QGridLayout(self.groupBox_5)
        self.gridLayout_9.setObjectName(_fromUtf8("gridLayout_9"))
        self.pB_Beta = QtGui.QProgressBar(self.groupBox_5)
        self.pB_Beta.setMaximumSize(QtCore.QSize(180, 200))
        self.pB_Beta.setMaximum(15)
        self.pB_Beta.setProperty("value", 1)
        self.pB_Beta.setTextVisible(False)
        self.pB_Beta.setInvertedAppearance(False)
        self.pB_Beta.setObjectName(_fromUtf8("pB_Beta"))
        self.gridLayout_9.addWidget(self.pB_Beta, 0, 2, 1, 1)
        self.pB_Alpha = QtGui.QProgressBar(self.groupBox_5)
        self.pB_Alpha.setMaximum(8)
        self.pB_Alpha.setProperty("value", 1)
        self.pB_Alpha.setTextVisible(False)
        self.pB_Alpha.setInvertedAppearance(True)
        self.pB_Alpha.setObjectName(_fromUtf8("pB_Alpha"))
        self.gridLayout_9.addWidget(self.pB_Alpha, 0, 1, 1, 1)
        self.label_20 = QtGui.QLabel(self.groupBox_5)
        self.label_20.setObjectName(_fromUtf8("label_20"))
        self.gridLayout_9.addWidget(self.label_20, 0, 0, 1, 1)
        self.label_14 = QtGui.QLabel(self.groupBox_5)
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.gridLayout_9.addWidget(self.label_14, 0, 3, 1, 1)
        self.gridLayout_4.addWidget(self.groupBox_5, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Interfaz EEG/PC/RobotArm", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_7.setTitle(QtGui.QApplication.translate("MainWindow", "Parpadeo \"Wink\"", None, QtGui.QApplication.UnicodeUTF8))
        self.label_11.setText(QtGui.QApplication.translate("MainWindow", "Izq.", None, QtGui.QApplication.UnicodeUTF8))
        self.label_12.setText(QtGui.QApplication.translate("MainWindow", "Der.", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("MainWindow", "Deflexion \"Gyro\"", None, QtGui.QApplication.UnicodeUTF8))
        self.label_18.setText(QtGui.QApplication.translate("MainWindow", "Izq.", None, QtGui.QApplication.UnicodeUTF8))
        self.label_19.setText(QtGui.QApplication.translate("MainWindow", "Der.", None, QtGui.QApplication.UnicodeUTF8))
        self.push_Iniciar.setText(QtGui.QApplication.translate("MainWindow", "Iniciar", None, QtGui.QApplication.UnicodeUTF8))
        self.push_Finalizar.setText(QtGui.QApplication.translate("MainWindow", "Pausar", None, QtGui.QApplication.UnicodeUTF8))
        self.push_Salir.setText(QtGui.QApplication.translate("MainWindow", "Salir", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_5.setTitle(QtGui.QApplication.translate("MainWindow", "               Relajacion                 Concentracion", None, QtGui.QApplication.UnicodeUTF8))
        self.label_20.setText(QtGui.QApplication.translate("MainWindow", "Abrir", None, QtGui.QApplication.UnicodeUTF8))
        self.label_14.setText(QtGui.QApplication.translate("MainWindow", "Cerrar", None, QtGui.QApplication.UnicodeUTF8))
