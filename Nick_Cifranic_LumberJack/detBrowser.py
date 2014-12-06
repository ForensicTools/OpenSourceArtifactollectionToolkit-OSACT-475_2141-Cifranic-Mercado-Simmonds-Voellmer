#!/usr/bin/env python
#Check which web browsers are installed

import os.path # Required to validate files
 

#Detects if Firefox browser is installed
firefoxInstalled = os.path.exists('C:\Program Files (x86)\Mozilla Firefox')
if firefoxInstalled:
	print ("Firefox Detected")

#Detects if Internet Explorer browser is installed
ieInstalled = os.path.exists('C:\Program Files\Internet Explorer')
if ieInstalled:
	print ("Internet Explorer Detected")
	

	
exists = os.path.exists('C:\Users\nick\AppData\Local\Microsoft\Windows\History')