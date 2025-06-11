import pyautogui
import time
import keyboard
import numpy as np
import win32api
import win32con

#time.sleep(1)


def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(np.random.uniform(0.1, 0.3))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

def sariya():
    pyautogui.moveTo(1122, 668, duration=np.random.uniform(0.05, 1))
    pyautogui.mouseDown()
    pyautogui.moveTo(849, 669, duration=np.random.uniform(0.05, 1))
    pyautogui.mouseUp()

def maviye():
    pyautogui.moveTo(849, 669, duration=np.random.uniform(0.05, 1))
    pyautogui.mouseDown()
    pyautogui.moveTo(1122, 669, duration=np.random.uniform(0.05, 1))
    pyautogui.mouseUp()

def sari():
    pyautogui.moveTo(849, 669 , duration=np.random.uniform(0.05, 1))
    pyautogui.mouseDown()
    time.sleep(np.random.uniform(0.01, 0.09))
    pyautogui.mouseUp()

def mavi():
    pyautogui.moveTo(1122, 668 , duration=np.random.uniform(0.05, 1))
    pyautogui.mouseDown()
    time.sleep(np.random.uniform(0.01, 0.09))
    pyautogui.mouseUp()

def repeat():
    pyautogui.moveTo(1221, 724 , duration=np.random.uniform(0.05, 1))
    pyautogui.mouseDown()
    time.sleep(np.random.uniform(0.01, 0.09))
    pyautogui.mouseUp()
    pyautogui.mouseDown()
    time.sleep(np.random.uniform(0.01, 0.09))
    pyautogui.mouseUp()

if pyautogui.pixel(414, 787) == (192, 164, 20):
    prev="s"
elif pyautogui.pixel(414, 787) == (30, 76, 209):
    prev="m"
elif pyautogui.pixel(414, 787) == (19, 122, 55):
    prev="y"
    
son_renk = "m"
son_durum = "m"


while True:
    if keyboard.is_pressed('q'):
        print("Programdan çıkılıyor...")
        break
    


    




  
    if pyautogui.pixelMatchesColor(910, 451, (242, 154, 18), tolerance=10):
        #lastm = pyautogui.pixel(382, 787)
       # lasts = pyautogui.pixel(382, 787)
        #lasty = pyautogui.pixel(382, 787)
        prev = pyautogui.pixel(414, 787)
       # bahis = pyautogui.pixel(910, 451)
        

        time.sleep(np.random.uniform(0.05, 0.15))

        
            

        if pyautogui.pixel(383, 783) == (194, 166, 22):
            son_durum = "s"
            if son_renk=="s":
                    sari()
                    son_renk=son_durum
                    time.sleep(np.random.uniform(5, 8))
            elif son_renk=="m":
                    repeat()
                    sariya()
                    son_renk=son_durum
                    time.sleep(np.random.uniform(5, 8))
            elif son_renk=="y":
                    repeat()
                    son_renk=son_durum
                    time.sleep(np.random.uniform(5, 8))

            
        elif pyautogui.pixel(383, 783) == (31, 77, 212):
            son_durum = "m"
            if son_renk=="m":
                    mavi()
                    son_renk=son_durum
                    time.sleep(np.random.uniform(5, 8))
            elif son_renk=="s":
                    repeat()
                    maviye()
                    son_renk=son_durum
                    time.sleep(np.random.uniform(5, 8))
            elif son_renk=="y":
                    repeat()
                    son_renk=son_durum
                    time.sleep(np.random.uniform(5, 8))


                    
        elif pyautogui.pixel(383, 783) == (19, 124, 55):
            son_durum = "y"
            if son_renk=="s":
                repeat()
                time.sleep(np.random.uniform(5, 8))
            elif son_renk=="m":
                repeat()
                time.sleep(np.random.uniform(5, 8))
            





        
        

