from flask import Flask, render_template, Response
import cv2 as cv
import imagezmq

app = Flask(__name__)
image_hub = imagezmq.ImageHub()

#camera = cv.VideoCapture("http://192.168.1.195:4747/video")

def gen_frames():
    while True:
        rpi_name, image = image_hub.recv_image()
    #cv2.imshow(rpi_name, image) # 1 window for each RPi
    #cv2.waitKey(1)
        image_hub.send_reply(b'OK')
        #success, frame = camera.read()
       # if not success:
       #     break
        #else:
        ret, buffer = cv.imencode('.jpg', image)
        frame = buffer.tobytes()
        yield (b'--frame\r\n'
                b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')  # concat frame one by one and show result

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == "__main__":
    app.run(debug=True)
