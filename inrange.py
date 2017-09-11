# Author: Pranay 
#convert the color space and threshold it
import cv2
import numpy as np

img = cv2.imread('/home/pranay/Desktop/task1_lm_set2 (1)/set-2/2. Task_Description/test_images/board_2.jpg')
lower_blue = np.array([110,50,50])
upper_blue = np.array([130,255,255])
hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
img2 = cv2.inRange(img,lower_blue, upper_blue )

cv2.imshow('image',img2)
cv2.waitKey(0)
cv2.destroyAllWindows()
