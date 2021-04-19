from turtle import pd
import pyodbc

class ScheduleDatabase():
    def __init__(self):
        self.connectionString = (
            r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
            r'DBQ=C:\Users\barte\Documents\GitHub\Kalendarz\schedule.accdb;'
        )
        self.scheduleConnection = pyodbc.connect(self.connectionString, autocommit=True)
        self.scheduleCursor = self.scheduleConnection.cursor()
        # self.printDatabase()

    def printDatabase(self):
        self.scheduleCursor.execute('Select * from LessonSchedule')
        for row in self.cursor.fetchall():
            print(row)

    def getDatabase(self):
        listOfClasses = []
        self.scheduleCursor.execute('Select * from LessonSchedule')
        for row in self.scheduleCursor.fetchall():
            listOfClasses.append(row)
        return listOfClasses

    def getNumberOfRecords(self):
        self.scheduleCursor.execute('Select * from LessonSchedule')
        rows = self.scheduleCursor.fetchall()
        return len(rows)

    def addingToDatabase(self, les, sta, end, dotw):
        self.scheduleCursor.execute("INSERT INTO LessonSchedule (Lesson, Start, End, DayOfTheWeek) VALUES (?, ?, ?, ?)",
                       (les, sta, end, dotw))
        self.scheduleCursor.commit()

    def deleteFromDatabase(self, name, start, end, dotw):
        self.scheduleCursor.execute("DELETE FROM LessonSchedule WHERE Lesson=(?) AND Start=(?) AND End=(?) AND DayOfTheWeek=(?)", (name), (start), (end), (dotw))

    def __del__(self):
        self.scheduleCursor.close()
        self.scheduleConnection.close()