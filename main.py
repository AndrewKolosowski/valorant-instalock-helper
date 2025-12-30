import pyautogui
import keyboard
import time

# Safety: move mouse to top-left corner to abort
pyautogui.FAILSAFE = True  # keep enabled for safety

# Get screen size
screen_width, screen_height = pyautogui.size()

# Percent-based positions
# first_x, first_y = int(screen_width * 0.15), int(screen_height * 0.59) #giovanne
# first_x, first_y = int(screen_width * 0.15), int(screen_height * 0.69) #reyna
first_x, first_y = int(screen_width * 0.05), int(screen_height * 0.69) #phoenix


second_x, second_y = int(screen_width * 0.50), int(screen_height * 0.70)

print(f"Click positions:")
print(f"  First: ({first_x}, {first_y})")
print(f"  Second: ({second_x}, {second_y})")
print("Press F8 to toggle clicking ON/OFF")

clicking = False

def toggle():
    global clicking
    clicking = not clicking
    print("CLICKING ON" if clicking else "CLICKING OFF")

keyboard.add_hotkey("F8", toggle)

while True:
    if clicking:
        pyautogui.moveTo(first_x, first_y, duration=0)  # instant movement
        time.sleep(0.15)  # wait 

        # Second click
        pyautogui.moveTo(second_x, second_y, duration=0)  # instant movement
        time.sleep(0.15)  # wait
    else:
        time.sleep(0.05)
