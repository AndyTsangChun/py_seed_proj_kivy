#! /usr/bin/env python

from kivy.app import App
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.properties import BooleanProperty
from kivy.uix.actionbar import ActionBar
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from app.ui.kv.widget.myactionbar import MyActionBar
from app.ui.kv.activity import CalendarActivity, VideoActivity

__author__ = "Andy Tsang"
__credits__ = ["Andy Tsang"]
__version__ = "0.0.0"
__maintainer__ = "Andy Tsang"
__email__ = "atc1992andy@gmail.com"

class ScreenManagement(ScreenManager):
	"""
	ScreenManager act as the controller between Screen or in android we called Activity
	In this example, the widget are defined in .kv 
	But you can also add those widget in this class as well
	"""

	def on_update(self, **kwargs):
		self.current_screen.on_update()
		# for key, val in self.ids.items():
		# 	val.on_update()