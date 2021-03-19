import cv2 as cv
import numpy as np
import pyautogui
import math

def Press(key):
    pyautogui.press(key)
# https://www.onlinepianist.com/virtual-piano

cap=cv.VideoCapture(0)
# cap.set(3,600)
# cap.set(4,800)

def nothing(x):
    pass

# cv.namedWindow('Trackbar')
# cv.createTrackbar("L-H","Trackbar",0,255,nothing)
# cv.createTrackbar("L-S","Trackbar",0,255,nothing)
# cv.createTrackbar("L-V","Trackbar",0,255,nothing)
# cv.createTrackbar("U-H","Trackbar",255,255,nothing)
# cv.createTrackbar("U-S","Trackbar",255,255,nothing)
# cv.createTrackbar("U-V","Trackbar",255,255,nothing)

while True:
    _,frame=cap.read()
    frame=cv.resize(frame,(580,600))
    frame=cv.flip(frame,1)
    frame=cv.GaussianBlur(frame,(5,5),0)
    #frame=cv.cvtColor(frame,cv.COLOR_BGR2RGB)

    hsv=cv.cvtColor(frame,cv.COLOR_BGR2HSV)
    # l_h=cv.getTrackbarPos("L-H", "Trackbar")
    # l_s=cv.getTrackbarPos("L-S", "Trackbar")
    # l_v=cv.getTrackbarPos("L-V", "Trackbar")
    # u_h=cv.getTrackbarPos("U-H", "Trackbar")
    # u_s=cv.getTrackbarPos("U-S", "Trackbar")
    # u_v=cv.getTrackbarPos("U-V", "Trackbar")
    
    # lower_black=np.array([l_h,l_s,l_v]) # get proper values from experimenting with trackbar.
    # upper_black=np.array([u_h,u_s,u_v]) 

    lower_black=np.array([0,0,0]) # get the proper values from experimenting with trackbar.
    upper_black=np.array([255,255,50])
    mask=cv.inRange(hsv, lower_black, upper_black)

    cv.rectangle(frame, (5,0), (40,250), (255,255,255),1)
    cv.rectangle(frame, (43,0), (75,250), (255,255,255),1)
    cv.rectangle(frame, (78,0), (105,250), (255,255,255),1)
    cv.rectangle(frame, (108,0), (140,250), (255,255,255),1)
    cv.rectangle(frame, (143,0), (175,250), (255,255,255),1)
    cv.rectangle(frame, (178,0), (205,250), (255,255,255),1)
    cv.rectangle(frame, (208,0), (240,250), (255,255,255),1)
    cv.rectangle(frame, (243,0), (275,250), (255,255,255),1)
    cv.rectangle(frame, (278,0), (305,250), (255,255,255),1)
    cv.rectangle(frame, (308,0), (340,250), (255,255,255),1)
    cv.rectangle(frame, (343,0), (375,250), (255,255,255),1)
    cv.rectangle(frame, (378,0), (405,250), (255,255,255),1)
    cv.rectangle(frame, (408,0), (440,250), (255,255,255),1)
    cv.rectangle(frame, (443,0), (475,250), (255,255,255),1)
    cv.rectangle(frame, (478,0), (505,250), (255,255,255),1)
    cv.rectangle(frame, (508,0), (540,250), (255,255,255),1)
    cv.rectangle(frame, (543,0), (575,250), (255,255,255),1)




    contours,_=cv.findContours(mask,cv.RETR_EXTERNAL,cv.CHAIN_APPROX_NONE)
   
        
    for contour in contours:   
        if cv.contourArea(contour)>14000 and cv.contourArea(contour)<26000:
            # print(cv.contourArea(contour))
            cv.drawContours(frame, contour,-1,(0,0,255),3)

            hull = cv.convexHull(contour,returnPoints = False)
            defects = cv.convexityDefects(contour,hull)

            for i in range(defects.shape[0]):
                s,e,f,d = defects[i,0]
                start = tuple(contour[s][0])
                end = tuple(contour[e][0])
                far = tuple(contour[f][0])
                x,y,p,q=start[0],start[1],far[0],far[1]
                dist = math.sqrt((x - p)**2 + (y - q)**2)
                
                # cv.line(frame,start,end,[0,255,0],2) draws the convex hull polygon.
                if (dist>=50):
                    cv.circle(frame,start,5,[20,240,255],-1) # draws the finger tips.

                if p > 5 and q > 0 and p < 40 and q < 250:
                    Press('Q') 
                    break      
                if p > 43 and q > 0  and p < 75 and q < 250:
                    Press('W') 
                    break      
                if p > 78 and q > 0 and p < 105 and q < 250:
                    Press('E') 
                    break      
                if p > 108 and q > 0 and p < 140 and q < 250:
                    Press('R') 
                    break      
                if p > 143 and q > 0 and p < 175 and q < 250:
                    Press('T') 
                    break      
                if p > 178 and q > 0 and p < 205 and q < 250:
                    Press('Y') 
                    break      
                if p > 208 and q > 0 and p < 240 and q < 250:
                    Press('U')  
                    break      
                if p > 243 and q > 0 and p < 275 and q < 250:
                    Press('I')
                    break      
                if p > 278 and q > 0 and p < 305 and q < 250:
                    Press('O') 
                    break      
                if p > 308 and q > 0 and p < 340 and q < 250:
                    Press('P') 
                    break      
                if p > 343 and q > 0 and p < 375 and q < 250:
                    Press('Z') 
                    break      
                if p > 378 and q > 0 and p < 405 and q < 250:
                    Press('X')
                    break 
                if p > 408 and q > 0 and p < 440 and q < 250:
                    Press('C')
                    break 
                if p > 443 and q > 0 and p < 475 and q < 250:
                    Press('V')
                    break 
                if p > 478 and q > 0 and p < 505 and q < 250:
                    Press('B')
                    break 
                if p > 508 and q > 0 and p < 540 and q < 250:
                    Press('N')
                    break
                if p > 543 and q > 0 and p < 575 and q < 250:
                    Press('M')
                    break      

    cv.imshow('frame',frame)
    # cv.imshow('mask',mask)

    key=cv.waitKey(1)
    if key==27:
        break;

cap.release()
cv.destroyAllWindows()