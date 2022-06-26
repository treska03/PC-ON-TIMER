import sqlite3


class Days:
    
    def __init__(self):
        self.connection = sqlite3.connect("db.sql")
        self.cursor = self.connection.cursor()
        self.create_table()
    
    def create_table(self):
        self.cursor.execute("CREATE TABLE IF NOT EXISTS Days (date DATE, time_spent INT)")

    def update(self, date, column, value):
        self.cursor.execute("UPDATE Days SET "+ column +"= :value WHERE date = :date", 
                            {"value": value, "date": date})

    def row_exists(self, today):
        self.cursor.execute("SELECT 1 FROM Days WHERE date =:date", {"date": today})
        return self.cursor.fetchone() is not None

    def create_row(self, today):
        if not self.row_exists(today):
            self.cursor.execute("INSERT INTO Days VALUES (:today, 0)", {"today": today})
