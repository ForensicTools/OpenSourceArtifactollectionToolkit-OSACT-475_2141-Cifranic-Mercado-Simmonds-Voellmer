## osactDemo_threading.py
## Author(s): Nick Cifranic & Daniel "Albinohat" Mercado
## This module contains the special thread subclasses used by the OSACT multithreaded demo.

## Standard Imports
import sys, threading

## Third-party Imports
import osactDemo_threading

osactDemo_threading.osactDemoThread("carmensandiego").join()
osactDemo_threading.osactDemoThread("filehistory").join()
osactDemo_threading.osactDemoThread("ielumberjack").join()
osactDemo_threading.osactDemoThread("gravedigger").join()
osactDemo_threading.osactDemoThread("forensicsviewer").join()

print "\nWaiting on the following threads to return...\n"

for thread in osactDemo_threading.threading.enumerate():
	print str(thread)
	
sys.exit()


