# ForensicsViewer.py

import subprocess

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
	
# This function returns the output of PSlist. 
	
def getPslist():
	pslist = subprocess.check_output('..\systeminternals\pslist')
	return pslist
	
# This function returns the output of PsLoggedon	

def getPsLoggedon():
	PsLoggedon = subprocess.check_output('..\systeminternals\PsLoggedon')
	return PsLoggedon

# This function returns the output of TCPcon.
# TCPcon is a command in systeminternals that will show detailed listings 
# of all TCP and UDP endpoints on your system, including the local and remote addresses 
# and state of TCP connections. 

def getTcpvcon():
	Tcpvcon = subprocess.check_output('..\systeminternals\Tcpvcon')
	return Tcpvcon

# This function returns the output of diskext. Diskext command that returns information 
# about what disks the partitions of a volume are located on (multipartition disks can reside on
# multiple disks) and where on the disk the partitions are located.	

def getDiskext():
	diskext = subprocess.check_output('..\systeminternals\diskext')
	return diskext

# S.M.A.R.T. Tools for Command Line
# This program will give you a list of IDE/ATA/SCSI drives. 
# /dev/sd* and /dev/hd* will be actual hard drives, CD/DVD drives, tape drives,
# or RAID volumes; it won’t give useful info for anything but hard drives.
# Usually a single hard drive will be “/dev/sda”.

def getSmartctl():
	smartctl = subprocess.check_output('..\systeminternals\smart\smartctl --scan')
	return smartctl
	
# MoonSols Windows Memory "DumpIt" 	This utility is used to generate a physical memory dump
# of Windows machines. It works with both 
# x86 (32-bits) and x64 (64-bits) machines.
# The raw memory dump is generated in the current directory, only a confirmation question is prompted before starting.
# Perfect to deploy the executable on USB keys, for quick incident responses needs.
# This program will create a dump file that is the same size as your installed RAM. 
	
def getDump():
	dump = subprocess.check_output('..\systeminternals\dump\DumpIt')
	return dump
