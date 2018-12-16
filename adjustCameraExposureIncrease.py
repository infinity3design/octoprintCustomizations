import os

os.system('sudo uvcdynctrl -s "Exposure, Auto" 1')
 
currentExposureValue = int(os.popen('uvcdynctrl -g "Exposure (Absolute)"').read())

if currentExposureValue < 240:
    newExposureValue = currentExposureValue + 15
else:
    newExposureValue = currentExposureValue

newExposureValueCommand = 'uvcdynctrl -s "Exposure (Absolute)" ' +  str(newExposureValue)

os.system(newExposureValueCommand)
