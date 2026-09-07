import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv

file = 'messi.jpg'
img = cv.imread('img/messi.jpg', cv.IMREAD_COLOR)
h, w, c = img.shape
cv.imshow('window', img)
cv.displayOverlay('window', f'file name: {file}\nwidth: {w} \nheight: {h} \nchannels: {c}')


cv.waitKey(0)
cv.destroyAllWindows()


