#Main Python File used to run the app and call in other classes/method from the Classes folder
#Team AMCJ
#Kean Senior Captstone
#All Logic should be here
#.KV files should hold the interface/gui
#===========================================
#Imports-------------------------
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.uix.image import Image



from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen


from os.path import exists

#--------------------------------
#Class Objects

#Home screen
class HomeScreen(MDScreen):
	pass
#Settings Screen
class SettingsScreen(MDScreen):
	pass

#============================================
#Color-Background Object to be used later
#colorBG = (.8509,.8235,.9137,1)
#The Graphics are built within the main.kv and other .kv files
#Main App
class MyApp(MDApp):
	#---------------------------------
	#Logic Methods
	#Builds the app
	def build(self):
		#
		self.theme_cls.material_style = 'M3'
		self.theme_cls.primary_palette = "Purple"
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
	#Get the user's profile pic if it exists, else use default
	def getProfilePic(self):
		if(exists('Data\Profile.png')):
			print('It Exists')
			return 'Data\Profile.png'
		else:
			print('It does not exists using default')
			return 'Images\Icons\ProfileDefault.png'
	#Get the user's name 
	def getName(self):
		return "User"
	

#Runs the application
if __name__ == '__main__':
	MyApp().run()
