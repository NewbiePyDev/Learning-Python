import pyautogui
import time
import keyboard
import pygetwindow
import cv2
import autoit

pyautogui.FAILSAFE = False
# pyautogui.mouseInfo()

x, y, w, h = (1196, 1304, 493, 65)
template = cv2.imread("image copy.png")
template = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)
# print()


def get():
    pal = pygetwindow.getActiveWindowTitle()
    if pal in ["Paltalk", "PALTALK CALL"]:
        return True


# call btn 4354,115
# cancel call btn 3575,720
count = 0
toggle = "`"
last_toggle_time = 0
delay_toggle = 0.1
flag = False
while not keyboard.is_pressed("q"):
    if get():

        if keyboard.is_pressed(toggle):
            current_time = time.time()
            if current_time - last_toggle_time > delay_toggle:
                flag = not flag
                last_toggle_time = current_time
                time.sleep(delay_toggle)
                pyautogui.alert(
                    text="Toggled On" if flag else "Toggled Off", title="Toggle Mode"
                )
        if flag:
            start = time.time()
            pyautogui.screenshot("ss.png", region=(x, y, w, h))
            screenshot = cv2.imread("ss.png", cv2.IMREAD_GRAYSCALE)
            result = cv2.matchTemplate(screenshot, template, cv2.TM_CCOEFF_NORMED)

            _, max_val, _, _ = cv2.minMaxLoc(result)
            print(max_val)

            if max_val >= 0.8:
                autoit.mouse_move(275, 236, speed=0)
                autoit.mouse_click("left", 275, 236, speed=0)
                close_time = time.time()
                end_t = print(f"Time to close tab: {close_time} - {start}")
                print("Closed Tab!")
            else:
                # print("Not seen")
                autoit.mouse_move(2386, 81, speed=0)  # call btn
                autoit.mouse_click("left", 2386, 81, speed=0)
                if pyautogui.pixelMatchesColor(1347, 951, (235, 87, 87), tolerance=30):
                    # time.sleep(0.0001)
                    autoit.mouse_move(1347, 951, speed=0)
                    autoit.mouse_click("left", 1347, 951, speed=0)
                    count += 1
                    keyboard.write(f"<3 {count} :)")
                    keyboard.press_and_release("enter")

                #     autoit.mouse_move(2778, 241)
                # autoit.mouse_click("left", 158, 245)
                else:
                    time.sleep(0.000001)

    else:
        print("Not in window")
        time.sleep(0.254)
#
# 3577,715
