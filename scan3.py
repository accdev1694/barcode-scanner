import cv2
from pyzbar import pyzbar
from phone_camera import phone_camera
import time
from clear import clear
import sys


def scan3():
    scanned = []
    while True:
        print("\nScan Barcode 3 (Blue Pallet Barcode)\n")
        time.sleep(2)
        print("Scanning...")
        time.sleep(6)
        # scan barcode3
        clear()
        try:
            barcode3 = phone_camera()
            # check if barcode is already scanned
            if barcode3 in scanned:
                raise ValueError("Barcode already scanned!\n")                
            if not barcode3:
                # check if a barcode is found
                raise ValueError("No Barcode found\n")
            elif barcode3[0][:3] != 'L11':
                raise ValueError("Expected Barcode not found, should start with 'L11'\n")
            # all checks passed             
            print("---> Successfully Scanned Barcode3\n")
            return barcode3

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