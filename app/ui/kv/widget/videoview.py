#! /usr/bin/env python

from kivy.app import App
from kivy.uix.image import Image
from kivy.graphics.texture import Texture
import cv2

__author__ = "Andy Tsang"
__credits__ = ["Andy Tsang"]
__version__ = "0.0.0"
__maintainer__ = "Andy Tsang"
__email__ = "atc1992andy@gmail.com"

class VideoView(Image):
	"""
	VideoView example which take frame in np.array from opencv
	Frame is obtained from App using kivy default App.get_running_app()
	"""
	def __init__(self, capture=None, fps=30, **kwargs):
		super(VideoView, self).__init__(**kwargs)

	def on_update(self, **kwargs):
		frame_idx = kwargs["frame_idx"]
		myapp = App.get_running_app()
		if myapp.current_frame is not None:
			frame = myapp.current_frame[frame_idx]
			# convert to texture for kivy display
			buf1 = cv2.flip(frame, 0)
			buf = buf1.tostring()
			image_texture = Texture.create(
				size=(frame.shape[1],frame.shape[0]), colorfmt='bgr')
			image_texture.blit_buffer(buf, colorfmt='bgr', bufferfmt='ubyte')
			self.texture = image_texture