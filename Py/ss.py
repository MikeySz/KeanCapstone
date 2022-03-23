#SaveSystem
#Imports ========================================
#Reading and Writing Data
import json

#Creating flies
import os.path
from os import path
from os.path import exists 
#==================================================
#dynamic path: look into this later

#DefaultDictionaryTemplate
def __defaultDT(uNum):

	return {
	#The Numbers are User IDs, it will make adding new users easier.
	#Each user will have a number, our main user(1) will not be deleted
		uNum:    #Main APP: uDB[1] ===========================
		#Within a UID, is two data dictionaries
		#User is all data relating to the user themselves
		{"user":   #Main APP: uDB[1]['user'] =========================
				{"username":"default", #Username used for loggin in
				"password":"default",  #Password used alongside username to log a user in
				"name": "",   #Name used to address the user within the app
				"email":""},  #User's email

		#Config is the system configurtion settings for the specifc user
		"config":  #Main APP: uDB[1]['config']==============================
				{"darkmode":False, #Decides what mode the app is in"Light/Dark"
				"theme":"Orange",} #The color of theme for the user
			}
		} #End of default file with only 1 user	
#-------------------------------------------------------------------------------------
#Create the default config file
def createDefault():
	#Checks if a file exists; Mostly to avoid overwriting a previous save
	#IF not, then we create the file
	if (not exists(r'Data\userDB.json')):
		#uDB is a multilayered dictionary structure
		uDB = __defaultDT(1)
		
		
		#Opens/creates the file
		uFile = open(r'Data\userDB.json', 'w+')
		#populates the file the default   
		with open(r'Data\userDB.json', 'w+') as filehandle:
			json.dump(uDB, filehandle)
#--------------------------------------------------------------------------------------
#Loads the userDB file into the the app when called
def load():
	with open(r'Data\userDB.json') as f:
		uDB = json.load(f)
		return uDB
#---------------------------------------------------------------------------------------
#saves the Local app userDB dictionary into the main save file
def save(uDB):
	print(uDB)
	with open(r'Data\userDB.json', 'w+') as filehandle:
		json.dump(uDB, filehandle)
	print("Save Success")
#---------------------------------------------------------------------------------------