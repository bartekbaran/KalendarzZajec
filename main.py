from turtle import pd
import pyodbc
from tkinter import *

class Application():
    def __init__(self):
        self.root = Tk()
        self.root.title('Application')
        self.root.config(background="#FFFFFF")
        # self.root.geometry("{0}x{1}+0+0".format(self.root.winfo_screenwidth() - 9, self.root.winfo_screenheight() - 7))
        self.root.geometry('400x300')
        self.addingTextBox()

    # def splittingIntoColumns(self):
    #     for i in range(5):
    #         self.leftFrame = Frame(self.root, width=self.width, height=self.height)
    #         self.frameList.append(self.leftFrame)
    #         self.leftFrame.grid(row=1, column=i, padx=5, pady=2)
    #         self.leftFrame.config(background="#F1F1F1")

    def addingTextBox(self):
        self.textBox = Text(self.root, height = 10, width = 300)
        self.label = Label(self.root, text = "Siema")
        self.label.config(font =("Roboto", 5))
        self.button = Button(self.root, height = 1, width = 5, text = "Zapisz", command = lambda:self.takeInput())
        self.textBox.pack()
        self.label.pack()
        self.button.pack()

    # def takeInput(self):
    #     self.INPUT = self.textBox.get("1.0", "end-1c")
    #     print(self.INPUT)

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

def addingToDatabase(cursor, les, sta, end, dotw):
    cursor.execute("INSERT INTO LessonSchedule (Lesson, Start, End, DayOfTheWeek) VALUES (?, ?, ?, ?)", (les, sta, end, dotw,))

def printDatabase(cursor):
    cursor.execute('select * from LessonSchedule')
    for row in cursor.fetchall():
        print(row)

if __name__ == '__main__':
    app = Application()
    app.start()

    connectionString = (
        r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
        r'DBQ=C:\Users\barte\Documents\GitHub\KalendarzZajec\schedule.accdb;'
    )

    connection = pyodbc.connect(connectionString, autocommit=True)
    cursor = connection.cursor()
    printDatabase(cursor)
    # addingToDatabase(cursor, "Lesson", "12:50", "14:20", "Monday")
    # printDatabase(cursor)

    cursor.commit()
    cursor.close()
    connection.close()
