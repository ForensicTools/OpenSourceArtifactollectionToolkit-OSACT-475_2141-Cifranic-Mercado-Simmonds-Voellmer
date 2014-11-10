## carmenSandiego.py
## Author: Daniel "Albinohat" Mercado
## This module is meant to assist in figuring out the physical locations that a Windows machine has been.
## Standard Imports
import array, binascii, re, sys, _winreg

## Third-party Imports.
import easyReg

## NetworkListProfile - This class describes a registry entry containing information about a network profile.
## Inheritance: easyReg.RegKey -> easyReg.RegKey 
##                             -> NetworkListProfile
class NetworkListProfile():
	## __init__ - Initializes the attributes of a NetworkListProfile instance.
	## self.moy_dict     	    - A dictionary mapping the months of the year.
	## self.dow_dict   	        - A dictionary mapping the days of the week.
	## self.category            -
	## self.date_created        - The date and time that the network profile was created.
	## self.date_last_connected -  
	## self.description         - A description of the network profile.
	## self.bool_ismanaged      - A boolean tracking whether or not this network is managed.
	## self.name_type           -
	## self.profile_name        - The friendly name of the profile.
	##
	## key               	    - The RegKey object associated with this network profile.
	def __init__(self, key):
		self.moy_dict = { "0001": "January",
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
		self.dow_dict = { "0000": "Sunday",
					      "0001": "Monday",
					      "0002": "Tuesday",
					      "0003": "Wednesday",
					      "0004": "Thursday",
					      "0005": "Friday",
					      "0006": "Saturday"
		}
		
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
				print "    NetworkListProfile.__init__(): Encountered invalid value, \"" + entry.value + ".\""
				sys.exit()

	## printNetworkListProfile - Prints out the attributes of a NetworkListProfile instance.
	def printNetworkListProfile(self):
		print "    NetworkListProfile.printNetworkListProfile()"
		print "        self.category: " + self.category
		print "        self.date_created: " + self.date_created
		print "        self.date_last_connected: " + self.date_last_connected
		print "        self.description: " + self.description
		print "        self.bool_ismanaged: " + str(self.bool_ismanaged)
		print "        self.name_type: " + self.name_type

## NetworkListProfile - This class describes a registry entry containing information about a network signature.
## Inheritance: easyReg.RegKey -> easyReg.RegKey 
##                             -> NetworkListSignature
class NetworkListSignature():
	## __init__ - Initializes the attributes of a NetworkListSignature instance.
	## self.default_gw_mac - The MAC address of the interface of the machine's default gateway assigned in this network.
	## self.description    - A description of the network signature
	## self.dns_suffix     - The DNS suffix applied to machines' hostnames on this network.
	## self.first_network  - 
	## self.profile_guid   - A unique identifier for the network assigned by Winders.
	## self.source         - 
	##
	## key               - The RegKey object associated with this network signature.
	def __init__(self, key):
		for entry in key.list_of_entries:
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
				print "    NetworkListProfile.__init__(): Encountered invalid value, \"" + entry.value + ".\""
				sys.exit()
			
	## printNetworkListSignature - Prints out the attributes of a NetworkListSignature instance.
	def printNetworkListSignature(self):
		print "    NetworkListSignature.printNetworkListSignature()"
		print "        self.default_gw_mac: " + self.default_gw_mac
		print "        self.description: " + self.description
		print "        self.dns_suffix: " + self.dns_suffix
		print "        self.first_network: " + self.first_network
		print "        self.profile_guid: " + self.profile_guid
		print "        self.source: " + self.source
			
## TimeZoneEntry - This class describes a registry entry containing information about the timezone(s) the computer has been in.		
## Inheritance: easyReg.RegKey -> easyReg.RegKey 
##                             -> TimeZoneEntry
class TimeZoneEntry():
	## __init__                       - Initialize the attributes of a TimeZoneEntry instance.
	## self.moy_dict     	          - A dictionary mapping the months of the year.
	## self.dow_dict   	              - A dictionary mapping the days of the week.
	## self.activetime_bias           - The active time bias. Bias + DaylightBias
	## self.bias                      - The number of minutes added due to timezone.
	## self.daylight_name             - 
	## self.bool_dynamic_dst_disabled - A boolean tracking whether or not dynamic DST is disabled.
	## self.daylight_bias  	          - The daylight bias. The number of minutes added due to DST.
	## self.daylight_start	          - Little-Endian hex encoded start date/time of DST.
	## self.standard_name             -
	## self.standard_start	          - Little-Endian hex encoded end date/time of DST.
	## self.time_zone_key_name        - The name of registry key storing information about the time zone in which this machine currently resides.
	##
	## key               - The RegKey object associated with this TimeZoneEntry instance.
	def __init__(self, key):
		self.moy_dict = { "0001": "Janurary",
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
		self.dow_dict = { "0000": "Sunday",
					      "0001": "Monday",
					      "0002": "Tuesday",
					      "0003": "Wednesday",
					      "0004": "Thursday",
					      "0005": "Friday",
					      "0006": "Saturday"
		}
		
		for entry in key.list_of_entries:
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
					else:
						print "    TimeZoneEntry.__init__(): Encountered invalid value, \"" + entry.value + ".\""
						sys.exit()
				
				elif (entry.value == "DynamicDaylightTimeDisabled"):
					self.bool_dynamic_dst_disabled = entry.data
				else:
					print "    TimeZoneEntry.__init__(): Encountered invalid value, \"" + entry.value + ".\""
					sys.exit()
					
			elif (entry.type == "REG_BINARY"):
				if ("Start" in self.value):
					temp = array.array('h', entry.data)
					temp.byteswap()
					temp_array = re.findall("....", binascii.hexlify(temp))
					temp_array[1] = self.moy_dict[str(temp_array[1])]
					temp_array[7] = self.dow_dict[str(temp_array[7])]
					
					if (entry.value == "DayLightStart"):
						self.daylight_start = self.temp_array
					elif (entry.value == "StandardStart"):
						self.standard_start = self.temp_array
					else: 
						print " TimeZoneEntry.__init__(): Encountered invalid value, \"" + entry.value + ".\""
						sys.exit()
						
			elif (entry.tpye == "REG_SZ"):
				if (entry.value == "DaylightName"):
					self.daylight_name = entry.data
				elif (entry.value == "StandardName"):
					self.standard_name = entry.data
				elif (entry.value == "TimeZoneKeyName"):
					self.time_zone_key_name = entry.data
				else: 
					print " TimeZoneEntry.__init__(): Encountered invalid value, \"" + entry.value + ".\""
					sys.exit()
					
			else:
				print "    TimeZoneEntry.__init__(): Encountered invalid type, \"" + entry.type + ".\""
				sys.exit()
		
	## printTimeZoneEntry - Prints out the attributes of a TimeZoneEntry instance.
	def printTimeZoneEntry(self):
		print "    TimeZoneEntry.printTimeZoneEntry()"
		print "        self.activetime_bias: " + str(self.activetime_bias)
		print "        self.bias: " + str(self.bias)
		print "        self.daylight_bias: " + str(self.daylight_bias)
		print "        self.daylight_name: " + self.daylight_name
		print "        self.bool_dynamic_dst_disabled: " + str(self.bool_dynamic_dst_disabled)
		print "        self.daylight_start: " + str(self.daylight_start)
		print "        self.standard_name: " + self.standard_name
		print "        self.standard_start: " + str(self.standard_start)
		print "        self.time_zone_key_name: " + self.time_zone_key_name
		
## End of TimeZoneEntry class
