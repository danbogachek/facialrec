from picamera import PiCamera
from picamera.array import PiRGBArray
from time import sleep
import cv2

file = ''

camera = PiCamera()
rawCapture = PiRGBArray(camera)

sleep(2)
camera.capture(rawCapture, format="bgr")
img = rawCapture.array
cv2.imwrite("blah.jpg", img)
