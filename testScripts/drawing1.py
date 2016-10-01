import numpy as np
import cv2

img = cv2.imread('go-car-15.jpg', cv2.IMREAD_COLOR)

font = cv2.FONT_HERSHEY_PLAIN
#FONT_HERSHEY_SIMPLEX


cv2.putText(img,'Aztec Parking Guidance System',(400,650), font, 2,(255,255,255),2,cv2.LINE_AA)

cv2.imshow('text1', img)
cv2.waitKey(0)
cv2.destroyAllWindows