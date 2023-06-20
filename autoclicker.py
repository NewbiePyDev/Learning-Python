import autoit
import keyboard
import time
toggle_key = 'q'
active = False
"""
This works in roblox.
"""
def toggle(): 
    global active
    active = not active

def main():
    if keyboard.is_pressed(toggle_key):
        toggle()
        time.sleep(0.25)
        
    while active:
        if keyboard.is_pressed(toggle_key):
            toggle()
            time.sleep(0.25)
            break
        else:
            autoit.mouse_click('left', speed=5)
            time.sleep(0.05)

while True:
    main()
