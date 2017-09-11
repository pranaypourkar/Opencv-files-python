# Author: Pranay 
import numpy as np
import cv2
cap = cv2.VideoCapture(0)
while(True):
 ret, frame = cap.read()
 cv2.imshow('frame',frame)
 if cv2.waitKey(3)==27 :
  break

cv2.imwrite('/home/pranay/abc.jpg',frame)

