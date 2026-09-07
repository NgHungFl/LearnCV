import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv

img = cv.imread('img/messi.jpg')

cv.imshow('Original Image', img)
cv.waitKey(0)
cv.destroyAllWindows()

