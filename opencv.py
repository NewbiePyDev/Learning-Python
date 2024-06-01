import keyboard
from cv2 import minMaxLoc, matchTemplate, TM_CCOEFF_NORMED, COLOR_BGR2GRAY, COLOR_BGRA2RGB, cvtColor, imread, IMREAD_GRAYSCALE
from numpy import frombuffer
import win32gui
import win32con
import win32ui
from time import sleep
from pygetwindow import getActiveWindowTitle
templates = {name: imread(name, IMREAD_GRAYSCALE) for name in ['A.png', 'W.png', 'E.png', 'Q.png', 'S.png', 'D.png']}


def roblox():
     sleep(0.005)
     rb = getActiveWindowTitle()
     if rb == 'Roblox':
          return True
     else:
          return False
     
threshold = 0.99

# capture_screen originally was pyautogui but i gave to gpt to make it take ss faster
def capture_screen():
    hwnd = win32gui.GetDesktopWindow()
    w, h = 1920, 1080
    hwndDC = win32gui.GetWindowDC(hwnd)
    mfcDC = win32ui.CreateDCFromHandle(hwndDC)
    saveDC = mfcDC.CreateCompatibleDC()
    saveBitMap = win32ui.CreateBitmap()
    saveBitMap.CreateCompatibleBitmap(mfcDC, w, h)
    saveDC.SelectObject(saveBitMap)
    result = win32gui.BitBlt(saveDC.GetSafeHdc(), 0, 0, w, h, mfcDC.GetSafeHdc(), 0, 0, win32con.SRCCOPY)
    bmpinfo = saveBitMap.GetInfo()
    bmpstr = saveBitMap.GetBitmapBits(True)
    img = frombuffer(bmpstr, dtype='uint8')
    img.shape = (h, w, 4)
    mfcDC.DeleteDC()
    saveDC.DeleteDC()
    win32gui.ReleaseDC(hwnd, hwndDC)
    win32gui.DeleteObject(saveBitMap.GetHandle())
    return cvtColor(img, COLOR_BGRA2RGB)

toggle = False

while True:
    sleep(0.005)

    if roblox():
        if keyboard.is_pressed('`'):
            toggle = not toggle
            sleep(0.05)
            print('Active' if toggle else "Inactive")

    if toggle and roblox(): 
        screenshot = capture_screen()
        screenshot_gray = cvtColor(screenshot, COLOR_BGR2GRAY)

        for name, template_gray in templates.items():
            result = matchTemplate(screenshot_gray, template_gray, TM_CCOEFF_NORMED)
            min_val, max_val, min_loc, max_loc = minMaxLoc(result)

            if max_val >= threshold:
                print(name.lower()[0])
                keyboard.press_and_release(name.lower()[0])
