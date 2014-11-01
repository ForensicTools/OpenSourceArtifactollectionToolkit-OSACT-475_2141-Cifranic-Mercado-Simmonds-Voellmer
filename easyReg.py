## easyReg.py
## A simple wrapper module for _winreg.

## TODO         - Write functions to return info rather than print in RegKey + RegEntry. [IN-PROGRESS] 

## Terminology  - To attempt to reduce confusion, here are some definitions of commonly used terms.
## Key          - A registry key.
## Subkey       - A key that resides directly under a key.
## Parent       - The key that resides directly above a key.
## Value/Entry  - A data entry for a given key.
## Data         - The contents of a value.

import sys, time, _winreg

## RegKey - A class which contains many attributes describing a registry key.
class RegKey():
	## __init__             - Initialize the attributes of a registry key.
	## self.handle          - A handle to this registry key.
	## self.parent          - The full path to the key above this registry key.
	## self.path            - The full path to this registry key.
	## self.name            - The name of this registry key.
	## self.list_of_entries - A list of RegEntry objects containing all information in this Registry Key.
	## self.list_of_subkeys - A list of RegKey objects containing the subkeys under this registry key.
	def __init__(self, path):
		self.handle          = easyOpenKey(path)
		self.path            = path		
		self.name            = self.path.split("\\")[-1]
		if (len(self.path.split("\\")) > 0):
			self.parent      = path[:-(len(self.name) + 1)]
		else:
			self.parent      = ""
		self.list_of_subkeys = []
		self.list_of_entries = []

	## addEntry - Add a registry entry under the this key.
	def addEntry(self, entry):
		self.list_of_entries.append(entry)

	## addSubkey - Add a registry key under the this key.
	def addSubkey(self, key):
		self.list_of_subkeys.append(key)
	
	## getEntries - Returns a list of tuples containing the value, type and data of each entry.
	def getEntries(self):
		self.tuples = []
		self.values = []
		self.types  = []
		self.datas  = []
		
		for entry in list_of_entries:
			self.values.append(entry.value)
			self.types.append(entry.type)
			self.datas.append(entry.data)
		
		self.tuples = zip(self.values, self.types, self.datas)
		return self.tuples
		
	## Returns a summary about the current RegKey object as a tuple.
	## 0 - Handle of the RegKey
	## 1 - Path of the RegKey
	## 2 - Name of the RegKey
	## 3 - Parent of this RegKey
	## 4 - # of entries in the RegKey
	## 5 - # of subkeys under this entry
	def getRegKey(self):
		return self.handle, self.path, self.name, self.parent, len(self.list_of_entries), len(self.list_of_subkeys)
	
	##  getSubkeys - Returns a tuples containing the names, paths and handles of each subkey.
	def getSubkeys(self):
		self.handles = []
		self.paths   = []
		self.names   = []
		
		for key in list_of_subkeys:
			self.names.append(key.name)
			self.paths.append(key.path)
			self.handles.append(key.hanle)
			
		self.tuples = zip(self.handles, self.paths, self.names)
		return self.tuples
		
	## populateEntries - Enumerates through entries of this key and populates the list of entries with RegEntry objects.
	def populateEntries(self):	
		## Loop through the entries until you run out.
		for i in range(1024):
			try:
				self.addEntry(RegEntry(_winreg.EnumValue(self.handle, i)))
				
			except EnvironmentError:
				break
				
	## populateSubkeys - Enumerates through subkeys of this key and populates the list of subkeys with key objects.
	def populateSubkeys(self):
		## Loop through the subkeys until you run out.
		for i in range(1024):
			try:
				self.addSubkey(RegKey(self.path + "\\" + _winreg.EnumKey(self.handle, i)))
				
			except EnvironmentError:
				break		

	## printEntries - Calls the printRegEntry method to print all entries of this registry key.
	def printEntries(self):
		for entry in self.list_of_entries:
			entry.printRegEntry()
				
	## printRegKey - Takes in a series of booleans to determine what is print. Input will later be a bit-mask.
	## b_e - Boolean determining if the list of entries is printed.
	## b_k - Bool determining if the list of subkeys is printed.
	def printRegKey(self):
		print "Name: " + self.name
		print " Handle: " + str(self.handle)
		print " Parent: " + self.parent
		print " # of Subkeys: " + str(len(self.list_of_subkeys))
		print " # of Entries: " + str(len(self.list_of_entries))
		print "  List of Entries..." 
		for entry in self.list_of_entries:
			print "    " + entry.value
	
		print "  List of Subkeys..."
		for key in self.list_of_subkeys:
			print "    " + key.path

		print "END OF KEY!\n"
			
	## printSubkeys - Calls the printRegKey method to print all subkeys of this registry key.
	def printSubkeys(self):
		for key in self.list_of_subkeys:
			key.printRegKey()

	## removeEntry - Remove a registry entry with a given name under this key.
	## n - The name of the entry to remove.
	def removeEntry(self, n):
		self.bool_found = 0
		for entry in self.list_of_entries:
			if (entry.value == n):
				self.list_of_entries.remove(entry)
				self.bool_found = 1
				break
		
		if (self.bool_found == 0):
			print "    easyReg.RegKey.removeEntry: There was no entry found with the name \"" + n + ".\""
	
	## removeSubkey - Removes a registry subkey with a given name under this key.
	## n - The name of the subkey to remove.
	def removeSubkey(self, n):
		self.bool_found = 0
		for key in self.list_of_subkeys:
			if (key.name == n):
				self.list_of_subkeys.remove(key)
				self.bool_found = 1 
				break
		
		if (self.bool_found == 0):
			print "    easyReg.RegKey.removeSubkey: There was no subkey found with the name \"" + n + ".\""

## End of RegKey class
			
## RegEntry - A class which contains many attributes describing a registry entry.
class RegEntry():
	## __init__   - Initialize the attributes of a User object.
	## self.value - Corresponds to the Name column in regedit.
	## self.type  - Corresponds to the type column in regedit.
	## self.data  - Corresponds to the data column in regedit.
	def __init__(self, tuple):
		self.value = tuple[0]
		if   (tuple[2] == 2):
			self.type = "REG_EXPAND_SZ"
		elif (tuple[2] == 3):
			self.type = "REG_BINARY"
		else:
			self.type = "REG_DWORD"
		self.data  = tuple[1]

	## printEntry - Prints the information of interest.
	## Meant to be used for debugging purposes only.
	def printRegEntry(self):
		print "   Value: "  + self.value
		print "    Type: "  + str(self.type)
		try:
			print "    Data: "  + str(self.data) + "\n"
		except UnicodeEncodeError:
			print "    BAD DATA! \n"
	
##End of RegEntry class		

## s - The key provided by the user. (string)
## k - The subkey to be created under the key. (string)
def easyCreateKey(s, k):
	_winreg.CreateKey(easyOpenKey(s), k)

## easyDelete Key - Deletes the specified key.
## s - The key provided by the user. (string)
def easyDeleteKey(s):
	_winreg.DeleteKey(easyOpenKey(s))

## easyDeleteValue - Deletes the specified value.
## Limitation - Keys with subkeys cannot be deleted.
## s - The key provided by the user. (string)
## v - The name of the value to be deleted. (string)
def easyDeleteValue(s, v):
	_winreg.DeleteValue(easyOpenKey(s), v)
	
## easyGetEntry - A function which returns a subkey of the provided key as a string.
## s - The key provided by the user. (string)
## i - The index of the subkey within the key. (int)	
def easyGetSubkey(s, i):
	return _winreg.EnumKey(easyOpenKey(s), i)

## easyGetValue - A function which returns a name, data, type tuple for a registry entry.
## s - The key provided by the user. (string)
## i - The index of the registry entry within the key. (int)
def easyGetValue(s, i):
	return _winreg.EnumValue(easyOpenKey(s), i)
	
## easyOpenKey - A function which returns a handle to the key specified.
## s - The key provided by the user. (string)
def easyOpenKey(s):
	## Create a list containing the hive and the name of the Registry key.
	t_k = s.split("\\", 1)

	## Set the required hive to one of the predefined CONSTs.
	if   (t_k[0] == "HKEY_CLASSES_ROOT"):
		return _winreg.OpenKey(_winreg.ConnectRegistry(None, _winreg.HKEY_CLASSES_ROOT), t_k[1])
	elif (t_k[0] == "HKEY_CURRENT_USER"):
		return _winreg.OpenKey(_winreg.ConnectRegistry(None, _winreg.HKEY_CURRENT_USER), t_k[1])
	elif (t_k[0] == "HKEY_LOCAL_MACHINE"):
		return _winreg.OpenKey(_winreg.ConnectRegistry(None, _winreg.HKEY_LOCAL_MACHINE), t_k[1])	
	elif (t_k[0] == "HKEY_USERS"):
		return _winreg.OpenKey(_winreg.ConnectRegistry(None, _winreg.HKEY_USERS), t_k[1])	
	elif (t_k[0] == "HKEY_PERFORMANCE_DATA"):
		return _winreg.OpenKey(_winreg.ConnectRegistry(None, _winreg.HKEY_PERFORMANCE_DATA), t_k[1])	
	elif (t_k[0] == "HKEY_CURRENT_CONFIG"):
		return _winreg.OpenKey(_winreg.ConnectRegistry(None, _winreg.HKEY_CURRENT_CONFIG), t_k[1])	
	elif (t_k[0] == "HKEY_DYN_DATA"):
		return _winreg.OpenKey(_winreg.ConnectRegistry(None, _winreg.HKEY_DYN_DATA), t_k[1])	
	else:
		print "SOMETHING TERRIBLE HAPPENED!"	

## easyQueryKey - Returns the following information from the key specified as a tuple.
## Index    Meaning
## 0	  - An integer giving the number of sub keys this key has.
## 1	  - An integer giving the number of values this key has.
## 2	  - A long integer giving when the key was last modified (if available) as 100's of nanoseconds since Jan 1, 1601.
##
## s      - The key provided by the user. (string)
def easyQueryKey(s):
	return _winreg.QueryInfoKey(easyOpenKey(s))	

## easyQueryValue - Returns the following information associated with value for the specified registry key as a tuple.
##Index    Meaning
## 0	 - The value of the registry item.
## 1	 - An integer giving the registry type for this value
##
## s     - The key provided by the user. (string)
## v     - The name of the value to be deleted. (string)
def easyQueryValue(s, v):
	return _winreg.QueryValueEx(easyOpenKey(s), v)

## easySaveKey - Exports key and its subkeys to a file.
## s - The key provided by the user. (string)
## f - the path and file name where the information will be saved. (string)
def easySaveKey(s, f):
	try:
		_winreg.SaveKey(easyOpenKey(s), f)
	except WindowsError:
		print "easyReg.easySaveKey Threw: " + str(sys.exc_info()[1])

