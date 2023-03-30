import cv2

img = cv2.imread("photos/obito.jpg")
img2 = cv2.imread("photos/obito.jpg")

#img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
#img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2LAB)

b, g, r = cv2.split(img)
a = cv2.merge((b,g,r))

cv2.imshow("r",r)
cv2.imshow("g",g)
cv2.imshow("b",b)
cv2.imshow("bgr",a)
cv2.waitKey()