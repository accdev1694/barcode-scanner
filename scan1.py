import cv2
from pyzbar import pyzbar
from phone_camera import phone_camera


def scan1():
    try:
        barcode1 = phone_camera()
        if not barcode1:
            raise ValueError("No Barcode found")
        elif barcode1[0][:2] != '02':
            raise ValueError("Expected Barcode not found, should start with '02'")
        part = f"{barcode1[0][3]}{barcode1[0][10:15]}"        # euro part number
        quantity = barcode1[0][-2:]         # euro quantity
        expiry = f"{barcode1[0][22:24]}.{
        barcode1[0][20:22]}.20{barcode1[0][18:20]}"  # euro expiry date
        return barcode1, part, quantity, expiry        
            
    except Exception as error:
        print("Error:", error)
        return None, None, None, None