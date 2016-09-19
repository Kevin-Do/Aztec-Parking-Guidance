import cv2
import numpy as np

cap = cv2.VideoCapture(0)
#first webcam

while(True):
       ret, frame = cap.read()
       grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
       cv2.imshow('nameFrame',frame)
       cv2.imshow('grey', grey)

       if cv2.waitKey(0) & 0xFF == ord('q'):
           break
cap.release()
cv2.destroyAllWindows

