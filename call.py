import pyautogui
from time import sleep
import keyboard
import pygetwindow


pyautogui.FAILSAFE = False


def get():
    pal = pygetwindow.getActiveWindowTitle()
    if pal in ['Paltalk', 'PALTALK CALL']:
        return True


toggle = False

while not keyboard.is_pressed('q'):
    if get():
        pyautogui.click(1796, 57)
        if pyautogui.pixelMatchesColor(891, 715, (235, 87, 87)):
            sleep(0.005)
            pyautogui.click(962, 701)
        pyautogui.click(152, 360, interval=0.01)

    else:
        print('Not in window')
        sleep(1)
# CF2F2F
