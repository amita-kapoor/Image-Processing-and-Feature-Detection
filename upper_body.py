import numpy as np
import cv2

img = cv2.imread('rr.jpg',0)

lowerBody_cascade = cv2.CascadeClassifier('haarcascade_upperbody.xml')

arrLowerBody = lowerBody_cascade.detectMultiScale(img)
if arrLowerBody != ():
        for (x,y,w,h) in arrLowerBody:
            cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)


cv2.imshow('rr',img)
cv2.waitKey(0)
cv2.destroyAllWindows()