from tkinter import *
import PIL.Image
import PIL.ImageTk

from Windows.AddHomeworkWindow import *
from Windows.DeleteHomeworkWindow import *

class HomeworkWindow():
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

    def settingUpView(self):
        self.root.geometry("1150x880+400+40")
        self.creatingButtonFrame(self.root)
        self.creatingTitleFrame(self.root)
        self.creatingHomeworkFrame(self.root)

    def creatingButtonFrame(self, root):
        self.buttonFrame = Frame(root, bg=self.bgColor, highlightbackground=self.frameColor, highlightthickness=1)

        setFreeSpace = Label(self.buttonFrame, bg=self.bgColor).grid(row=0, column=0, pady=30)

        self.addClassIcon = self.creatingIconImage(self.colorVersion, "addIcon.png")
        addingClassButton = Button(self.buttonFrame, image=self.addClassIcon, bd=0, padx=1, bg=self.bgColor,
                                command=lambda: self.newWindow(1))
        addingClassButton.grid(row=1, column=0, pady=10)

        self.deleteClassIcon = self.creatingIconImage(self.colorVersion, "deleteIcon.png")
        deleteClassButton = Button(self.buttonFrame, text="Delete class", image=self.deleteClassIcon, bd=0, padx=1, bg=self.bgColor,
                                command=lambda: self.newWindow(2))
        deleteClassButton.grid(row=2, column=0, pady=10)

        setMoreFreeSpace = Label(self.buttonFrame, bg=self.bgColor).grid(row=4, column=0, pady=310)

        self.backIcon = self.creatingIconImage(self.colorVersion, "smallBackIcon.png")
        backButton = Button(self.buttonFrame, image=self.backIcon, bd=0, bg=self.bgColor,
                            command=lambda: self.getBack())
        backButton.grid(row=7, column=0, pady=10)

        self.buttonFrame.place(x=0, y=0)

    def creatingTitleFrame(self, root):
        self.titleFrame = Frame(root, bg=self.bgColor, highlightbackground=self.frameColor, highlightthickness=1)
        self.titleFrame.columnconfigure(0, minsize=1114)
        self.title = Label(self.titleFrame, text="Homework", font=("Helvetica", 24), bg=self.bgColor, fg=self.textColor,
                           pady=20).grid()

        self.titleFrame.place(x=36, y=0)

    def creatingHomeworkFrame(self, root):
        self.homeworkFrame = Frame(root, bg=self.bgColor)
        self.homeworkFrame.rowconfigure((0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10), minsize=80)
        self.printingHomework(self.homeworkFrame)

        self.homeworkFrame.place(x=37, y=82)

    def creatingIconImage(self, colorVersion, imagePath):
        self.icon = PIL.ImageTk.PhotoImage(PIL.Image.open(f"images/{colorVersion}/{imagePath}"))
        return self.icon

    def printingHomework(self, frame):
        homeworkLabels = []
        rowCounter = 0
        listOfHomework = self.database.sortDatabase()

        for i in range(len(listOfHomework)):
            homeworkLabels.append(Label(frame, text=listOfHomework[i][1] + '\n' + 'Due to: ' + listOfHomework[i][2] + '\n' + listOfHomework[i][3],
                                        height=4, width=124, font=("Helvetica", 12), bg=self.buttonColor, fg=self.textColor,
                                        highlightcolor=self.frameColor, borderwidth=1, highlightthickness=1))
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