import os
import time

os.system('uvcdynctrl -s "Focus, Auto" 0')
os.system('uvcdynctrl -s "Focus (absolute)" 15')

os.system('uvcdynctrl -s "Exposure, Auto" 3')
time.sleep(3)
os.system('uvcdynctrl -s "Exposure, Auto" 1')

currentExposureValue = int(os.popen('uvcdynctrl -g "Exposure (Absolute)"').read())

baselineExposureValue = currentExposureValue / 3

baselineExposureValueCommand = 'uvcdynctrl -s "Exposure (Absolute)" ' +  str(baselineExposureValue)

os.system(baselineExposureValueCommand)

os.system('uvcdynctrl -s "Saturation" 155')
