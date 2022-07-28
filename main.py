import os
import threading
import time
from datetime import date

import dbhandler
import window
from utils import DataReader, TimeHandler

#Enable window to pop up when threshold is reached
remind, threshold = DataReader.get_data("config.json", "remind", "threshold") 


def prepare_and_return_time_spent_before(today):
    INSTANCE = dbhandler.Days()
    INSTANCE.create_row(today)
    
    INSTANCE.cursor.execute("SELECT time_spent FROM Days WHERE date = :date", {"date" : today})
    time_spent_before_this_activation = INSTANCE.cursor.fetchone()[0]
    del INSTANCE
    return time_spent_before_this_activation


def window_loop(so_far, limit):
    if limit > so_far:
        time.sleep(limit - so_far)
        
    while True:
        response = []
        hours, minutes, seconds = TimeHandler.unpack_seconds(so_far)
        window.popup(response, hours, minutes, seconds)
        response = response[0]

        print(f'Sleeping for {response} minutes')
        if response == -2:
            os.system('shutdown -s -t 0')
        elif response == -1:
            break
        else:
            time.sleep(response*60)


def db_updater_loop(before_last_activation_spent : int, on_day : str, turn_on_timestamp : float):
    INSTANCE = dbhandler.Days()
    while True:
        today = date.today().strftime("%d/%m/%Y")
        if today != on_day:
            INSTANCE.create_row(today)
            turn_on_timestamp = time.time()
            before_last_activation_spent = 0

        elapsed = round(before_last_activation_spent + time.time() - turn_on_timestamp, 0)
        INSTANCE.update(today, "time_spent", elapsed)
        INSTANCE.connection.commit()
        print("+5")
        
        time.sleep(5)




def main():
    today = date.today().strftime("%d/%m/%Y")
    turn_on_timestamp = time.time()
    time_spent_before_this_activation = prepare_and_return_time_spent_before(today)

    if not remind:
        db_updater_loop(time_spent_before_this_activation, today, turn_on_timestamp)
        exit()

    process1 = threading.Thread(target=db_updater_loop, args=(time_spent_before_this_activation, today, turn_on_timestamp))
    process1.start()
        
    process2 = threading.Thread(target=window_loop, args=(time_spent_before_this_activation, threshold*60))
    process2.start()


if __name__ == "__main__":
    main()

