import cv2
from pyzbar import pyzbar
from phone_camera import phone_camera


def scan1(barcode1):
    try:
        barcode1 = phone_camera()
        if barcode1[0][:2] == '00':
            pass
    except:
        exit()
    part = f"{barcode1[0][3]}{barcode1[0][10:15]}"        # euro part number
    quantity = barcode1[0][-2:]         # euro quantity
    expiry = f"{barcode1[0][22:24]}.{
        barcode1[0][20:22]}.20{barcode1[0][18:20]}"  # euro expiry date
    return part, quantity, expiry