## carmenSandiego.py
## Author: Daniel "Albinohat" Mercado
## This module is meant to assist in figuring out the physical locations that a Windows machine has been.

## TODO - Modify moy and dow dictionaries to be const, class vars rather than instanced variables. [ DONE ] 
##      - Rename NetworkListProfile to NetworkProfile. [ DONE ]
##      - Rename NetworkListSignature to NetworkSignature. [ DONE ]
##      - Rename TimeZoneEntry class to TimeZoneProfile. [ DONE ]

## Standard Imports
import array, binascii, re, sys

## Third-party Imports.
import easyReg

## NetworkProfile - This class describes a registry entry containing information about a network profile.
## Inheritance: easyReg.RegKey -> easyReg.RegKey 
##                             -> NetworkProfile
class NetworkProfile():
	## This list contains all of the network profile RegKey objects.
	list_of_network_profiles = []

	## populateNetworkProfiles - Populates the list of network profiles.
	## k                       - The RegKey containing all of the network profile.
	def populateManagedNetworks(k):
		for key in k.list_of_subkeys:
			NetworkProfile.list_of_network_profiles.append(k)
			
	## __init__ - Initializes the attributes of a NetworkProfile instance.
	## self.category            -
	## self.date_created        - The date and time that the network profile was created.
	## self.date_last_connected -  
	## self.description         - A description of the network profile.
	## self.bool_ismanaged      - A boolean tracking whether or not this network is managed.
	## self.name_type           -
	## self.profile_name        - The friendly name of the profile.
	##
	## k                 	    - The RegKey object associated with this network profile.
	def __init__(self, key):		
		for entry in key.list_of_entries:
			if (entry.value == "Category"):
				self.category = entry.data	
			elif (entry.value == "DateCreated"):
				self.date_created = entry.data			
			elif (entry.value == "DateLastConnected"):
				self.date_last_connected = entry.data 		
			elif (entry.value == "Description"):
				self.description = entry.data		
			elif (entry.value == "Managed"):
				self.bool_ismanaged = entry.data		
			elif (entry.value == "NameType"):
				self.name_type = entry.data	
			elif (entry.value == "ProfileName"):
				self.profile_name = entry.data	
			else:
				print "    NetworkProfile.__init__(): Encountered invalid value, \"" + entry.value + ".\""
				sys.exit()

	## printNetworkProfile - Prints out the attributes of a NetworkProfile instance.
	def printNetworkProfile(self):
		print "    NetworkProfile.printNetworkProfile()"
		print "        self.category: " + self.category
		print "        self.date_created: " + self.date_created
		print "        self.date_last_connected: " + self.date_last_connected
		print "        self.description: " + self.description
		print "        self.bool_ismanaged: " + str(self.bool_ismanaged)
		print "        self.name_type: " + self.name_type

## End of NetworkProfile class.		
		
## NetworkSignature - This class describes a registry key containing information about a network signature.
## Inheritance: easyReg.RegKey -> easyReg.RegKey 
##                             -> NetworkSignature
class NetworkSignature():
	## This list contains all of the managed and unmanaged network RegKey objects.
	list_of_managed_networks   = []
	list_of_unmanaged_networks = []

	## populateManagedNetworks - Populates the list of managed network signatures.
	## k                       - The RegKey containing all of the network signatures.
	def populateManagedNetworks(k):
		for key in k.list_of_subkeys:
			NetworkSignature.list_of_managed_networks.append(k)

	## populateUnmanagedNetworks - Populates the list of unmanaged network signatures.
	## k                         - The RegKey containing all of the network signatures.
	def populateManagedNetworks(k):
		for key in k.list_of_subkeys:
			NetworkSignature.list_of_unmanaged_networks.append(k)
	
	## __init__ - Initializes the attributes of a NetworkSignature instance.
	## self.default_gw_mac - The MAC address of the interface of the machine's default gateway assigned in this network.
	## self.description    - A description of the network signature
	## self.dns_suffix     - The DNS suffix applied to machines' hostnames on this network.
	## self.first_network  - 
	## self.profile_guid   - A unique identifier for the network assigned by Winders.
	## self.source         - 
	##
	## k                   - The RegKey object associated with this network signature.
	def __init__(self, key):
		for entry in k.list_of_entries:
			if (entry.value == "DefaultGatewayMac"):
				self.default_gw_mac = entry.data
			if (entry.value == "Description"):
				self.description = entry.data
			if (entry.value == "DnsSuffix"):
				self.dns_suffix = entry.data
			if (entry.value == "FirstNetwork"):
				self.first_network = entry.data
			if (entry.value == "ProfileGuid"):
				self.profile_guid = entry.data
			if (entry.value == "source"):
				self.source = entry.data
			else:
				print "    NetworkProfile.__init__(): Encountered invalid value, \"" + entry.value + ".\""
				sys.exit()
				
	## printNetworkSignature - Prints out the attributes of a NetworkSignature instance.
	def printNetworkSignature(self):
		print "    NetworkSignature.printNetworkSignature()"
		print "        self.default_gw_mac: " + self.default_gw_mac
		print "        self.description: " + self.description
		print "        self.dns_suffix: " + self.dns_suffix
		print "        self.first_network: " + self.first_network
		print "        self.profile_guid: " + self.profile_guid
		print "        self.source: " + self.source

## End of NetworkSignature class.
		
## TimeZoneProfile - This class describes a registry key containing information about the timezone(s) the computer has been in.		
## Inheritance: easyReg.RegKey -> easyReg.RegKey 
##                             -> TimeZoneProfile
class TimeZoneProfile():
	## MOY_DICT - A dictionary mapping the months of the year. (Const)
	## DOW_DICT - A dictionary mapping the days of the week. (Const)
	MOY_DICT = { "0001": "January",
					  "0002": "February",
					  "0003": "March",
					  "0004": "April",
					  "0005": "May",
					  "0006": "June",
					  "0007": "July",
					  "0008": "August",
					  "0009": "September",
					  "000a": "October",
					  "000b": "November",
					  "000c": "December"
	}
	DOW_DICT = { "0000": "Sunday",
					  "0001": "Monday",
					  "0002": "Tuesday",
					  "0003": "Wednesday",
					  "0004": "Thursday",
					  "0005": "Friday",
					  "0006": "Saturday"
	}	
	
	## __init__ - Initialize the attributes of a TimeZoneProfile instance.
	## self.activetime_bias           - The active time bias. Bias + DaylightBias
	## self.bias                      - The number of minutes added due to timezone.
	## self.daylight_name             - 
	## self.bool_dynamic_dst_disabled - A boolean tracking whether or not dynamic DST is disabled.
	## self.daylight_bias  	          - The daylight bias. The number of minutes added when DST is active.
	## self.daylight_start	          - Little-Endian hex encoded start date/time of DST.
	## self.standard_bias             - The standard bias. The number of minutes added when DST is not active.
	## self.standard_name             -
	## self.standard_start	          - Little-Endian hex encoded end date/time of DST.
	## self.time_zone_key_name        - The name of registry key storing information about the time zone in which this machine currently resides.
	##
	## k                              - The RegKey object associated with this TimeZoneProfile instance.
	def __init__(self, k):		
		for entry in k.list_of_entries:
			
			entry.printRegEntry()
			
			if (entry.type == "REG_DWORD"):
				if ("Bias" in entry.value):
					## Perform a 2s-complement on the DWORD to get # of minutes +/- UTC.
					## Final value is what is added to local time to get UTC.
					temp = entry.data
					if ((temp & 1 << (32-1)) != 0):
						temp = temp - (1 << 32)
					
					## Determine which bias this is and set the value of the correct attribute.
					if   (entry.value == "Bias"):
						self.bias = temp
					elif (entry.value == "ActiveTimeBias"):
						self.activetime_bias = temp
					elif (entry.value == "DaylightBias"):
						self.daylight_bias = temp
					elif (entry.value == "StandardBias"):
						self.standard_bias = temp					
					else:
						print "    TimeZoneProfile.__init__(): Encountered invalid value, \"" + entry.value + ".\""
						sys.exit()
				
				elif (entry.value == "DynamicDaylightTimeDisabled"):
					self.bool_dynamic_dst_disabled = entry.data
		
				else:
					print "    TimeZoneProfile.__init__(): Encountered invalid value, \"" + entry.value + ".\""
					sys.exit()
					
			elif (entry.type == "REG_BINARY"):
				if ("Start" in entry.value):
					temp = array.array('h', entry.data)
					temp.byteswap()
					temp_array = re.findall("....", binascii.hexlify(temp))
					temp_array[1] = TimeZoneProfile.MOY_DICT[str(temp_array[1])]
					temp_array[7] = TimeZoneProfile.DOW_DICT[str(temp_array[7])]
					
					if (entry.value == "DaylightStart"):
						self.daylight_start = temp_array
					elif (entry.value == "StandardStart"):
						self.standard_start = temp_array
					else: 
						print "    TimeZoneProfile.__init__(): Encountered invalid value, \"" + entry.value + ".\""
						sys.exit()
						
			elif (entry.type == "REG_SZ"):
				if (entry.value == "DaylightName"):
					self.daylight_name = entry.data
					
				elif (entry.value == "StandardName"):
					self.standard_name = entry.data	
				elif (entry.value == "TimeZoneKeyName"):
					self.time_zone_key_name = entry.data
				else: 
					print "    TimeZoneProfile.__init__(): Encountered invalid value, \"" + entry.value + ".\""
					sys.exit()
					
			else:
				print "    TimeZoneProfile.__init__(): Encountered invalid type, \"" + entry.type + ".\""
				sys.exit()
		
	## printTimeZoneProfile - Prints out the attributes of a TimeZoneProfile instance.
	def printTimeZoneProfile(self):
		print "    TimeZoneProfile.printTimeZoneProfile()"
		print "        self.activetime_bias: " + str(self.activetime_bias)
		print "        self.bias: " + str(self.bias)
		print "        self.daylight_bias: " + str(self.daylight_bias)
		print "        self.daylight_name: " + self.daylight_name
		print "        self.bool_dynamic_dst_disabled: " + str(self.bool_dynamic_dst_disabled)
		print "        self.daylight_start: " + str(self.daylight_start)
		print "        self.standard_bias: " + str(self.standard_bias)
		print "        self.standard_name: " + self.standard_name
		print "        self.standard_start: " + str(self.standard_start)
		print "        self.time_zone_key_name: " + self.time_zone_key_name
		
## End of TimeZoneProfile class
