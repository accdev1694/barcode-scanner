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
from calculate_rate import calculate_rate


def main():
    scanned = []    
    euro_pallet_count = 0
    blue_pallet_count = 0
    scanned_blue_pallets = []
    pallet_details = []
    scanned_euro_pallets = []
    start_time = datetime.now().time().replace(microsecond=0)
    start_date = datetime.now().date()
    start_day = datetime.now().replace(microsecond=0)
    durations = 0

# >>> start the day || store records in csv file || check args
    user_name, task = check_args(sys.argv)

# >>> logging in to start work <<< ---------------------
    logged_in = True
    while logged_in:
        clear()
        user_input = input("Press '1' to start working\n")
        if user_input != '1':
            continue
        # take note of current day and time
        clear()
        start_time = datetime.now().time().replace(microsecond=0)
        start_day = datetime.now().replace(microsecond=0)
        print()
        with open(f"{task}-{user_name}-{start_date}.csv", "a") as file:
            file.write(f"{user_name} is logged in for {task.upper()}\nDate: {
                start_date} \nStart Time: {start_time}\n")

# ----- >>> start work <<< --------------------------------
            while True:                
                product_no, quantity, expiry_date = scan1()
                if product_no in scanned:
                    print("Euro Pallet already scanned!\n")
                    continue
                clear()
                print("Successfully Scanned!\n")
                scanned.append(product_no)
                scan_two = scan2()
                if scan_two == "next euro":
                    continue
                lot_no, pallet_no = scan_two

# --------- >>> user decision after current Euro pallet <<< ------------------
                user_input = input("Is the Blue Pallet Full? 'y/n'\n").lower()
                scanned_euro_pallets.append(pallet_no)
                euro_pallet_count += 1
                end_time = datetime.now().time().replace(microsecond=0)
                duration = (datetime.now().replace(microsecond=0)) - start_day
                duration = round((duration.total_seconds() / 60), 1)
                durations += duration
                pallet_details.append(f"\n{euro_pallet_count}.) Euro Pallet No: {pallet_no}\n Date: {start_date}\n Start Time: {
                                      start_time}\n Finish Time: {end_time}\n Time Taken: {duration} minutes\n Part No: {product_no}\n Batch No: {lot_no}\n Expiry Date: {expiry_date}\n\n{calculate_rate(duration, 1, 6, task.lower())}\n")

                file.write(f"\n{pallet_details[-1]} for this pallet\n")
                clear()
                print(f"{(calculate_rate(duration, 1, 6, task.lower()))} for this pallet\n")
                print(f"{(calculate_rate(durations, euro_pallet_count, 6, task.lower()))} today\n")

                if user_input == 'n':
                    # reset the time and day
                    start_time = datetime.now().time().replace(microsecond=0)
                    start_day = datetime.now().replace(microsecond=0)
                    continue
                # scan barcode 3
                while True:
                    lin_number = scan3()
                    if lin_number in scanned_blue_pallets:
                        clear()
                        print("Blue Pallet already scanned!")                        
                        user_input = input("Press 1: 'Scan again' or 2: 'next euro'\n")
                        if user_input == '1':
                            continue
                        else:
                            break                        
                    if lin_number == "next euro":
                        break
                    clear()
                    print("Successfully Scanned!\n")
                    blue_pallet_count += 1
                    scanned_blue_pallets.append(lin_number)
                    pallet_details.append(f" LIN Number: {lin_number[0]}")

                    # next user action
                    user_input = input(
                        "Press '1' for next Euro Pallet or '2' to Log out\n")
                    clear()
                    if user_input == '1':
                        # reset the time and day
                        start_time = datetime.now().time().replace(microsecond=0)
                        start_day = datetime.now().replace(microsecond=0)
                        break
                    elif user_input == '2':
                        file.write(f"\n\nSummary on {start_date}\n User: {
                                user_name}\n Pallets Completed:\n")
                        counter = 1
                        for euro_pallet in scanned_euro_pallets:
                            file.write(f"{counter}.) {euro_pallet}\n")
                            counter += 1
                        file.write(f"Total Blue Pallets Completed: {
                                blue_pallet_count}\n")
                        file.write(f"Total Euro Pallets Completed: {
                                euro_pallet_count}\n")
                        file.write(f"Total Time Taken: {
                                round(durations, 1)} minutes\n")
                        file.write(
                            f"\n{calculate_rate(durations, euro_pallet_count, 6, task.lower())} Today\n")
                        print(f"\nYou Logged Out.\n{
                            (calculate_rate(durations, euro_pallet_count, 6, task.lower()))} Today\n")
                        file.write(f"\n\n{user_name} Logged out:\nDate: {
                            datetime.now().date()}\nTime: {datetime.now().time().replace(microsecond=0)}\n\n")
                        sys.exit("Goodbye\n")

main()
