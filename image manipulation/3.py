import cv2 as cv

img = cv.imread('image2.jpg')
cv.imshow('game',img)

# grayscaling an image
gray = cv.cvtColor(img , cv.COLOR_BGR2GRAY)
cv.imshow('gray',gray)

# blur
blur = cv.GaussianBlur(img,(9,9),cv.BORDER_DEFAULT)
cv.imshow('blur',blur)

# edge cascade
edge = cv.Canny(img, 125, 175)      # can also pass blur to get less and neat edges
cv.imshow('canny edges',edge)


# dilating (thickens the canny edges)
dil = cv.dilate(edge,(7,7),iterations=2)
cv.imshow('dilated',dil)

# eroding (shapens the canny edges)
er = cv.erode(edge,(7,7),iterations=2)
cv.imshow('eroded',er)

# resize
resize = cv.resize(img,(500,500) , interpolation=cv.INTER_AREA)
cv.imshow('Resized',resize)

# cropping
cropped = img[50:200 , 200:400]
cv.imshow('cropped',cropped)

cv.waitKey(0)