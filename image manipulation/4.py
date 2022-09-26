import cv2 as cv
import numpy as np

img  = cv.imread('image2.jpg')

cv.imshow('image',img)

# translating an image
def translate(img, x ,y):
    transMat = np.float32([[1,0,x],[0,1,y]])
    dimensions = (img.shape[1],img.shape[0])
    return cv.warpAffine(img,transMat, dimensions)

trans = translate(img, 100 , 100)
cv.imshow('trans',trans)

# rotating an image
def rotate(img, angle,point=None):
    (height,width)=img.shape[:2]

    if point is None:
        point = (width//2 , height//2)

    rotMat = cv.getRotationMatrix2D(point,angle,1.0)
    dimensions = (width,height)

    return cv.warpAffine(img,rotMat,dimensions)

rotated = rotate(img, 45)
cv.imshow('rotated',rotated)


cv.waitKey(0)