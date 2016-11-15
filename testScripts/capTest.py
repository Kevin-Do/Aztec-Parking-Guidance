import cv2
import numpy as np

cap = cv2.VideoCapture('parkinglot1.mp4',)
#first webcam= 0, video files specified
fgbg = cv2.createBackgroundSubtractorMOG2()

while(True):
       ret, frame = cap.read()
       fgmask = fgbg.apply(frame)

       grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
       font = cv2.FONT_HERSHEY_PLAIN
       cv2.putText(fgmask, 'Aztec Parking Guidance System', (400, 700), font, 2, (255, 255, 255), 2, cv2.LINE_AA)

       cv2.imshow('nameFrame',fgmask)
    #  cv2.imshow('grey', grey)

       if cv2.waitKey(35) & 0xFF == ord('q'):
           break
cap.release()
cv2.destroyAllWindows

