#ADAPTIVE THREESOLDHINg  #scanneeerrrrr
import cv2
import numpy as np
import matplotlib.pyplot as plt
img=cv2.imread(r'C:\Users\SWAPNIL RAI\Desktop\sample.jpeg')
#converting
img1=cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
# applying different thresholding 
# techniques on the input image
thresh1 = cv2.adaptiveThreshold(img1, 255, cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY, 199, 5)
thresh2 = cv2.adaptiveThreshold(img1, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY, 199, 5)
# the window showing output images
# with the corresponding thresholding 
# techniques applied to the input image
cv2.imshow('Adaptive Mean', thresh1)
cv2.imshow('Adaptive Gaussian', thresh2)
# De-allocate any associated memory usage  
if cv2.waitKey(0) & 0xff == 27: 
    cv2.destroyAllWindows() 
