# Cet essai consiste a conprendre les bases de opencv en sauvegardant les fichiers
import cv2 as cv
import os
os.remove('save.avi')
fourcc = cv.VideoWriter_fourcc(*'XVID')  
out = cv.VideoWriter('save.avi',fourcc, 20.0, (640,480))  
cap = cv.VideoCapture(0)
while True:
    ret, frame = cap.read()
    gray = cv.cvtColor(frame, cv.COLOR_BGR2BGRA)
    cv.imshow('frame', gray)
    out.write(frame)
    if cv.waitKey(1) == ord('q'):
        break 
cv.destroyAllWindows()