#! /usr/bin/env python

from kivy.uix.screenmanager import Screen
from kivy.uix.gridlayout import GridLayout
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.popup import Popup

__author__ = "Andy Tsang"
__credits__ = ["Andy Tsang"]
__version__ = "0.0.0"
__maintainer__ = "Andy Tsang"
__email__ = "atc1992andy@gmail.com"

class CalendarActivity(Screen):
	"""
	Activity class
	"""
	def on_update(self, **kwargs):
		pass

ROWS = 3
COLS = 7

class CalendarPanel(GridLayout):
	"""
	Here demonstrate to generate cell inside class without .kv
	note that, the view will not be render before running both .kv and .py
	the view is created in sequence of .py followed by .kv
	here shows that, even rows and cols was not defined in the constructor above 
	it will override by the definition in .kv
	"""
	def __init__(self, **kwargs):
		super(CalendarPanel, self).__init__(**kwargs)
		self.load_content(self)

	def load_content(self, content):
		for i in range(ROWS*COLS):
			content.add_widget(Button(text="py"+str(i), on_press=self.buttonCallBack))

	def on_update(self, **kwargs):
		pass

	def buttonCallBack(self, instance):
		"""
		Callback function for Button
		Show a popup with the button text
		"""
		popup = Popup(title="Pressed!!!",
				content=Label(text=instance.text),
				size=(100, 100),
				size_hint=(0.3, 0.3),
				auto_dismiss=True)
		popup.open()