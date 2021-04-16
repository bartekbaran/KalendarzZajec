from tkinter import *
from Database import *

def addClass(database):
    root = Tk()
    root.title("Add new class")

    eventNameLabel = Label(root, text="Event name: ")
    eventNameLabel.grid(row=0, column=0)
    eventNameEntry = Entry(root)
    eventNameEntry.grid(row=0, column=1)

    eventStartLabel = Label(root, text="Time of start: ")
    eventStartLabel.grid(row=1, column=0)
    eventStartEntry = Entry(root)
    eventStartEntry.grid(row=1, column=1)

    eventEndLabel = Label(root, text="End: ")
    eventEndLabel.grid(row=2, column=0)
    eventEndEntry = Entry(root)
    eventEndEntry.grid(row=2, column=1)

    eventDateLabel = Label(root, text="Date: ")
    eventDateLabel.grid(row=3, column=0)
    eventDateDayEntry = Entry(root)
    eventDateDayEntry.grid(row=3, column=1)
    eventDateMonthEntry = Entry(root)
    eventDateMonthEntry.grid(row=3, column=2)
    eventDateYearEntry = Entry(root)
    eventDateYearEntry.grid(row=3, column=3)

    addToDatabaseButton = Button(root, text="Add", command=database.addingToDatabase("Math", "14:40", "16:10", "Wednesday"))

    root.mainloop()