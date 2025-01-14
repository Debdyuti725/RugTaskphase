import cv2 as cv
import numpy as np


videocapture = cv.VideoCapture('Ball_Tracking.mp4')  


while True:
    #reading the frame
    isTrue, frame = videocapture.read()
    if not isTrue:
        break

    
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)#convert to hsv

    #range of the ball
    l = np.array([40, 50, 40])
    u = np.array([90, 255, 255])

    #creating binary image
    mask = cv.inRange(hsv, l, u)

    #finding contours in binary image
    contours,h = cv.findContours(mask, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

    #drawing a cirlce around the ball
    for i in contours:
        
        (x, y), r = cv.minEnclosingCircle(i)#getting center and radius
        c = (int(x), int(y))#centre
        
        r = int(r)#radius
        
       
        if r > 10:  
            cv.circle(frame, c, r, (0, 0, 255), 5)

    #display
    cv.imshow('Ball Tracking', frame)

    
    if cv.waitKey(20) & 0xFF == ord('d'):
        break

cv.destroyAllWindows()