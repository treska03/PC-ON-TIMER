import sqlite3

from utils import TimeHandler


class Days:
    
    def __init__(self):
        self.connection = sqlite3.connect("PC-TIMER-DB.sql")
        self.cursor = self.connection.cursor()
    
    def create_table(self):
        self.cursor.execute("CREATE TABLE IF NOT EXISTS Days (date DATE, time_spent INT)")

    def update(self, date, column, value):
        self.cursor.execute("UPDATE Days SET "+ column +"= :value WHERE date = :date", 
                            {"value": value, "date": date})
    
    def get_time_spent(self, today):
        self.cursor.execute("SELECT time_spent FROM Days WHERE date = :date", {"date" : today})
        time_spent_before_this_activation = self.cursor.fetchone()[0]
        return time_spent_before_this_activation
    
    def fill_missing_days(self, today):
        latest_day = self.get_last_row()
        for date in TimeHandler.yield_dates_between(latest_day, today):
            self.create_row(date.strftime("%d/%m/%Y"))

    def row_exists(self, day):
        self.cursor.execute("SELECT 1 FROM Days WHERE date =:day", {"day": day})
        return self.cursor.fetchone() is not None

    def create_row(self, day):
        if not self.row_exists(day):
            self.cursor.execute("INSERT INTO Days VALUES (:day, 0)", {"day": day})

    def get_last_row(self):
        return self.cursor.execute("SELECT * FROM Days ORDER BY date DESC LIMIT 1").fetchone()[0]
