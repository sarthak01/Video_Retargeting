import cv2
import numpy
import test_min

img = cv2.imread('Images/tree2.jpg')
obj = test_min.pyARAP(img, 1, 2)
vector = obj.getVector_S()
#print(vector)
