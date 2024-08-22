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

    # start the day by opening a new csv file to keep record
    # if user adds their name as a command line argument
    if len(sys.argv) == 2:
        user_name = sys.argv[1]
        # write user details at top of csv file
        with open("rework.csv", "a") as file:
            file.write(f"Name: {user_name} is logged in \nDate: {
                start_date} \nStart Time: {start_time}\n")

            # user logs in
            logged_in = True
            while logged_in:

                # scan euro pallet
                scanning_barcode1 = True
                while scanning_barcode1:
                    clear()
                    print("\nScan barcode 1 (TOP Barcode on Euro Pallet)\n")
                    # take note of current day and time
                    start_time = datetime.now().time().replace(microsecond=0)
                    start_day = datetime.now().replace(microsecond=0)
                    time.sleep(2)
                    print("Waiting to scan...\n")
                    time.sleep(6)
                    # scan barcode 2
                    clear()
                    # if barcode1 scans as expected
                    if scan1()[0] != None:
                        clear()
                        barcode1, product_no, quantity, expiry_date = scan1()
                        clear()
                        print("---> Successfully Scanned Barcode1\n")

                        # scan barcode2
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
                            continue

                    # if barcode 1 returns None
                    else:
                        user_input = input(
                            "\nPress any Key to scan Barcode1 again or '1' to quit\n")
                        if user_input == "1":
                            clear()
                            sys.exit("\nHurts to see you go!\n")
                        else:
                            continue

    # if user fails to type their name as a command line argument
    else:
        clear()
        print("Must have exactly 2 command line arguments")
        time.sleep(2)
        sys.exit("Add Your name as command line argument\n")


main()
