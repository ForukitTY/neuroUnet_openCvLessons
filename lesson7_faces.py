import cv2
import numpy as np

img = cv2.imread("photos/kennedy.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces = cv2.CascadeClassifier("faces.xml")


res = faces.detectMultiScale(gray,2.2,2)

for (x, y, w, h) in res:
    cv2.rectangle(img, (x,y), (x+w, y+h), (0,0,255), 3)

cv2.imshow("",img)
cv2.waitKey()
