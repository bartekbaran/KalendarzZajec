from HomeworkDatabase import *
from tkinter import *

class HomeworkWindow():
    def __init__(self, database, root, application):
        self.root = root
        self.root.config(background="#FFFFFF")

        self.application = application
        self.database = database

        self.homeworkNameVar = StringVar()
        self.homeworkDueToVar = StringVar()
        self.homeworkDescriptionVar = StringVar()

    def settingUpView(self):
        self.homeworkNameLabel = Label(self.root, text="Event name: ").grid(row=0, column=0)
        self.homeworkNameEntry = Entry(self.root, textvariable=self.homeworkNameVar)
        self.homeworkNameEntry.grid(row=0, column=1)

        self.homeworkDueToLabel = Label(self.root, text="Time of start: ").grid(row=1, column=0)
        self.homeworkDueToEntry = Entry(self.root, textvariable=self.homeworkDueToVar)
        self.homeworkDueToEntry.grid(row=1, column=1)

        self.homeworkDescriptionLabel = Label(self.root, text="Day of the Week: ").grid(row=2, column=0)
        self.homeworkDescriptionEntry = Entry(self.root, textvariable=self.homeworkDescriptionVar)
        self.homeworkDescriptionEntry.grid(row=2, column=1)

        # addToDatabaseButton = Button(root, text="Add", command=database.addingToDatabase("Math", "14:40", "16:10", "Wednesday"))
        self.addToDatabaseButton = Button(self.root, text="Add", bd=1, bg='#b7c8c9', activebackground='#94a0a1',
                                        command=lambda:self.gettingStrings())
        self.addToDatabaseButton.grid(row=3, column=0)

    def gettingStrings(self):
        self.homeworkNameVar = self.homeworkNameEntry.get()
        self.homeworkDueToVar = self.homeworkDueToEntry.get()
        self.homeworkDescriptionVar = self.homeworkDescriptionEntry.get()
        self.database.addingToDatabase(self.homeworkNameVar, self.homeworkDueToVar, self.homeworkDescriptionVar)
        self.clearWindow()

    def clearWindow(self):
        for child in self.root.winfo_children():
            child.destroy()
        self.application.refreshingWindow(self.root)