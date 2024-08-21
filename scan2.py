import cv2
from pyzbar import pyzbar
from phone_camera import phone_camera


def scan2():
    try:
        barcode2 = phone_camera()
        if not barcode2:
            raise ValueError("No Barcode found")
        elif barcode2[0][:2] != '00':
            raise ValueError("Expected Barcode not found, should start with '00'")
        lot_no = barcode2[0][22:]             # euro lot no
        pallet_no = barcode2[0][10:20]        # euro pallet number
        return barcode2, lot_no, pallet_no
            
    except Exception as error:
        print("Error:", error)
        exit()