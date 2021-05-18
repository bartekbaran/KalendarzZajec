from tkinter import *

from Windows.AddHomeworkWindow import *
from Windows.DeleteHomeworkWindow import *

class HomeworkWindow():
    def __init__(self, database, root, application):
        self.root = root
        self.root.config(background="#FFFFFF")

        self.application = application
        self.database = database

    def settingUpView(self):
        addingHomeworkButton = Button(self.root, text="Add new homework", width=25, height=10, command=lambda:self.newWindow(1), font=("Helvetica", 10), bd=0, padx=1)
        addingHomeworkButton.grid(row=0, column=0)

        deleteHomeworkButton = Button(self.root, text="Delete homework", width=25, height=10, command=lambda:self.newWindow(2), font=("Helvetica", 10), bd=0, padx=1)
        deleteHomeworkButton.grid(row=1, column=0)

        backButton = Button(self.root, text="Back", width=25, height=10, command=lambda:self.getBack(), font=("Helvetica", 10), bd=0, padx=1)
        backButton.grid(row=2, column=0)

        homeworkLabel = Label(self.root, text="Homework", height=10, width=200, font=("Helvetica", 10), background='#918f8a')
        homeworkLabel.grid(row=0, column=1)

        self.printingHomework()

    def printingHomework(self):
        homeworkLabels = []
        rowCounter = 1
        listOfHomework = self.database.sortDatabase()

        for i in range(len(listOfHomework)):
            homeworkLabels.append(Label(self.root, text=listOfHomework[i][1] + '\n' + 'Due to: ' + listOfHomework[i][2] + '\n' + listOfHomework[i][3], height=10, width=200, font=("Helvetica", 10)))
            homeworkLabels[i].grid(row=rowCounter, column=1)
            rowCounter += 1

    def newWindow(self, id):
        self.clearWindow()
        if id == 1:
            newWindow = AddHomeworkWindow(self.database, self.root, self)
        elif id == 2:
            newWindow = DeleteHomeworkWindow(self.database, self.root, self)
        else:
            print("Placeholder")
        newWindow.settingUpView()

    def refreshingWindow(self, root):
        self.root = root
        self.settingUpView()

    def clearWindow(self):
        for child in self.root.winfo_children():
            child.destroy()

    def getBack(self):
        for child in self.root.winfo_children():
            child.destroy()
        self.application.refreshingWindow(self.root)