import numpy as np
import cv2
import sys
import subprocess as sub


from picamera import PiCamera
from picamera.array import PiRGBArray
from time import sleep

file = "processed.jpg"

camera = PiCamera()
camera.framerate = 32


def process(img):
	pass
	



rawCapture = PiRGBArray(camera)
sleep(.1)
camera.capture(rawCapture, format="bgr")

img = rawCapture.array

facer = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces = facer.detectMultiScale(gray, 1.3, 5)

for (x,y,w,h) in faces:
	cv2.rectangle(img, (x,y), (x+w, y+h), (0, 255, 0), 2)

if len(faces) < 1:
	print "no faces detected"

else:

	cv2.imwrite(file, img)
	substring = "sudo fbi -d /dev/fb0 -a -T 2 {}".format(file)
	sub.call(substring, shell=True)
	print "done"
