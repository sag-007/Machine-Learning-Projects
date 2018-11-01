import cv2
import pyautogui as mouse

model=cv2.CascadeClassifier('closed_palm.xml')
video=cv2.VideoCapture(0)

while True:
    ret,frames=video.read()
    objects=model.detectMultiScale(frames,1.2,10)
    if len(objects):
        mouse.press('space')
    cv2.imshow('Video',frames)
    
    if cv2.waitKey(1)&0xFF==ord('q'):
        break
        
video.release()
cv2.destroyAllWindows()