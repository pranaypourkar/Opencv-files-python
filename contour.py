# Author: Pranay 

import cv2
import numpy as np


img = cv2.imread('/home/pranay/Desktop/task1_lm_set2 (1)/set-2/2. Task_Description/test_images/board_2.jpg')

lower_blue = np.array([110,50,50])
upper_blue = np.array([130,255,255])
hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
img2 = cv2.inRange(img,lower_blue, upper_blue )

# find contours in the thresholded image
contours = cv2.findContours(img2.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)[0]
cnt = contours[0]
#cv2.drawContours(img, [cnt], 0, (0,255,0), 3)

#Contour Perimeter
#perimeter = cv2.arcLength(cnt,True)
#Contour Approximation

approx = cv2.approxPolyDP(cnt,0.1*cv2.arcLength(cnt,True),True)
print approx
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

