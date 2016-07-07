import sys
from PyQt4 import QtCore, QtGui
from scipy.io import savemat
import loadmat_new
from os import getcwd as getdir
from os import path as pth
from os.path import exists
from os import makedirs
import collections
from distutils.dir_util import copy_tree

final_folder = {}
dir_wrk = getdir()

trans_fol = {'Test_1_A':'Meditar','Test_1_B':'Concentrar',
			'Left_Movement':'Mano Izq.','Right_Movement':'Mano Der.',
			'Left_Wink':'Wink Izq.','Right_Wink':'Wink Der.',
			'Standard':'Estandar','Offline':'Offline','EOG':'EOG'}

def ChckFolds(self, profile_folder):
	dir_bar_values = {'Test_1_A':self.prB_meditar,
	'Test_1_B':self.prB_restar,'Left_Movement':self.prB_Imgleft,
	'Right_Movement':self.prB_Imgright,'Left_Wink':self.prB_Wleft,
	'Right_Wink':self.prB_Wright,'Standard':self.prB_Estandar,
	'Offline':self.prB_Offline,'EOG':self.prB_EOG}
	for x,y in enumerate(profile_folder.keys()):
		if sum(profile_folder[y].values()) == 5:
			palette = QtGui.QPalette()
			pal = dir_bar_values[y]
			palette.setColor(QtGui.QPalette.Highlight,
			QtGui.QColor(QtCore.Qt.green))
			pal.setPalette(palette)

def save_prof(self,profi, profile_folder):
	if profi['name'] and profi['age'] and profi['gender'] == 'NA':
		self.label_results.setText("Nombre de usuario vacio")
	else:
		nam = profi['name']; age = profi['age']; sex = profi['gender']
		exec "details = {'name':'%s','age':'%s','gender':'%s'}" % (nam,age,sex)
		for x,y in enumerate(profile_folder.keys()):
			re_temp = {}
			for w,z in enumerate(profile_folder[y].keys(),start=1):
				exec "re_temp['a%s']=profile_folder['%s']['%s']" % (w-1,y,w)
			final_folder[y] = re_temp
		# Copy folders to the user backup
		usr_f = '%s_%s_%s' %(nam,age,sex); usr_fname = '%s' %(nam)
		if not exists(dir_wrk+'/Profile/Temp/'+usr_f):
			self.label_results.setText("Guardando datos...")
			exec "savemat('%s/Profile/Data/%s_%s_%s.mat',{'folders':final_folder,'personal details':details}, do_compression=1)" %(dir_wrk,nam,age,sex)
			makedirs(dir_wrk+'/Profile/Temp/'+usr_f)
			makedirs(dir_wrk+'/User_Data/'+usr_fname)
			makedirs(dir_wrk+'/User_Data/'+usr_fname+'/Parameters_files')
			makedirs(dir_wrk+'/User_Data/'+usr_fname+'/SVM_DataFile')
			makedirs(dir_wrk+'/User_Data/'+usr_fname+'/Dump_Files')
			copy_tree(dir_wrk+'/Features/Parameters_files',dir_wrk+'/User_Data/'+usr_fname+'/Parameters_files')
			copy_tree(dir_wrk+'/Features/SVM_DataFile',dir_wrk+'/User_Data/'+usr_fname+'/SVM_DataFile')
			copy_tree(dir_wrk+'/Features/Dump_Files',dir_wrk+'/User_Data/'+usr_fname+'/Dump_Files')
			copy_tree(dir_wrk+'/channels/',dir_wrk+'/Profile/Temp/'+usr_f)
			self.label_results.setText("Usuario nuevo creado y guardado")
		else:
			self.label_results.setText("Guardando datos...")
			copy_tree(dir_wrk+'/Features/Parameters_files',dir_wrk+'/User_Data/'+usr_fname+'/Parameters_files')
			copy_tree(dir_wrk+'/Features/SVM_DataFile',dir_wrk+'/User_Data/'+usr_fname+'/SVM_DataFile')
			copy_tree(dir_wrk+'/Features/Dump_Files',dir_wrk+'/User_Data/'+usr_fname+'/Dump_Files')
			copy_tree(dir_wrk+'/channels/',dir_wrk+'/Profile/Temp/'+usr_f)
			self.label_results.setText("Datos de usuario guardado")
			exec "savemat('%s/Profile/Data/%s_%s_%s.mat',{'folders':final_folder,'personal details':details}, do_compression=1)" %(dir_wrk,nam,age,sex)

def check_prof(self,profi, current_folder):
	nam = profi['name']; age = profi['age']; sex = profi['gender']
	exec "fname = '%s/Profile/Data/%s_%s_%s.mat'" % (dir_wrk,nam,age,sex)
	usr_f = '%s_%s_%s' %(nam,age,sex)
	if pth.isfile(fname):
		exec "temporalis = loadmat_new.loadmat('%s/Profile/Data/%s_%s_%s.mat')"  %(dir_wrk,nam,age,sex)
		copy_tree(dir_wrk+'/Profile/Temp/'+usr_f,dir_wrk+'/channels/')
		profi_current = temporalis['folders']
		new_fol = {}
		for x,y in enumerate(collections.OrderedDict(sorted(temporalis['folders'].items())).keys()):
			new_fol[y] = str( collections.OrderedDict(sorted(temporalis['folders'][y].items())).values() ).strip('[]')
		self.label_results.setText("{:<20}		{:<30}\n{:<20}	{:<30}\n{:<20}	{:<30}\n{:<20}	{:<30}\n{:<20}	{:<30}\n{:<20}	{:<30}\n{:<20}	{:<30}\n{:<20}	{:<30}\n{:<20}	{:<30}\n{:<20}	{:<30}".
		format('folder','Trials 1-5',trans_fol[new_fol.keys()[0]],new_fol[new_fol.keys()[0]],
										trans_fol[new_fol.keys()[1]],new_fol[new_fol.keys()[1]],
										trans_fol[new_fol.keys()[2]],new_fol[new_fol.keys()[2]],
										trans_fol[new_fol.keys()[3]],new_fol[new_fol.keys()[3]],
										trans_fol[new_fol.keys()[4]],new_fol[new_fol.keys()[4]],
										trans_fol[new_fol.keys()[5]],new_fol[new_fol.keys()[5]],
										trans_fol[new_fol.keys()[6]],new_fol[new_fol.keys()[6]],
										trans_fol[new_fol.keys()[6]],new_fol[new_fol.keys()[7]],
										trans_fol[new_fol.keys()[6]],new_fol[new_fol.keys()[8]]))
		for x,y in enumerate(profi_current.keys()):
			re_temp = {}
			for w,z in enumerate(profi_current[y].keys(),start=1):
				exec "re_temp['%s']=profi_current['%s']['a%s']" % (w,y,w-1)
			final_folder[y] = re_temp
		ChckFolds(self, final_folder)
		return final_folder
	else:
		self.label_results.setText("Usuario no encontrado")
		ChckFolds(self, current_folder)
		return current_folder
