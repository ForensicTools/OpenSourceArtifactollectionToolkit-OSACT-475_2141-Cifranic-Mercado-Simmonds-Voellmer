## fileHistory.py
## Author: Daniel "Albinohat" Mercado
## This module aims to gather information about recent file history on a Windows machine.

## Standard Imports
import binascii, os, time, win32security

## Third-party Imports
from win32com.shell import shell, shellcon
import easyReg

## RecentFile - This call contains information about a recently opened or saved file.
class RecentFile():
	## __init__ - Initialize the attributes of a RecentFile instance.
	## self.entry - The registry entry associated with this file.
	## self.file  - The human-readable name associated with the PIDL stored in self.data.
	## self.meta  - A Metadata object containing metadata about a self.file.
	##
	## entry      - The registry object associated with this file.
	def __init__(self, entry):
		self.entry = entry
		## Verify the integrity of the PIDL which should be 20 bytes long.
		if (int(binascii.hexlify(self.entry.data[0:1]), 16) == 20):
			self.file = shell.SHGetPathFromIDList(shell.StringAsPIDL(self.entry.data))
			try:
				self.meta = Metadata(self.file, os.stat(self.file))

			except WindowsError:
				self.meta = "File non-existent, deleted or insufficient permissions. No metadata available."
		else:
			self.file = "INVALID_FORMAT"
			self.meta = "Invalid Registry Entry. No metadata available."

	## getRecentFile - Returns attributes of the RecentFile instance as a tuple.
	## Index 0       - The registry entry associated with this file.
	## Index 1       - The human-readable name associated with the PIDL stored in self.data.
	## Index 2       - Either a tuple containing the metadata of this file or a string stating that the file is inaccessible.
	def getRecentFile(self):
			if (isinstance(self.meta, Metadata)):
				return str(self.entry.value), str(self.file), self.meta.getMetadata()

			elif (type(self.meta) is str):
				return str(self.entry.value), str(self.meta)			

	## printRecentFile - Prints out the attributes of the printRecentFile instance.
	def printRecentFile(self):
		if (self.file != "INVALID_FORMAT"):
			print "    RecentFile.printRecentFile()"
			print "        Value: " + str(self.entry.value)
			if (isinstance(self.meta, Metadata)):
				self.meta.printMetadata()
			elif (type(self.meta) is str):
				print "        " + str(self.meta)

## End of RecentFile class

## Metadata - This class contains information describing a file.
class Metadata():
	## __init__   - Initialize the attributes of a Metadata instance.
	## self.file  - The name of the file passed in form RegEntry.__init__().
	## self.owner - The owner of the current file. (Tuple)
	## self.sid   - The Security Identifier (SID) of the owner of the current file.
	## self.size  - The size of the file.
	## self.mtime - The time the file was last modified.
	## self.atime - The time the file was last accessed (opened).
	## self.ctime - The time the file was created.
	##
	## file       - The name of the file passed in from RecentFile.__init__().	
	## f_obj      - The file object passed in from RecentFile.__init__().
	def __init__(self, file, f_obj):
		self.file = file
		self.sid  = win32security.GetFileSecurity(self.file, win32security.OWNER_SECURITY_INFORMATION).GetSecurityDescriptorOwner()
		if (self.file != "INVALID_FORMAT"):
			try:
				self.owner = win32security.LookupAccountSid(None, self.sid)
			except:
				self.owner = "No Matching User for SID: " + str(self.sid)[6:]
		else:
			self.owner = ""

		if (type(self.owner) is str):
			self.owner = self.owner
		else:
			self.owner = self.owner[1] + "\\" + self.owner[0]

		self.size  = f_obj.st_size
		self.mtime = f_obj.st_mtime
		self.atime = f_obj.st_atime
		self.ctime = f_obj.st_ctime

	## getMetadata - Returns the attributes of the Metadata instance as a tuple.
	## Index 0     - The owner of the current file. (Tuple)
	## Index 1     - The Security Identifier (SID) of the owner of the current file.
	## Index 2     - The size of the file.
	## Index 3     - The time the file was last modified.
	## Index 4     - The time the file was last accessed (opened).
	## Index 5     - The time the file was created.
	def getMetadata(self):
		return str(self.file), str(self.sid)[6:], str(self.owner), str(self.size), str(time.strftime("%Y-%m-%dT%H:%M:%S", time.gmtime(self.mtime))), str(time.strftime("%Y-%m-%dT%H:%M:%S", time.gmtime(self.atime))), str(time.strftime("%Y-%m-%dT%H:%M:%S", time.gmtime(self.ctime)))

	## printMetadata - Prints out the attributes of the Metadata instance.
	def printMetadata(self):
		print "    Metadata.printMetadata()"
		print "        File: " + str(self.file)
		print "        SID: " + str(self.sid)[6:]
		print "        Owner: " + str(self.owner)
		print "        File Size: " + str(self.size)
		print "        Modified: " + str(time.strftime("%Y-%m-%dT%H:%M:%S", time.gmtime(self.mtime)))
		print "        Accessed: " + str(time.strftime("%Y-%m-%dT%H:%M:%S", time.gmtime(self.atime)))
		print "        Created: " + str(time.strftime("%Y-%m-%dT%H:%M:%S", time.gmtime(self.ctime)) + "\n")

##End of Metadata class
