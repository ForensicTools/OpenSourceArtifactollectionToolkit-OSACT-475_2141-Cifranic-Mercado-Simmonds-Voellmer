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

print "==TEST 1==\n"
print "Creating RegKey objects."
test_regkey1 = easyReg.RegKey(test_key1)
test_regkey2 = easyReg.RegKey(test_key2)
test_regkey3 = easyReg.RegKey(test_key3)

## Populate the entries and subkeys of the RegKey objects.
print "\n==TEST 2==\n"
print "Populating the entries and subkeys of the RegKey objects."
test_regkey1.populateEntries()
test_regkey1.populateSubkeys()

test_regkey2.populateEntries()
test_regkey2.populateSubkeys()

test_regkey3.populateEntries()
test_regkey3.populateSubkeys()

print "\n==TEST 3==\n"
print "Getting summary of test_regkey1 via getRegKey()."
print test_regkey1.getRegKey()

print "\n==TEST 4==\n"
print "Getting entry tuples of test_regkey1 via getEntries()."
print "This also tests getRegEntry() of the RegEntry class."
for each in test_regkey1.getEntries():
	print "   " + str(each)

print "\n==TEST 5==\n"
print "Getting subkey tuples of test_regkey1 via getSubkeys."	
for each in test_regkey1.getSubkeys():
	print "    " + str(each)

print "\n==TEST 6==\n"
print "Removing an RegEntry object from the list within test_regkey2."
test_regkey2.printRegKey()
test_regkey2.removeEntry("Current")
test_regkey2.printRegKey()

print "==TEST 7==\n"
print "Removing a RegKey object from the list within test_regkey3."
test_regkey3.printRegKey()
test_regkey3.removeSubkey("ControlSet001")
test_regkey3.printRegKey()

print "==ALL TESTS PASSED=="