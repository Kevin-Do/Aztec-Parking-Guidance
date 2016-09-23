import cv2
import numpy as np

cap = cv2.VideoCapture('parkinglot1.mp4',0)
reduce = cv2.createBackgroundSubtractorMOG2()
#first webcam= 0, video files specified
# Setup SimpleBlobDetector parameters.
params = cv2.SimpleBlobDetector_Params()

# Change thresholds
params.minThreshold = 10;
params.maxThreshold = 200;

# Filter by Area.
params.filterByArea = True
params.minArea = 900

# Filter by Circularity
params.filterByCircularity = True
params.minCircularity = 0.1

# Filter by Convexity
params.filterByConvexity = True
params.minConvexity = 0.87

# Filter by Inertia
params.filterByInertia = True
params.minInertiaRatio = 0.01

# Create a detector with the parameters
ver = (cv2.__version__).split('.')
if int(ver[0]) < 3 :
    detector = cv2.SimpleBlobDetector(params)
else :
    detector = cv2.SimpleBlobDetector_create(params)

detector = cv2.SimpleBlobDetector_create(params)


while(True):
    ret, frame = cap.read()
    backgroundReduce = reduce.apply(frame)
    keypoints = detector.detect(backgroundReduce)

    fg_with_keypoints = cv2.drawKeypoints(backgroundReduce, keypoints, np.array([]), (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

    font = cv2.FONT_HERSHEY_PLAIN
    cv2.putText(fg_with_keypoints, 'Aztec Parking Guidance System', (400, 700), font, 2, (255, 255, 255), 2, cv2.LINE_AA)

    cv2.imshow('nameFrame',fg_with_keypoints)

    if cv2.waitKey(20) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows

