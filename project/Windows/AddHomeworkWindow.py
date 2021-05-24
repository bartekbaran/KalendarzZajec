import tkinter as tk
from tkinter import messagebox

from tkcalendar import *
import PIL.Image
import PIL.ImageTk

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
        self.root.geometry('380x280+700+300')
        self.root.configure(bg="#22333B")

        self.formTitle = tk.Label(self.root, text="Adding homework", font=("Helvetica", 24), bg="#22333B", fg="#FFFFFF").grid(
                                                                                    row=0, columnspan=2, pady=20, padx=10)

        self.homeworkNameEntry = tk.Entry(self.root, textvariable=self.homeworkNameVar, width=40)
        self.homeworkNameEntry.insert(0, "                --Insert homework name--")
        self.homeworkNameEntry.grid(row=1, columnspan=2, pady=5, padx=10)

        self.homeworkDueToEntry = DateEntry(self.root, width=18, background='grey', foreground='white', borderwidth=2, textvariable=self.homeworkDueToVar)
        self.homeworkDueToEntry.insert(0, "--Choose deadline--")
        self.homeworkDueToEntry.grid(row=2, columnspan=2, pady=5, padx=10)

        self.homeworkDescriptionEntry = tk.Entry(self.root, textvariable=self.homeworkDescriptionVar, width=60)
        self.homeworkDescriptionEntry.insert(0, "                                             --Description--")
        self.homeworkDescriptionEntry.grid(row=3, columnspan=2, pady=5, padx=10)

        self.addHomeworkIcon = self.creatingIconImage("addClassIcon.png")
        self.addHomeworkButton = tk.Button(self.root, image=self.addHomeworkIcon, bd=0, bg="#22333B",
                                             command=lambda: self.gettingStrings())
        self.addHomeworkButton.grid(row=7, column=1, pady=20, padx=10)

        self.backToPrevIcon = self.creatingIconImage("backIcon.png")
        self.backToPrevButton = tk.Button(self.root, image=self.backToPrevIcon, bd=0, bg="#22333B",
                                                command=lambda: self.clearWindow())
        self.backToPrevButton.grid(row=7, column=0, pady=20)

    def creatingIconImage(self, imagePath):
        self.icon = PIL.ImageTk.PhotoImage(PIL.Image.open(f"images/{imagePath}"))
        return self.icon


    def isNull(self):
        if len(self.homeworkNameVar) == 0 or len(self.homeworkDueToVar) == 0 or len(self.homeworkDescriptionVar) == 0:
            return False
        else:
            return True

    def gettingStrings(self):
        self.homeworkNameVar = self.homeworkNameEntry.get()
        self.homeworkDueToVar = self.homeworkDueToEntry.get()
        self.homeworkDescriptionVar = self.homeworkDescriptionEntry.get()

        if self.isNull():
            self.database.addingToDatabase(self.homeworkNameVar, self.homeworkDueToVar, self.homeworkDescriptionVar)
            self.clearWindow()
        else:
            messagebox.showinfo("Error", "Incorrect entries")

    def clearWindow(self):
        for child in self.root.winfo_children():
            child.destroy()
        self.application.refreshingWindow(self.root)