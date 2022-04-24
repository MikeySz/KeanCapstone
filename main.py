#Main Python File used to run the app and call in other classes/method from the Classes folder
#Team AMCJ
#Kean Senior Captstone
#All Logic should be here
#.KV files should hold the interface/gui
#Note: Look into Sphinx 
#===========================================
#Imports-------------------------
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.uix.image import Image

from kivy.core.window import Window
from kivy.factory import Factory
from kivy.uix.modalview import ModalView



from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.dialog import MDDialog
from kivymd.utils import asynckivy
from kivymd.uix.menu import MDDropdownMenu

from kivymd.uix.filemanager import MDFileManager
from kivymd.theming import ThemeManager
from kivymd.toast import toast

from os.path import exists
import time

from kivy.core.window import Window
Window.size = (400,600)

from Py import ss

from plyer import filechooser 
import shutil 
from os.path import join
import os
import time

#----
import requests
from bs4 import BeautifulSoup
from kivy.core.text import LabelBase
from kivy.core.window import Window

#--------------------------------
#Class Objects

#Home screen
class HomeScreen(MDScreen):
	pass
#Settings Screen
class SettingsScreen(MDScreen):
	pass
#TOS Screen
class TosScreen(MDScreen):
	pass
#Edit Profile Screen
class ProfileScreen(MDScreen):
	pass
#Login screen
class LoginScreen(MDScreen):
	pass
class SetupScreen(MDScreen):
	pass
class SignupScreen(MDScreen):
	pass




#============================================
#Check/Load Save data here
#NewUser= True
#ss.createDefaults()
#============================================
#Color-Background Object to be used later
#colorBG = (.8509,.8235,.9137,1)
#The Graphics are built within the main.kv and other .kv files
#Main App
class MyApp(MDApp):
	title = "Solaire"
	#Api Key for the Weather
	api_key = "08969b47088a3aec7aed9f2547c9083e"
	#---------------------------------
	#save system can create default files
	ss.createDefault()
	#Loading data in
	uDB = ss.load()
	#Current Logged in user
	uID = ''
	#name attribute
	name = 'User'
	#darkMode
	dkMode = False
	#Logic Methods
	#profile picture path
	proPic = ''
	cwd = os.getcwd()
	#print(cwd)
#====================File Manager=======================
	def file_manager_open(self):
		path = " "
		try:
			path = filechooser.open_file()[0]
		except:	
			print("something went wrong")

		print(path)
		if path.endswith(".png") or path.endswith(".jpg") or path.endswith(".jpeg"):
			print("Valid Image")
			#print(join(self.cwd, 'Data'))
			ProfilePic = r"Data\\"+'User'+self.uID+".png"
			shutil.copy(path, join(self.cwd, ProfilePic))
			os.chdir(self.cwd)
			self.setProfilePic(ProfilePic)
		elif(path == " "):
			os.chdir(self.cwd)
			self.dialog = MDDialog( text="No File Selected! ", radius=[20, 7, 20, 7],)
			self.dialog.open()
		else:
			self.dialog = MDDialog( text="Invalid File Type! Please Use a .jpg/.jpeg or .png file! ", radius=[20, 7, 20, 7],)
			self.dialog.open()
	

