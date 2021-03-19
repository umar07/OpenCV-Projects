# Air Piano


Air Piano is a computer vision based project that allows you to play a virtual piano through hand-gesture.

* First, the hand is detected using the the black color mask we created using the HSV scale. For this purpose, I chose to wear a pair of black gloves because detecting the skin color was comparitively tougher and would have deprived the project from generalisation.

* After the hand is detected, we draw a convex hull, to find the surrounding convex polygon. From this polygon we extract the finger-tips using the convexity defects function. The convexity defect function returns three points out of which our interest is only in the first set of points.(Read more through the links)
There is also a filter applied to get just the fingertips using the distance between the points, while you may also chose to use the angle between the fingers to achieve the same.

* The last part includes the PyAutoGUI library which allows you to do the keyboard operations depending on the co-ordintates of you hand movements(fingertips to be precise).
[Link to virtual piano keyboard](https://www.onlinepianist.com/virtual-piano)

![Demonstration](https://github.com/umar07/OpenCV-Projects/blob/main/Air-Piano/airpiano.png?raw=true "Demonstration picture")

## To run the project-
* Fork the project and clone it in your repo.
* Run the requirements.txt file as 
`pip install -r requirements.txt`
* Run the program and the streaming window will open.
* Then go to [Virtual Piano keyboard](https://www.onlinepianist.com/virtual-piano) and select that window. Now make finger-movements inside the white lines of your streaming window to play the piano!



The following are the sources I used to learn and that helped me build this project successfully-
1. [Finger-tip detection](https://abnerrjo.github.io/blog/2015/11/15/fingertip-detection-on-opencv/)
2. [Convex Hull](https://docs.opencv.org/3.4/d7/d1d/tutorial_hull.html)
3. [Convexity Defects](https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_contours/py_contours_more_functions/py_contours_more_functions.html)
4. [Hand Detection](https://medium.com/analytics-vidhya/hand-detection-and-finger-counting-using-opencv-python-5b594704eb08)

