import keyboard
import time
import pyautogui

while True:
    if keyboard.is_pressed('r'):
        print('reloading')
        pyautogui.press('1')  
        pyautogui.press('e')  
        pyautogui.press('2') 
        pyautogui.press('e') 
        pyautogui.press('3') 
        pyautogui.press('e') 
        pyautogui.press('4') 
        pyautogui.press('e') 
        pyautogui.press('5')  
        pyautogui.press('e')  
        pyautogui.press('6') 
        pyautogui.press('e')  
        pyautogui.press('7')  
        pyautogui.press('e')  
        pyautogui.press('8')  
        print('Finished')
        time.sleep(.5)
