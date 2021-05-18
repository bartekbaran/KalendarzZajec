from turtle import pd
import pyodbc
import os

class HomeworkDatabase():
    def __init__(self):
        DIR = os.path.dirname(os.path.abspath(__file__)) + "\homework.accdb;"
        self.connectionString = (
            r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
            r'DBQ='+DIR
        )
        self.homeworkConnection = pyodbc.connect(self.connectionString, autocommit=True)
        self.homeworkCursor = self.homeworkConnection.cursor()
        try:
            self.homeworkCursor.execute('CREATE TABLE Homework (id autoincrement, Task varchar(50), DueTo varchar(50), Description varchar(255))')
            self.homeworkCursor.commit()
        except:
            print("Table already exists!")

    def printDatabase(self):
        self.homeworkCursor.execute('SELECT * FROM Homework')
        for row in self.homeworkCursor.fetchall():
            print(row)

    def sortDatabase(self):
        listOfClasses = []
        self.homeworkCursor.execute('SELECT * FROM Homework')
        for row in self.homeworkCursor.fetchall():
            listOfClasses.append(row)
        return listOfClasses

    def getNumberOfRecords(self):
        self.homeworkCursor.execute('SELECT * FROM Homework')
        rows = self.homeworkCursor.fetchall()
        return len(rows)

    def addingToDatabase(self, name, dueTo, desc):
        print(name, dueTo, desc)
        self.homeworkCursor.execute('INSERT INTO Homework (Task, DueTo, Description) VALUES (?, ?, ?)',
                            (name, dueTo, desc))
        self.homeworkCursor.commit()

    def deleteFromDatabase(self, task, dueTo, desc):
        self.homeworkCursor.execute('DELETE FROM Homework WHERE Task=(?) AND DueTo=(?) AND Description=(?)', (task, dueTo, desc))
        self.homeworkCursor.commit()

    def __del__(self):
        self.homeworkCursor.close()
        self.homeworkConnection.close()