#!/usr/bin/env python

import os

file_list = next(os.walk(r'C:\Users\nick\AppData\Local\Microsoft\Windows\Temporary Internet Files\Low\Content.IE5'))[1]


for file_list in file_list:        # Second Example
   print ('Sub Directory : ', file_list ) 