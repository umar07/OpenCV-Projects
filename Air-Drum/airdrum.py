import cv2 as cv
import numpy as np
import pyautogui

def Press(key):
    pyautogui.press(key)

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
    frame=cv.resize(frame,(600,600))
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
    
    # lower_green=np.array([l_h,l_s,l_v]) # get proper values from experimenting with trackbar.
    # upper_green=np.array([u_h,u_s,u_v]) 

    lower_green=np.array([25,121,86]) # get the proper values from experimenting with trackbar.
    upper_green=np.array([88,255,255])
    mask=cv.inRange(hsv, lower_green, upper_green)

    cv.rectangle(frame, (10,0), (145,150), (255,0,0),1)
    cv.putText(frame,'RIDE',(55,75),cv.FONT_HERSHEY_SIMPLEX,0.8,(0,0,255),2,cv.LINE_AA)
    cv.rectangle(frame, (150,0), (295,150), (0,0,255),1)
    cv.putText(frame,'RIDE BELL',(165,75),cv.FONT_HERSHEY_SIMPLEX,0.8,(255,0,0),2,cv.LINE_AA)
    cv.rectangle(frame, (300,0), (445,150), (255,0,0),1)
    cv.putText(frame,'HITHAT',(335,75),cv.FONT_HERSHEY_SIMPLEX,0.8,(0,0,255),2,cv.LINE_AA)
    cv.putText(frame,'close',(338,92),cv.FONT_HERSHEY_SIMPLEX,0.8,(0,0,255),2,cv.LINE_AA)
    cv.rectangle(frame, (450,0), (595,150), (0,0,255),1)
    cv.putText(frame,'CRASH',(480,75),cv.FONT_HERSHEY_SIMPLEX,0.8,(255,0,0),2,cv.LINE_AA)


    cv.rectangle(frame, (0,155), (50,295), (255,0,0),1)
    cv.putText(frame,'SNARE',(3,235),cv.FONT_HERSHEY_SIMPLEX,0.8,(0,0,255),2,cv.LINE_AA)
    cv.rectangle(frame, (0,300), (50,440), (0,0,255),1)
    cv.putText(frame,'SNARE RIM',(5,370),cv.FONT_HERSHEY_SIMPLEX,0.8,(255,0,0),2,cv.LINE_AA)
    
    cv.rectangle(frame, (550,155), (600,295), (255,0,0),1)
    cv.putText(frame,'HIT HAT',(500,225),cv.FONT_HERSHEY_SIMPLEX,0.8,(0,0,255),2,cv.LINE_AA)
    cv.rectangle(frame, (550,300), (600,440), (0,0,255),1)
    cv.putText(frame,'HIT HAT',(500,370),cv.FONT_HERSHEY_SIMPLEX,0.8,(255,0,0),2,cv.LINE_AA)
    cv.putText(frame,'close',(505,392),cv.FONT_HERSHEY_SIMPLEX,0.8,(255,0,0),2,cv.LINE_AA)


    cv.rectangle(frame, (0,450), (145,600), (255,0,0),1)
    cv.putText(frame,'TOM HI',(35,535),cv.FONT_HERSHEY_SIMPLEX,0.8,(0,0,255),2,cv.LINE_AA)
    cv.rectangle(frame, (150,450), (295,600), (0,0,255),1)
    cv.putText(frame,'TOM MID',(175,535),cv.FONT_HERSHEY_SIMPLEX,0.8,(255,0,0),2,cv.LINE_AA)
    cv.rectangle(frame, (300,450), (445,600), (255,0,0),1)
    cv.putText(frame,'TOM LOW',(325,535),cv.FONT_HERSHEY_SIMPLEX,0.8,(0,0,255),2,cv.LINE_AA)
    cv.rectangle(frame, (450,450), (595,600), (0,0,255),1)
    cv.putText(frame,'KICK',(485,535),cv.FONT_HERSHEY_SIMPLEX,0.8,(255,0,0),2,cv.LINE_AA)

    contours,_=cv.findContours(mask,cv.RETR_TREE,cv.CHAIN_APPROX_NONE)
    for contour in contours:   
        if cv.contourArea(contour)>400:
            cv.drawContours(frame, contour,-1,(0,0,255),3)
            M = cv.moments(contour)
            cx = int(M['m10']/M['m00']) #finding the center using Moments
            cy = int(M['m01']/M['m00'])
            cv.circle(frame, (cx, cy), 7, (255, 255, 255), -1)

            if cx > 10 and cy > 0 and cx < 145 and cy < 150:
                Press('7') #RIDE
                break      
            if cx > 150 and cy > 0  and cx < 295 and cy < 150:
                Press('8') #RIDE BELL
                break      
            if cx > 300 and cy > 0 and cx < 445 and cy < 150:
                Press('6') #HIT HAT CLOSE
                break      
            if cx > 450 and cy > 0 and cx < 595 and cy < 150:
                Press('9') #CRASH
                break      
            
            
            if cx > 0 and cy > 155 and cx < 50 and cy < 295:
                Press('2') #SNARE
                break      
            if cx > 0 and cy > 300 and cx < 50 and cy < 440:
                Press('3') #SNARE RIM
                break      
            if cx > 550 and cy > 155 and cx < 600 and cy < 295:
                Press('4') #HIT HAT 
                break      
            if cx > 550 and cy > 380 and cx < 600 and cy < 440:
                Press('5') #HIT HAT OPEN 
                break      
            
            
            if cx > 0 and cy > 450 and cx < 145 and cy < 600:
                Press('q') #TOM HI
                break      
            if cx > 150 and cy > 450 and cx < 295 and cy < 600:
                Press('w') #TOM MID
                break      
            if cx > 300 and cy > 450 and cx < 445 and cy < 600:
                Press('e') #TOM LOW 
                break      
            if cx > 450 and cy > 450 and cx < 595 and cy < 600:
                Press('1') #HIT HAT OPEN 
                break 

    

    cv.imshow('frame',frame)
    #cv.imshow('mask',mask)

    key=cv.waitKey(1)
    if key==27:
        break;

cap.release()
cv.destroyAllWindows()