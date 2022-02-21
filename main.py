#Main Python File used to run the app and call in other classes/method from the Classes folder
#Team AMCJ
#Kean Senior Captstone
#===========================================
#Imports-------------------------
import kivy
from kivy.app import App
from kivy.uix.label import Label

#--------------------------------

class MyApp(App):
	def build(self):
		return Label(text = "Hello World")

if __name__ == '__main__':
	MyApp().run()
