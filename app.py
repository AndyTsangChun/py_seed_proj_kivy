#! /usr/bin/env python
import time
import cv2
import argparse, json
from pyutil import basic_args, str2bool, PyLogger
from app import AppController

__author__ = "Andy Tsang"
__credits__ = ["Andy Tsang"]
__version__ = "0.0.0"
__maintainer__ = "Andy Tsang"
__email__ = "atc1992andy@gmail.com"

def run(arg):
	# import Setting
	setting_path = "setting.json"
	with open(setting_path) as setting_buffer:
		settings = json.loads(setting_buffer.read())
		settings.update(vars(arg))
	logger = PyLogger(log=True,debug=True)

	app = AppController(settings=settings, logger=logger)
	# play a video
	app.isLoop = settings["video_loop"]
	if settings["video_path"] is not "0":
		app.updateVideoSource(settings["video_path"])
	else:
		app.isLoop = False
		app.updateVideoSource(0)
	app.start()

if __name__ == "__main__":
	parser = argparse.ArgumentParser(description="Desc")
	parser = basic_args(parser)
	# these argument temporary not available, since blocked by kivy default parser, to be fix
	parser.add_argument("-l", "--video_loop", type=str2bool, nargs='?', default="True",
						help="Loop default video or not.")
	parser.add_argument("-p", "--video_path", type=str, default="app/static/video.mp4",
						 help="Demo video path.")
	arg = parser.parse_args()
	st = time.time()
	run(arg)
	print("Finished:{}".format(time.time()-st))
