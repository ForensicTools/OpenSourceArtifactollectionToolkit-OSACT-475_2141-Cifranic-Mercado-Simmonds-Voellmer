## carmenSandiegoUnitTest.py
## Author: Daniel "Albinohat" Mercado

## Standard Imports
import sys

## Third-party Imports.
import carmenSandiego, easyReg

## Initialize RegKey objects for testing NetworkProfile and NetworkSignature classes.
## Then populate their lists of subkeys so they can looped through.
## Administrator Account needed to access network profile and signature keys.
network_profile_test_key = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\NetworkList\Profiles"
network_profile_test_regkey = easyReg.RegKey(network_profile_test_key)
network_profile_test_regkey.populateSubkeys()

network_profile_test_regkey.printRegKey()

network_signature_managed_test_key = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\NetworkList\Signatures\Managed"
network_signature_managed_test_regkey = easyReg.RegKey(network_signature_managed_test_key)
network_signature_managed_test_regkey.populateSubkeys()


network_signature_unmanaged_test_key = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\NetworkList\Signatures\Unmanaged"
network_signature_unmanaged_test_regkey = easyReg.RegKey(network_signature_unmanaged_test_key)
network_signature_unmanaged_test_regkey.populateSubkeys()

## Initialize RegKey object for testing TimeZoneProfile class.
## Populate its list of entries to initialize TimeZoneProfile class.
timezone_test_key = "HKEY_LOCAL_MACHINE\SYSTEM\ControlSet001\Control\TimeZoneInformation"
timezone_test_regkey = easyReg.RegKey(timezone_test_key)
timezone_test_regkey.populateEntries()

## Populate lists of keys containing the network profiles and signatures.
for key in network_profile_test_regkey.list_of_subkeys:
	print "hi"
	NetworkProfile.populateNetworkProfiles(key)

for key in network_signature_managed_test_regkey.list_of_subkeys:
	print "bye"
	NetworkSignature.populateManagedNetworks(key)

for key in network_signature_unmanaged_test_regkey.list_of_subkeys:
	print "sigh"
	NetworkSignature.populateUnmanagedNetworks(key)

sys.exit()

## Initialize TimeZoneProfile class instances uses the above regKey objects.
timezone_profile = carmenSandiego.TimeZoneProfile(timezone_test_regkey)

## Print out instances of the carmenSandiego class instances.
timezone_profile.printTimeZoneProfile()
