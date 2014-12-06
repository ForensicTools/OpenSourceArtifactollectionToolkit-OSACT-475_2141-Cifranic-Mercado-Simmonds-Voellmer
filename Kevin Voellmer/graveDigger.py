# graveDigger.py
# This module contains functions for recovering information about deleted files and for what files the user has been accessing/searching
# Kevin Voellmer 10/26/2014

import sys, easyReg, _winreg


## Only works on Windows 7
## Returns search queries from the search bar on the start menu
def wordWheelQuery():
	localKey = easyReg.RegKey("HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Explorer\WordWheelQuery")
	print "Recent Search Terms"
	localKey.populateEntries()
	for entry in localKey.list_of_entries:
		if entry.getRegEntry()[1] != "MRUListEx":
			print entry.getRegEntry()[3]
	
#wordWheelQuery()

## Only works on XP
## Returns search terms used in the search assistant

##in progress
def ACMRU():

	netSearch = easyReg.RegKey("NTUSER.DAT\Software\Microsoft\Search Assistant\ACMru\5001")
	docName = easyReg.RegKey("NTUSER.DAT\Software\Microsoft\Search Assistant\ACMru\5603")
	wordPhrase = easyReg.RegKey("NTUSER.DAT\Software\Microsoft\Search Assistant\ACMru\5604")
	objects = easyReg.RegKey("NTUSER.DAT\Software\Microsoft\Search Assistant\ACMru\5647")
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
##

def lastVisitedMRU():
	localKey = easyReg.RegKey("HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Explorer\ComDlg32\LastVisitedPidlMRU")
	print "Recently Opened Files and Associated Programs"
	localKey.populateEntries()
	for entry in localKey.list_of_entries:
		if entry.getRegEntry()[1] != "MRUListEx":
			print entry.getRegEntry()[3]
	
	
	
def runMRU():
	localKey = easyReg.RegKey("HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Explorer\RunMRU")
	print "Recent Run Commands"
	localKey.populateEntries()
	for entry in localKey.list_of_entries:
		if entry.getRegEntry()[1] != "MRUListEx":
			print entry.getRegEntry()[3]
	
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

wordWheelQuery()
print ""
print ""
lastVisitedMRU()
print ""
print ""
runMRU()