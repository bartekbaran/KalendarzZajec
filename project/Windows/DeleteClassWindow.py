from project.Databases.ScheduleDatabase import *
from tkinter import *

class DeleteClassWindow():
    def __init__(self, database, root, application):
        self.root = root
        self.root.config(background="#FFFFFF")

        self.application = application
        self.database = database
        self.root.attributes("-alpha", 1)
        self.settingUpView()

    def settingUpView(self):
        week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
        dayOfTheWeekLabel = []
        for x in range(5):
            dayOfTheWeekLabel.append(Label(self.root, text=week[x], width=40, height=10, background="#918f8a"))
            dayOfTheWeekLabel[x].grid(row=0, column=x + 1)

        self.deleteClassButtons = []
        rowCounter = [1, 1, 1, 1, 1]
        listOfClasses = self.database.getDatabase()
        for x in range(len(listOfClasses)):
            if listOfClasses[x][4] == 'Monday':
                self.deleteClassButtons.append(Button(self.root, text=listOfClasses[x][1] + '\n' + listOfClasses[x][2] + " - " + listOfClasses[x][3],
                                                      width=40, height=10, bd=0, command=lambda button=listOfClasses[x]:self.deleteFromDatabase(button)))
                self.deleteClassButtons[x].grid(row=rowCounter[0], column=1)
                rowCounter[0] += 1
            elif listOfClasses[x][4] == 'Tuesday':
                self.deleteClassButtons.append(Button(self.root, text=listOfClasses[x][1] + '\n' + listOfClasses[x][2] + " - " + listOfClasses[x][3],
                                                      width=40, height=10, bd=0, command=lambda button=listOfClasses[x]:self.deleteFromDatabase(button)))
                self.deleteClassButtons[x].grid(row=rowCounter[1], column=2)
                rowCounter[1] += 1
            elif listOfClasses[x][4] == 'Wednesday':
                self.deleteClassButtons.append(Button(self.root, text=listOfClasses[x][1] + '\n' + listOfClasses[x][2] + " - " + listOfClasses[x][3],
                                                      width=40, height=10, bd=0, command=lambda button=listOfClasses[x]:self.deleteFromDatabase(button)))
                self.deleteClassButtons[x].grid(row=rowCounter[2], column=3)
                rowCounter[2] += 1
            elif listOfClasses[x][4] == 'Thursday':
                self.deleteClassButtons.append(Button(self.root, text=listOfClasses[x][1] + '\n' + listOfClasses[x][2] + " - " + listOfClasses[x][3],
                                                      width=40, height=10, bd=0, command=lambda button=listOfClasses[x]:self.deleteFromDatabase(button)))
                self.deleteClassButtons[x].grid(row=rowCounter[3], column=4)
                rowCounter[3] += 1
            elif listOfClasses[x][4] == 'Friday':
                self.deleteClassButtons.append(Button(self.root, text=listOfClasses[x][1] + '\n' + listOfClasses[x][2] + " - " + listOfClasses[x][3],
                                                      width=40, height=10, bd=0, command=lambda button=listOfClasses[x]:self.deleteFromDatabase(button)))
                self.deleteClassButtons[x].grid(row=rowCounter[4], column=5)
                rowCounter[4] += 1

    def deleteFromDatabase(self, string):
        self.database.deleteFromDatabase(string[1], string[2], string[3], string[4])
        self.clearWindow()

    def clearWindow(self):
        for child in self.root.winfo_children():
            child.destroy()
        self.application.refreshingWindow(self.root)