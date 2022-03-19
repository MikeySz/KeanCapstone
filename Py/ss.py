#SaveSystem
#Imports ========================================
#Reading and Writing Data
import json

#Creating flies
import os.path
from os import path
from os.path import exists 
#==================================================

def createDefaults():
	
	if (not exists(r'Data\userconfig.json')):
		uConfig = {
		"username":"default",
		"password":"default",
		"name": ""
		}
		sConfig = {
		"darkmode":False,
		"theme":"Purple",
		}
		uFile = open(r'Data\userconfig.json', 'w+')
		with open(r'Data\userconfig.json', 'w+') as filehandle:
			json.dump(uConfig, filehandle)

		sFile = open(r'Data\settingsconfig.json', 'w+')
		with open(r'Data\settingsconfig.json', 'w+') as filehandle:
			json.dump(sConfig, filehandle)





def save(filepath, key, value):
	return true

def fullSave(filepath, fDict):
	pass
def load(filepath):
	pass


#def isFileReal(filePath):
#	if not path.exists(filePath):
#		return False
#	else: 
#		return True


#def test():
#	return True