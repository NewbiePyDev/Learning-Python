import keyboard
import time
import cv2
import pyautogui
import pygetwindow as gw
import autoit


threshold = 0.95
def roblox():
    window = gw.getActiveWindowTitle()
    if window == "Roblox":
        return True
    else:
        return False
    
template = cv2.imread('bandage.png')
template = cv2.imread('bandage.png', cv2.COLOR_BGR2GRAY)
count = 0
while not keyboard.is_pressed('q'):
    if roblox():  
        if pyautogui.pixelMatchesColor(1237,838, (223,180,81), tolerance=50):
            count +=1
            print('You died', count, 'time(s).')
            autoit.mouse_click('left',1237,838, speed=5)
    pyautogui.screenshot('ss.png')
    screenshot = cv2.imread('ss.png')
    screenshot = cv2.imread('ss.png', cv2.COLOR_BGR2GRAY)

    result = cv2.matchTemplate(
        templ=template,
        image=screenshot,
        method=cv2.TM_CCOEFF_NORMED
    )
    __, max_val, __, __ = cv2.minMaxLoc(result)
    if roblox() and max_val >= threshold:
        time.sleep(0.25)
        keyboard.press_and_release('3')
        time.sleep(0.25)
        keyboard.press_and_release('2')
        time.sleep(0.25)
        keyboard.press_and_release('1')