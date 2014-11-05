#!/usr/bin/env python
import os.path # Required to validate files
import getpass #used to get user

#GLOBAL-VARIABLES
name = getpass.getuser()
	
def createRepo():
	#get username
	#name = getpass.getuser()	
	
	print ('Creating container to store browser artifacts')
		
	#check if directory is existing, if not, create one

	#save the path
	path = 'C:\\Users\\' + name + '\\Desktop\\artifacts'
	makeDirectory(path)
	
	
	
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
	
	
		


def history():
#Records websites visited by date & time. Details stored for each 
#local user account. Records number of times visited (frequency). 
#Also tracks access of local system files.	
	print ("Entered History Function")
	
	#get username
	name = getpass.getuser()
	#save the path
	historyFolder = 'C:\\Users\\' + name + '\\Desktop\\artifacts\\History'
	
	#function to create a new folder - 1 Parameter for a string, location
	makeDirectory(historyFolder);
		
	
	histFolder = os.path.exists(os.path.expandvars("%LOCALAPPDATA%\Microsoft\Windows\History"))

	if histFolder:
		print ("\tYou have access to the history folder, creating short-cut to the repo")
		
	else:
		print ("Unable to grant access to the history folder, please check your user privileges")
		

 
def cookie():
	#Cookies give insight into what websites have been visited 
	#and what activities may have taken place there
	print ("Entered Cookie Function")


def cache():
	#The cache is where webpage components can be stored locally
	#to speed up subsequent visits. Gives the investigator a 
	#“Snapshot in time” of what a user was looking at on-line	
	print ("Enter Cache Function")

	
def sessionRestore():
	print ("Enter Session Restore Function")
	
def flash():
	print ("Enter Flash Function")
	
def makeDirectory( tehPath ):

#make a new directory if it doest already exist
	dirExists = os.path.exists(os.path.expanduser(tehPath))
	if dirExists:
		print ("\tDirectory already created")
	else:
		print ("Creating Directory: ", tehPath)	
		os.mkdir(os.path.expanduser(tehPath))			

def main():
	createRepo();
	#browserDetection(); 
	history();
	# cookie();
	# cache();
	# sessionRestore();
	# flash(); 
	 


if __name__ == "__main__":
	main()
	
