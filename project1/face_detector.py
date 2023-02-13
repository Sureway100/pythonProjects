# import opencv 
import cv2

# check version installed
print(cv2.__version__)

trained_faces = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# chose an image to predict
testOne = cv2.imread('humanFace.png')
# testOne = cv2.imread('humanFace2.png')

# turn selected image to gray
gray_testOne = cv2.cvtColor(testOne, cv2.COLOR_BGR2GRAY)

# detect faces
face_cord = trained_faces.detectMultiScale(gray_testOne)

# draw rectangles around the faces 
cv2.rectangle(gray_testOne, (307, 115), (336,336), (0,255,0), 2)





cv2.imshow('Sureway Result', gray_testOne)

cv2.waitKey()


print("code completed")