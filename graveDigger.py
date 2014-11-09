# graveDigger.py
# This module contains functions for recovering information about deleted files and for what files the user has been accessing/searching
# Kevin Voellmer 10/26/2014

import sys, easyReg, _winreg

## Only works on Windows 7
## Returns search queries from the search bar on the start menu
def wordWheelQuery():
	localKey = easyReg.RegKey("HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Explorer\WordWheelQuery")
	print str(localKey)
	print str(localKey.handle)
	for i in range(1024):
		try:
			print str(i)
			print str(_winreg.EnumValue(localKey.handle, i))
			localKey.list_of_entries.append(easyReg.RegEntry(_winreg.EnumValue(localKey.handle, i)))
		except EnvironmentError:
			break
	for entry in localKey.list_of_entries:
		entry.printEntry()
	
#wordWheelQuery()

## Only works on XP
## Returns search terms used in the search assistant
#def ACMRU():

##

def lastVisitedMRU():
	localKey = easyReg.RegKey("HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Explorer\ComDlg32\LastVisitedPidlMRU")
	print str(localKey)
	print str(localKey.handle)
	for i in range(1024):
		try:
			print str(i)
			print str(_winreg.EnumValue(localKey.handle, i))
			localKey.list_of_entries.append(easyReg.RegEntry(_winreg.EnumValue(localKey.handle, i)))
		except EnvironmentError:
			break
	for entry in localKey.list_of_entries:
		entry.printEntry()
	
	
#lastVisitedMRU()

##

#def thumbs():

##

## only works on Vista/7
#def thumbnails():

##

## only works on xp
#def xpRecycleBin():

##

## only works on 7
#def RecycleBin():

##

#def index():

##