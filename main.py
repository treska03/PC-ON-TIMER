import os
import time
from datetime import date

import dbhandler
import window

threshold = 10 #IMPORT FROM CONFIG

def window_loop(so_far, limit):
    if limit > so_far:
        time.sleep(limit - so_far)
        
    while True:
        response = window.popup()
        if response == -1:
            os.system('shutdown -s -t 0')
        elif response == 0:
            break
        else:
            time.sleep(response*60)


def looper(INSTANCE, before_last_activation_spent, on_day, turn_on_timestamp):
    start_background_process = window_loop(threshold) #THREADING
    while True:
        today = date.today().strftime("%d/%m/%Y")
        if today != on_day:
            INSTANCE.create_row(today)
            turn_on_timestamp = time.time()
            before_last_activation_spent = 0

        #in seconds
        elapsed = round(before_last_activation_spent + time.time() - turn_on_timestamp, 0)
        INSTANCE.update(today, "time_spent", elapsed)
        INSTANCE.connection.commit()
        
        time.sleep(5)




def main():
    today = date.today().strftime("%d/%m/%Y")
    turn_on_timestamp = time.time()
    INSTANCE = dbhandler.Days()
    INSTANCE.create_row(today)
    
    INSTANCE.cursor.execute("SELECT time_spent FROM Days WHERE date = :date", {"date" : today})
    time_spent_before_this_activation = INSTANCE.cursor.fetchone()[0]

    window_loop(time_spent_before_this_activation, threshold*60)
    looper(INSTANCE, time_spent_before_this_activation, today, turn_on_timestamp)



main()





#TURN OFF, REMIND LATER, 
#ADD CONFIG MENU
#ADD POPUP WINDOW
