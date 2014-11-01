# james.py
import subprocess

# This will allow for debugging.
bool_debug = 1
# sysinternal_dir = 'I:\Windows Forensics\project\SysinternalsSuite\\'
# sysinternal_dir1 = 'I:\Windows Forensics\project\SysinternalsSuite\\'
# This function returns the output of ipconfig.
def getIpconfig():
	ipconfig = subprocess.check_output('ipconfig /all')
	return ipconfig
	
# This function returns the output of whoami.
def getWhoami():
	whoami = subprocess.check_output('whoami')
	return whoami
	
# This fuction returns the output of PSlist. 	
def getPslist():
	pslist = subprocess.check_output('.\systeminternals\pslist')
	return pslist
	
# This function returns the output of PsLoggedon	
def getPsLoggedon():
	PsLoggedon = subprocess.check_output('.\systeminternals\PsLoggedon')
	return PsLoggedon
	
# This fuction returns the output of TCPcon.
# TCPcon is a command in systeminternals that will show detailed listings 
# of all TCP and UDP endpoints on your system, including the local and remote addresses 
# and state of TCP connections. 

def getTcpvcon():
		Tcpvcon = subprocess.check_output('.\systeminternals\Tcpvcon')
		return Tcpvcon

# This function returns the output of diskext. Diskext command that returns information 
# about what disks the partitions of a volume are located on (multipartition disks can reside on
# multiple disks) and where on the disk the partitions are located.	

def getDiskext():
	diskext = subprocess.check_output('.\systeminternals\diskext')
	return diskext
	
# This if statement allows for debugging of ipconfig & whoami is true. 	
if (bool_debug == 1):	
	print getIpconfig()
	print getWhoami()
	print getPslist()
	print getPsLoggedon()
	print getTcpvcon()
	print getDiskext()
	
	