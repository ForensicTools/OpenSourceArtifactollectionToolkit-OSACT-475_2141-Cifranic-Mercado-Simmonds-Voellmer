## fileHistoryUnitTest.py
## Author: Daniel "Albinohat" Mercado
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

## Initialize the registry key object using either the current user or SID specified.
if (len(sys.argv)  == 2):
	## Commented line contains key containing last 20 opened/saved files in a dialog.
	mru_key = easyReg.RegKey("HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Explorer\ComDlg32\OpenSavePidlMRU\\" + sys.argv[1])
	
else:
	## Commented line contains key containing last 20 opened/saved files in a dialog.
	mru_key = easyReg.RegKey("HKEY_USERS\\" + sys.argv[2] + "\Software\Microsoft\Windows\CurrentVersion\Explorer\ComDlg32\OpenSavePidlMRU\\" + sys.argv[1])

## Populate the entries of mru_key.	
mru_key.populateEntries()

# Print the recent file by looping through the entries of mru_key and initialize RecentFile objects.
#mru_key.printEntries()

for entry in mru_key.list_of_entries:
	fileHistory.RecentFile(entry).printRecentFile()