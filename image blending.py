import cv2
import numpy as np

img1 = cv2.imread('aa.jpg')
img2 = cv2.imread('bc.jpg')

import cv2
img = cv2.imread('aa.jpg')
height, width, channels = img.shape
print (height, width, channels)

r = 500.0 / img.shape[1]
dim = (500, int(img.shape[0] * r))
resized = cv2.resize(img, dim, interpolation = cv2.INTER_LINEAR)
#cv2.imshow("resized", resized)
#cv2.waitKey(0)


img1 = cv2.imread('bc.jpg')
height1, width1, channels1 = img1.shape
#print (height1, width1, channels1)

r1 = 500.0 / img1.shape[1]
dim1= (500, int(img1.shape[0] * r1))
resized1 = cv2.resize(img1, dim, interpolation = cv2.INTER_LINEAR)
#cv2.imshow("resized1", resized1)
#cv2.waitKey(0)


dst = cv2.addWeighted(resized,0.8,resized1,0.5,0.5)
cv2.imshow('dst',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
