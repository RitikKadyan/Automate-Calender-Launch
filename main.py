import datetime
import os
import time
import pyautogui as py

try:
    f = open("logGC.txt", "a")  # Open log file
    os.startfile("C:\\Users\\Ritik\\AppData\\Local\\Programs\\Notion\\Notion.exe")  # File path to my Notion application
    f.write(f"Successfully opened Notion at {str(datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S'))}.\n")  # Write log
    time.sleep(5)  # Wait 5 seconds for application to load
    Notion = py.getWindowsWithTitle("Personal Calendar")  # Find an active Notion window
    NotionTop = Notion[0].top  # Gets the Top side location of the Notion Window
    NotionLeft = Notion[0].left  # Gets the Left side location of the Notion Window
    if NotionLeft != "1912" or NotionTop != "-693":  # If not at desired location(In my case top left of my second monitor) then execute
        py.moveTo(2000, 100)  # Move the cursor to the second monitor
        time.sleep(0.1)  # Wait for screen to update
        py.moveTo(NotionLeft+Notion[0].width-80, NotionTop+5)  # Move to the Maximize button
        py.click()  # Click
    f.close()  # Close file
except IOError as E:
    f = open("logGC.txt", "a")  # Open log file
    f.write(f"Could not open Notion at {str(datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S'))} due to error {E}.\n") # Write log
    f.close()  # Close file
