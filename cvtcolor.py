# Author: Pranay 
#convert the color space
import cv2
import numpy as np

img = cv2.imread('/home/pranay/Desktop/task1_lm_set2 (1)/set-2/2. Task_Description/test_images/board_2.jpg')
hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

cv2.imshow('image',hsv)
cv2.waitKey(0)
cv2.destroyAllWindows()
