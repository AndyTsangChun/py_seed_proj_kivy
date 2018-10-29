#! /usr/bin/env python
# get monitor resolution
from pyutil import getScreenInfo
w = getScreenInfo()[0].width
h = getScreenInfo()[0].height

# config has to be set be fore import window
from kivy.config import Config
DEFAULT_WINDOW_WIDTH = 0.9
DEFAULT_WINDOW_HEIGHT = 0.9
# setting window size and position
Config.set('graphics', 'position', 'custom')
Config.set('graphics', 'width', '{}'.format(int(w*DEFAULT_WINDOW_WIDTH)))
Config.set('graphics', 'height', '{}'.format(int(h*DEFAULT_WINDOW_HEIGHT)))
Config.set('graphics', 'left', '{}'.format(int(w*((1-DEFAULT_WINDOW_WIDTH)/2))))
Config.set('graphics', 'top', '{}'.format(int(w*((1-DEFAULT_WINDOW_HEIGHT)/2))))
# here we hide the title bar using fake fullscreen attribute
Config.set('graphics', 'fullscreen', 'fake')

# import kivy object
import kivy
kivy.require('1.10.1')
from kivy.app import App
from kivy.lang import Builder
from kivy.clock import Clock
from app.ui.kv.main import ScreenManagement
# import other dependency
import cv2

__author__ = "Andy Tsang"
__credits__ = ["Andy Tsang"]
__version__ = "0.0.0"
__maintainer__ = "Andy Tsang"
__email__ = "atc1992andy@gmail.com"

# refresh rate, not really meant the fps of the video we are playing
FPS = 30

class AppController(App):
	def __init__(self, settings, logger, **kwargs):
		super(AppController, self).__init__(**kwargs)
		self.settings = settings
		self.__logger=logger
		# Application window title
		self.title = "Demo"
		# Video Source
		self.current_src = 0
		# Init video stream with opencv
		self.capturer = cv2.VideoCapture(self.current_src)
		self.current_frame = None
		# variables if we want to loop the video
		self.isLoop = False
		self.frame_count = 0

	def build(self):
		"""
		Kivy rendering function, load main window .kv file
		kivy root actually has a feature to find it related .kv file
		if build was not defined and for instance, this class called "TestApp"
		kivy will automatically search for test.kv
		"""
		main_window = Builder.load_file("app/ui/kv/main.kv")

		return main_window

	def start(self):
		# set a timer for app main loop
		Clock.schedule_interval(self.on_update, 1.0/FPS)
		# run ui rendering
		self.run()

	def on_update(self, dt):
		"""
		An update function act as a logic main loop
		Args:
			dt (float): the time elipse from last interval

		"""
		if self.capturer is not None:
			self.updateVideoFrame()
		# root here refer to ScreenManagement which defined in main.kv
		self.root.on_update()

	def updateVideoSource(self, new_src):
		"""
		A function just for updating video source we are playing
		Args:
			new_src (str): video/source path
		"""
		self.current_src = new_src
		self.capturer = cv2.VideoCapture(self.current_src)

	def updateVideoFrame(self):
		"""
		A function to update the current frame and managing looping the video
		"""
		if self.frame_count == self.capturer.get(cv2.CAP_PROP_FRAME_COUNT) and self.isLoop: 
		    self.frame_count = 0
		    self.capturer = cv2.VideoCapture(self.current_src)
		ret, frame = self.capturer.read()
		self.current_frame = [frame]
		self.frame_count += 1


