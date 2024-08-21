import cv2
from pyzbar import pyzbar
from phone_camera import phone_camera
from scan1 import scan1


def main():
    barcode1, part_no, euro_quantity, expiry_date = scan1()
    print(barcode1)
    
main()