import cv2 as cv

capture = cv.VideoCapture("http://192.168.1.195:4747/video")

def stream():
    if not capture.isOpened():
        print("Cannot open camera")
        exit()

    while(True):
        ret, frame = capture.read()
        cv.imshow('livestream', frame)

        if cv.waitKey(1) == ord('q'):
            break

    capture.release()
    cv.destroyAllWindows()

stream()
