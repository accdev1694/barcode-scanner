import cv2
from pyzbar import pyzbar

# steps
# 1. Download the ip scanner app to your phone
# 2. Go to start camera and copy the ip address
# 3. Save it as value of the url variable in your code
# 4. Call the videocapture function in the cv2 module
#       and save value in cap variable
# 4. Call the read function on the video capture return values
# 5. The read function returns two values: a boolean (success or failure to read)
#       and the video frame
# 6. check if next resize the frame
#


def phone_camera():
    # Save camera ip address as value of the url variable
    url = "http://192.168.26.111:8080/video"
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
        # loop through all the barcodes and set the frame dimensions
        for barcode in barcodes:
            (x, y, w, h) = barcode.rect
            cv2.rectangle(frame, (x, y), (x + y + w + h), (0, 0, 255), 1)
            barcode_data = barcode.data.decode("utf-8")
            # add codes to the barcode list
            code.append(barcode_data)

        cv2.imshow("Scanner", frame)
        # if there exists a barcode, release the video and close the capture window
        if len(code) == 1:
            break

    cap.release()
    cv2.destroyAllWindows()
    # return the barcode as a list, asumming its more than 1
    return code
