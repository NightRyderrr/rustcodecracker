import keyboard
import pyautogui
import time

# made by NightRyderrr
# NightRyderrr8007 on discord

global count
file1 = open('numbers.txt', 'r')
Lines = file1.readlines()
while True:
    count = input("Type line to start one, if 1 leave blank or type 1")
    if count == "" or " ":
        count = 1
        break
    elif count != 1:
        print("if you input text, close and reopen the script")
        pass






#                            change if needed
# detects if hotkey is pressed  |
def getinput():               # \/
    if keyboard.is_pressed('insert'):
        return True


# gets line from numbers.txt and writes them
def getline(count):
    data = Lines[count]
    pyautogui.write(data)
    print(data)
    time.sleep(1)



# main function
# checks for input
# if input == True , runs getline():
# else: it passes

while True:
    getinput()
    if getinput() == True:
        getline(count)
        count += 1
    else:
        pass