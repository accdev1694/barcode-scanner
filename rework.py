import cv2
from pyzbar import pyzbar
from phone_camera import phone_camera
from scan1 import scan1
from datetime import datetime
from clear import clear


def main():
    euro_pallet_count = 0
    blue_pallet_count = 0
    scanned_euro_pallets = []
    scanned_blue_pallets = []
    pallet_details = []
    user_name = input('Name:\n')
    start_time = datetime.now().time().replace(microsecond=0)
    start_date = datetime.now().date()
    start_day = datetime.now().replace(microsecond=0)
    durations = 0
    
    # start the day by opening a new csv file to keep record
    with open("rework.csv", "a") as file:
        logged_in = True
        while logged_in:
            file.write(f"Name: {user_name} \nDate: {
                       start_date} \nStart Time: {start_time}\n")
            
            # scan euro pallet
            scanning_barcode_one = True
            while scanning_barcode_one:
                print("\nScan TOP Barcode on Euro Pallet\n")
                # take note of current day and time
                start_time = datetime.now().time().replace(microsecond=0)
                start_day = datetime.now().replace(microsecond=0)
                print("Waiting to scan...\n")
                # scan barcode 2                
                barcode1, product_no, quantity, expiry_date = scan1()
                clear()                
                print("Successfully scanned barcode1\n")                
                # scan barcode 2
                print("Scan BOTTOM Barcode on Euro Pallet\n")
                 
                
                
                
            
                
    
main()