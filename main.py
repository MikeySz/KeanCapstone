#Main Python File used to run the app and call in other classes/method from the Classes folder
#Team AMCJ
#Kean Senior Captstone
#All Logic should be here
#.KV files should hold the interface/gui
#===========================================
#Imports-------------------------
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager,Screen


#--------------------------------
class HomeScreen(Screen):
	pass

class SettingsScreen(Screen):
	pass



GUI = Builder.load_file("main.kv")
class MyApp(App):
	def build(self):
		return GUI

	def change_screen(self,screen_name,transition,direction):
		# Screen manager from main.kv
		#print(self.root.ids) #Code used to test the screen_name id
		
		#when change_screen is called, it grabs the screen_id
		#from the page(screen) calling the change_screen method
		#sets the id to match the new id
		screen_manager = self.root.ids['screen_manager']
		
		screen_manager.current = screen_name
		#


#Runs the application
if __name__ == '__main__':
	MyApp().run()
