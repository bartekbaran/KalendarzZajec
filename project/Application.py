import webbrowser

from tkinter import *

from Databases.HomeworkDatabase import *
from Windows.AddClassWindow import *
from Windows.DeleteClassWindow import *
from Windows.HomeworkWindow import *


class Application():
    def __init__(self):
        self.scheduleDatabase = ScheduleDatabase()
        self.homeworkDatabase = HomeworkDatabase()

        self.root = Tk()
        self.root.title('Corona Calendar')
        self.root.config(background="#FFFFFF")
        self.root.geometry("{0}x{1}+0+0".format(self.root.winfo_screenwidth() - 9, self.root.winfo_screenheight() - 7))

        self.url = ""

        self.settingUpFirstView()

    def settingUpFirstView(self):
        week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
        dayOfTheWeekLabel = []

        # Creating Buttons visible in the left part of screen
        addingClassButton = Button(self.root, text="Add new class", width=25, height=10, command=lambda:self.newWindow(1), font=("Helvetica", 10), bd=0, padx=1)
        addingClassButton.grid(row=0, column=0)

        deleteClassButton = Button(self.root, text="Delete class", width=25, height=10, command=lambda:self.newWindow(2), font=("Helvetica", 10), bd=0, padx=1)
        deleteClassButton.grid(row=1, column=0)

        homeworkButton = Button(self.root, text="Homework", width=25, height=10, command=lambda:self.newWindow(3), font=("Helvetica", 10), bd=0, padx=1)
        homeworkButton.grid(row=2, column=0)

        goToClassButton = Button(self.root, text="Go to class", width=25, height=10, command=lambda:self.openApplication(), font=("Helvetica", 10), bd=0, padx=1)
        goToClassButton.grid(row=3, column=0)

        changeViewButton = Button(self.root, text="Change view", width=25, height=10, command=lambda:self.clearWindow(), font=("Helvetica", 10), bd=0, padx=1)
        changeViewButton.grid(row=4, column=0)

        for i in range(5):
            dayOfTheWeekLabel.append(Label(self.root, text=week[i], width=40, height=10, background="#918f8a", font=("Helvetica", 10)))
            dayOfTheWeekLabel[i].grid(row=0, column=i+1)

        self.printingClasses()

    def printingClasses(self):
        classLabels = []
        rowCounter = [1, 1, 1, 1, 1]
        listOfClasses = self.scheduleDatabase.sortDatabase()
        for i in range(len(listOfClasses)):
            if listOfClasses[i][4] == 'Monday':
                classLabels.append(Button(self.root, text=listOfClasses[i][1] + '\n' + listOfClasses[i][2] + " - " + listOfClasses[i][3] + '\n' + listOfClasses[i][5],
                                          width=40, height=10, font=("Helvetica", 10), bd=0, command=lambda url=listOfClasses[i][6]:self.openApplication(url)))
                classLabels[i].grid(row=rowCounter[0], column=1)
                rowCounter[0] += 1
            elif listOfClasses[i][4] == 'Tuesday':
                classLabels.append(Button(self.root, text=listOfClasses[i][1] + '\n' + listOfClasses[i][2] + " - " + listOfClasses[i][3] + '\n' + listOfClasses[i][5],
                                          width=40, height=10, font=("Helvetica", 10), bd=0, command=lambda url=listOfClasses[i][6]:self.openApplication(url)))
                classLabels[i].grid(row=rowCounter[1], column=2)
                rowCounter[1] += 1
            elif listOfClasses[i][4] == 'Wednesday':
                classLabels.append(Button(self.root, text=listOfClasses[i][1] + '\n' + listOfClasses[i][2] + " - " + listOfClasses[i][3] + '\n' + listOfClasses[i][5],
                                          width=40, height=10, font=("Helvetica", 10), bd=0, command=lambda url=listOfClasses[i][6]:self.openApplication(url)))
                classLabels[i].grid(row=rowCounter[2], column=3)
                rowCounter[2] += 1
            elif listOfClasses[i][4] == 'Thursday':
                classLabels.append(Button(self.root, text=listOfClasses[i][1] + '\n' + listOfClasses[i][2] + " - " + listOfClasses[i][3] + '\n' + listOfClasses[i][5],
                                          width=40, height=10, font=("Helvetica", 10), bd=0, command=lambda url=listOfClasses[i][6]:self.openApplication(url)))
                classLabels[i].grid(row=rowCounter[3], column=4)
                rowCounter[3] += 1
            elif listOfClasses[i][4] == 'Friday':
                classLabels.append(Button(self.root, text=listOfClasses[i][1] + '\n' + listOfClasses[i][2] + " - " + listOfClasses[i][3] + '\n' + listOfClasses[i][5],
                                          width=40, height=10, font=("Helvetica", 10), bd=0, command=lambda url=listOfClasses[i][6]:self.openApplication(url)))
                classLabels[i].grid(row=rowCounter[4], column=5)
                rowCounter[4] += 1

    def newWindow(self, id):
        self.clearWindow()
        if id == 1:
            newWindow = AddClassWindow(self.scheduleDatabase, self.root, self)
        elif id == 2:
            newWindow = DeleteClassWindow(self.scheduleDatabase, self.root, self)
        elif id == 3:
            newWindow = HomeworkWindow(self.homeworkDatabase, self.root, self)
        else:
            print("placeholder")
        newWindow.settingUpView()

    def clearWindow(self):
        for child in self.root.winfo_children():
            child.destroy()

    def openApplication(self, url):
        webbrowser.register('chrome',
                            None,
                            webbrowser.BackgroundBrowser(
                                "C:\Program Files\Google\Chrome\Application\chrome.exe"))
        webbrowser.get('chrome').open(url)

    def refreshingWindow(self, root):
        self.root = root
        self.settingUpFirstView()

    def start(self):
        self.root.mainloop()