import cv2
import numpy as np

img = cv2.imread("photos/obito.jpg")
blank = np.zeros(img.shape[:2], dtype='uint8')

circle = cv2.circle(blank.copy(), (560, 140), 80, 255, -1)
square = cv2.rectangle(blank.copy(), (25, 25), (2500, 150), 150, -1)

#img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # для bitwise картинок они должны быть одинакового типа и размера
asd = cv2.bitwise_and(circle,square)
img = cv2.bitwise_and(img,img, mask=asd)

cv2.imshow("cir", circle)
cv2.imshow("rec", square)
cv2.imshow("res", img)
cv2.waitKey()
