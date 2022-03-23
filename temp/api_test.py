import kivy
kivy.require('1.10.0')

from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDRectangleFlatButton
from kivymd.uix.textfield import MDTextField
from googleapiclient.discovery import build

# search_helper = '''
# MDTextField:
# 	hint_text: "Enter keywords"
# 	pos_hint: {'x': 0.6, 'y': .9}
# 	size_hint: (0.3, 1)
# '''

class MainApp(MDApp):
	def build(self):
		screen = Screen()
		self.searchText = MDTextField(
			hint_text='Search', 
			pos_hint={'x': 0.6, 'y': .9},
			size_hint=(0.2, 1)
		)
		screen.add_widget(self.searchText)
		button = MDRectangleFlatButton(
			text="Submit",
			pos_hint={'x': 0.81, 'y': .93},
			on_release=self.run_search
		)
		screen.add_widget(button)
		return screen

	def run_search(self, obj):
		api_key = 'AIzaSyAmmmNrh3usjygIzlvZYfKsckuZu8qM4Ns'
		youtube = build('youtube', 'v3', developerKey=api_key)
		request = youtube.search().list(
			q=self.searchText.text,
			part='snippet',
			type='video',
			eventType='live',
			maxResults="20"
		)
		response = request.execute()
		print(response)

		for item in response['items']:
			print(item['snippet']['title'])
			#print(item['snippet']['description'])

		label = MDLabel(text="Results here", halign="center")
		return label
		youtube.close()


MainApp().run()
