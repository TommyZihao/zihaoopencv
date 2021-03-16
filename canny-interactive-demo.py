import cv2
import numpy as np

img = cv2.imread('IMG_20201120_010304.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray,(3,3),0)

cv2.namedWindow('canny demo')

cv2.createTrackbar('Min','canny demo',100, 1000, lambda x: None)
cv2.createTrackbar('Max','canny demo',100, 1000, lambda x: None)

try:
    while(True):
        low_thres = cv2.getTrackbarPos('Min','canny demo')
        max_thres = cv2.getTrackbarPos('Max','canny demo')
        edge = cv2.Canny(blur, low_thres, max_thres)
        dst = cv2.bitwise_and(img, img, mask=edge) # 将边缘加上原图的颜色显示
        cv2.imshow('canny demo', dst)
        if cv2.waitKey(1) == 27:
            break
except:
    print('循环出了问题')

cv2.destroyAllWindows()
