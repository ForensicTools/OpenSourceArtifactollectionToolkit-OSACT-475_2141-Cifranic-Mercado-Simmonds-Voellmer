# ForensicsViewerUnitTests.py
# This prints the results of the commands stated above. 
# This if statement allows for debugging of ipconfig & whoami is true. 	

import ForensicsViewer

otp = open('output.log', 'w+')

otp.write(ForensicsViewer.getIpconfig())
otp.write(ForensicsViewer.getWhoami())
otp.write(ForensicsViewer.getPslist())
otp.write(ForensicsViewer.getPsLoggedon())
otp.write(ForensicsViewer.getTcpvcon())
otp.write(ForensicsViewer.getDiskext())
otp.write(ForensicsViewer.getSmartctl())

otp.flush()
otp.close()
#print ForensicsViewer.getDump()

