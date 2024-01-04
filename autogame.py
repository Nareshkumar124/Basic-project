import cv2
import pyautogui as pyt 
import numpy
import time
def tree(gray):
    for i in range(360,400):
        for j in range(800,900):
            if gray[i,j]<22:
                return True
    return False

if __name__=="__main__":
    time.sleep(5)
    pyt.press("up")
    while(True):
        shot=pyt.screenshot()
        img=numpy.array(shot)
        gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        if tree(gray):
            pyt.press('up')
