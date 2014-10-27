## lastFile.py

## Imports
from win32com.shell import shell, shellcon
import binascii, easyReg, os, time, win32security

class RecentFile():
	## __init__   - Initialize the attributes of a registry entry (File).
	## self.entry - The registry entry associated with this file.
	## self.file  - The human-readable name associated with the PIDL stored in self.data.
	## self.meta  - A Metadata object containing metadata about a self.file.
	##
	## entry - The registry object associated with this file.
	def __init__(self, entry):
		self.entry = entry
		## Verify the integrity of the PIDL which should be 20 bytes long.
		if (int(binascii.hexlify(self.entry.data[0:1]), 16) == 20):
			self.file = shell.SHGetPathFromIDList(shell.StringAsPIDL(self.entry.data))
			self.meta = Metadata(self.file, os.stat(self.file))
		else:
			self.file = "INVALID_FORMAT"

	## printDevice - Prints the information of interest.
	def printRecentFile(self):
		if (self.file != "INVALID_FORMAT"):
			print "Value: "   + self.entry.value
			print "  File: "  + self.file
			self.meta.printMetadata()
		
##End of RegEntry class	

class Metadata():
	## __init__   - Initialize the attributes of a File
	## self.file  - The name of the file passed in form RegEntry.__init__().
	#  self.dev   - The device on which the file was saved.
	## self.owner - The owner of the current file. (Tuple)
	## self.sid   - The Security Identifier (SID) of the owner of the current file.
	## self.uid   - A list containing the name, domain and type of the owner of the file.
	## self.size  - The size of the file.
	## self.mtime - The time the file was last modified.
	## self.atime - The time the file was last accessed (opened).
	## self.ctime - The time the file was created.
	##
	## file      - The name of the file passed in from RecentFile.__init__().	
	## f_obj      - The file object passed in from RecentFile.__init__().
	def __init__(self, file, f_obj):
		self.file  = file
		#self.dev   = f_obj.st_dev
		self.sid = win32security.GetFileSecurity(self.file, win32security.OWNER_SECURITY_INFORMATION).GetSecurityDescriptorOwner()
		if (self.file != "INVALID_FORMAT"):
			try:
				self.owner = win32security.LookupAccountSid(None, self.sid)
			except:
				self.owner = "No Matching User for SID: " + str(self.sid)[6:]
		else:
			self.owner = ""
		self.size  = f_obj.st_size
		self.mtime = f_obj.st_mtime
		self.atime = f_obj.st_atime
		self.ctime = f_obj.st_ctime

	def printMetadata(self):
		#print "    Device: "    + str(self.dev)
		print     "    SID: " + str(self.sid)[6:]
		if (type(self.owner) is str):
			print "    Owner: "     + str(self.owner)
		else:
			print "    Owner: "     + self.owner[1] + "\\" + self.owner[0]
			
		print "    File Size: " + str(self.size)
		print "    Modified: "  + time.strftime("%Y-%m-%dT%H:%M:%S", time.gmtime(self.mtime))
		print "    Accessed: "  + time.strftime("%Y-%m-%dT%H:%M:%S", time.gmtime(self.atime))
		print "    Created: "   + time.strftime("%Y-%m-%dT%H:%M:%S", time.gmtime(self.ctime)) + "\n"
		
##End of Metadata class	