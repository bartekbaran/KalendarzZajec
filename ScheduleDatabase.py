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
        self.cursor.execute('Select * from Homework')
        for row in self.cursor.fetchall():
            print(row)

    def getDatabase(self):
        listOfClasses = []
        self.cursor.execute('Select * from Homework')
        for row in self.cursor.fetchall():
            listOfClasses.append(row)
        return listOfClasses

    def getNumberOfRecords(self):
        self.cursor.execute('Select * from Homework')
        rows = self.cursor.fetchall()
        return len(rows)

    def addingToDatabase(self, les, sta, end, dotw):
        self.cursor.execute("INSERT INTO Homework (Task, DueTo, Description) VALUES (?, ?, ?, ?)",
                       (les, sta, end, dotw))
        self.cursor.commit()

    def deleteFromDatabase(self, task, dueTo, desc):
        self.cursor.execute("DELETE FROM Homework WHERE Task=(?) AND DueTo=(?) AND Description=(?)", (task), (dueTo), (desc))

    def __del__(self):
        self.cursor.close()
        self.connection.close()