## easySetValue - Sets the data of the given value name for the key specified. 
## s - The key provided by the user. (string)
## v - The name of the value to be deleted. (string)
## t - The type of the data. (string)
## d - The data to be stored.
def easySetValue(s, v, t, d):
	## Set the required type to one of the predefined CONSTs.
	if   (t == "REG_BINARY"):
		_winreg.SetValueEx(easyOpenKey(s), n, 0, winreg.REG_BINARY, d)
	elif (t == "REG_DWORD"):
		_winreg.SetValueEx(easyOpenKey(s), n, 0, winreg.REG_DWORD, d)
	elif (t == "REG_DWORD_LITTLE_ENDIAN"):
		_winreg.SetValueEx(easyOpenKey(s), n, 0, winreg.REG_DWORD_LITTLE_ENDIAN, d)
	elif (t == "REG_DWORD_BIG_ENDIAN"):
		_winreg.SetValueEx(easyOpenKey(s), n, 0, winreg.REG_DWORD_BIG_ENDIAN, d)
	elif (t == "REG_EXPAND_SZ"):
		_winreg.SetValueEx(easyOpenKey(s), n, 0, winreg.REG_EXPAND_SZ, d)
	elif (t == "REG_LINK"):
		_winreg.SetValueEx(easyOpenKey(s), n, 0, winreg.REG_LINK, d)
	elif (t == "REG_MULTI_SZ"):
		_winreg.SetValueEx(easyOpenKey(s), n, 0, winreg.REG_MULTI_SZ, d)
	elif (t == "RREG_NONE"):
		_winreg.SetValueEx(easyOpenKey(s), n, 0, winreg.REG_NONE, d)
	elif (t == "REG_RESOURCE_LIST"):
		_winreg.SetValueEx(easyOpenKey(s), n, 0, winreg.REG_RESOURCE_LIST, d)
	elif (t == "REG_FULL_RESOURCE_DESCRIPTOR"):
		_winreg.SetValueEx(easyOpenKey(s), n, 0, winreg.REG_FULL_RESOURCE_DESCRIPTOR, d)
	elif (t == "REG_RESOURCE_REQUIREMENTS_LIST"):
		_winreg.SetValueEx(easyOpenKey(s), n, 0, winreg.REG_RESOURCE_REQUIREMENTS_LIST, d)
	elif (t == "REG_SZ"):
		_winreg.SetValueEx(easyOpenKey(s), n, 0, winreg.REG_SZ, d)
	## Throw an exception if the type is invalid.
	else:
		raise TypeError("The data type specified was invalid!", t)

## listSubkeys - Returns a list of subkeys under a given registry key.
## s - The key provided by the user. (string)
def listSubkeys(s):
	## Open the key specified.
	key = easyOpenKey(s)
	## Initialize a list to hold the subkeys.
	subkeys = []
	
	## Loop through the subkeys until you run out.
	for i in range(1024):
		try:
			subkeys.append(_winreg.EnumKey(key, i))
		except:
			return subkeys

## listValues - Returns the values of a given registry key.
## s - The key provided by the user. (string)
def listValues(s):
	## Open the key specified.
	key = easyOpenKey(s)
	## Initialize a list to hold the values.
	values = []

	## Loop through the values until you run out.
	for i in range(1024):
		try:
			values.append(_winreg.EnumValue(key, i))
		except:
			return values

## walkReg - Walks through the registry starting at a specified key or Hive.
## k  - A RegKey object.
## n  - The maximum number of levels of subkeys to walk. Will be decremented in each iteration.
## fn - A user-defined function to be run each time walkReg runs. It takes a list as a parameter in order to let the user have maximum control over the parameter sent.
## l  - The list to be passed to function fn.
def walkReg(k, n, fn, l):
	if (n > 0):
		## Loop through the subkeys until you run out.
		for i in range(1024):
			try:
				current = k.path + "\\" + _winreg.EnumKey(k.handle, i)
				k.addSubkey(RegKey(current))

			except EnvironmentError:
				## Sort the list of registry entries.
				k.list_of_subkeys.sort(key=lambda k: k.name, reverse=False)
				break

		## Loop through the entries of the current key until you run out.
		for j in range(1024):
			try:
				k.addEntry(RegEntry(_winreg.EnumValue(k.handle, j)))

			except EnvironmentError:
				## Sort the list of registry entries.
				k.list_of_entries.sort(key=lambda e: e.value, reverse=False)		
				break
		
		## Recursively go through all of the sub entries until you run out of information of n = 0
		for key in k.list_of_subkeys:
			## Call the user-defined function.
			fn(l)
			walkReg(key, (n - 1), fn)	
	else:
		return
		
## End of helper functions
## End of easyReg.py
