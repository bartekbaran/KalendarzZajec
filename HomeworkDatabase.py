from turtle import pd
import pyodbc

class HomeworkDatabase():
    def __init__(self):
        self.connectionString = (
            r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
            r'DBQ=C:\Users\barte\Documents\GitHub\Kalendarz\homework.accdb;'
        )
        self.homeworkConnection = pyodbc.connect(self.connectionString, autocommit=True)
        self.homeworkCursor = self.homeworkConnection.cursor()
        # self.printDatabase()

    def printDatabase(self):
        self.homeworkCursor.execute('Select * from Homework')
        for row in self.homeworkCursor.fetchall():
            print(row)

    def getDatabase(self):
        listOfClasses = []
        self.homeworkCursor.execute('Select * from Homework')
        for row in self.homeworkCursor.fetchall():
            listOfClasses.append(row)
        return listOfClasses

    def getNumberOfRecords(self):
        self.homeworkCursor.execute('Select * from Homework')
        rows = self.homeworkCursor.fetchall()
        return len(rows)

    def addingToDatabase(self, name, dueTo, desc):
        print(name, dueTo, desc)
        self.homeworkCursor.execute("INSERT INTO Homework (Task, DueTo, Description) VALUES (?, ?, ?)",
                            (name, dueTo, desc))
        self.homeworkCursor.commit()

    def deleteFromDatabase(self, task, dueTo, desc):
        self.homeworkCursor.execute("DELETE FROM Homework WHERE Task=(?) AND DueTo=(?) AND Description=(?)", (task), (dueTo),
                            (desc))
        self.homeworkCursor.commit()

    def __del__(self):
        self.homeworkCursor.close()
        self.homeworkConnection.close()