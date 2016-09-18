import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("go-car-15.jpg",0 )
# greyscale filter OR cv2.0

# IMREAD_COLOR
# IMREAD_UNCHANGED

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows
