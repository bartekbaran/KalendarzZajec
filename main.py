from turtle import pd
import pyodbc
from tkinter import *
from Panel import *

class Application():
    def __init__(self):
        self.root = Tk()
        self.root.title('Application')
        self.root.config(background="#FFFFFF")
        self.root.geometry("{0}x{1}+0+0".format(self.root.winfo_screenwidth() - 9, self.root.winfo_screenheight() - 7))

        self.frameList = []
        self.text = ""

        self.width = (self.root.winfo_screenwidth() - 9) / 5 - 5
        self.height = self.root.winfo_screenheight() - 7

        self.splittingIntoColumns()
        # self.addingTextBox()


    def splittingIntoColumns(self):
        for i in range(5):
            self.leftFrame = Frame(self.root, width=self.width, height=self.height)
            self.frameList.append(self.leftFrame)
            for x in range(10):
                self.leftFrame.grid(row=x, column=i, padx=5, pady=2)
                self.leftFrame.config(background="#F1F1F1")

    def addingTextBox(self):
        self.textBox = Text(self.root, height = 25, width = 50)
        self.label = Label(self.root, text = "Siema")
        self.label.config(font =("Roboto", 20))
        self.button = Button(self.root, height = 2, width = 20, text = "Zapisz", command = lambda:self.takeInput())
        self.textBox.pack()
        self.label.pack()
        self.button.pack()

    def takeInput(self):
        self.INPUT = self.textBox.get("1.0", "end-1c")
        print(self.INPUT)

    def start(self):
        self.root.mainloop()

    # def createWidgets(self):
    #     self.hiThere = tk.Button(self)
    #     self.hiThere["text"] = "Hello World\n(click me)"
    #     self.hiThere["command"] = self.sayHi
    #     self.hiThere.pack(side="top")
    #
    #     self.quit = tk.Button(self, text="QUIT", fg="red", command=self.master.destroy)
    #     self.quit.pack(side="bottom")
    #
    # def sayHi(self):
    #     print("Hi there, everyone!")


if __name__ == '__main__':
    app = Application()
    app.start()

    # connectionString = (
    #     r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
    #     r'DBQ=C:\Users\barte\Documents\GitHub\KalendarzZajec\schedule.accdb;'
    # )
    # connection = pyodbc.connect(connectionString, autocommit=True)
    # cursor = connection.cursor()
    # cursor.execute('select * from LessonSchedule')
    #
    # for row in cursor.fetchall():
    #     print(row)
    #
    # cursor.close()
    # connection.close()
