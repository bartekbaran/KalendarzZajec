from ScheduleDatabase import *
from HomeworkDatabase import *
from AddClassWindow import *
from DeleteClassWindow import *
from tkinter import *

class Application():
    def __init__(self):
        self.scheduleDatabase = ScheduleDatabase()
        self.homeworkDatabase = HomeworkDatabase()
        self.root = Tk()
        self.root.title('Corona Calendar')
        self.root.config(background="#FFFFFF")
        # self.root.geometry("{0}x{1}+0+0".format(self.root.winfo_screenwidth() - 9, self.root.winfo_screenheight() - 7))
        self.settingUpFirstView()

    def settingUpFirstView(self):
        week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
        dayOfTheWeekLabel = []

        # Creating Buttons visible in the left part of screen
        addingClassButton = Button(self.root, text="Add new class", width=25, height=10, command=lambda:self.newWindow(1))
        addingClassButton.grid(row=0, column=0)

        deleteClassButton = Button(self.root, text="Delete class", width=25, height=10, command=lambda:self.newWindow(2))
        deleteClassButton.grid(row=1, column=0)

        homeworkButton = Button(self.root, text="Homework", width=25, height=10)
        homeworkButton.grid(row=2, column=0)

        goToClassButton = Button(self.root, text="Go to class", width=25, height=10)
        goToClassButton.grid(row=3, column=0)

        changeViewButton = Button(self.root, text="Change view", width=25, height=10)
        changeViewButton.grid(row=4, column=0)

        for i in range(5):
            dayOfTheWeekLabel.append(Label(self.root, text=week[i], width=40, height=10, background="#918f8a"))
            dayOfTheWeekLabel[i].grid(row=0, column=i+1)

        self.printingClasses()

    def printingClasses(self):
        classLabels = []
        rowCounter = [1, 1, 1, 1, 1]
        listOfClasses = self.scheduleDatabase.getDatabase()
        for i in range(len(listOfClasses)):
            if listOfClasses[i][4] == 'Monday':
                classLabels.append(Label(self.root, text=listOfClasses[i][1], width=40, height=10))
                classLabels[i].grid(row=rowCounter[0], column=1)
                rowCounter[0] += 1
            elif listOfClasses[i][4] == 'Tuesday':
                classLabels.append(Label(self.root, text=listOfClasses[i][1], width=40, height=10))
                classLabels[i].grid(row=rowCounter[1], column=2)
                rowCounter[1] += 1
            elif listOfClasses[i][4] == 'Wednesday':
                classLabels.append(Label(self.root, text=listOfClasses[i][1], width=40, height=10))
                classLabels[i].grid(row=rowCounter[2], column=3)
                rowCounter[2] += 1
            elif listOfClasses[i][4] == 'Thursday':
                classLabels.append(Label(self.root, text=listOfClasses[i][1], width=40, height=10))
                classLabels[i].grid(row=rowCounter[3], column=4)
                rowCounter[3] += 1
            elif listOfClasses[i][4] == 'Friday':
                classLabels.append(Label(self.root, text=listOfClasses[i][1], width=40, height=10))
                classLabels[i].grid(row=rowCounter[4], column=5)
                rowCounter[4] += 1

    def newWindow(self, id):
        root = Tk()
        if id == 1:
            newWindow = AddClassWindow(self.scheduleDatabase, root)
        elif id == 2:
            newWindow = DeleteClassWindow(self.scheduleDatabase, root)
        else:
            print("placeholder")
        root.mainloop()

    def start(self):
        self.root.mainloop()