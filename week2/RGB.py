import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv
img = np.zeros((100,600,3), np.uint8)

def rgb(x):
    """Trackbar callback function."""
    r = cv.getTrackbarPos('R', 'window')
    g = cv.getTrackbarPos('G', 'window')
    b = cv.getTrackbarPos('B', 'window')
    img[:] = [b, g, r]
    cv.displayOverlay('window', f'R: {r} G: {g} B: {b}')
    cv.imshow('window', img)


cv.imshow('window', img)
cv.createTrackbar('R', 'window', 0, 255, rgb)
cv.createTrackbar('G', 'window', 0, 255, rgb)       
cv.createTrackbar('B', 'window', 0, 255, rgb)
cv.waitKey(0)
cv.destroyAllWindows()