import cv2
from pyzbar import pyzbar
from phone_camera import phone_camera
from datetime import datetime
import sys
from clear import clear
import time


def scan1():
    while True:
        print("\nScan barcode 1 (TOP Barcode on Euro Pallet)\n")
        time.sleep(2)
        print("Scanning...\n")
        time.sleep(6)
        # scan barcode1
        clear()
        # if barcode1 scans as expected
        try:
            barcode1 = phone_camera()
            # check if a barcode is found
            if not barcode1:
                raise ValueError("No Barcode found\n")
            # check if barcode is the expected type
            elif barcode1[0][:2] != '02':
                raise ValueError("Expected Barcode not found, should start with '02'\n")
            # all checks passed
            product_no = f"{barcode1[0][3]}{barcode1[0][10:15]}"
            quantity = barcode1[0][-2:]
            expiry_date = f"{barcode1[0][22:24]}.{barcode1[0][20:22]}.20{barcode1[0][18:20]}"
            return product_no, quantity, expiry_date

        except Exception as error:
            print(f"Error: {error}")
            while True:
                user_input = input("Press '1' to scan again\n")
                if user_input == '1':
                    break
                else:
                    print("Invalid Input!\n")                
                    continue

