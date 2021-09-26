# Ce deuxieme essai a été fait pour comprendre les bases de 
# la reconaissance faciale avec un fichiers xml
import cv2
import numpy as np
import os

face_cascade=cv2.CascadeClassifier("haar.xml")
cap=cv2.VideoCapture(0)
os.remove('save2.avi')
fourcc = cv2.VideoWriter_fourcc(*'XVID')  
out = cv2.VideoWriter('save2.avi',fourcc, 20.0, (640,480))   

while True:
    ret, frame=cap.read()

    gray=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = np.array(gray, dtype='uint8')
    face=face_cascade.detectMultiScale(gray, 1.3, 10)
    for x, y, w, h in face:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
    out.write(frame)
    if cv2.waitKey(1)&0xFF==ord('q'):
        break
    cv2.imshow('video', frame)
cap.release()
cv2.destroyAllWindows()
