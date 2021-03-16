import cv2
import numpy as np

img = cv2.imread('shrink2.png')
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
        
        # 下面A、B两个代码块选一个运行
        
        # A代码将边缘加上原图的颜色显示
        # dst = cv2.bitwise_and(img, img, mask=edge) 
        
        # B代码：将原图加上边缘显示
        gray_to_bgr = cv2.cvtColor(edge, cv2.COLOR_GRAY2BGR);
        gray_to_bgr[:,:,0]=gray_to_bgr[:,:,0]/255*50
        gray_to_bgr[:,:,1]=gray_to_bgr[:,:,1]/255*205
        gray_to_bgr[:,:,2]=gray_to_bgr[:,:,2]/255*50
        dst = cv2.add(img, gray_to_bgr)
        
        cv2.imshow('canny demo', dst)
        if cv2.waitKey(1) in [113,27]: # 按键盘上的q或esc退出
            break
except:
    print('循环出了问题')

cv2.destroyAllWindows()
