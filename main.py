#Main Python File used to run the app and call in other classes/method from the Classes folder
#Team AMCJ
#Kean Senior Captstone
#===========================================
#Imports-------------------------
import kivy
from kivy.app import App
from kivy.lang import Builder

#--------------------------------
GUI = Builder.load_file("main.kv")


class MyApp(App):
	def build(self):
		return GUI

#Runs the application
if __name__ == '__main__':
	MyApp().run()
