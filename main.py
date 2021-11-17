import keyboard
import pyautogui
import time
import pygame


file1 = open('numbers.txt', 'r')
Lines = file1.readlines()



def getline():
    count = 0
    while keyboard.is_pressed('shift + ctrl'):
        for line in Lines:
            count += 1
            time.sleep(1)
     #   pyautogui.write(line)
            print(line.format(count, line.strip()))








while True:
    getline()



