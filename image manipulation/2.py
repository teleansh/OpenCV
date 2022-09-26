import cv2 as cv 

# resizing and rescaling --------------------------------------

img = cv.imread('granny.jpg')
cv.imshow('cat',img)

def rescaleFrame(frame,scale=0.75):
    wid = int(frame.shape[1]*scale)
    hi = int(frame.shape[0] *scale)

    dimensions = (wid,hi)

    return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)  # to resize

k = rescaleFrame(img)
cv.imshow('catsmall',k)
cv.waitKey(0)

