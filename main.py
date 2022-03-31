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



from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.dialog import MDDialog
from kivymd.utils import asynckivy


from os.path import exists

from kivy.core.window import Window
Window.size = (400,600)

from Py import ss

#--------------------------------
#Class Objects

#Home screen
class HomeScreen(MDScreen):
	pass
#Settings Screen
class SettingsScreen(MDScreen):
	pass

#Login screen
class LoginScreen(MDScreen):
	pass
class SetupScreen(MDScreen):
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

	#Builds the app
	def build(self):
		#
		
		self.theme_cls.material_style = 'M3'
		self.theme_cls.primary_palette = "Orange"
		self.theme_cls.theme_style = "Light"
		return Builder.load_file("main.kv")
	
	#Toggle DarkMode
	def toggleDarkMode(self, switchObject, switchValue):
		if(switchValue):
			self.theme_cls.theme_style = "Dark"	
		else:
			self.theme_cls.theme_style = "Light"	

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
	#Get the user's profile pic if it exists, else use default
	def getProfilePic(self):
		if(exists('Data\Profile.png')):
			print('It Exists')
			return 'Data\Profile.png'
		else:
			print('It does not exists using default')
			return 'Images\Icons\ProfileDefault.png'
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
				self.loadConfig('1') #Load the configuration for '1'
				self.change_screen('home_screen') #change the screen
			#Else we display a dialog box with the error.
			else:
				self.dialog = MDDialog( text="Invalid username and/or password! Please Try Again!", radius=[20, 7, 20, 7],)
				self.dialog.open()

	#Loads the defaults/user settings into the system
	def loadConfig(self,uID):
		self.theme_cls.primary_palette = self.uDB[uID]['config']['theme']
		self.name = self.uDB[uID]['user']['name']
		#Test Code
		#print(self.name)
		#self.root.ids['sUname'].title = self.getName()+"'s Profile"
		#print(self.root.ids.home_screen.ids['sUname'])
		#print(self.getName() +"'s Profile")
		#Sets the name
		self.root.ids.home_screen.ids['sUname'].title = self.getName() +"'s Profile"

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


	#Get the user's name 
	def getName(self):
		return self.name

		#return self.name

	def getDarkMode(self):
		return self.dkMode
	

#Runs the application
if __name__ == '__main__':
	MyApp().run()
