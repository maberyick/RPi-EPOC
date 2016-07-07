from pygame import mixer
from PyQt4 import QtCore, QtGui
from random import randint as ran

""" Sound Mixer """
mixer.init()
alert_1 = mixer.Sound('Alert/snd1.wav')
alert_2 = mixer.Sound('Alert/snd2.wav')

""" Alpha """
def alfa_closede(self):
	self.label_prompt.setText("Cerrar ojos y Relajarse")
	alert_1.play()
""" Beta """
def beta_rest(self):
	exec "self.label_prompt.setText('Contar hacia atras en 3 desde %s')" %(ran(300,1000))
	alert_1.play()
""" Mu """
def mu_onleft(self):
	self.label_prompt.setText("Imaginar apretar la mano izquierda")
	alert_1.play()
def mu_onright(self):
	self.label_prompt.setText("Imaginar apretar la mano derecha")
	alert_1.play()
""" Arctifacts """
def emg_wleft(self):
	self.label_prompt.setText("Guino ojo izquierdo")
	alert_1.play()
def emg_wright(self):
	self.label_prompt.setText("Guino ojo derecho")
	alert_1.play()
""" Hacer Nada """
def donothing(self):
	self.label_prompt.setText("Hacer Nada")
	alert_1.play()
""" Relajarse """
def standard_re(self):
	self.label_prompt.setText("Relajarse")
""" Guardando """
def savinginfo(self):
	self.label_prompt.setText("Guardando archivos...")
	alert_2.play()
""" Finito """
def finito(self):
	self.label_prompt.setText(" ")
""" Offline """
def offline_re(self):
	self.label_prompt.setText("Dejar el EEG alejado y no puesto")
""" EOG """
def _eog(self):
	self.label_prompt.setText("Mover los ojos a la Izquierda")
	alert_1.play()
