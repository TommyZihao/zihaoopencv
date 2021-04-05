# 导入opencv-python
import cv2

# 处理帧函数
clahe = cv2.createCLAHE(clipLimit=0, tileGridSize=(6,6))
def process_frame(img):
    hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    h, s, v = cv2.split(hsv_img)
    v_clahe = clahe.apply(v)
    clahe_hsv_img = cv2.merge((h, s, v_clahe))
    frame = cv2.cvtColor(clahe_hsv_img, cv2.COLOR_HSV2BGR)
    return frame
  
  # 调用摄像头，实时CLAHE直方图变换
# 同济子豪兄 2021-4-5

# 获取摄像头，传入0表示获取系统默认摄像头
cap = cv2.VideoCapture(0)

# 打开cap
cap.open(0)

# 无限循环，直到break被触发
while cap.isOpened():
    # 获取画面
    flag, frame = cap.read()
    if not flag:
        break
    
    ## 处理帧函数
    frame = process_frame(frame)
    
    # 展示处理后的三通道图像
    cv2.imshow('my_window',frame)

    if cv2.waitKey(1) in [113,27]: # 按键盘上的q或esc退出
        break
    
# 关闭摄像头
cap.release()

# 关闭图像窗口
cv2.destroyAllWindows()
