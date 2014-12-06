#!/usr/bin/env python

import os, winshell
from win32com.client import Dispatch
import getpass #used to get username

#get username
name = getpass.getuser()
	
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



			   #os.path.expandvars("%LOCALAPPDATA%\Microsoft\Windows\History")