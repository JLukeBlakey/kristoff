#!/usr/bin/env python
from flask import Flask, render_template, Response
import cv2 as cv

capture = cv.VideoCapture("http://192.168.1.195:4747/video")

app = Flask(__name__)

@app.route("/")
def stream():
    return "<img src='http://192.168.1.195:4747/video' alt='http://192.168.1.195:4747/video'>"


#def capture():
#    if not capture.isOpened():
#
#        print("Cannot open camera")
#        exit()
#
#    while(True):
#        ret, frame = capture.read()
#        cv.imshow('livestream', frame)
#
#        if cv.waitKey(1) == ord('q'):
#            break
#
#    capture.release()
#    cv.destroyAllWindows()
