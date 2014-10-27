## fileHistoryUnitTest.py
## This script returns the most recently opened/saved files using the windows open/save prompts.
## CLAs (2)
## 1 - REQUIRED - File extension without leading dot ro star for last 20 regardless of extension.
## 2 - OPTIONAL - SID of the user to get info for.

import easyReg, fileHistory, sys, _winreg

##Validate command line arguments
for arg in sys.argv:
	arg.lower()

if(len(sys.argv) < 2 or len(sys.argv) > 3):
	print "\n    Invalid syntax! Usage: lasfFile.py *|extension [SID]\n"
	sys.exit()

## List which will contain registry entries (files).
list_of_recent_files = []

## Bool enabling debug output.
bool_debug = 1
	
## Connect to the Registry, specifying the hive you wish to connect to.
if (len(sys.argv)  == 2):
	## Commented line contains key containing last 20 opened/saved files in a dialog.
	local_key = easyReg.easyOpenKey("HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Explorer\ComDlg32\OpenSavePidlMRU\\" + sys.argv[1])
	
else:
	## Commented line contains key containing last 20 opened/saved files in a dialog.
	local_key = easyReg.easyOpenKey("HKEY_USERS\\" + sys.argv[2] + "\Software\Microsoft\Windows\CurrentVersion\Explorer\ComDlg32\OpenSavePidlMRU\\" + sys.argv[1])

## Loop through the values until you run out.
for i in range(20):
	try:
		temp_file = fileHistory.RecentFile(easyReg.RegEntry(_winreg.EnumValue(local_key, i)))
		if (temp_file.entry.value != "MRUListEx"):
			list_of_recent_files.append(temp_file)
		
	except EnvironmentError:
		break
		
## Sort the list of recent files.
list_of_recent_files.sort(key=lambda f: int(f.entry.value), reverse=False)

## Print the entries.
if (bool_debug == 1):
	for file in list_of_recent_files:
		file.printRecentFile()