import webbrowser

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

        self.root = Tk()
        self.root.title('Corona Calendar')
        self.root.config(background="#FFFFFF")
        self.root.geometry("{0}x{1}+0+0".format(self.root.winfo_screenwidth() - 9, self.root.winfo_screenheight() - 7))
        self.root.resizable(False, False)

        self.rootIcon = self.creatingIconImage("rootIcon.png")
        self.root.iconphoto(False, self.rootIcon)

        self.url = ""

        self.settingUpView()


    def settingUpView(self):
        self.root.geometry("1545x830+40+40")
        self.root.config(bg="#FFFFFF")

        self.creatingButtonFrame(self.root)
        self.creatingWeekLabelsFrame(self.root)
        self.creatingClassFrame(self.root)

    def creatingButtonFrame(self, root):
        self.buttonFrame = Frame(root, bg="#FFFFFF", highlightbackground="black", highlightthickness=1)

        setFreeSpace = Label(self.buttonFrame, bg="#FFFFFF").grid(row=0, column=0, pady=30)

        self.addClassIcon = self.creatingIconImage("addIcon.png")
        addingClassButton = Button(self.buttonFrame, image=self.addClassIcon, bd=0, padx=1, bg="#FFFFFF",
                                command=lambda: self.newWindow(1))
        addingClassButton.grid(row=1, column=0, pady=10)

        self.deleteClassIcon = self.creatingIconImage("deleteIcon.png")
        deleteClassButton = Button(self.buttonFrame, text="Delete class", image=self.deleteClassIcon, bd=0, padx=1, bg="#FFFFFF",
                                command=lambda: self.newWindow(2))
        deleteClassButton.grid(row=2, column=0, pady=10)

        self.homeworkIcon = self.creatingIconImage("homeworkIcon.png")
        homeworkButton = Button(self.buttonFrame, image=self.homeworkIcon, bd=0, padx=1, bg="#FFFFFF",
                                command=lambda: self.newWindow(3))
        homeworkButton.grid(row=3, column=0, pady=10)

        setMoreFreeSpace = Label(self.buttonFrame, bg="#FFFFFF").grid(row=4, column=0, pady=202)

        self.gitIcon = self.creatingIconImage("gitIcon.png")
        gitButton = Button(self.buttonFrame, image=self.gitIcon, bd=0, bg="#FFFFFF",
                           command=lambda url="https://github.com/bartekbaran/KalendarzZajec":self.openApplication(url))
        gitButton.grid(row=5, column=0, pady=10)

        self.questionIcon = self.creatingIconImage("questionIcon.png")
        questionButton = Button(self.buttonFrame, image=self.questionIcon, bd=0, bg="#FFFFFF")
        questionButton.grid(row=6, column=0, pady=10)

        self.settingsIcon = self.creatingIconImage("settingsIcon.png")
        settingsButton = Button(self.buttonFrame, image=self.settingsIcon, bd=0, bg="#FFFFFF",
                                command=lambda :self.newWindow(4))
        settingsButton.grid(row=7, column=0, pady=10)

        self.buttonFrame.place(x=0, y=0)

    def creatingWeekLabelsFrame(self, root):
        self.weekLabelsFrame = Frame(root, bg="#FFFFFF", highlightbackground="black", highlightthickness=1)

        self.mondayIcon = self.creatingIconImage("mondayIcon.png")
        mondayLabel = Label(self.weekLabelsFrame, image=self.mondayIcon, bd=0).grid(row=0, column=0, padx=1)

        self.tuesdayIcon = self.creatingIconImage("tuesdayIcon.png")
        tuesdayLabel = Label(self.weekLabelsFrame, image=self.tuesdayIcon, bd=0).grid(row=0, column=1, padx=1)

        self.wednesdayIcon = self.creatingIconImage("wednesdayIcon.png")
        wednesdayLabel = Label(self.weekLabelsFrame, image=self.wednesdayIcon, bd=0).grid(row=0, column=2, padx=1)

        self.thursdayIcon = self.creatingIconImage("thursdayIcon.png")
        thursdayLabel = Label(self.weekLabelsFrame, image=self.thursdayIcon, bd=0).grid(row=0, column=3, padx=1)

        self.fridayIcon = self.creatingIconImage("fridayIcon.png")
        fridayLabel = Label(self.weekLabelsFrame, image=self.fridayIcon, bd=0).grid(row=0, column=4, padx=1)

        self.weekLabelsFrame.place(x=35, y=0)

    def creatingClassFrame(self, root):
        self.classFrame = Frame(root, bg="#FFFFFF")
        self.classFrame.columnconfigure((1, 2, 3, 4, 5, 6, 7, 8, 9, 10), minsize=300)

        self.printingClasses(self.classFrame)

        self.classFrame.place(x=36, y=82)

    def creatingIconImage(self, imagePath):
        self.icon = PIL.ImageTk.PhotoImage(PIL.Image.open(f"images/{imagePath}"))
        return self.icon


    def printingClasses(self, frame):
        classLabels = []
        rowCounter = [1, 1, 1, 1, 1]
        listOfClasses = self.scheduleDatabase.sortDatabase()

        for i in range(len(listOfClasses)):
            if listOfClasses[i][4] == 'Monday':
                classLabels.append(Button(frame, text=listOfClasses[i][1] + '\n' + listOfClasses[i][2] + " - " + listOfClasses[i][3] + '\n' + listOfClasses[i][5],
                                          width=33, height=4, font=("Helvetica", 12), bd=0, borderwidth=1, highlightthickness=1,
                                          command=lambda url=listOfClasses[i][6]:self.openApplication(url)))
                classLabels[i].grid(row=rowCounter[0], column=1)
                rowCounter[0] += 1
            elif listOfClasses[i][4] == 'Tuesday':
                classLabels.append(Button(frame, text=listOfClasses[i][1] + '\n' + listOfClasses[i][2] + " - " + listOfClasses[i][3] + '\n' + listOfClasses[i][5],
                                          width=33, height=4, font=("Helvetica", 12), bd=0, borderwidth=1, highlightthickness=1,
                                          command=lambda url=listOfClasses[i][6]:self.openApplication(url)))
                classLabels[i].grid(row=rowCounter[1], column=2)
                rowCounter[1] += 1
            elif listOfClasses[i][4] == 'Wednesday':
                classLabels.append(Button(frame, text=listOfClasses[i][1] + '\n' + listOfClasses[i][2] + " - " + listOfClasses[i][3] + '\n' + listOfClasses[i][5],
                                          width=33, height=4, font=("Helvetica", 12), bd=0, borderwidth=1, highlightthickness=1,
                                          command=lambda url=listOfClasses[i][6]:self.openApplication(url)))
                classLabels[i].grid(row=rowCounter[2], column=3)
                rowCounter[2] += 1
            elif listOfClasses[i][4] == 'Thursday':
                classLabels.append(Button(frame, text=listOfClasses[i][1] + '\n' + listOfClasses[i][2] + " - " + listOfClasses[i][3] + '\n' + listOfClasses[i][5],
                                          width=33, height=4, font=("Helvetica", 12), bd=0, borderwidth=1, highlightthickness=1,
                                          command=lambda url=listOfClasses[i][6]:self.openApplication(url)))
                classLabels[i].grid(row=rowCounter[3], column=4)
                rowCounter[3] += 1
            elif listOfClasses[i][4] == 'Friday':
                classLabels.append(Button(frame, text=listOfClasses[i][1] + '\n' + listOfClasses[i][2] + " - " + listOfClasses[i][3] + '\n' + listOfClasses[i][5],
                                          width=33, height=4, font=("Helvetica", 12), bd=0, borderwidth=1, highlightthickness=1,
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


    def openApplication(self, url):
        webbrowser.register('chrome',
                            None,
                            webbrowser.BackgroundBrowser(
                                "C:\Program Files\Google\Chrome\Application\chrome.exe"))
        webbrowser.get('chrome').open(url)


    def refreshingWindow(self, root):
        self.root = root
        self.root.config(background="#FFFFFF")
        self.settingUpView()


    def start(self):
        self.root.mainloop()