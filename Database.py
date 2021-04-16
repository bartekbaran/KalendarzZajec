from turtle import pd
import pyodbc

class Database():
    def __init__(self):
        self.connectionString = (
            r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
            r'DBQ=C:\Users\barte\Documents\GitHub\KalendarzZajec\schedule.accdb;'
        )
        self.connection = pyodbc.connect(self.connectionString, autocommit=True)
        self.cursor = self.connection.cursor()
        self.printDatabase()

    def printDatabase(self):
        self.cursor.execute('Select * from LessonSchedule')
        for row in self.cursor.fetchall():
            print(row)

    def addingToDatabase(self, les, sta, end, dotw):
        self.cursor.execute("INSERT INTO LessonSchedule (Lesson, Start, End, DayOfTheWeek) VALUES (?, ?, ?, ?)",
                       (les, sta, end, dotw,))
        self.cursor.commit()

    def __del__(self):
        print("Destruktor")
        self.cursor.close()
        self.connection.close()