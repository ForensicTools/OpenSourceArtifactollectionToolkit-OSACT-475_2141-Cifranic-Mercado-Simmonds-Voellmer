#!/usr/bin/env python
import os.path # Required to validate files
import getpass #used to get user

#GLOBAL-VARIABLES
name = getpass.getuser()
		
#Modulated functions	
def browserDetection():
	print ("Entering Browser Detection Function")
	#Checks to see if internet explorer is installed
	import os.path # Required to validate files
	 
	#Detects if Internet Explorer browser is installed
	ieInstalled = os.path.exists('C:\Program Files\Internet Explorer')
	if ieInstalled:
		print ("\tInternet Explorer Detected")
	else:
		print ("Internet Explorer Not found, exiting program")
		exit()
		
def history(): # Passes a function to create History Shortcut
#Records websites visited by date & time. Details stored for each 
#local user account. Records number of times visited (frequency). 
#Also tracks access of local system files.	
	print ("Entered History Function")
	
	#save the path
	historyFolder = 'C:\\Users\\' + name + '\\Desktop\\artifacts\\History'
	
	#function to create a new folder - 1 Parameter for a string, location
	makeDirectory(historyFolder);
		
	#Check if path exists
	histFolder = os.path.exists(os.path.expandvars("%LOCALAPPDATA%\Microsoft\Windows\History"))

	if histFolder:
		print ("\tYou have access to the history folder, creating short-cut to the repo")
		createHistShortcut(); #if it exists, goto function to create shortcut for user 
	else:
		print ("Unable to grant access to the history folder, please check your user privileges")
	 
	 
def cookie():
	#Cookies give insight into what websites have been visited 
	#and what activities may have taken place there
	print ("Entered Cookie Function")
	
	source = 'C:\\Users\\' + name + '\\AppData\\Roaming\\Microsoft\\Windows\\Cookies\\Low'
	dest = 'C:\\Users\\' + name + '\\Desktop\\artifacts\\Cookies'
	
	#Copies the cookies from it's source to the destination in the artifacts folder
	#2 Parameters - Source and Destination
	CopyFileContents( source, dest )
		

def cache():
	#The cache is where webpage components can be stored locally
	#to speed up subsequent visits. Gives the investigator a 
	#“Snapshot in time” of what a user was looking at on-line	
	print ("Enter Cache Function")
	
	#Retrieve the temporary internet files 
	source = r'C:\Users\nick\AppData\Local\Microsoft\Windows\Temporary Internet Files\Low\Content.IE5'
	#source = r'C:\Users\nick\AppData\Local\Microsoft\Windows\Temporary Internet Files'
	dest = r'C:\Users\nick\Desktop\artifacts\cache'
	CopyFileContents( source, dest )
	
	#list file extensions and store in an Array
	#file_list = next(os.walk(r'C:\Users\nick\AppData\Local\Microsoft\Windows\Temporary Internet Files\Low\Content.IE5'))[1]

	
	
	# for file_list in file_list:        # Second Example
		# print ('Sub Directory : ', counter, file_list ) 
		
	
	
def sessionRestore():
	print ("Enter Session Restore Function")
	
	#save the path
	sessionFolder = 'C:\\Users\\' + name + '\\Desktop\\artifacts\\Session_Restore'
	
	#function to create a new folder - 1 Parameter for a string, location
	makeDirectory(sessionFolder);
	
	#Check if path exists (returns T/F)
	sessionFolder = os.path.exists(os.path.expandvars("%LOCALAPPDATA%\Microsoft\Windows\History"))

	if sessionFolder:
		print ("\tYou have access to the Session Restore folder, creating short-cut to the repo")
		
		#Now start writng things to the directory
		sourcePath = 'C:\\Users\\' + name + '\\AppData\\Local\\Microsoft\\Internet Explorer\\Recovery'
		destPath = 'C:\\Users\\' + name + '\\Desktop\\artifacts\\Session_Restore'
		CopyFileContents( sourcePath, destPath )
		
	else:
		print ("Unable to Create to the Session folder, please check your user privileges")
	
	
	
def flash():
	print ("Enter Flash Function")
	
		
	#save the path
	flashFolder = 'C:\\Users\\' + name + '\\Desktop\\artifacts\\Flash_Settings'
	
	#function to create a new folder - 1 Parameter for a string, location
	makeDirectory(flashFolder);
	
	#Check if path exists (returns T/F)
	flashFolder = os.path.exists(os.path.expandvars("%LOCALAPPDATA%\Microsoft\Windows\History"))

	if flashFolder:
		print ("\tYou have access to the Session Restore folder, creating short-cut to the repo")
		
		#Now start writng things to the directory
		sourcePath = 'C:\\Users\\' + name + '\\AppData\\Roaming\\Macromedia\\Flash Player\\macromedia.com\\support\\flashplayer\\sys'
		destPath = 'C:\\Users\\' + name + '\\Desktop\\artifacts\\Flash_Settings'
		CopyFileContents( sourcePath, destPath )
		
	else:
		print ("Flash is not installed on this system, therefore, will not check for flash settings")

#Non-Modulated Functions
def createRepo():
	
	print ('Creating container to store browser artifacts')
		
	#check if directory is existing, if not, create one

	#save the path
	path = 'C:\\Users\\' + name + '\\Desktop\\artifacts'
	makeDirectory(path)
	
	
def makeDirectory( tehPath ):

#make a new directory if it doest already exist
	dirExists = os.path.exists(os.path.expanduser(tehPath))
	if dirExists:
		print ("\tDirectory already created")
	else:
		print ("Creating Directory: ", tehPath)	
		os.mkdir(os.path.expanduser(tehPath))			

def createHistShortcut():
	import os, winshell
	from win32com.client import Dispatch
		
	#desktop = winshell.desktop()
	desktop = 'C:\\Users\\' + name + '\\Desktop\\artifacts\\History'
	path = os.path.join(desktop, "Browsing History.lnk")

	#Target is the history section
	target = os.path.expandvars("%LOCALAPPDATA%\Microsoft\Windows\History")
	wDir = r"P:\Media\Media Player Classic"
	icon = r"C:\Users\nick\Documents\GitHub\OpenSourceArtifactollectionToolkit-OSACT-475_2141-Cifranic-Mercado-Simmonds-Voellmer\Scripts\iconStore\historyi.ico"
	 
	shell = Dispatch('WScript.Shell')
	shortcut = shell.CreateShortCut(path)
	shortcut.Targetpath = target
	shortcut.WorkingDirectory = wDir
	shortcut.IconLocation = icon
	shortcut.save()
		
		
def CopyFileContents( sourcePath, destPath ):
	import shutil
	
	for root, dirs, files in os.walk(sourcePath):

		#figure out where we're going
		dest = destPath + root.replace(sourcePath, '')
		
		#if we're in a directory that doesn't exist in the destination folder
		#then create a new folder
		if not os.path.isdir(dest):
			os.mkdir(dest)
			print('Directory created at: ' + dest)

		#loop through all files in the directory
		for f in files:

			#compute current (old) & new file locations
			oldLoc = root + '\\' + f
			newLoc = dest + '\\' + f

			if not os.path.isfile(newLoc):
				try:
					shutil.copy2(oldLoc, newLoc)
					print('File ' + f + ' copied.')
				except IOError:
					print('file "' + f + '" already exists')

				
def main():
	createRepo();
	#browserDetection(); 
	#history();
	
	#cookie();
	#cache();
	#sessionRestore();
	flash(); 
	 


if __name__ == "__main__":
	main()
	
