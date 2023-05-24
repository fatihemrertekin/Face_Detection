import cv2 as cv
import numpy as np

kamera = cv.VideoCapture(0)

while (True):
    ret, videoGoruntu = kamera.read()

    haar_cascade = cv.CascadeClassifier("haar_face.xml")

    faces = haar_cascade.detectMultiScale(videoGoruntu,scaleFactor=1.1,minNeighbors=3)

    print("detected number of faces:", len(faces))

    for x,y,w,h in faces:
        cv.rectangle(videoGoruntu, (x,y), (x + w,y + h), (0,200,250), 2)

    cv.imshow("Detected faces", videoGoruntu)

    if cv.waitKey(50) & 0xFF == ord('x'):
        break

kamera.release()

cv.destroyAllWindows()
