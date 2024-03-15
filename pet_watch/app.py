from flask import Flask, render_template, Response
import imagezmq
import cv2

app = Flask(__name__)
image_hub = imagezmq.ImageHub(open_port='tcp://*:5555')


def gen_frames():
    while True:
        #camera = cv2.VideoCapture("http://192.168.50.104:4747/video")
        #success, frame = camera.read()
        #if not success:
        #    break
        #else:
        rpi_name, frame = image_hub.recv_image()

        image_hub.send_reply(b'OK')


        #cv2.imshow(rpi_name, image) # 1 window for each RPi
        #cv2.waitKey(1)
        #image_hub.send_reply(b'OK')       

        ret, buffer = cv2.imencode('.jpg', frame)
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
