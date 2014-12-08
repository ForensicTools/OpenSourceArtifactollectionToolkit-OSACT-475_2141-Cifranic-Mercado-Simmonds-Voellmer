## osactDemo_threading.py
## Author(s): Nick Cifranic & Daniel "Albinohat" Mercado
## This module contains the special thread subclasses used by the OSACT multithreaded demo.

## Standard Imports
import subprocess, sys, threading

## ExecuteCommandThread - A thread which parses through and executes a command.
class osactDemoThread(threading.Thread):
	## __init__ - Initializes the attributes of the osactDemoThread instance.
	## self.thread_id   - A unique ID assigned to each thread.
	## self.test_name   - The name of the test to run.
	def __init__(self, test_name):
		threading.Thread.__init__(self)
		self.thread_id   = threading.activeCount() + 1
		self.test_name   = test_name
		
		self.start()

	## run - This method calls the executeCommand method of the specified feature set.
	def run(self):
		if (self.test_name == "carmensandiego"):
			subprocess.call("python ./carmenSandiegoUnitTests.py")
		elif (self.test_name == "filehistory"):
			subprocess.call("python ./fileHistoryUnitTests.py")
		elif (self.test_name == "ielumberjack"):
			subprocess.call("python ./ieLumberJackUnitTests.py")
		elif (self.test_name == "gravedigger"):
			subprocess.call("python ./graveDigger.py")
		elif (self.test_name == "forensicsviewer"):
			subprocess.call("python ./ForensicsViewerUnitTests.py")
		else:
			sys.exit()