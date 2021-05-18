import tkinter as tk
from tkcalendar import *

class AddHomeworkWindow():
    def __init__(self, database, root, application):
        self.root = root
        self.root.config(background="#FFFFFF")

        self.application = application
        self.database = database

        self.homeworkNameVar = tk.StringVar()
        self.homeworkDueToVar = tk.StringVar()
        self.homeworkDescriptionVar = tk.StringVar()

    def settingUpView(self):
        self.homeworkNameLabel = tk.Label(self.root, text="Homework name: ").grid(row=0, column=0)
        self.homeworkNameEntry = tk.Entry(self.root, textvariable=self.homeworkNameVar, width=20)
        self.homeworkNameEntry.grid(row=0, column=1)

        self.homeworkDueToLabel = tk.Label(self.root, text="Due to: ").grid(row=1, column=0)
        self.homeworkDueToEntry = DateEntry(self.root, width=18, background='grey', foreground='white', borderwidth=2, textvariable=self.homeworkDueToVar)
        self.homeworkDueToEntry.grid(row=1, column=1)

        self.homeworkDescriptionLabel = tk.Label(self.root, text="Description: ").grid(row=2, column=0)
        self.homeworkDescriptionEntry = tk.Entry(self.root, textvariable=self.homeworkDescriptionVar, width=20)
        self.homeworkDescriptionEntry.grid(row=2, column=1)

        self.addToDatabaseButton = tk.Button(self.root, text="Add", bd=1, bg='#b7c8c9', activebackground='#94a0a1',
                                             command=lambda:self.gettingStrings())
        self.addToDatabaseButton.grid(row=3, columnspan=2)

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