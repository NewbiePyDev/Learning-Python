import pyautogui
from time import sleep
import keyboard
import pygetwindow
import cv2

pyautogui.FAILSAFE = False


x, y, w, h = 892, 977, 57, 50
template = cv2.imread('share.png')
template = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)


def get():
    pal = pygetwindow.getActiveWindowTitle()
    if pal in ['Paltalk', 'PALTALK CALL']:
        return True


toggle = False

while not keyboard.is_pressed('q'):
    if get():
        pyautogui.screenshot('ss.png', region=(x, y, w, h))
        screenshot = cv2.imread('ss.png', cv2.IMREAD_GRAYSCALE)
        result = cv2.matchTemplate(
            screenshot,
            template,
            cv2.TM_CCOEFF_NORMED
        )

        _, max_val, _, _ = cv2.minMaxLoc(result)
        print(max_val)

        if max_val >= 0.9:
            pyautogui.click(218, 186)
            sleep(0.05)
            print('Clicked seen')
        else:
            print('Not seen')
            pyautogui.click(1796, 57)
            if pyautogui.pixelMatchesColor(891, 715, (235, 87, 87)):
                sleep(0.005)
                pyautogui.click(962, 701)
            pyautogui.click(152, 360, interval=0.01)

    else:
        print('Not in window')
        sleep(1)
# CF2F2F
