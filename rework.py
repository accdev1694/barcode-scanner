import cv2
from pyzbar import pyzbar
from phone_camera import phone_camera
from scan1 import scan1
from datetime import datetime
from clear import clear
from scan2 import scan2
import time


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
            scanning_barcode1 = True
            while scanning_barcode1:
                try:
                    print("\nScan barcode 1 (TOP Barcode on Euro Pallet)\n")
                    # take note of current day and time
                    start_time = datetime.now().time().replace(microsecond=0)
                    start_day = datetime.now().replace(microsecond=0)
                    time.sleep(2)
                    print("Waiting to scan...\n")
                    time.sleep(5)
                    # scan barcode 2                
                    barcode1, product_no, quantity, expiry_date = scan1()
                    clear()                
                    print(barcode1)
                    print("---> Successfully Scanned Barcode 1\n")                
                    scanning_barcode1 = False                    
                except:
                    if barcode1 == None:                        
                        print("Try scanning Barcode 1 again")
                        continue
                
                scanning_barcode2 = True
                while scanning_barcode2:
                    try:
                        time.sleep(3)
                        clear()
                        # scan barcode 2
                        print("Scan Barcode 2 (BOTTOM Barcode on Euro Pallet)\n")
                        time.sleep(2)
                        print("Waiting to scan...\n")                
                        time.sleep(5)
                        clear()
                        barcode2, lot_no, pallet_no = scan2()
                        clear()
                        print(barcode2)
                        print("---> Successfully Scanned Barcode 2\n")                
                        scanning_barcode2 = False                        
                    except:
                        if barcode2 == None:
                            print("Try scanning Barcode 2 again")
                            continue
                time.sleep(2)
                clear()                
                print("Kindly Begin Rework...")
                time.sleep(2)
                clear()
                # user decision after current Euro pallet
                user_input = input("Is the Blue Pallet Full? 'y/n'").lower()
                if user_input == 'y':
                    end_time = datetime.now().time().replace(microsecond=0)                    
                    duration = (datetime.now().replace(microsecond=0)) - start_day
                    duration = f"{duration.total_seconds() / 60:.1f}"
                    durations += float(duration)
                    pallet_details.append(f"{euro_pallet_count}.) Euro Pallet No: {pallet_no} \nDate: {start_date}\nUser: {
                        user_name} \nStart Time: {start_time} \nFinish Time: {end_time} \nTime Taken: {duration} minutes \nPart No: {
                        product_no} \nBatch No: {lot_no} \nExpiry Date: {expiry_date}")
                    for detail in pallet_details:
                        file.write(detail, "\n")
                        scanning_barcode1 = False
                        
                        
                elif user_input == 'n':
                        start_time = datetime.now().time().replace(microsecond=0)
                        start_date = datetime.now().date()
                        start_day = datetime.now().replace(microsecond=0)
                        continue
                
                
                # scan barcode 3
                clear()
                print("Now scan Barcode 3 (Blue Pallet Barcode)")
                time.sleep(2)
                print("Waiting to scan...\n")                
                time.sleep(5)
                clear()
                #barcode2, lot_no, pallet_no = scan3()
            break
                
                 
    print("End")
                
                
            
                
    
main()