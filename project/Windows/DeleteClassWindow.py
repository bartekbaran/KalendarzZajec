from project.Databases.ScheduleDatabase import *
from tkinter import *
import PIL.Image
import PIL.ImageTk

class DeleteClassWindow():
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
        self.root.attributes("-alpha", 1)
        self.settingUpView()

    def settingUpView(self):
        self.root.geometry("1510x800+200+120")

        self.creatingWeekFrame(self.root)
        self.creatingClassesFrame(self.root)
        self.creatingBottomFrame(self.root)

    def creatingWeekFrame(self, root):
        self.weekLabelsFrame = Frame(root, bg=self.bgColor, highlightbackground=self.frameColor, highlightthickness=1)

        self.mondayIcon = self.creatingIconImage(self.colorVersion, "mondayIcon.png")
        mondayLabel = Label(self.weekLabelsFrame, image=self.mondayIcon, bd=0).grid(row=0, column=0, padx=1)

        self.tuesdayIcon = self.creatingIconImage(self.colorVersion, "tuesdayIcon.png")
        tuesdayLabel = Label(self.weekLabelsFrame, image=self.tuesdayIcon, bd=0).grid(row=0, column=1, padx=1)

        self.wednesdayIcon = self.creatingIconImage(self.colorVersion, "wednesdayIcon.png")
        wednesdayLabel = Label(self.weekLabelsFrame, image=self.wednesdayIcon, bd=0).grid(row=0, column=2, padx=1)

        self.thursdayIcon = self.creatingIconImage(self.colorVersion, "thursdayIcon.png")
        thursdayLabel = Label(self.weekLabelsFrame, image=self.thursdayIcon, bd=0).grid(row=0, column=3, padx=1)

        self.fridayIcon = self.creatingIconImage(self.colorVersion, "fridayIcon.png")
        fridayLabel = Label(self.weekLabelsFrame, image=self.fridayIcon, bd=0).grid(row=0, column=4, padx=1)

        self.weekLabelsFrame.place(x=0, y=0)

    def creatingClassesFrame(self, root):
        self.classesFrame = Frame(root, bg=self.bgColor)
        self.classesFrame.columnconfigure((1, 2, 3, 4, 5, 6, 7, 8, 9, 10), minsize=300)

        self.deleteClassButtons = []
        rowCounter = [1, 1, 1, 1, 1]
        listOfClasses = self.database.getDatabase()
        for x in range(len(listOfClasses)):
            if listOfClasses[x][4] == 'Monday':
                self.deleteClassButtons.append(Button(self.classesFrame,
                                                      text=listOfClasses[x][1] + '\n' + listOfClasses[x][2] + " - " +
                                                           listOfClasses[x][3],
                                                      width=33, height=4, font=("Helvetica", 12), bd=0, borderwidth=1, highlightthickness=1,
                                                      bg=self.buttonColor, fg=self.textColor,
                                                      command=lambda button=listOfClasses[x]: self.deleteFromDatabase(
                                                          button)))
                self.deleteClassButtons[x].grid(row=rowCounter[0], column=1)
                rowCounter[0] += 1
            elif listOfClasses[x][4] == 'Tuesday':
                self.deleteClassButtons.append(Button(self.classesFrame,
                                                      text=listOfClasses[x][1] + '\n' + listOfClasses[x][2] + " - " +
                                                           listOfClasses[x][3],
                                                      width=33, height=4, font=("Helvetica", 12), bd=0, borderwidth=1, highlightthickness=1,
                                                      bg=self.buttonColor, fg=self.textColor,
                                                      command=lambda button=listOfClasses[x]: self.deleteFromDatabase(button)))
                self.deleteClassButtons[x].grid(row=rowCounter[1], column=2)
                rowCounter[1] += 1
            elif listOfClasses[x][4] == 'Wednesday':
                self.deleteClassButtons.append(Button(self.classesFrame,
                                                      text=listOfClasses[x][1] + '\n' + listOfClasses[x][2] + " - " +
                                                           listOfClasses[x][3],
                                                      width=33, height=4, font=("Helvetica", 12), bd=0, borderwidth=1, highlightthickness=1,
                                                      bg=self.buttonColor, fg=self.textColor,
                                                      command=lambda button=listOfClasses[x]: self.deleteFromDatabase(button)))
                self.deleteClassButtons[x].grid(row=rowCounter[2], column=3)
                rowCounter[2] += 1
            elif listOfClasses[x][4] == 'Thursday':
                self.deleteClassButtons.append(Button(self.classesFrame,
                                                      text=listOfClasses[x][1] + '\n' + listOfClasses[x][2] + " - " +
                                                           listOfClasses[x][3],
                                                      width=33, height=4, font=("Helvetica", 12), bd=0, borderwidth=1, highlightthickness=1,
                                                      bg=self.buttonColor, fg=self.textColor,
                                                      command=lambda button=listOfClasses[x]: self.deleteFromDatabase(button)))
                self.deleteClassButtons[x].grid(row=rowCounter[3], column=4)
                rowCounter[3] += 1
            elif listOfClasses[x][4] == 'Friday':
                self.deleteClassButtons.append(Button(self.classesFrame,
                                                      text=listOfClasses[x][1] + '\n' + listOfClasses[x][2] + " - " +
                                                           listOfClasses[x][3],
                                                      width=33, height=4, font=("Helvetica", 12), bd=0, borderwidth=1, highlightthickness=1,
                                                      bg=self.buttonColor, fg=self.textColor,
                                                      command=lambda button=listOfClasses[x]: self.deleteFromDatabase(button)))
                self.deleteClassButtons[x].grid(row=rowCounter[4], column=5)
                rowCounter[4] += 1

        self.classesFrame.place(x=0, y=82)

    def creatingBottomFrame(self, root):
        self.bottomFrame = Frame(root, bg=self.bgColor, highlightbackground=self.frameColor, highlightthickness=1)
        self.bottomFrame.columnconfigure(0, minsize=1478)
        self.bottomFrame.columnconfigure(1, minsize=32)
        self.bottomFrame.rowconfigure(0, minsize=35)

        self.backToMainMenuIcon = self.creatingIconImage(self.colorVersion, "smallBackIcon.png")
        self.backToMainWindowButton = Button(self.bottomFrame, image=self.backToMainMenuIcon, bd=0, bg=self.bgColor,
                                                command=lambda: self.clearWindow())
        self.backToMainWindowButton.grid(column=1)

        self.bottomFrame.place(x=0, y=765)

    def creatingIconImage(self, colorVersion, imagePath):
        self.icon = PIL.ImageTk.PhotoImage(PIL.Image.open(f"images/{colorVersion}/{imagePath}"))
        return self.icon

    def deleteFromDatabase(self, string):
        self.database.deleteFromDatabase(string[1], string[2], string[3], string[4])
        self.clearWindow()

    def clearWindow(self):
        for child in self.root.winfo_children():
            child.destroy()
        self.application.refreshingWindow(self.root)