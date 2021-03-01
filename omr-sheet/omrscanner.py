import cv2 as cv
import numpy as np
import mapper  # how to import from some other folder?????
import imutils
from sorting_contours import sort_contours

img=cv.imread('/home/umar/ML-AI/OpenCV-Projects/omr-sheet/omr_test_01.png')
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
scan=cv.warpPerspective(orig,transform,(600,600))
original=scan.copy()
res=scan.copy()

# cv.imshow("original",orig)
# cv.imshow("Scanned",scan)

ANSWER_KEY = {0: 1, 1: 4, 2: 0, 3: 3, 4: 1} #corerct answer keys


scangray=cv.cvtColor(scan,cv.COLOR_BGR2GRAY)
_,thresh = cv.threshold(scangray, 0, 255,cv.THRESH_BINARY_INV+cv.THRESH_OTSU)

cnts = cv.findContours(thresh.copy(), cv.RETR_EXTERNAL,cv.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)

# questionCnts = []

# # loop over the contours   ---- this method didnt work.
# for c in cnts:
# 	# compute the bounding box of the contour, then use the
# 	# bounding box to derive the aspect ratio
# 	(x, y, w, h) = cv.boundingRect(c)
# 	ar = w / float(h)
# 	# in order to label the contour as a question, region
# 	# should be sufficiently wide, sufficiently tall, and
# 	# have an aspect ratio approximately equal to 1
# 	if w >= 25 and h >= 25 and ar >= 0.8 and ar <= 1.2:
# 		questionCnts.append(c)

contour_list = [] #list for all the circular answer contours.
for contour in cnts:
    approx = cv.approxPolyDP(contour,0.01*cv.arcLength(contour,True),True)
    area = cv.contourArea(contour)
    if ((len(approx) > 10) & (area > 400) ): #had to adjust parameters by trial and error.  
        contour_list.append(contour)

#print(contour_list)
scanbubble=cv.drawContours(scan,contour_list,-1,(0,0,255),3)
#cv.imshow('bubble',scanbubble)

# sort the question contours top-to-bottom, then initialize
# the total number of correct answers
contour_list = sort_contours(contour_list,
	method="top-to-bottom")[0]
correct = 0
# each question has 5 possible answers, to loop over the
# question in batches of 5
for (q, i) in enumerate(np.arange(0, len(contour_list), 5)):
	# sort the contours for the current question from
	# left to right, then initialize the index of the
	# bubbled answer
	cnts = sort_contours(contour_list[i:i + 5])[0]
	bubbled = None
	# loop over the sorted contours
	for (j, c) in enumerate(cnts):
		# construct a mask that reveals only the current
		# "bubble" for the question
		mask = np.zeros(thresh.shape, dtype="uint8")
		cv.drawContours(mask, [c], -1, 255, -1)
		# apply the mask to the thresholded image, then
		# count the number of non-zero pixels in the
		# bubble area
		mask = cv.bitwise_and(thresh, thresh, mask=mask)
		total = cv.countNonZero(mask)
		# if the current total has a larger number of total
		# non-zero pixels, then we are examining the currently
		# bubbled-in answer
		if bubbled is None or total > bubbled[0]:
			bubbled = (total, j)
	# initialize the contour color and the index of the
	# *correct* answer
	color = (0, 0, 255)
	k = ANSWER_KEY[q]
	# check to see if the bubbled answer is correct
	if k == bubbled[1]:
		color = (0, 255, 0)
		correct += 1
	# draw the outline of the correct answer on the test
	res=cv.drawContours(res, [cnts[k]], -1, color, 3)

    # grab the test taker
score = (correct / 5.0) * 100
print("[INFO] score: {:.2f}%".format(score))
cv.putText(res, "{:.2f}%".format(score), (10, 30),
	cv.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 2)
cv.imshow("Original", original)
cv.imshow("Exam", res)
cv.waitKey(0)

