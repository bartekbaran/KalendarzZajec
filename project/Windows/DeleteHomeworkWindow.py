from tkinter import *

class DeleteHomeworkWindow():
    def __init__(self, database, root, application):
        self.root = root
        self.root.config(background='#FFFFFF')

        self.application = application
        self.database = database

    def settingUpView(self):
        homeworkLabels = []
        rowCounter = 0
        listOfHomework = self.database.sortDatabase()

        for i in range(len(listOfHomework)):
            homeworkLabels.append(Button(self.root, text=listOfHomework[i][1] + '\n' + 'Due to: ' + listOfHomework[i][2] + '\n' + listOfHomework[i][3],
                                         height=10, width=200, bd=0, padx=1, font=("Helvetica", 10), command=lambda button=listOfHomework[i]:self.deleteFromDatabase(button)))
            homeworkLabels[i].grid(row=rowCounter, column=5)
            rowCounter += 1

    def deleteFromDatabase(self, button):
        print(button[1], button[2], button[3])
        self.database.deleteFromDatabase(button[1], button[2], button[3])
        self.getBack()

    def getBack(self):
        for child in self.root.winfo_children():
            child.destroy()
        self.application.refreshingWindow(self.root)