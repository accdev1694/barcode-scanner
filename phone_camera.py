import cv2
from pyzbar import pyzbar

# steps
# 1. Download the ip webcam app to your phone
# 2. Go to start camera and copy the ip address
# 3. switch off your wifi, and put on your hotspot
# 4. connect your pc to your phones hotspot
# in your webcam app, start server


def phone_camera():
    # Save camera ip address as value of the url variable
    url = "http://192.168.8.201:8080/video"
    # Call the videocapture function in the cv2 module
    cap = cv2.VideoCapture(url)
    code = []
    while True:
        # try to read or decode the video capture, saving in variable
        ret, frame = cap.read()
        # if it cant read, close the video and release all windows
        if not ret:
            break
        # if it reads successfully, resize the frame and decode it
        frame = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)
        barcodes = pyzbar.decode(frame)
        # loop through all the barcodes and set the frame dimensions, add codes to the barcode list
        for barcode in barcodes:
            (x, y, w, h) = barcode.rect
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 1)
            barcode_data = barcode.data.decode("utf-8")
            code.append(barcode_data)

        cv2.imshow("Scanner Scanner", frame)
        if len(code) >= 1:
            cap.release()
            cv2.destroyAllWindows()
            return code

