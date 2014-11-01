## easyRegUnitTests.py

import easyReg

#easyReg.easySetValue("weee", "test", "bork", "weeeeee")

test_key1 = "HKEY_LOCAL_MACHINE\SYSTEM\ControlSet001\Services\EventLog\Application"
test_key4 = "HKEY_LOCAL_MACHINE\SYSTEM\ControlSet001\Services\EventLog\Application\test"
test_key2 = "HKEY_CURRENT_USER\Console"
test_key3 = "HKEY_LOCAL_MACHINE\SOFTWARE\FileZilla 3\fzshellext"
test_key4 = "HKEY_LOCAL_MACHINE\SYSTEM\Select"
test_key5 = "HKEY_LOCAL_MACHINE\SYSTEM"
#for each in easyReg.listSubkeys(test_key1):
	#print each

#print ""

#print easyReg.easyQueryKey(test_key1)

#print easyReg.easyQueryValue(test_key1, "File")

def test_fn():
	print "derp"

test_regkey = easyReg.RegKey(test_key4)

test_regkey.populateEntries()

test_regkey.populateSubkeys()

test_regkey.printRegKey(1, 1)

#easyReg.walkReg(easyReg.RegKey("HKEY_LOCAL_MACHINE\SOFTWARE"), 2, test_fn)

#easyReg.easySaveKey(test_key1 + "\\Test", "out.weee")

#easyReg.easyCreateKey(test_key1, "Test")

#easyReg.easyDeleteValue(test_key1, "File")