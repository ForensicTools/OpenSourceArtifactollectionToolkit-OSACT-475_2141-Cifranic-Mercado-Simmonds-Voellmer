## easyRegUnitTests.py

## Import easyReg for testing and sys for argv and exit.
import easyReg, sys

## Test keys to initialize RegKey objects.
test_key1 = "HKEY_LOCAL_MACHINE\SYSTEM\ControlSet001\Services\EventLog\Application"
test_key2 = "HKEY_LOCAL_MACHINE\SYSTEM\Select"
test_key3 = "HKEY_LOCAL_MACHINE\SYSTEM"

## A test function which takes a list as a parameter for testing with walkReg.
test_list = [1, 2, 3]
def test_fn(test_list):
	print "derp"

## Initialize RegKey Objects
## HKEY_LOCAL_MACHINE\SYSTEM\ControlSet001\Services\EventLog\Application has entries and subkeys.
## HKEY_LOCAL_MACHINE\SYSTEM\Select has entries but no subkeys.
## HKEY_LOCAL_MACHINE\SYSTEM has subkeys but no entries.
test_regkey1 = easyReg.RegKey(test_key1)
test_regkey2 = easyReg.RegKey(test_key2)
test_regkey3 = easyReg.RegKey(test_key3)

## Populate the entries and subkeys of the RegKey objects.
test_regkey1.populateEntries()
test_regkey1.populateSubkeys()

test_regkey2.populateEntries()
test_regkey2.populateSubkeys()

test_regkey3.populateEntries()
test_regkey3.populateSubkeys()


sys.exit()
test_regkey2.printRegKey()
test_regkey2.removeEntry("Current")
test_regkey2.printRegKey()

test_regkey3.printRegKey()
test_regkey3.removeSubkey("ControlSet001")
test_regkey3.printRegKey()