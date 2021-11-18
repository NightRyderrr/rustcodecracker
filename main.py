import keyboard
import pyautogui

#made by NightRyderrr
#NightRyderrr8007 on discord


file1 = open('numbers.txt', 'r')
Lines = file1.readlines()
#                            change if needed
#detects if hotkey is pressed  |
def getinput():               #\/
    if keyboard.is_pressed('shift + ctrl'):
        return True
    

#gets line from numbers.txt and writes them
def getline():
    count = 0
    for line in Lines:
        count += 1
        pyautogui.write(line.format(count, line.strip()))
        print(line.format(count, line.strip()))
        time.sleep(1)
        break

        

#main function
#checks for input
#if input == True , runs getline():
#else: it passes
while True:
    getinput():
    if getinput() == True:
        getline():
    else:
        pass
         



