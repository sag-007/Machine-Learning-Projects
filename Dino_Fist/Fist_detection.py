import cv2
import pyautogui as mouse

model=cv2.CascadeClassifier('closed_palm.xml')
video=cv2.VideoCapture(0)

while True:
    ret,frames=video.read()
    objects=model.detectMultiScale(frames,1.2,10)
    for x,y,w,h in objects:
        cv2.rectangle(frames,(x,y),(x+h,y+w),7,2)
    cv2.imshow('Video',frames)
    
    if cv2.waitKey(1)&0xFF==ord('q'):
        break
        
video.release()
cv2.destroyAllWindows()