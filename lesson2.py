import cv2
import numpy as np

img = cv2.imread(r'photos/obito.jpg')
#img = cv2.resize(img, (600, 600))
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

img = cv2.Canny(img,200,200)  # контуры

kernel = np.ones((5,5), np.uint8)
img = cv2.dilate(img, kernel, iterations=1)  # Расширение контура

img = cv2.erode(img, kernel, iterations=1)  # Сжатиие контура

img2 = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)  # Сжатиие + Расширение (удаляет шум снаружи)
img3 = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)  # Расширение + Сжатиие (удаляет шум внутри)

cv2.imshow("res",img)
cv2.waitKey()
