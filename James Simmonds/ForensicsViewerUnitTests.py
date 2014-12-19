# forensicsViewerUnitTests.py
# This prints the results of the commands stated above. 
# This if statement allows for debugging of ipconfig & whoami is true. 	

import forensicsViewer

otp = open('output.log', 'w+')

otp.write(forensicsViewer.getIpconfig())
otp.write(forensicsViewer.getWhoami())
otp.write(forensicsViewer.getPslist())
otp.write(forensicsViewer.getPsLoggedon())
otp.write(forensicsViewer.getTcpvcon())
otp.write(forensicsViewer.getDiskext())
otp.write(forensicsViewer.getSmartctl())

otp.flush()
otp.close()
#print forensicsViewer.getDump()

