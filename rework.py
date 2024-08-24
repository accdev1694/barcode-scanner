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
    scanned_blue_pallets = []
    pallet_details = []
    scanned_euro_pallets = []
    start_time = datetime.now().time().replace(microsecond=0)
    start_date = datetime.now().date()
    start_day = datetime.now().replace(microsecond=0)
    durations = 0

# >>> start the day || store records in csv file || check args
    user_name = check_args(sys.argv)

# >>> logging in to start work <<< ---------------------
    logged_in = True
    while logged_in:
        user_input = input("Press '1' to start working\n")
        if user_input != '1':
            continue
        # take note of current day and time
        start_time = datetime.now().time().replace(microsecond=0)
        start_day = datetime.now().replace(microsecond=0)
        with open("rework.csv", "a") as file:
            file.write(f"Name: {user_name} is logged in \nDate: {
                start_date} \nStart Time: {start_time}\n")

# ----- >>> start work <<< --------------------------------
            while True:
                product_no, quantity, expiry_date = scan1()
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
                duration = f"{duration.total_seconds() / 60:.1f}"
                durations += float(duration)
                pallet_details.append(f"\n{euro_pallet_count}.) Euro Pallet No: {pallet_no}\n Date: {start_date}\n Start Time: {
                                      start_time}\n Finish Time: {end_time}\n Time Taken: {duration} minutes\n Part No: {product_no}\n Batch No: {lot_no}\n Expiry Date: {expiry_date}")
                file.write(f"\n{pallet_details[-1]}\n")

                if user_input == 'n':
                    # reset the time and day
                    start_time = datetime.now().time().replace(microsecond=0)
                    start_day = datetime.now().replace(microsecond=0)
                    continue
                # scan barcode 3
                lin_number = scan3()
                if lin_number == "next euro":
                    continue
                blue_pallet_count += 1
                scanned_blue_pallets.append(lin_number[0])
                pallet_details.append(f" LIN Number: {lin_number[0]}")

                # next user action
                user_input = input(
                    "Press '1' for next Euro Pallet or '2' to Log out\n")
                if user_input == '1':
                    # reset the time and day
                    start_time = datetime.now().time().replace(microsecond=0)
                    start_day = datetime.now().replace(microsecond=0)
                    continue
                elif user_input == '2':
                    file.write(f"\nSummary on {start_date}\n User: {
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
                               durations / 60:.2f} minutes\n")
                    file.write(f"\n\n{user_name} Logged out at {
                               datetime.now().replace(microsecond=0)}")
                    print(f"{user_name} Logged out at {
                          datetime.now().replace(microsecond=0)}")
                    break
        break
    print("End")
        

main()

print("Very End")
