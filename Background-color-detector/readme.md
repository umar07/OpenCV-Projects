***Ever wondered how the Instagram stories pick a background automatically when you add an image?!*** Well they analyse your picture through different algorithms and produce a background matching with the image. They primarily use the "colors" present in the image to process the output.


Here in this project you find 2 techniques to detect a suitable background for the input image. The first approach is to separate the RGB matrices and then do a frequency count for each pixel value in the 3 RGB matrices individually using the Counter() function. After that, you select the 10 most frequent values present and take the average of them to get the resultant pixel value. Finally, just produce a blank image using np.zeros() and fill it with the background color obtained to show the final result. 
This is a very naive approach but produces results in just 40 lines of code!

The second approach is to use K-Means Clustering algorithm on the RGB values and find clusters of different set of colors present in the image. After that, again make use of frequency count and finally find the background color. 
This method involves the use of unsupervised machine learning and it's applications extend much beyond background color detection. Image segmentation tasks make heavy use of this approach of using K-Means Clustering on the image.

##### Sources used to learn-

1. [Using K-Means Clustering on image](https://towardsdatascience.com/color-identification-in-images-machine-learning-application-b26e770c4c71)
2. [Using separate RGB values](https://medium.com/generalist-dev/background-colour-detection-using-opencv-and-python-22ed8655b243)


