import re
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class AddClassWindow():
    def __init__(self, database, root, application):
        self.root = root
        self.root.config(background="#FFFFFF")

        self.application = application
        self.database = database

        self.eventNameVar = tk.StringVar()
        self.eventStartVar = tk.StringVar()
        self.eventEndVar = tk.StringVar()
        self.eventDateVar = tk.StringVar()
        self.eventPlatformVar = tk.StringVar()
        self.eventUrlVar = tk.StringVar()

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

        self.eventPlatformLabel = tk.Label(self.root, text="Platform: ").grid(row=4, column=0)
        self.eventPlatformCombo = ttk.Combobox(self.root, textvariable=self.eventPlatformVar)
        self.eventPlatformCombo['values'] = ('Zoom',
                                         'Microsoft Teams',
                                         'Upel',
                                         'Webex')
        self.eventPlatformCombo.grid(row=4, column=1)

        self.eventUrlLabel = tk.Label(self.root, text="URL: ").grid(row=5, column=0)
        self.eventUrlEntry = tk.Entry(self.root, textvariable=self.eventUrlVar)
        self.eventUrlEntry.grid(row=5, column=1)

        self.addToDatabaseButton = tk.Button(self.root, text="Add", bd=1, bg='#b7c8c9', activebackground='#94a0a1',
                                        command=lambda:self.gettingStrings())
        self.addToDatabaseButton.grid(row=6, column=0)

    def gettingStrings(self):
        self.eventNameVar = self.eventNameEntry.get()
        self.eventStartVar = self.eventStartEntry.get()
        self.eventEndVar = self.eventEndEntry.get()
        self.eventDateVar = self.eventDateCombo.get()
        self.eventPlatformVar = self.eventPlatformCombo.get()
        self.eventUrlVar = self.eventUrlEntry.get()

        #if self.dateChecker() and self.platformChecker():
        self.database.addingToDatabase(self.eventNameVar, self.eventStartVar, self.eventEndVar, self.eventDateVar, self.eventPlatformVar, self.eventUrlVar)
        self.clearWindow()

    def dateChecker(self):
        if (len(self.eventStartVar) == 4 or len(self.eventStartVar) == 5) and len(self.eventEndVar) == 5:
            pattern = '([0-9]+):([0-9]+)'
            if re.match(pattern, self.eventStartVar) and re.match(pattern, self.eventEndVar):
                return True
            else:
                messagebox.showinfo("Error", "Incorrect time of start or end")
                return False
        else:
            messagebox.showinfo("Error", "Incorrect time of start or end")
            return False

    def platformChecker(self):
        if self.eventPlatformVar == 'Zoom':
            pattern = '(https://zoom.us)(.+[0-9a-zA-Z])'
            if re.match(pattern, self.eventUrlVar):
                return True
            else:
                messagebox.showinfo("Error", "Incorrect URL")
                return False
        elif self.eventPlatformVar == 'Microsoft Teams':
            pattern = '(https://teams.microsoft.com)(.+[0-9a-zA-Z])'
            if re.match(pattern, self.eventUrlVar):
                return True
            else:
                messagebox.showinfo("Error", "Incorrect URL")
                return False
        elif self.eventPlatformVar == 'Upel':
            pattern = '(https://upel2.cel.agh.edu.pl)(.+[0-9a-zA-Z])'
            if re.match(pattern, self.eventUrlVar):
                return True
            else:
                messagebox.showinfo("Error", "Incorrect URL")
                return False
        elif self.eventPlatformVar == 'Webex':
            pattern = '(https://iet-agh.webex.com)(.+[0-9a-zA-Z])'
            if re.match(pattern, self.eventUrlVar):
                return True
            else:
                messagebox.showinfo("Error", "Incorrect URL")
                return False
        else:
            messagebox.showinfo("Error", "Incorrect URL")
            return False

    def clearWindow(self):
        for child in self.root.winfo_children():
            child.destroy()
        self.application.refreshingWindow(self.root)