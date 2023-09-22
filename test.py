import pyautogui
import time
Delay = 10
Keys = "The quick brown fox jumps over the lazy dog."
if __name__ == "__main__":
    time.sleep(Delay)
    pyautogui.write(Keys,interval=0.1)