from turtle import pd
import pyodbc

class ScheduleDatabase():
    def __init__(self):
        self.connectionString = (
            r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
            r'DBQ=C:\Users\barte\Documents\GitHub\Kalendarz\schedule.accdb;'
        )
        self.connection = pyodbc.connect(self.connectionString, autocommit=True)
        self.cursor = self.connection.cursor()
        # self.printDatabase()

    def printDatabase(self):
        self.cursor.execute('Select * from LessonSchedule')
        for row in self.cursor.fetchall():
            print(row)

    def getDatabase(self):
        listOfClasses = []
        self.cursor.execute('Select * from LessonSchedule')
        for row in self.cursor.fetchall():
            listOfClasses.append(row)
        return listOfClasses

    def getNumberOfRecords(self):
        self.cursor.execute('Select * from LessonSchedule')
        rows = self.cursor.fetchall()
        return len(rows)

    def addingToDatabase(self, les, sta, end, dotw):
        self.cursor.execute("INSERT INTO LessonSchedule (Lesson, Start, End, DayOfTheWeek) VALUES (?, ?, ?, ?)",
                       (les, sta, end, dotw))
        self.cursor.commit()

    def deleteFromDatabase(self, name, start, end, dotw):
        self.cursor.execute("DELETE FROM LessonSchedule WHERE Lesson=(?) AND Start=(?) AND End=(?) AND DayOfTheWeek=(?)", (name), (start), (end), (dotw))
        self.cursor.commmit()

    def __del__(self):
        self.cursor.close()
        self.connection.close()