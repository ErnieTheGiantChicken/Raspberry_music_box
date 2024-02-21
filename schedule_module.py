
from datetime import datetime
import time
special_times = ['10:24']


def schedule_task(minute,action,special_times):
    # Getting current time
    now = datetime.now()
    minute = minute * 60 
    current_time = now.strftime('%S')
    # Aliging with 0 second in order to be precise 
    for second in range(0,60):
        now = datetime.now()
        current_time = now.strftime('%S')
        print(current_time)
        if current_time == "00":
            print("!! Aligned second !!")
            print("!! Entering main part of function !!")
            break 
        time.sleep(1)
        
    # Aligning with multiple of 5 minute in order to reach the times
    while True:
       print("!! Entering 5 aligning section !!")
       now = datetime.now() 
       current_time = now.strftime('%M')
       print(current_time)
       if int(current_time) % 5 == 0:
           break
       time.sleep(60)
       
    # Entering main part that checks the time at set minute interval
    while True:
        print("!! Main part entering !!")
        now = datetime.now()
        current_time = now.strftime('%H:%M')
        if current_time in special_times:
            action()
        time.sleep(minute)
