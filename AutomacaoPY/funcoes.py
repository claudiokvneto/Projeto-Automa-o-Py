
import pyautogui
import time
import keyboard
import pyperclip

def copiar():
    keyboard.press_and_release('ctrl + c')
    time.sleep(0.5)

def colar():
    keyboard.press_and_release('ctrl + v')