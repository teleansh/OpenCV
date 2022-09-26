import cv2 as cv


# Reading image --------------------------------------------

img = cv.imread('granny.jpg')
cv.imshow('image',img)      # anything can be used as name


# Rescaling the frame --------------------------------------

def rescaleFrame(frame,scale=0.75):
    wid = int(frame.shape[1]*scale)
    hi = int(frame.shape[0] *scale)

    dimensions = (wid,hi)

    return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)


# Reading video --------------------------------------------

capture = cv.VideoCapture('vid.mkv')
while True:
    isTrue,frame= capture.read()

    #frameres=rescaleFrame(frame,scale=0.2)

    cv.imshow('vid',frame)      # anything can be used as name
    
    #cv.imshow('resize', frameres)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break   # stop on pressing 'd'
capture.release()
cv.deatroyAllWindows()

cv.waitKey(0)