#========================================================

	#Logic that runs before the app starts, can be used to set the intial screen
	def on_start(self):

		#If default user exists then load setup screen
		if (self.uDB['1']['user']['username'] == "default"):
			screen_manager = self.root.ids['screen_manager']
			screen_manager.current = "setup_screen"
		#Else we load into a login_screen
		else:
			screen_manager = self.root.ids['screen_manager']
			screen_manager.current = "login_screen"

		#--------------------------------------------------------------------
		#Weather Startup grab location from the devices:
		try:
			soup = BeautifulSoup(requests.get(f"https://www.google.com/search?q=weather+at+my+current+location").text,"html.parser")
			temp = soup.find("span", class_="BNeawe tAd8D AP7Wnd")
			location = ''.join(filter(lambda item: not item.isdigit(), temp.text)).split(",", 1)
			self.get_weather(location[0])
		except requests.ConnectionError:
			print("Unable to connect")
			exit()



		#---------------------------------------------------------------------

	#Builds the app
	def build(self):
		
		#Set the COLOR and THEME of the app
		self.theme_cls.material_style = 'M3'
		self.theme_cls.primary_palette = "Orange"
		self.theme_cls.theme_style = "Light"
		return Builder.load_file("main.kv")
	


	#Method that changes the screen
	def change_screen(self,screen_name):
		# Screen manager from main.kv
		#print(self.root.ids) #Code used to test the screen_name id
		
		#when change_screen is called, it grabs the screen_id
		#from the page(screen) calling the change_screen method
		screen_manager = self.root.ids['screen_manager']
		#sets the id to match the new id only if current id is not equal to new one
		if (screen_name != screen_manager.current):			
			screen_manager.current = screen_name
	#Returns the minimum size of an object
	def getMinSize(self, width, height):
		if width > height:
			return height
		else:
			return width

	#Login- requires username and password
	def login(self, usr, pw):
		#Grab the length of the uDB dictionary
		i = len(self.uDB)
		c = 1  #Counter c starts at 1 (to be used with a loop)
		if(i == 1): #If there is only one record, then we do one check for each
			uTrue = (self.uDB['1']['user']['username'] == usr)
			pTrue = (self.uDB['1']['user']['password'] == pw)
			#is the two booleans are both true we login
			if (uTrue and pTrue):
				self.uID = '1'  #set the app's userID to '1', used when selecting/editing data
				self.loadConfig(self.uID) #Load the configuration for '1'
				self.change_screen('home_screen') #change the screen
			#Else we display a dialog box with the error.
			else:
				self.dialog = MDDialog( text="Invalid username and/or password! Please Try Again!", radius=[20, 7, 20, 7],)
				self.dialog.open()
		elif(i > 1):#We have mutliple records
			uTrue = False
			pTrue = False
			while(c <= i):
				#Check each record
				uTrue = (self.uDB[str(c)]['user']['username'] == usr)
				pTrue = (self.uDB[str(c)]['user']['password'] == pw)
				if(uTrue and pTrue):
					self.uID = str(c)
					self.loadConfig(self.uID)
					self.change_screen('home_screen')
					break
				c = c+1
			if(not uTrue or not pTrue):
				self.dialog = MDDialog( text="Invalid username and/or password! Please Try Again!", radius=[20, 7, 20, 7],)
				self.dialog.open()





	#Loads the defaults/user settings into the system
	def loadConfig(self,uID):
		self.theme_cls.primary_palette = self.uDB[uID]['config']['theme']
		self.name = self.uDB[uID]['user']['name']
		#self.root.ids.home_screen.text_color_active = self.uDB[uID]['config']['theme']

		#Test Code
		#print(self.name)
		#self.root.ids['sUname'].title = self.getName()+"'s Profile"
		#print(self.root.ids.home_screen.ids['sUname'])
		#print(self.getName() +"'s Profile")
		#Sets the name
		self.root.ids.home_screen.ids['sUname'].title = self.getName() +"'s Profile"

		self.proPic = self.uDB[uID]['user']['profilepic']
		print(self.getProfilePic())
		self.root.ids.home_screen.ids['pic'].canvas.get_group('a')[0].source = self.getProfilePic()

		if (self.uDB[uID]['config']['darkmode']):
			self.dkMode = True
			self.theme_cls.theme_style = "Dark"
			self.root.ids.home_screen.ids['darkmodeswitch'].active = self.dkMode

#Code for setting up the intital user
	def setUpMain(self, name,usr,pw,email):
		#Note: Make this into it's own method that validates each part
		#returns a boolean alongside a string
		#Error checks that return a dialog box with the first error
		if(name == "" or name == " " or name.casefold() == "default"):
			self.dialog = MDDialog( text="Invalid name! Please Try Again! ", radius=[20, 7, 20, 7],)
			self.dialog.open()
		if(usr == "" or usr == " " or usr.casefold() == "default"):
			self.dialog = MDDialog( text="Invalid Username! Please Try Again!", radius=[20, 7, 20, 7],)
			self.dialog.open()	
		elif(len(pw)<6):
			self.dialog = MDDialog( text="Invalid Password! Must be atleast 6 characters long ", radius=[20, 7, 20, 7],)
			self.dialog.open()
		#if all goes fine, we modify the default user and save the file	
		else:
			self.uDB['1']['user'].update({'name':name})
			self.uDB['1']['user'].update({'username':usr})
			self.uDB['1']['user'].update({'password':pw})
			self.uDB['1']['user'].update({'email':email})
			
			ss.save(self.uDB)
			self.loadConfig('1')
			self.login(usr,pw)
			
			#print('1' in self.uDB) #We can use this to check if a key exists
#Code for adding a new account
	def addAccount(self, name,usr,pw,email):
		#Note: Make this into it's own method that validates each part
		#returns a boolean alongside a string
		#Error checks that return a dialog box with the first error
		if(name == "" or name == " " or name.casefold() == "default"):
			self.dialog = MDDialog( text="Invalid name! Please Try Again! ", radius=[20, 7, 20, 7],)
			self.dialog.open()
		if(usr == "" or usr == " " or usr.casefold() == "default"):
			self.dialog = MDDialog( text="Invalid Username! Please Try Again!", radius=[20, 7, 20, 7],)
			self.dialog.open()	
		elif(len(pw)<6):
			self.dialog = MDDialog( text="Invalid Password! Must be atleast 6 characters long ", radius=[20, 7, 20, 7],)
			self.dialog.open()
		#if all goes fine, we modify the default user and save the file	
		else:
			i = 2;
			while str(i) in  self.uDB.keys():
				i = i + 1

		#creating a temporary dictionary to add to the main one	
			tempDB = ss.defaultDT(i)
			tempDB[i]['user'].update({'name':name})
			tempDB[i]['user'].update({'username':usr})
			tempDB[i]['user'].update({'password':pw})
			tempDB[i]['user'].update({'email':email})

			self.uDB.update(tempDB)
			
			ss.save(self.uDB)
			self.uDB = ss.load()
			print(self.uDB)



			self.loadConfig(str(i))
			self.login(usr,pw)
			
			#print('1' in self.uDB) #We can use this to check if a key exists
		#Toggle DarkMode; adds value to uDB and saves to the .json file
