import cv2
from pyzbar import pyzbar
from phone_camera import phone_camera
from clear import clear
import time
from datetime import datetime
import sys


def scan2():
    while True:
        print("Scan Barcode 2 (BOTTOM Barcode on Euro Pallet)\n")
        time.sleep(2)
        print("Scanning...\n")
        time.sleep(6)
        # scan barcode2
        clear()
        # if barcode2 scans as expected
        try:
            barcode2 = phone_camera()
            # check if a barcode is found
            if not barcode2:
                raise ValueError("No Barcode found\n")
            # check if barcode is the expected type
            elif barcode2[0][:2] != '00':
                raise ValueError(
                    "Expected Barcode not found, should start with '00'\n")
            # all checks passed
            lot_no = barcode2[0][22:]
            pallet_no = barcode2[0][10:20]
            print("---> Successfully Scanned Barcode 2\n")
            return lot_no, pallet_no

        except Exception as error:
            print("Error:", error)
            while True:
                user_input = input("Press '1' to scan again or '2' to scan next euro\n")            
                if user_input == '1':
                    break
                elif user_input == '2':
                    print("Scan the next Euro Pallet and keep working!\n")
                    return "next euro"
                else:
                    print("Invalid Input!\n")
                    continue