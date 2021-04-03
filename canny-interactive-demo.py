import cv2
import numpy as np

# 载入图片
# img = cv2.imread('images/IMG_20201209_023607.jpg')
img = cv2.imread('crack.png')

w, h = img.shape[0:2]

# 放缩，用于窗口过大或过小时
# Ratio =5
# new_shape = (int(h/Ratio), int(w/Ratio))
# img = cv2.resize(img, new_shape)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# gray = cv2.resize(gray, new_shape)

# 预处理
# gray = cv2.GaussianBlur(gray,(3,3),0)

window_name = 'trackbar demo' # 显示图片窗口的名称
cv2.namedWindow(window_name) # 窗口大小可以改变

cv2.createTrackbar('Min', window_name, 100, 1000, lambda x: None)
cv2.createTrackbar('Max', window_name, 100, 1000, lambda x: None)

try:
    while(True):
        low_thres = cv2.getTrackbarPos('Min',window_name)
        max_thres = cv2.getTrackbarPos('Max',window_name)
        result = cv2.Canny(gray, low_thres, max_thres)
        
        # 下面A、B两个代码块选一个运行
        
        # A代码将边缘加上原图的颜色显示
        # dst = cv2.bitwise_and(img, img, mask=edge) 
        
        # B代码：将原图加上边缘显示
        gray_to_bgr = cv2.cvtColor(result, cv2.COLOR_GRAY2BGR);
        gray_to_bgr[:,:,0]=gray_to_bgr[:,:,0]/255*50
        gray_to_bgr[:,:,1]=gray_to_bgr[:,:,1]/255*205
        gray_to_bgr[:,:,2]=gray_to_bgr[:,:,2]/255*50
        dst = cv2.add(img, gray_to_bgr)
        
        cv2.imshow(window_name, dst)
        if cv2.waitKey(1) in [113,27]: # 按键盘上的q或esc退出
            break
except:
    print('循环出了问题')

cv2.destroyAllWindows()
