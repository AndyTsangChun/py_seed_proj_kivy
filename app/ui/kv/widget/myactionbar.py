#! /usr/bin/env python

from kivy.uix.actionbar import ActionBar
from kivy.lang import Builder

__author__ = "Andy Tsang"
__credits__ = ["Andy Tsang"]
__version__ = "0.0.0"
__maintainer__ = "Andy Tsang"
__email__ = "atc1992andy@gmail.com"

class MyActionBar(ActionBar):
	"""
	Customised Action Bar
	"""
	def build(self):
		actionBar = Builder.load_file("app/ui/kv/widget/actionbar.kv")

		return actionBar
