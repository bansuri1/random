import pyautogui as pag
import time

# note: browser window should be open somewhere on the left side of the screen
# works for windows 10 where start menu is on the bottom left of the screen

pag.moveTo(5,1079,2)
pag.click()
time.sleep(1)

pag.write('Chrome',0.1)
pag.hotkey('enter')

time.sleep(1) 
pag.moveTo(1674,1053,1)
pag.click()

time.sleep(1)
pag.moveTo(1693,984,2)
pag.click()

time.sleep(2) 
pag.moveTo(725,125,2)
pag.click()

time.sleep(2) 
pag.moveTo(700,700,2)
pag.click()

