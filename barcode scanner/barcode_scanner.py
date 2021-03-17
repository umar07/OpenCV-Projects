import cv2 as cv
import numpy as np
from pyzbar.pyzbar import decode

#img=cv.imread('/home/umar/ML-AI/barcode scanner/qrcode2.jpg')
cap=cv.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)

#height, width = img.shape[:2]
#code=decode((img[:, :, 0].astype('uint8').tobytes(), width, height))

#code=decode(img)
#print(code)

while True:

    success,img=cap.read()
    #code=decode(img)
    if(not success):
        break

    for barcode in decode(img):
            
        # (x, y, w, h) = barcode.rect
        # cv.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 5)
        pts=np.array([barcode.polygon],np.int32)
        pts=pts.reshape((-1,1,2))
        cv.polylines(img,[pts],True,(255,0,255),5)
        pts2=barcode.rect
        #print(barcode.data) #in byte form
        data=barcode.data.decode('utf-8') #in string form
        print(data)
        # print(barcode.type)
        font = cv.FONT_HERSHEY_SIMPLEX
        cv.putText(img,data,(pts2[0],pts2[1]), font, 1,(255,0,255),2)


    cv.imshow("Image", img)
    cv.waitKey(1)
    if 	cv.waitKey(40)==27:
	    break

cv.destroyAllWindows()
cap.release()