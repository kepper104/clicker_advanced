import keyboard
import pyautogui
from keyboard import add_hotkey

playing = True




def toggle():
    global playing
    if playing == False:
        playing = True
        print('made true')
    else:
        playing = False
        print('made false')

add_hotkey("insert", toggle)

while playing == True:
    pyautogui.press('e')
    pyautogui.PAUSE = 0.3

while playing == False:
    pass