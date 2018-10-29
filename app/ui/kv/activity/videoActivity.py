#! /usr/bin/env python
from kivy.uix.screenmanager import Screen
from app.ui.kv.widget.videoview import VideoView

__author__ = "Andy Tsang"
__credits__ = ["Andy Tsang"]
__version__ = "0.0.0"
__maintainer__ = "Andy Tsang"
__email__ = "atc1992andy@gmail.com"

class VideoActivity(Screen):
	"""
	Activity class
	"""
	def on_update(self, **kwargs):
		# though self.ids to access object assigned in .kv
		self.ids.my_video_view.on_update(frame_idx=0)