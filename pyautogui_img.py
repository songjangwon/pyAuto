import pyautogui


print(pyautogui.position())


# i = pyautogui.locateOnScreen('7.png', confidence=0.8)
# j = pyautogui.locateOnScreen('4.png', confidence=0.8)
#
# q = pyautogui.center(i)
#
# i = pyautogui.locateCenterOnScreen('7.png', confidence=0.8)
#
# pyautogui.click(q)
# pyautogui.click(j)


#pyautogui.screenshot('1.png', region = (1490, 684 , 30,30))


i = pyautogui.locateOnScreen('1.png', confidence=0.8)

pyautogui.click(i)