import webbrowser
import os
from tkinter import *
from tkinter.tix import *
import PIL.Image
import PIL.ImageTk

from Databases.HomeworkDatabase import *
from Windows.AddClassWindow import *
from Windows.DeleteClassWindow import *
from Windows.HomeworkWindow import *
from Windows.SettingsWindow import *


class Application():
    def __init__(self):
        self.scheduleDatabase = ScheduleDatabase()
        self.homeworkDatabase = HomeworkDatabase()

        self.colorVersion = "bright"
        self.bgColor = "#FFFFFF"
        self.buttonColor = "#f3f3f3"
        self.textColor = "#000000"
        self.frameColor = "#000000"

        self.root = Tk()
        self.root.title('Corona Calendar')
        self.root.config(background=self.bgColor)
        self.root.geometry("{0}x{1}+0+0".format(self.root.winfo_screenwidth() - 9, self.root.winfo_screenheight() - 7))
        self.root.resizable(False, False)

        self.rootIcon = self.creatingIconImage(self.colorVersion, "rootIcon.png")
        self.root.iconphoto(False, self.rootIcon)

        self.url = ""

        self.settingUpView()


    def settingUpView(self):
        self.root.geometry("1545x830+40+40")
        self.root.config(bg=self.bgColor)



        self.creatingButtonFrame(self.root)
        self.creatingWeekLabelsFrame(self.root)
        self.creatingClassFrame(self.root)

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

        self.homeworkIcon = self.creatingIconImage(self.colorVersion, "homeworkIcon.png")
        homeworkButton = Button(self.buttonFrame, image=self.homeworkIcon, bd=0, padx=1, bg=self.bgColor,
                                command=lambda: self.newWindow(3))
        homeworkButton.grid(row=3, column=0, pady=10)

        setMoreFreeSpace = Label(self.buttonFrame, bg=self.bgColor).grid(row=4, column=0, pady=202)

        self.gitIcon = self.creatingIconImage(self.colorVersion, "gitIcon.png")
        gitButton = Button(self.buttonFrame, image=self.gitIcon, bd=0, bg=self.bgColor,
                           command=lambda url="https://github.com/bartekbaran/KalendarzZajec":self.openApplication(url))
        gitButton.grid(row=5, column=0, pady=10)

        self.questionIcon = self.creatingIconImage(self.colorVersion, "questionIcon.png")
        questionButton = Button(self.buttonFrame, image=self.questionIcon, bd=0, bg=self.bgColor,
                                command=lambda: self.aboutMeMessagebox())
        questionButton.grid(row=6, column=0, pady=10)

        self.settingsIcon = self.creatingIconImage(self.colorVersion, "settingsIcon.png")
        settingsButton = Button(self.buttonFrame, image=self.settingsIcon, bd=0, bg=self.bgColor,
                                command=lambda :self.newWindow(4))
        settingsButton.grid(row=7, column=0, pady=10)

        self.buttonFrame.place(x=0, y=0)

    def creatingWeekLabelsFrame(self, root):

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

        self.weekLabelsFrame.place(x=35, y=0)

    def creatingClassFrame(self, root):

        self.classFrame = Frame(root, bg=self.bgColor)
        self.classFrame.columnconfigure((1, 2, 3, 4, 5, 6, 7, 8, 9, 10), minsize=300)

        self.printingClasses(self.classFrame)

        self.classFrame.place(x=36, y=82)

    def creatingIconImage(self, colorVersion, imagePath):
        self.icon = PIL.ImageTk.PhotoImage(PIL.Image.open(f"images/{colorVersion}/{imagePath}"))
        return self.icon


    def printingClasses(self, frame):
        classLabels = []
        rowCounter = [1, 1, 1, 1, 1]
        listOfClasses = self.scheduleDatabase.sortDatabase()

        for i in range(len(listOfClasses)):
            if listOfClasses[i][4] == 'Monday':
                classLabels.append(Button(frame, text=listOfClasses[i][1] + '\n' + listOfClasses[i][2] + " - " + listOfClasses[i][3] + '\n' + listOfClasses[i][5],
                                          width=33, height=4, font=("Helvetica", 12), bd=0, borderwidth=1, highlightthickness=1, bg=self.buttonColor, fg=self.textColor,
                                          command=lambda url=listOfClasses[i][6]:self.openApplication(url)))
                classLabels[i].grid(row=rowCounter[0], column=1)
                rowCounter[0] += 1
            elif listOfClasses[i][4] == 'Tuesday':
                classLabels.append(Button(frame, text=listOfClasses[i][1] + '\n' + listOfClasses[i][2] + " - " + listOfClasses[i][3] + '\n' + listOfClasses[i][5],
                                          width=33, height=4, font=("Helvetica", 12), bd=0, borderwidth=1, highlightthickness=1, bg=self.buttonColor, fg=self.textColor,
                                          command=lambda url=listOfClasses[i][6]:self.openApplication(url)))
                classLabels[i].grid(row=rowCounter[1], column=2)
                rowCounter[1] += 1
            elif listOfClasses[i][4] == 'Wednesday':
                classLabels.append(Button(frame, text=listOfClasses[i][1] + '\n' + listOfClasses[i][2] + " - " + listOfClasses[i][3] + '\n' + listOfClasses[i][5],
                                          width=33, height=4, font=("Helvetica", 12), bd=0, borderwidth=1, highlightthickness=1, bg=self.buttonColor, fg=self.textColor,
                                          command=lambda url=listOfClasses[i][6]:self.openApplication(url)))
                classLabels[i].grid(row=rowCounter[2], column=3)
                rowCounter[2] += 1
            elif listOfClasses[i][4] == 'Thursday':
                classLabels.append(Button(frame, text=listOfClasses[i][1] + '\n' + listOfClasses[i][2] + " - " + listOfClasses[i][3] + '\n' + listOfClasses[i][5],
                                          width=33, height=4, font=("Helvetica", 12), bd=0, borderwidth=1, highlightthickness=1, bg=self.buttonColor, fg=self.textColor,
                                          command=lambda url=listOfClasses[i][6]:self.openApplication(url)))
                classLabels[i].grid(row=rowCounter[3], column=4)
                rowCounter[3] += 1
            elif listOfClasses[i][4] == 'Friday':
                classLabels.append(Button(frame, text=listOfClasses[i][1] + '\n' + listOfClasses[i][2] + " - " + listOfClasses[i][3] + '\n' + listOfClasses[i][5],
                                          width=33, height=4, font=("Helvetica", 12), bd=0, borderwidth=1, highlightthickness=1, bg=self.buttonColor, fg=self.textColor,
                                          command=lambda url=listOfClasses[i][6]:self.openApplication(url)))
                classLabels[i].grid(row=rowCounter[4], column=5)
                rowCounter[4] += 1


    def newWindow(self, id):
        self.clearWindow()
        if id == 1:
            newWindow = AddClassWindow(self.scheduleDatabase, self.root, self)
        elif id == 2:
            newWindow = DeleteClassWindow(self.scheduleDatabase, self.root, self)
        elif id == 3:
            newWindow = HomeworkWindow(self.homeworkDatabase, self.root, self)
        elif id == 4:
            newWindow = SettingsWindow(self.root, self)
        else:
            print("Placeholder")
        newWindow.settingUpView()


    def clearWindow(self):
        for child in self.root.winfo_children():
            child.destroy()

    def colorModeChanger(self):
        colorSettings = open("colorSettings.txt", "r")
        for line in colorSettings.readlines():
            print(line)
            if str(line) == "bright":
                self.colorVersion = "bright"
                self.bgColor = "#FFFFFF"
                self.buttonColor = "#f3f3f3"
                self.textColor = "#000000"
                self.frameColor ="#000000"
            elif str(line) == "dark":
                self.colorVersion = "dark"
                self.bgColor = "#000000"
                self.buttonColor = "#35393C"
                self.textColor = "pink"
                self.frameColor = "#FFFFFF"
        colorSettings.close()

    def openApplication(self, url):
        settingsFile = open("settings.txt", "r")
        for line in settingsFile.readlines():
            if str(line[:5]) == "Path:":
                print(line[5:len(line)-1])
                self.path = line[5:len(line)-1]
        webbrowser.register('chrome',
                            None,
                            webbrowser.BackgroundBrowser(
                                f'{self.path}'))
        webbrowser.get('chrome').open(url)

    def aboutMeMessagebox(self):
        messagebox.showinfo("AboutME", "This app was created by Bartosz Baran and Piotr Ziemba. BBKB")

    def refreshingWindow(self, root):
        self.root = root
        self.colorModeChanger()
        self.settingUpView()


    def start(self):
        self.root.mainloop()