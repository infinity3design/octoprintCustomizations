import os

os.system('sudo uvcdynctrl -s "Focus, Auto" 0')
 
currentFocusValue = int(os.popen('uvcdynctrl -g "Focus (Absolute)"').read())
newFocusValue = currentFocusValue + 5
newFocusValueCommand = 'uvcdynctrl -s "Focus (Absolute)" ' +  str(newFocusValue)

os.system(newFocusValueCommand)
