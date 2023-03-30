import cv2
import numpy as np
vid = cv2.VideoCapture(r'videos/F1.mp4')

im2 = cv2.imread('photos/obito.jpg')

def rotate(img_param, angle):
    h, w = img_param.shape[:2]
    point = (w//2, h//2)
    mat = cv2.getRotationMatrix2D(point, angle, 1)
    return cv2.warpAffine(img_param, mat, (w, h))

def transform(img_param, x, y):
    mat = np.float32([[1,0,x],[0,1,y]])
    return cv2.warpAffine(img_param, mat, (img_param.shape[1],img_param.shape[0]))

def contours(img_param):
    img_param = cv2.cvtColor(img_param, cv2.COLOR_BGR2GRAY)  # переход из цветного в серое
    img_param = cv2.GaussianBlur(img_param, (5, 5), 0)  # размытие
    img_param = cv2.Canny(img_param, 70, 80)   # переход из серого в ЧБ
    con, hir = cv2.findContours(img_param, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

    return con

#im2 = rotate(im2,20)
#im2 = transform(im2, 500,500)

new_im = np.zeros(im2.shape, dtype="uint8")
con = contours(im2)
cv2.drawContours(new_im, con, -1, color=(255, 0, 255), thickness=1)  # создал свою матритицу и на нее нанес контуры с картинки
cv2.imshow("",new_im)
cv2.waitKey()

while False:
    success, img = vid.read()

    img = cv2.resize(img, (900, 600))
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


    img = cv2.Canny(img, 200, 200)  # контуры
    #
    kernel = np.ones((5, 5), np.uint8)
    # img = cv2.dilate(img, kernel, iterations=1)  # Расширение контура
    #
    # img = cv2.erode(img, kernel, iterations=1)  # Сжатиие контура
    #
    img2 = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)  # Сжатиие + Расширение (удаляет шум снаружи)
    # img3 = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)  # Расширение + Сжатиие (удаляет шум внутри)

    img = cv2.flip(img, 1)

    cv2.imshow("res",img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

