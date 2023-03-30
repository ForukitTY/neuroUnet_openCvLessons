import cv2
import numpy as np

mx = np.zeros((600,900,3), dtype='uint8')

color = 255,0,0

mx[:] = 150,30,100

cv2.rectangle(mx, (int(mx.shape[0]*0.3), int(mx.shape[1]*0.3)), (mx.shape[0] - mx.shape[0]//3, mx.shape[1] - mx.shape[1]//3), color, thickness=5)

cv2.imshow("",mx)
cv2.waitKey()