from ScheduleDatabase import *
import tkinter as tk
from tkinter import ttk

class AddClassWindow():
    def __init__(self, database, root):
        self.root = root
        self.root.config(background="#FFFFFF")

        self.database = database

        self.eventNameVar = tk.StringVar()
        self.eventStartVar = tk.StringVar()
        self.eventEndVar = tk.StringVar()
        self.eventDateVar = tk.StringVar()

        self.settingUpView()

    def settingUpView(self):
        self.eventNameLabel = tk.Label(self.root, text="Event name: ").grid(row=0, column=0)
        self.eventNameEntry = tk.Entry(self.root, textvariable=self.eventNameVar)
        self.eventNameEntry.grid(row=0, column=1)

        self.eventStartLabel = tk.Label(self.root, text="Time of start: ").grid(row=1, column=0)
        self.eventStartEntry = tk.Entry(self.root, textvariable=self.eventStartVar)
        self.eventStartEntry.grid(row=1, column=1)

        self.eventEndLabel = tk.Label(self.root, text="End: ").grid(row=2, column=0)
        self.eventEndEntry = tk.Entry(self.root, textvariable=self.eventEndVar)
        self.eventEndEntry.grid(row=2, column=1)

        self.eventDateLabel = tk.Label(self.root, text="Day of the Week: ").grid(row=3, column=0)
        self.eventDateCombo = ttk.Combobox(self.root, textvariable=self.eventDateVar)
        self.eventDateCombo['values'] = ('Monday',
                                    'Tuesday',
                                    'Wednesday',
                                    'Thursday',
                                    'Friday')
        self.eventDateCombo.grid(row=3, column=1)

        # addToDatabaseButton = Button(root, text="Add", command=database.addingToDatabase("Math", "14:40", "16:10", "Wednesday"))
        self.addToDatabaseButton = tk.Button(self.root, text="Add", bd=1, bg='#b7c8c9', activebackground='#94a0a1',
                                        command=lambda:self.gettingStrings())
        self.addToDatabaseButton.grid(row=4, column=0)

    def gettingStrings(self):
        self.eventNameVar = self.eventNameEntry.get()
        self.eventStartVar = self.eventStartEntry.get()
        self.eventEndVar = self.eventEndEntry.get()
        self.eventDateVar = self.eventDateCombo.get()
        self.database.addingToDatabase(self.eventNameVar, self.eventStartVar, self.eventEndVar, self.eventDateVar)
        self.deleteWindow()

    def deleteWindow(self):
        self.root.destroy()