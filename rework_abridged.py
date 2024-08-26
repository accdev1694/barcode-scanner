import pyzbar
import cv2
import time
from datetime import datetime
from clear import clear
from scan2 import scan2
import sys
from check_args import check_args
from calculate_rate import calculate_rate


def main():
    counter = 0
    pallet_nos = []
    durations = 0
    pallet_details = []
    start_time = datetime.now().time().replace(microsecond=0)
    start_date = datetime.now().date()
    start_day = datetime.now().replace(microsecond=0)

    # begin work
    user_name, task = check_args(sys.argv)

    # log in
    while True:
        user_input = input("Press '1' to log_in or '2' to quit:\n")
        if user_input == '1':
            pass
        elif user_input == '2':
            sys.exit("Farewell ...")
        else: 
            continue
        # start time
        start_time = datetime.now().time().replace(microsecond=0)
        start_day = datetime.now().replace(microsecond=0)
        print()
        with open(f"{task}-{user_name}-{start_date}.csv", "a") as file:
            file.write(f"{user_name} is logged in for {task.title()}\nDate: {
                start_date} \nStart Time: {start_time}\n")

            # in session
            while True:
                user_input = input(
                    "Press '1' to start new session or '2' to quit:\n")
                if user_input != '1':
                    sys.exit("Farewell ...")
                # begin work
                while True:
                    scan_two = scan2()
                    lot_no, pallet_no = scan_two
                    user_input = input(
                        "Press '1' to scan next Euro of '2' to finish session:\n").lower()
                    pallet_nos.append(pallet_no)
                    counter += 1
                    end_time = datetime.now().time().replace(microsecond=0)
                    duration = (datetime.now().replace(microsecond=0)) - start_day
                    duration = round((duration.total_seconds() / 60), 1)
                    durations += duration
                    pallet_details.append(f"\n{counter}.) Euro Pallet No: {pallet_no}\n Date: {start_date}\n Start Time: {
                        start_time}\n Finish Time: {end_time}\n Time Taken: {duration} minutes\n\n{calculate_rate(duration, 1, 6, task.lower())}\n")

                    file.write(f"\n{pallet_details[-1]}\n")
                    print((calculate_rate(duration, 1, 6, task.lower())))

                    if user_input == '1':
                        # reset the time and day
                        start_time = datetime.now().time().replace(microsecond=0)
                        start_day = datetime.now().replace(microsecond=0)
                        continue
                    else:
                        break
                break
            
        
            file.write(f"\n\nSummary on {start_date}\n User: {
                user_name}\n Pallets Completed:\n")
            incrementer = 1
            for pallet in pallet_nos:
                file.write(f"{incrementer}.) {pallet}\n")
                incrementer += 1

            file.write(f"Total Euro Pallets Completed: {
                counter}\n")
            file.write(f"Total Time Taken: {
                durations} minutes\n")
            file.write(
                f"\n{calculate_rate(durations, counter, 6, task.lower())} Today\n")
            print(f"\nYou Logged Out.\n{
                (calculate_rate(durations, counter, 6, task.lower()))} Today")
            file.write(f"\n\n{user_name} Logged out:\nDate: {
                datetime.now().date()}\nTime: {datetime.now().time().replace(microsecond=0)}")
            break
    print("Farewell ...")


main()
