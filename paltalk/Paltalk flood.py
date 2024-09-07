import pyautogui
import keyboard
import time
import pygetwindow as pw
import math

toggle = "`"
rd = 0  # Variable rd
count = 0  # Counter for number of msg sent
delay_toggle = 0.1  # Delay for Toggle
delay_enter = 0.1
1  # Delay to press Enter
flag = False  # Used for Toggling on and off
increasing = True  # Used for the variable rd
title = "Paltalk"  # Title of window we want to attack

print(pw.getAllTitles())
time.sleep(1)


def get():
    # Checks if the active window's title matches the `title` variable
    active = pw.getActiveWindowTitle()
    return active == title


# ask = pyautogui.prompt(
#     text="What do you want to send? ", title="Paltalk Flooder", default=""
# )


ask = 0
if ask is None:
    ask = "<3"

freq = 3

last_toggle_time = 0  # Variable used for debouncing

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
            mul = rd * count
            if increasing:
                rd += 1
                if rd >= 15:
                    increasing = False
            else:
                rd -= 1
                if rd <= 1:
                    increasing = True

            sin_val = (math.sin(count * freq) + 1) / 2
            spaces = int(sin_val * 50)
            message = f"‎ " * spaces + str(f"<3 Thank you <3")
            m = mul
            count += 0.1

            keyboard.write(message)
            time.sleep(delay_enter)
            keyboard.press_and_release("enter")
    else:
        print("Not active")
        if flag:
            flag = not flag
        time.sleep(1)
