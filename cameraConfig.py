import os
import time

os.system('sudo uvcdynctrl -s "Focus, Auto" 0')
os.system('sudo uvcdynctrl -s "Focus (absolute)" 15')

os.system('sudo uvcdynctrl -s "Exposure, Auto" 3')
time.sleep(3)
os.system('sudo uvcdynctrl -s "Exposure, Auto" 1')

currentExposureValue = int(os.popen('uvcdynctrl -g "Exposure (Absolute)"').read())

baselineExposureValue = currentExposureValue / 3

baselineExposureValueCommand = 'uvcdynctrl -s "Exposure (Absolute)" ' +  str(baselineExposureValue)

os.system(baselineExposureValueCommand)

os.system('sudo uvcdynctrl -s "Saturation" 155')
