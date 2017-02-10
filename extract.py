import numpy as np
import cv2
import sys


facer = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eyer = cv2.CascadeClassifier('haarcascade_eye.xml')

img = cv2.imread(sys.argv[1])
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = facer.detectMultiScale(gray, 1.3, 5)

for (x,y,w,h) in faces:
	cv2.rectangle(img, (x,y), (x+w, y+h), (0, 255, 0), 2)


cv2.imwrite("processed.jpg", img)
print "done"
