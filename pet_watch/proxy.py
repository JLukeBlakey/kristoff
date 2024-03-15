import socket
import imagezmq
from imutils.video import VideoStream

rtsp_url = "http://192.168.50.104:4747/video"
vs = VideoStream(rtsp_url).start()

server = imagezmq.ImageSender(connect_to="tcp://127.0.0.1:5555")

rpiName = socket.gethostname()

while True:
	frame = vs.read()
	server.send_image(rpiName, frame)
