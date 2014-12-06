import os
import shutil
sourcePath = r'C:\Users\nick\AppData\Roaming\Microsoft\Windows\Cookies\Low'
destPath = r'C:\Users\nick\Desktop\artifacts\Cookies'
for root, dirs, files in os.walk(sourcePath):

    #figure out where we're going
    dest = destPath + root.replace(sourcePath, '')
    
    #if we're in a directory that doesn't exist in the destination folder
    #then create a new folder
    if not os.path.isdir(dest):
        os.mkdir(dest)
        print('Directory created at: ' + dest)

    #loop through all files in the directory
    for f in files:

        #compute current (old) & new file locations
        oldLoc = root + '\\' + f
        newLoc = dest + '\\' + f

        if not os.path.isfile(newLoc):
            try:
                shutil.copy2(oldLoc, newLoc)
                print('File ' + f + ' copied.')
            except IOError:
                print('file "' + f + '" already exists')