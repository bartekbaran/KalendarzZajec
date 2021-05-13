from turtle import pd
import pyodbc
import os

class ScheduleDatabase():
    def __init__(self):
        DIR = os.path.dirname(os.path.abspath(__file__)) + "\schedule.accdb;"
        self.connectionString = (
            r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
            r'DBQ='+DIR
        )
        self.scheduleConnection = pyodbc.connect(self.connectionString, autocommit=True)
        self.scheduleCursor = self.scheduleConnection.cursor()
        try:
            self.scheduleCursor.execute("""CREATE TABLE LessonSchedule (id autoincrement, Lesson varchar(50), TimeOfStart varchar(50), TimeOfEnd varchar(50), DayOfTheWeek varchar(50))""")
            self.scheduleCursor.commit()
        except:
            print("Tabela juz istnieje!")


    def printDatabase(self):
        self.scheduleCursor.execute("SELECT * FROM LessonSchedule")
        for row in self.cursor.fetchall():
            print(row)

    def getDatabase(self):
        listOfClasses = []
        self.scheduleCursor.execute("SELECT * FROM LessonSchedule")
        for row in self.scheduleCursor.fetchall():
            listOfClasses.append(row)
        return listOfClasses

    def getNumberOfRecords(self):
        self.scheduleCursor.execute("SELECT * FROM LessonSchedule")
        rows = self.scheduleCursor.fetchall()
        return len(rows)

    def addingToDatabase(self, les, sta, end, dotw):

        self.scheduleCursor.execute("INSERT INTO LessonSchedule (Lesson, TimeOfStart, TimeOfEnd, DayOfTheWeek) VALUES (?, ?, ?, ?)",
                       (les, sta, end, dotw))
        self.scheduleCursor.commit()

    def deleteFromDatabase(self, name, start, end, dotw):
        self.scheduleCursor.execute("DELETE FROM LessonSchedule WHERE Lesson=(?) AND TimeOfStart=(?) AND TimeOfEnd=(?) AND DayOfTheWeek=(?)", (name, start, end, dotw))

    def sortDatabase(self):
        listOfClasses = []
        self.scheduleCursor.execute('SELECT * FROM LessonSchedule')
        for row in self.scheduleCursor.fetchall():
            listOfClasses.append(row)
        return listOfClasses

    def __del__(self):
        self.scheduleCursor.close()
        self.scheduleConnection.close()