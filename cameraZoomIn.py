import os
 
currentZoomValue = int(os.popen('uvcdynctrl -g "Zoom, Absolute"').read())

if currentZoomValue <180:
    newZoomValue = currentZoomValue + 20
else:
    newZoomValue = 180

newZoomValueCommand = 'uvcdynctrl -s "Zoom, Absolute" ' +  str(newZoomValue)

os.system(newZoomValueCommand)
