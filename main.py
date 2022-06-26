import time
from datetime import date

import dbhandler
import window

threshold = 10



def looper(INSTANCE, before_last_activation_spent, on_day, turn_on_timestamp):
    while True:
        today = date.today().strftime("%d/%m/%Y")
        if today != on_day:
            INSTANCE.create_row(today)
            turn_on_timestamp = time.time()
            before_last_activation_spent = 0

        elapsed = round(before_last_activation_spent + time.time() - turn_on_timestamp, 0)
        INSTANCE.update(today, "time_spent", elapsed)
        INSTANCE.connection.commit()
        
        if elapsed > threshold:
            print(f"{threshold} minutes elapsed")
            window.popup()
        
        time.sleep(5)

        while i > 0:
            i = 1 #some_function()



def main():
    today = date.today().strftime("%d/%m/%Y")
    turn_on_timestamp = time.time()
    INSTANCE = dbhandler.Days()
    INSTANCE.create_row(today)
    
    INSTANCE.cursor.execute("SELECT time_spent FROM Days WHERE date = :date", {"date" : today})
    time_spent_before_this_activation = INSTANCE.cursor.fetchone()[0]

    looper(INSTANCE, time_spent_before_this_activation, today, turn_on_timestamp)



main()



#ADD CONFIG MENU
#ADD POPUP WINDOW
