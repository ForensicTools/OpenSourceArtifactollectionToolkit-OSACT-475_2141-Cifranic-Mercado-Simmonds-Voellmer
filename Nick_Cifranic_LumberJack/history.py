#!/usr/bin/env python
#checks history 
import os.path # Required to validate files

ieInstalled = os.path.exists(os.path.expandvars("%LOCALAPPDATA%\Microsoft\Windows\History"))

print (ieInstalled)
