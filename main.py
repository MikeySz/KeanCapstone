#Main Python File used to run the app and call in other classes/method from the Classes folder
#Team AMCJ
#Kean Senior Captstone
#All Logic should be here
#.KV files should hold the interface/gui
#===========================================
#Imports-------------------------
from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen

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
		self.theme_cls.theme_style = "Dark"
		self.theme_cls.theme_style = "Dark"
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
	

#Runs the application
if __name__ == '__main__':
	MyApp().run()
