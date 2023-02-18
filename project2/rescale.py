
# resize a video or an image

import cv2 as cv

img = cv.imread('assets/humanFace.png')
cv.imshow('my face', img)


# frame to be resized and scale value is your actual big or small size as you want, also try 0.2(this should be smaller)
# 1 is width and 0 is height
def rescaleFrame(frame, scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)


# for images resizing
resized_img = rescaleFrame(img)
cv.imshow('resized image', resized_img)


# for video resizing
# capture = cv.VideoCapture('assets/file_example.mp4')
# while True:
#     isTrue, frame = capture.read()
#     frame_resized = rescaleFrame(frame)
#     cv.imshow('NEW video', frame)
#     cv.imshow('resized video', frame_resized)
#     if cv.waitKey(20) & 0xFF == ord('d'):
#         break

# capture.release()
# cv.destroyAllWindows()


cv.waitKey(0)
