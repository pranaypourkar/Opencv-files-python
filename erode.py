# Author: Pranay 
import cv2
import numpy as np

img = cv2.imread('/home/pranay/Desktop/task1_lm_set2 (1)/set-2/2. Task_Description/test_images/board_2.jpg')

erosion = cv2.erode(img, cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5)),iterations = 1)

cv2.imshow('image',erosion)
cv2.waitKey(0)
cv2.destroyAllWindows()
