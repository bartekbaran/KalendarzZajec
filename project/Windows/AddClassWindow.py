import re
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import PIL.Image
import PIL.ImageTk

class AddClassWindow():
    def __init__(self, database, root, application):
        self.root = root

        self.application = application
        self.database = database

        self.colorVersion = application.colorVersion
        self.bgColor = application.bgColor
        self.buttonColor = application.buttonColor
        self.textColor = application.textColor
        self.frameColor = application.frameColor

        self.root.config(background=self.bgColor)

        self.eventNameVar = tk.StringVar()
        self.eventStartVar = tk.StringVar()
        self.eventEndVar = tk.StringVar()
        self.eventDateVar = tk.StringVar()
        self.eventPlatformVar = tk.StringVar()
        self.eventUrlVar = tk.StringVar()

    def settingUpView(self):
        self.root.geometry('400x330+700+300')
        self.root.configure(bg=self.bgColor)

        self.formTitle = tk.Label(self.root, text=" Adding new class", font=("Helvetica", 24), bg=self.bgColor, fg=self.textColor,
                                  pady=20).grid(row=0, columnspan=2)

        self.eventNameEntry = tk.Entry(self.root, textvariable=self.eventNameVar, width=60, bg=self.bgColor, fg=self.textColor)
        self.eventNameEntry.insert(0, "                                       --Insert event name--")
        self.eventNameEntry.grid(row=1, column=0, columnspan=2, pady=5, padx=15)

        self.eventStartEntry = tk.Entry(self.root, textvariable=self.eventStartVar, bg=self.bgColor, fg=self.textColor)
        self.eventStartEntry.insert(0, " --Insert time of start-- ")
        self.eventStartEntry.grid(row=2, column=0, pady=5)

        self.eventEndEntry = tk.Entry(self.root, textvariable=self.eventEndVar, bg=self.bgColor, fg=self.textColor)
        self.eventEndEntry.insert(0, " --Insert time of end-- ")
        self.eventEndEntry.grid(row=2, column=1, pady=5)

        self.eventDateCombo = ttk.Combobox(self.root, textvariable=self.eventDateVar, width=40)
        self.eventDateCombo.insert(0, "                       --Select day of a class--")
        self.eventDateCombo['values'] = ('Monday',
                                         'Tuesday',
                                         'Wednesday',
                                         'Thursday',
                                         'Friday')
        self.eventDateCombo.grid(row=3, column=0, columnspan=2, pady=5)

        self.eventPlatformCombo = ttk.Combobox(self.root, textvariable=self.eventPlatformVar, width=40)
        self.eventPlatformCombo.insert(0, "                       --Choose platform--")
        self.eventPlatformCombo['values'] = ('Zoom',
                                             'Microsoft Teams',
                                             'Upel',
                                             'Webex')
        self.eventPlatformCombo.grid(row=4, column=0, columnspan=2, pady=5)

        self.eventUrlEntry = tk.Entry(self.root, textvariable=self.eventUrlVar, width=60, bg=self.bgColor, fg=self.textColor)
        self.eventUrlEntry.insert(0, "                                             --Insert URL--")
        self.eventUrlEntry.grid(row=5, column=0, columnspan=2, pady=5)

        self.addClassIcon = self.creatingIconImage(self.colorVersion, "addClassIcon.png")
        self.addToDatabaseButton = tk.Button(self.root, image=self.addClassIcon, bd=0, bg=self.bgColor,
                                             command=lambda: self.gettingStrings())
        self.addToDatabaseButton.grid(row=7, column=1, pady=20)

        self.backToMainMenuIcon = self.creatingIconImage(self.colorVersion, "backIcon.png")
        self.backToMainWindowButton = tk.Button(self.root, image=self.backToMainMenuIcon, bd=0, bg=self.bgColor,
                                                command=lambda: self.clearWindow())
        self.backToMainWindowButton.grid(row=7, column=0, pady=20)

    def creatingIconImage(self, colorVersion, imagePath):
        self.icon = PIL.ImageTk.PhotoImage(PIL.Image.open(f"images/{colorVersion}/{imagePath}"))
        return self.icon

    def isNull(self):
        if len(self.eventNameVar) == 0 or len(self.eventStartVar) == 0 or len(self.eventEndVar) == 0 or len(self.eventDateVar) == 0 or len(self.eventPlatformVar) == 0 or len(self.eventUrlVar) == 0:
            return False
        else:
            return True

    def gettingStrings(self):
        self.eventNameVar = self.eventNameEntry.get()
        self.eventStartVar = self.eventStartEntry.get()
        self.eventEndVar = self.eventEndEntry.get()
        self.eventDateVar = self.eventDateCombo.get()
        self.eventPlatformVar = self.eventPlatformCombo.get()
        self.eventUrlVar = self.eventUrlEntry.get()

        if self.isNull():
            if self.dateChecker() and self.platformChecker():
                self.database.addingToDatabase(self.eventNameVar, self.eventStartVar, self.eventEndVar,
                                               self.eventDateVar, self.eventPlatformVar, self.eventUrlVar)
                self.clearWindow()
        else:
            messagebox.showinfo("Error", "Incorrect entries")

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