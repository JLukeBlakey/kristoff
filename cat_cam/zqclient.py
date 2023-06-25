# run this program on each RPi to send a labelled image stream
import socket
import time
from imutils.video import VideoStream
import imagezmq
import cv2 as cv

#sender = imagezmq.ImageSender(connect_to='tcp://jeff-macbook:5555')
#
#rpi_name = socket.gethostname() # send RPi hostname with each image
##picam = VideoStream(usePiCamera=True).start()
#
#
##time.sleep(2.0)  # allow camera sensor to warm up
#while True:  # send images as stream until Ctrl-C
#    success, frame = capture.read()
#    sender.send_image(rpi_name, frame)
#    #image = cappure,picam.read()
#    #sender.send_image(rpi_name, image)
#
rtsp_url = "http://192.168.1.195:4747/video"
vs = VideoStream(rtsp_url).start()

#sender = imagezmq.ImageSender(connect_to="tcp://46.226.106.83:5555")
sender = imagezmq.ImageSender(connect_to="tcp://127.0.0.1:5555")

rpiName = socket.gethostname()

#vs = VideoStream(usePiCamera=True).start()
#vs = VideoStream(src='http://192.168.1.195:4747/video').start()
#capture = cv.VideoCapture("http://192.168.1.195:4747/video")
 
while True:
	# read the frame from the camera and send it to the server
	frame = vs.read()
	#success, frame = capture.read()
	sender.send_image(rpiName, frame)
