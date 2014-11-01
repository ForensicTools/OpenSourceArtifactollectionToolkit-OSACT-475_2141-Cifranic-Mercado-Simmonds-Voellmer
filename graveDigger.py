# graveDigger.py
# This module contains functions for recovering information about deleted files and what files the user has been accessing/searching for
# Kevin Voellmer 10/26/2014

import sys, easyReg, _winreg



# only works on 7
# returns search queries from the search bar on the start menu
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
			print str("out of for loop")
			break
	for entry in localKey.list_of_entries:
		entry.printEntry()
	
#wordWheelQuery()
## only works on XP
## returns search terms used in the search assistant
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
			print str("out of for loop")
			break
	for entry in localKey.list_of_entries:
		entry.printEntry()
	
	
lastVisitedMRU()
##
#def thumbs():

## only works on Vista/7
#def thumbnails():

## only works on xp
#def xpRecycleBin():

## only works on 7
#def RecycleBin():

##
#def index():
