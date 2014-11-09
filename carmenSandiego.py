## getTimezones.py
## This script will calculate the time zones in each of the control sets in the registry.

## Standard Imports
import array, binascii, re, _winreg

## Third-party Imports.

## NetworkListProfile - This class describes a registry entry containing information about a network profile.
## Inheritance: easyReg.RegKey -> easyReg.RegKey -> NetworkListProfile
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
	## entry               	    - The registry object associated with this file.
	def __init__(self, entry):
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
## Inheritance: easyReg.RegKey -> easyReg.RegKey -> NetworkListSignature
class NetworkListSignature():
	## __init__ - Initializes the attributes of a NetworkListSignature instance.
	## self.default_gw_mac - The MAC address of the interface of the machine's default gateway assigned in this network.
	## self.description    - A description of the network signature
	## self.dns_suffix     - The DNS suffix applied to machines' hostnames on this network.
	## self.first_network  - 
	## self.profile_guid   - A unique identifier for the network assigned by Winders.
	## self.source         - 
	##
	## entry               - The registry object associated with this file.
	def __init__(self, entry):
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
class TimeZoneEntry():
	## __init__                - Initialize the attributes of a registry entry (File).
	## self.moy_dict     	   - A dictionary mapping the months of the year.
	## self.dow_dict   	       - A dictionary mapping the days of the week.
	## self.activetime_bias    - The active time bias. Bias + DaylightBias
	## self.bias               - The number of minutes added due to timezone.
	## self.daylight_bias  	   - The daylight bias. The number of minutes added due to DST.
	## self.daylight_start	   - Little-Endian hex encoded start date/time of DST.
	## self.standard_start	   - Little-Endian hex encoded end date/time of DST.
	##
	## entry               	   - The registry object associated with this file.
	def __init__(self, entry):
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
				
		if (entry.type == "REG_DWORD"):
			if ("Bias" in entry.value):
				## Perform a 2s-complement on the DWORD to get # of minutes +/- UTC.
				## Final value is what is added to local time to get UTC.
				self.temp = entry.data
				if ((self.temp & 1 << (32-1)) != 0):
					self.temp = self.temp - (1 << 32)
				
				## Determing which bias this is and set the value of the correct attribute.
				if   (entry.value == "Bias"):
					self.bias = self.temp
				elif (entry.value == "ActiveTimeBias"):
					self.activetime_bias = self.temp
				elif (entry.value == "DaylightBias"):
					self.daylight_bias = self.temp
				self.temp = ""
				
		elif (entry.type == "REG_BINARY"):
			if ("Start" in self.value):
				self.temp = array.array('h', entry.data)
				self.temp.byteswap()
				self.temp_array = re.findall("....", binascii.hexlify(self.temp))
				self.temp_array[1] = self.moy_dict[str(self.temp_array[1])]
				self.temp_array[7] = self.dow_dict[str(self.temp_array[7])]
		
	## printTimeZoneEntry - Prints the information of interest.
	def printTimeZoneEntry(self):
		print "  Value: "  + entry.value
		print "    Type: " + entry.type
		if (entry.type == "REG_BINARY"):
			print "    Key: Year, Month, Week (1-5), Hour, Minute, Second, Millisecond, Day of week"  
		print "    Data: " + str(self.temp) + "\n"
		
## End of TimeZoneEntry class
