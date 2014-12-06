## easyRegUnitTests.py

## Import easyReg for testing and sys for argv and exit.
import easyReg, sys

## Test keys to initialize RegKey objects.
test_key1 = "HKEY_LOCAL_MACHINE\SYSTEM\ControlSet001\Services\EventLog\Application"
test_key2 = "HKEY_LOCAL_MACHINE\SYSTEM\Select"
test_key3 = "HKEY_LOCAL_MACHINE\SYSTEM"

## A list to be passed to the test function.
test_list = [1, 2, 3]

## A test function which takes a list as a parameter for testing with walkReg.
def test_fn(test_list):
	print "    This is a test function! Mic test..."
	for each in test_list:
		print "    " + str(each) + "..."
	
	print "    This concludes the test function!"
	
## Initialize RegKey Objects
## HKEY_LOCAL_MACHINE\SYSTEM\ControlSet001\Services\EventLog\Application has entries and subkeys.
## HKEY_LOCAL_MACHINE\SYSTEM\Select has entries but no subkeys.
## HKEY_LOCAL_MACHINE\SYSTEM has subkeys but no entries.

print "==TEST 1=="
print "Creating RegKey objects.\n"
test_regkey1 = easyReg.RegKey(test_key1)
test_regkey2 = easyReg.RegKey(test_key2)
test_regkey3 = easyReg.RegKey(test_key3)

## Populate the entries and subkeys of the RegKey objects.
print "\n==TEST 2=="
print "Populating the entries and subkeys of the RegKey objects.\n"
test_regkey1.populateEntries()
test_regkey1.populateSubkeys()

test_regkey2.populateEntries()
test_regkey2.populateSubkeys()

test_regkey3.populateEntries()
test_regkey3.populateSubkeys()

print "\n==TEST 3=="
print "Sorting the list of entries and subkeys of the RegKey objects.\n"
test_regkey1.sortEntries("numeric")
test_regkey1.sortSubkeys("numeric")

test_regkey2.sortEntries("alphabetical")
test_regkey2.sortSubkeys("alphabetical")

test_regkey3.sortEntries("alphabetical")
test_regkey3.sortSubkeys("alphabetical")

print "\n==TEST 4=="
print "Getting summary of test_regkey1 via getRegKey()."
print test_regkey1.getRegKey()

print "\n==TEST 5=="
print "Getting entry tuples of test_regkey1 via getEntries()."
print "This also tests getRegEntry() of the RegEntry class.\n"
for each in test_regkey1.getEntries():
	print "   " + str(each)

print "\n==TEST 6=="
print "Getting subkey tuples of test_regkey1 via getSubkeys.\n"	
for each in test_regkey1.getSubkeys():
	print "    " + str(each)

print "\n==TEST 7=="
print "Removing an RegEntry object from the list within test_regkey2.\n"
test_regkey2.printRegKey()
test_regkey2.removeEntry("Current")
test_regkey2.printRegKey()

print "==TEST 8=="
print "Removing a RegKey object from the list within test_regkey3.\n"
test_regkey3.printRegKey()
test_regkey3.removeSubkey("ControlSet001")
test_regkey3.printRegKey()

print "==TEST 9=="
print "Walking the registry n layers deep from starting RegKey."
print "Must run the function fn in each key.\n"
easyReg.walkReg(test_regkey3, 3, test_fn, test_list)

print "\n==ALL TESTS PASSED=="
