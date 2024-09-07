import pyautogui
import time
import keyboard
import pygetwindow
import cv2
import autoit


# pyautogui.mouseInfo()


toggle_key = "`"
last_toggle_time = 0
delay_toggle = 0.1
flag = False
x, y, w, h = 892, 977, 57, 50
template = cv2.imread("share.png")
template = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)


def pal():
    a = pygetwindow.getActiveWindowTitle()
    return a in ["PALTALK CALL", "Paltalk"]


def toggle_flag():
    global flag, last_toggle_time
    flag = not flag
    pyautogui.alert(text="Toggled On" if flag else "Toggled Off", title="Toggle Mode")
    last_toggle_time = time.time()


def btn():
    current_time = time.time()
    if current_time - last_toggle_time > delay_toggle:  # debouncing
        toggle_flag()


def check():
    global last_toggle_time
    current_time = time.time()
    if keyboard.is_pressed(toggle_key):
        if current_time - last_toggle_time > delay_toggle:  # debouncing
            toggle_flag()

    if flag:
        if pal():
            pyautogui.screenshot("ss2.png", region=(x, y, w, h))
            screenshot = cv2.imread("ss2.png", cv2.IMREAD_GRAYSCALE)
            result = cv2.matchTemplate(screenshot, template, cv2.TM_CCOEFF_NORMED)

            _, max_val, _, _ = cv2.minMaxLoc(result)
            print(max_val)

            if max_val >= 0.75:
                autoit.mouse_click("left", 218, 186, speed=0)
                print("Clicked seen")
            else:
                print("Not seen")
                autoit.mouse_click("left", 1796, 57, speed=0)
                if pyautogui.pixelMatchesColor(891, 715, (235, 87, 87)):
                    autoit.mouse_click("left", 962, 701, speed=0)
        else:
            print("Not in window")
    else:
        pass


while True:
    check()
