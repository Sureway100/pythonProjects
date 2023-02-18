import cv2 as cv
import numpy as np

blank = np.zeros((500, 500, 3), dtype='uint8')
cv.imshow('blank img', blank)

# paint the image a certain color
# blank[:] = 0, 255, 0
blank[200:300, 300:400] = 0, 0, 255
cv.imshow('Green', blank)


# draw a rectangle
cv.rectangle(blank, (0, 0), (250, 250), (0, 255, 0), thickness=2)
cv.imshow('rectangle', blank)

cv.waitKey()
