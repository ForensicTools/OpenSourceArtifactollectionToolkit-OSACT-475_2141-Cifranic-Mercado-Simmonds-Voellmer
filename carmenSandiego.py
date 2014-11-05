## getTimezones.py
## This script will calculate the time zones in each of the control sets in the registry.

## Imports
import array, binascii, easyReg, re, _winreg

class TimeZoneEntry():
	## __init__                - Initialize the attributes of a registry entry (File).
	## self.moy_dict     	   - A dictionary mapping the months of the year.
	## self.dow_dict   	       - A dictionary mapping the days of the week.
	## self.entry          	   - The registry entry associated with this file.
	## self.activetime_bias    - The active time bias. Bias + DaylightBias
	## self.bias               - The number of minutes added due to timezone.
	## self.daylight_bias  	   - The daylight bias. The number of minutes added due to DST.
	## self.daylight_start	   - Little-Endian hex encoded start date/time of DST.
	## self.standard_start	   - Little-Endian hex encoded end date/time of DST.
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
		
## End of RegTimeZoneEntry class