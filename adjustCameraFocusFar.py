import os

os.system('sudo uvcdynctrl -s "Focus, Auto" 0')
 
currentFocusValue = int(os.popen('uvcdynctrl -g "Focus (Absolute)"').read())

if currentFocusValue >= 5:
    newFocusValue = currentFocusValue - 5
else:
    newFocusValue = currentFocusValue

newFocusValueCommand = 'uvcdynctrl -s "Focus (Absolute)" ' +  str(newFocusValue)

os.system(newFocusValueCommand)
