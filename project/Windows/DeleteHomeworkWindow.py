from tkinter import *
import PIL.Image
import PIL.ImageTk

class DeleteHomeworkWindow():
    def __init__(self, database, root, application):
        self.root = root

        self.colorVersion = application.colorVersion
        self.bgColor = application.bgColor
        self.buttonColor = application.buttonColor
        self.textColor = application.textColor
        self.frameColor = application.frameColor

        self.root.config(background=self.bgColor)

        self.application = application
        self.database = database

    def settingUpView(self):
        self.root.geometry("1100x880+400+40")

        self.creatingTitleFrame(self.root)
        self.creatingHomeworkFrame(self.root)
        self.creatingBottomFrame(self.root)


    def creatingTitleFrame(self, root):
        self.titleFrame = Frame(root, bg=self.bgColor, highlightbackground=self.frameColor, highlightthickness=1)
        self.titleFrame.columnconfigure(0, minsize=1100)
        self.title = Label(self.titleFrame, text="Homework", font=("Helvetica", 24), bg=self.bgColor, fg=self.textColor,
                                  pady=20).grid()

        self.titleFrame.place(x=0, y=0)

    def creatingHomeworkFrame(self, root):
        self.homeworkFrame = Frame(root, bg=self.bgColor)
        self.homeworkFrame.rowconfigure((0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10), minsize=80)
        self.loadingClassesToFrame(self.homeworkFrame)

        self.homeworkFrame.place(x=0, y=82)

    def creatingBottomFrame(self, root):
        self.bottomFrame = Frame(root, bg=self.bgColor, highlightbackground=self.frameColor, highlightthickness=1)
        self.bottomFrame.columnconfigure(0, minsize=1068)
        self.bottomFrame.columnconfigure(1, minsize=32)
        self.bottomFrame.rowconfigure(0, minsize=35)

        self.backToMainMenuIcon = self.creatingIconImage(self.colorVersion, "smallBackIcon.png")
        self.backToMainWindowButton = Button(self.bottomFrame, image=self.backToMainMenuIcon, bd=0, bg=self.bgColor,
                                                command=lambda: self.getBack())
        self.backToMainWindowButton.grid(column=1)

        self.bottomFrame.place(x=0, y=845)

    def loadingClassesToFrame(self, frame):
        homeworkLabels = []
        rowCounter = 0
        listOfHomework = self.database.sortDatabase()

        for i in range(len(listOfHomework)):
            homeworkLabels.append(Button(frame,
                                         text=listOfHomework[i][1] + '\n' + 'Due to: ' + listOfHomework[i][2] + '\n' +
                                              listOfHomework[i][3],
                                         height=4, width=122, bd=0, padx=1, font=("Helvetica", 12), bg=self.buttonColor, fg=self.textColor,
                                         highlightcolor=self.frameColor, borderwidth=1, highlightthickness=1,
                                         command=lambda button=listOfHomework[i]: self.deleteFromDatabase(button)))
            homeworkLabels[i].grid(row=rowCounter, column=5)
            rowCounter += 1


    def creatingIconImage(self, colorVersion, imagePath):
        self.icon = PIL.ImageTk.PhotoImage(PIL.Image.open(f"images/{colorVersion}/{imagePath}"))
        return self.icon


    def deleteFromDatabase(self, button):
        print(button[1], button[2], button[3])
        self.database.deleteFromDatabase(button[1], button[2], button[3])
        self.getBack()

    def getBack(self):
        for child in self.root.winfo_children():
            child.destroy()
        self.application.refreshingWindow(self.root)