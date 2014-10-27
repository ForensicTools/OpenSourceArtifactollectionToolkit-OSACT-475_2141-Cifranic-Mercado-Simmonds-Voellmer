# james.py
import subprocess

# This will allow for debugging.
bool_debug = 1
sysinternal_dir = 'I:\Windows Forensics\project\SysinternalsSuite\\'
sysinternal_dir1 = 'I:\Windows Forensics\project\SysinternalsSuite\\'
# This function returns the output of ipconfig.
def getIpconfig():
	ipconfig = subprocess.check_output('ipconfig /all')
	return ipconfig
	
# This function returns the output of whoami.
def getWhoami():
	whoami = subprocess.check_output('whoami')
	return whoami
# This fuction returns the output of PSlist	
def getPslist():
	pslist = subprocess.check_output(sysinternal_dir + 'pslist')
	return pslist
# This function returns the output of PsLoggedon	
def getPsLoggedon():
	PsLoggedon = subprocess.check_output(sysinternal_dir1 + 'PsLoggedon')
	return PsLoggedon	
	
# This if statement allows for debugging of ipconfig & whoami is true. 	
if (bool_debug == 1):	
	print getIpconfig()
	print getWhoami()
	print getPslist()
	print getPsLoggedon()
	
	