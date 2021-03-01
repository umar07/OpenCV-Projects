import cv2 as cv
import numpy as np
import mapper

img=cv.imread('/home/umar/ML-AI/omr-sheet/omr_test_01.png')
img=cv.resize(img,(800,600))
orig=img.copy()

gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
blur=cv.GaussianBlur(gray,(5,5),0)
edge=cv.Canny(blur,30,50) 

contours,_=cv.findContours(edge,cv.RETR_EXTERNAL,cv.CHAIN_APPROX_SIMPLE)
contours=sorted(contours,key=cv.contourArea,reverse=True)

for c in contours:
    arc=cv.arcLength(c,True) #true = closed shape
    approx=cv.approxPolyDP(c,0.02*arc,True)

    if len(approx)==4:
        target=approx
        break

# print(target)
approx=mapper.mapp(target)
pts=np.float32([[0,0],[600,0],[600,600],[0,600]])
transform=cv.getPerspectiveTransform(approx,pts)
dst=cv.warpPerspective(orig,transform,(600,600))

cv.imshow("original",orig)
cv.imshow("Scanned",dst)
cv.waitKey(0) 
cv.destroyAllWindows()