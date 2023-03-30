import cv2
import numpy as np
import imutils
import easyocr
from matplotlib import pyplot as pl

img = cv2.imread('photos/audi.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

img_filter = cv2.bilateralFilter(gray, 11, 15, 15)
edges = cv2.Canny(img_filter,30, 200)

cont = cv2.findContours(edges.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cont = imutils.grab_contours(cont)
cont = sorted(cont, key=cv2.contourArea, reverse=True)[:8]

pos = None
for c in cont:
    approx = cv2.approxPolyDP(c, 14, True)
    if len(approx) == 4:
        pos = approx
        break

mask = np.zeros(gray.shape, np.uint8)
#pl.imshow(cv2.cvtColor(mask, cv2.COLOR_BGR2RGB))  # черная маска
cv2.drawContours(mask, [pos], -1, 255, thickness=-1)  # создал свою матритицу и на нее нанес контуры с картинки
#pl.imshow(cv2.cvtColor(mask, cv2.COLOR_BGR2RGB))  # маска с белым прямогульником
bitw_img = cv2.bitwise_and(img, img, mask=mask)   # применил маску к каринке. Номер на черном фоне

y,x = np.where(mask==255)   # нашел координаты номера на черном фоне
x1, y1 = np.min(x), np.min(y)  # верхнюю левую
x2, y2 = np.max(x), np.max(y)  # правую нижнюю
crop = gray[y1:y2, x1:x2]
#pl.imshow(cv2.cvtColor(crop, cv2.COLOR_BGR2RGB))

text = easyocr.Reader(['en'])
text = text.readtext(crop)
txt = text[0][-2].upper()
#print(txt)

imgFinal=cv2.rectangle(img,(x1,y1),(x2,y2), (0,255,0),4)
final_image=cv2.putText(img,txt,(x2+10,y1-10),cv2.FONT_HERSHEY_PLAIN,3,(0,0,0),20)
final_image=cv2.putText(img,txt,(x2+10,y1-10),cv2.FONT_HERSHEY_PLAIN,3,(0,0,255),4)

pl.imshow(cv2.cvtColor(final_image, cv2.COLOR_BGR2RGB))
#pl.imshow(cv2.cvtColor(bitw_img, cv2.COLOR_BGR2RGB))
pl.show()