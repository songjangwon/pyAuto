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


#  전체플레이 220 70

# pyautogui.screenshot('게임시작.png', region = (1500, 160 , 60,60))


i = pyautogui.locateOnScreen('closeButton.png', confidence=0.9)
pyautogui.moveTo(i)



# pyautogui.click(i)