import cv2
from pyzbar import pyzbar
from phone_camera import phone_camera
from datetime import datetime
import sys
from clear import clear
import time


def scan1():
    scanning_barcode1 = True
    while scanning_barcode1:
        print("\nScan barcode 1 (TOP Barcode on Euro Pallet)\n")        
        time.sleep(2)
        print("Waiting to scan...\n")
        time.sleep(6)
        # scan barcode 2
        clear()
        # if barcode1 scans as expected
        try:
            barcode1 = phone_camera()
            if not barcode1:
                raise ValueError("No Barcode found")
            elif barcode1[0][:2] != '02':
                raise ValueError(
                    "Expected Barcode not found, should start with '02'")
            product_no = f"{barcode1[0][3]}{
                barcode1[0][10:15]}"        # euro part number
            quantity = barcode1[0][-2:]         # euro quantity
            expiry_date = f"{barcode1[0][22:24]}.{
                barcode1[0][20:22]}.20{barcode1[0][18:20]}"  # euro expiry date
            scanning_barcode1 = False
            return "---> Successfully Scanned Barcode1\n", barcode1, product_no, quantity, expiry_date
        except Exception as error:
            print(f"Error: {error}")
            user_input = input(
                "\nPress any Key to scan Barcode1 again or '1' to quit\n")
            if user_input == "1":
                clear()
                sys.exit("\nHurts to see you go!\n")
                scanning_barcode1 = False                
            else:
                continue            
