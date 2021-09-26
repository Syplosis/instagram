# pour finir, je me suis rendu comtpe que c'etait compliqué de controler 
# instagram avec un reconnaisance des mains, car il n'existe aucun 
# fichiers cascade sur les mains et il aurait fallut que j'en créé un. 
# Je n'ai pas réussi a en créer un donc j'ai fait le système avec des couleurs.
from selenium.webdriver.common.by import By
import win32api
from win32api import *
import selenium.webdriver as webdriver
import time
import win32con
import cv2
import numpy

cap=cv2.VideoCapture(0)
driver = webdriver.Chrome("chromedriver.exe")
driver.get("https://instagram.com")
win32api.SetCursorPos((500,480))


while True:
    ret, frame=cap.read()
    myimg = frame# Là tu remplaces par l'utilisation de la webcam
    avg_color_per_row = numpy.average(myimg, axis=0)
    avg_color = numpy.average(avg_color_per_row, axis=0)
    if avg_color[0] > 170 and avg_color[2] < 110:
        win32api.mouse_event(win32con.MOUSEEVENTF_WHEEL, 500, 480, -40, 0) 
    elif avg_color[2] > 190 and avg_color[0] < 165:
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,500,480,0,0)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,500,480,0,0)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,500,480,0,0)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,500,480,0,0)
    elif avg_color[0] < 120 and avg_color[1] > 170 and avg_color[2] > 160:
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,500,480,0,0)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,500,480,0,0)
    if cv2.waitKey(1)==ord('q'):
        break
    cv2.imshow('video', frame)
cap.release()
cv2.destroyAllWindows()

def scroll(max):
    i = 1
    win32api.SetCursorPos((500,480))
    while i < max:
        win32api.mouse_event(win32con.MOUSEEVENTF_WHEEL, 500, 480, -1, 0)
        time.sleep(5)
        i = i + 1

