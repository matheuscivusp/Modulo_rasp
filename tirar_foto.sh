#!/bin/bash

DATE=$(date +"%Y-%m-%d_%H:%M:%S_Logitech_C920_Pro")

fswebcam -r 1920x1080 --no-banner /home/pi/Documents/upload_drive/ $DATE.jpg