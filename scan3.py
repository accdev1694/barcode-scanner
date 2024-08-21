import cv2
from pyzbar import pyzbar
from phone_camera import phone_camera


def scan3():
    try:
        barcode3 = phone_camera()
        if not barcode3:
            raise ValueError("No Barcode found")
        elif barcode3[0][:3] != 'L11':
            raise ValueError(
                "Expected Barcode not found, should start with 'L11'")
        return barcode3

    except Exception as error:
        print("Error:", error)
        return None, None, None, None
