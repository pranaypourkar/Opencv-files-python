# Author: Pranay 
import cv2
import numpy as np


img = cv2.imread('/home/pranay/Desktop/task1_lm_set2 (1)/set-2/2. Task_Description/test_images/board_2.jpg')
print img.size;#Total number of pixels is accessed by img.size:
print img.shape;# It returns a tuple of number of rows, columns and channels (if image is color):
print img.dtype;#Image datatype is obtained by img.dtype
img = img[0:99,0:99]#to define region of interest in an image
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
