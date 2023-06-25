import socket
import imagezmq
import cv2 as cv
from imutils.video import VideoStream

sender = imagezmq.ImageSender(connect_to="tcp://46.226.106.83:5555")
#sender = imagezmq.ImageSender(connect_to="tcp://127.0.0.1:5555")

rpiName = socket.gethostname()

rtsp_url = "http://192.168.1.195:4747/video"
vs = VideoStream(rtsp_url).start() 


while True:
	frame = vs.read()
	sender.send_image(rpiName, frame)