#---------------------------Visual----------------------------------------------------------
	def pwMaskToggle(self):
		print(success)

	def toggleDarkMode(self, switchObject, switchValue):
		if(switchValue):
			self.theme_cls.theme_style = "Dark"	
			self.uDB[self.uID]['config']['darkmode'] = switchValue
			#print(self.uDB)
			ss.save(self.uDB)
		else:
			self.theme_cls.theme_style = "Light"
			self.uDB[self.uID]['config']['darkmode'] = switchValue	
			#print(self.uDB)
			ss.save(self.uDB)

#-------------------Get/Set------------------------------------------------------------------------
	#Get the user's name 
	def getName(self):
		return self.name

		#return self.name

	def getDarkMode(self):
		return self.dkMode
	
	#Get the user's profile pic if it exists, else use default
	def getProfilePic(self):
		if(exists(self.proPic)):
			print('It Exists')
			return self.proPic
			
		else:
			print('It does not exists using default')
			return 'Images\Icons\ProfileDefault.png'
	
	def setProfilePic(self, profilePic):
		if(exists(profilePic)):
			print('New Pic')
			print(profilePic)
			print(exists(profilePic))
			self.uDB[self.uID]['user']['profilepic'] = profilePic
			ss.save(self.uDB)
			#self.root.ids.home_screen.ids['pic'].canvas.get_group('a')[0].source = r"Images\Icons\ProfileDefault.png'"#self.getProfilePic()
			self.root.ids.home_screen.ids['pic'].canvas.get_group('a')[0].source = profilePic
			self.dialog = MDDialog( text="Upload Successful! Reset Required to View Changes! ", radius=[20, 7, 20, 7],)
			self.dialog.open()
		else:
			print('It does not exists')


	def getPalette(self):
		return self.theme_cls.primary_palette

	def setPalette(self, color):
		print(color)
		self.theme_cls.primary_palette = color
		self.uDB[self.uID]['config']['theme'] = color
		ss.save(self.uDB)

	#---------------------------------Weather Related Functions--------------------------------
	def get_weather(self, city_name):
		try:
			url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={self.api_key}"
			response = requests.get(url)
			x = response.json()
			if x["cod"] != "404":  # Gets weather values
				temperature = round((x["main"]["temp"] - 273.15) * (9 / 5) + 32)
				humidity = x["main"]["humidity"]
				weather = x["weather"][0]['main']
				id = str(x["weather"][0]["id"])
				wind_speed = round(x["wind"]["speed"] * 18 / 5)
				location = x["name"] + ", " + x["sys"]["country"]
				#self.root.ids.home_screen.ids['city_name'].text

				self.root.ids.home_screen.ids['temperature'].text = f"[b]{temperature}[/b]"
				self.root.ids.home_screen.ids['weather'].text = str(weather)
				self.root.ids.home_screen.ids['humidity'].text = "Humidity:        "+f"{humidity}%"
				#self.root.ids.home_screen.ids['wind_speed'].text = f"{wind_speed} km/h"
				self.root.ids.home_screen.ids['location'].text = location
				# if id == "800":  # Matches weather with corresponding icons
				#     self.root.ids.weather_image.source = "assets/loc.png"
				# elif "200" <= id <= "232":
				#     self.root.ids.weather_image.source = "assets/loc.png"
				# elif "300" <= id <= "321" and "500" <= id <= "531":
				#     self.root.ids.weather_image.source = "assets/loc.png"
				# elif "200" <= id <= "232":
				#     self.root.ids.weather_image.source = "assets/loc.png"
				# elif "200" <= id <= "232":
				#     self.root.ids.weather_image.source = "assets/loc.png"
				# elif "200" <= id <= "232":
				#     self.root.ids.weather_image.source = "assets/loc.png"
			else:
				print("City Unknown")
		except requests.ConnectionError:
			print("Unable to connect")

	def search_weather(self):
		city_name = self.root.ids.home_screen.ids['city_name'].text
		if city_name != "":
			self.get_weather(city_name)


	#-----------------------------------------------------------------------------------------

#Runs the application
if __name__ == '__main__':
	MyApp().run()
