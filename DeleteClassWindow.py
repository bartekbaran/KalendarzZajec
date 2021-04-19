from ScheduleDatabase import *
from tkinter import *

class DeleteClassWindow():
    def __init__(self, database, root, application):
        self.root = root
        self.root.config(background="#FFFFFF")

        self.application = application
        self.database = database

        self.settingUpView()

    def settingUpView(self):
        week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
        dayOfTheWeekLabel = []
        for i in range(5):
            dayOfTheWeekLabel.append(Label(self.root, text=week[i], width=40, height=10, background="#918f8a"))
            dayOfTheWeekLabel[i].grid(row=0, column=i+1)

        self.deleteClassButtons = []
        rowCounter = [1, 1, 1, 1, 1]
        listOfClasses = self.database.getDatabase()
        for i in range(len(listOfClasses)):
            if listOfClasses[i][4] == 'Monday':
                self.deleteClassButtons.append(Button(self.root, text=listOfClasses[i][1] + '\n' + listOfClasses[i][2] + " - " + listOfClasses[i][3], width=40, height=10, bd=0, command=lambda:self.deleteFromDatabase(listOfClasses[i])))
                self.deleteClassButtons[i].grid(row=rowCounter[0], column=1)
                rowCounter[0] += 1
            elif listOfClasses[i][4] == 'Tuesday':
                self.deleteClassButtons.append(Button(self.root, text=listOfClasses[i][1] + '\n' + listOfClasses[i][2] + " - " + listOfClasses[i][3], width=40, height=10, bd=0, command=lambda:self.deleteFromDatabase(listOfClasses[i])))
                self.deleteClassButtons[i].grid(row=rowCounter[1], column=2)
                rowCounter[1] += 1
            elif listOfClasses[i][4] == 'Wednesday':
                self.deleteClassButtons.append(Button(self.root, text=listOfClasses[i][1] + '\n' + listOfClasses[i][2] + " - " + listOfClasses[i][3], width=40, height=10, bd=0, command=lambda:self.deleteFromDatabase(listOfClasses[i])))
                self.deleteClassButtons[i].grid(row=rowCounter[2], column=3)
                rowCounter[2] += 1
            elif listOfClasses[i][4] == 'Thursday':
                self.deleteClassButtons.append(Button(self.root, text=listOfClasses[i][1] + '\n' + listOfClasses[i][2] + " - " + listOfClasses[i][3], width=40, height=10, bd=0, command=lambda:self.deleteFromDatabase(listOfClasses[i])))
                self.deleteClassButtons[i].grid(row=rowCounter[3], column=4)
                rowCounter[3] += 1
            elif listOfClasses[i][4] == 'Friday':
                self.deleteClassButtons.append(Button(self.root, text=listOfClasses[i][1] + '\n' + listOfClasses[i][2] + " - " + listOfClasses[i][3], width=40, height=10, bd=0, command=lambda:self.deleteFromDatabase(listOfClasses[i])))
                self.deleteClassButtons[i].grid(row=rowCounter[4], column=5)
                rowCounter[4] += 1

    def deleteFromDatabase(self, string):
        self.database.deleteFromDatabase(string[1], string[2], string[3], string[4])
        self.clearWindow()

    def clearWindow(self):
        for child in self.root.winfo_children():
            child.destroy()
        self.application.refreshingWindow(self.root)