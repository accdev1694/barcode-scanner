# Barcode-Scanner Program


## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)


## Overview
**Barcode Scanner** Is a vanilla python Program takes inventory of the work rate of users during rework at a factory by scanning the labels on the pallets, while it takes detail information from the labels, calculates the performance based on number of pallets completed per time, comparing this rate with the set work target and alerting the user in real-time, about their performance. This prompts them on the need to step up while they work.

## Features
- 1. phone_camera.py: This module uses pyzbar and cv2 to turn a phone camera into a scanner. It opens the video camera and takes snapshots of the barcode, simulating a scan, and returns the value of the captured frame
- 2. scan1.py: This module uses the phone_camera.py module to scan the top, first barcode on the Euro Pallet
- 3.  scan2.py: This module uses the phone_camera.py module to scan the bottom, second barcode on the Euro Pallet
- 4. scan3.py module: This module uses the phone_camera.py module to scan the bottom, third barcode on the Blue Pallet after completion
- 5. rework.py: This is the main file for the application. it scans the pallets, prints performance reports to the user, and records full work details including overall daily performance on a csv file, created dynamically and named dynamically
- 6. check_args.py: This module takes in the command-line arguments and ensures that the user types their name as a second argument. 
- 7. calculate_rate.py: This module takes as input, the actual work speed of the user as well as the work target for that job type, returning the work rate, and performance prompt to the user

## Installation
Follow the steps below to run the app

1. **Clone the repository:**
    - ```bash
        # clone the repo:
        git clone git@github.com:accdev1694/barcode-scanner.git

    - ```bash
        # open the working folder:
        cd rework-app
    

2. **Install dependencies:**    
- install python as well as python interpreter
- install vscode or any similar IDE
- ```bash
    # install the pyzbar module 
    pip install pyzbar
- ```bash
    pip install cv2
- ```
    import time
- ```
    import pyzbar
- ```
    from clear import clear
- ```
    from datetime import datetime
- ```
    import cv2

3. **Run the app:**
    ```bash
    # starting the app
    python rework.py user_name


## Usage
You must supply your name as a 2nd command-line argument or the app will fail. if you are adding more than one name, enclose within quotes or seperate them with a symbol such as dashes or underscores, but not spaces




