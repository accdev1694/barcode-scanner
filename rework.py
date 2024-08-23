import cv2
from pyzbar import pyzbar
from phone_camera import phone_camera
from scan1 import scan1
from scan2 import scan2
from scan3 import scan3
from datetime import datetime
from clear import clear
import time
import sys
from check_args import check_args


def main():
    euro_pallet_count = 0
    blue_pallet_count = 0
    scanned_euro_pallets = []
    scanned_blue_pallets = []
    pallet_details = []
    start_time = datetime.now().time().replace(microsecond=0)
    start_date = datetime.now().date()
    start_day = datetime.now().replace(microsecond=0)
    durations = 0

    # start the day || store records in csv file || check args
    user_name = check_args(sys.argv)
    with open("rework.csv", "a") as file:
        file.write(f"Name: {user_name} is logged in \nDate: {
            start_date} \nStart Time: {start_time}\n")

        # take note of current day and time
        start_time = datetime.now().time().replace(microsecond=0)
        start_day = datetime.now().replace(microsecond=0)
        # --> scan1
        scan_one = scan1()
        if len(scan_one) == 5:
            print(scan_one[0])
        else:
            print(scan_one)
        sys.exit()
            
            
        '''# scan barcode2
                scanning_barcode2 = True
                while scanning_barcode2:
                    clear()
                    print("Scan Barcode 2 (BOTTOM Barcode on Euro Pallet)\n")
                    time.sleep(2)
                    print("Waiting to scan...\n")
                    time.sleep(6)
                    clear()
                    # if barcode2 scans as expected
                    if scan2()[0] != None:
                        # if barcode2 has not been previously scanned
                        if scan2()[2] not in scanned_euro_pallets:
                            # scan barcode 2
                            barcode2, lot_no, pallet_no = scan2()
                            clear()
                            print("---> Successfully Scanned Barcode 2\n")
                            euro_pallet_count += 1
                            scanned_euro_pallets.append(pallet_no)
                            time.sleep(2)
                            print("Kindly Begin Rework...")
                            time.sleep(2)
                            scanning_barcode2 = False
                        # if barcode2 has been previously scanned
                        else:
                            clear()
                            print(
                                f"Pallet {scan2()[2]} has already been scanned")
                            scanning_barcode2 = False
                    # if barcode2 returns None
                    else:
                        user_input = input(
                            "\nPress any Key to scan Barcode2 again or '1' to quit\n")
                        if user_input == "1":
                            clear()
                            sys.exit("\nHurts to see you go!\n")
                        else:
                            continue

                # user decision after current Euro pallet
                user_input = input(
                    "Is the Blue Pallet Full? 'y/n'\n").lower()
                end_time = datetime.now().time().replace(microsecond=0)
                duration = (datetime.now().replace(
                    microsecond=0)) - start_day
                duration = f"{duration.total_seconds() / 60:.1f}"
                durations += float(duration)
                pallet_details.append(f"\n{euro_pallet_count}.) Euro Pallet No: {pallet_no} \nDate: {start_date}\nUser: {
                    user_name} \nStart Time: {start_time} \nFinish Time: {end_time} \nTime Taken: {duration} minutes \nPart No: {
                    product_no} \nBatch No: {lot_no} \nExpiry Date: {expiry_date}")
                for detail in pallet_details:
                    file.write(f"{detail}\n")

                # if current blue pallet is full
                if user_input == 'y':
                    # scan barcode 3
                    scanning_barcode3 = True
                    while scanning_barcode3:
                        print("Now scan Barcode 3 (Blue Pallet Barcode)")
                        time.sleep(2)
                        print("Waiting to scan...\n")
                        time.sleep(6)
                        clear()
                        # if barcode3 scans as expected
                        if scan3()[0] != None:
                            # if barcode3 has not been previously scanned
                            if scan3()[0] not in scanned_blue_pallets:
                                barcode3 = scan3()
                                clear()
                                print(
                                    "---> Successfully Scanned Barcode 3\n")
                                scanned_blue_pallets.append(barcode3)
                                blue_pallet_count += 1
                                user_input = input(
                                    "Press 'l' log out or 'n' to start a new Euro pallet").lower()
                                # log out
                                if user_input == 'l':
                                    file.write(f"\nSummary on {start_date} \nUser: {
                                        user_name} \nPallets Completed:\n")
                                    for number in scanned_euro_pallets:
                                        file.write(f"{euro_pallet_count}.) {
                                                    number}\n")
                                    file.write(f"Total Blue Pallets Completed: {
                                                blue_pallet_count}\n")
                                    file.write(f"Total Time Taken: {
                                        durations / 60:.2f} minutes")
                                    sys.exit(f"{user_name} Logged out at {
                                                datetime.now().replace(microsecond=0)}")
                                elif user_input == 'n':
                                    scanning_barcode3 = False

                            # if barcode3 has been previously scanned
                            else:
                                clear()
                                print(
                                    f"Pallet {scan3()[0]} has already been scanned")
                                scanning_barcode3 = False
                        # if barcode3 returns None
                        else:
                            user_input = input(
                                "Press any key to scan again or key '1' to scan Euro pallet").lower()
                            if user_input == '1':
                                continue
                            else:
                                start_time = datetime.now().time().replace(microsecond=0)
                                start_date = datetime.now().date()
                                start_day = datetime.now().replace(microsecond=0)
                                scanning_barcode3 = False
                # if current blue pallet isnt full
                elif user_input == 'n':
                    start_time = datetime.now().time().replace(microsecond=0)
                    start_date = datetime.now().date()
                    start_day = datetime.now().replace(microsecond=0)
                    continue '''


main()
