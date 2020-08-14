import cv2

a=cv2.VideoCapture("http://v.m.china.com.cn/media/video/20200813/15/0c1c4053cd2afc3854ee5d5f63ce718f.mp4")
for _ in range(int(a.get(cv2.CAP_PROP_FRAME_COUNT))):
    success,img=a.read()
    cv2.imshow("test",img)
    cv2.waitKey(0)