from flask import Flask, render_template, Response
import cv2 as cv
import imagezmq
#from werkzeug.wrappers import request, Response

app = Flask(__name__)
image_hub = imagezmq.ImageHub()

def gen_frames():
    while True:
        rpi_name, image = image_hub.recv_image()
        image_hub.send_reply(b'OK')
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
