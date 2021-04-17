import tkinter as tk
from tkinter import ttk
from Database import *

def addClass(database):
    root = tk.Tk()
    root.title("Add new class")

    eventNameVar = tk.StringVar()
    eventStartVar = tk.StringVar()
    eventEndVar = tk.StringVar()
    eventDateVar = tk.StringVar()

    eventNameLabel = tk.Label(root, text="Event name: ")
    eventNameLabel.grid(row=0, column=0)
    eventNameEntry = tk.Entry(root, textvariable=eventNameVar)
    eventNameEntry.grid(row=0, column=1)

    eventStartLabel = tk.Label(root, text="Time of start: ")
    eventStartLabel.grid(row=1, column=0)
    eventStartEntry = tk.Entry(root, textvariable=eventStartVar)
    eventStartEntry.grid(row=1, column=1)

    eventEndLabel = tk.Label(root, text="End: ")
    eventEndLabel.grid(row=2, column=0)
    eventEndEntry = tk.Entry(root, textvariable=eventEndVar)
    eventEndEntry.grid(row=2, column=1)

    eventDateLabel = tk.Label(root, text="Day of the Week: ")
    eventDateLabel.grid(row=3, column=0)
    eventDateCombo = ttk.Combobox(root, textvariable=eventDateVar)
    eventDateCombo['values'] = ('Monday',
                                'Tuesday',
                                'Wednesday',
                                'Thursday',
                                'Friday')
    eventDateCombo.grid(row=3, column=1)

    # addToDatabaseButton = Button(root, text="Add", command=database.addingToDatabase("Math", "14:40", "16:10", "Wednesday"))
    addToDatabaseButton = tk.Button(root, text="Add", bd=1, bg='#b7c8c9', activebackground='#94a0a1', command=lambda:addButton(database, root, eventNameVar.get(), eventStartVar.get(), eventEndVar.get(), eventDateVar.get()))
    addToDatabaseButton.grid(row=4,column=0)

    root.mainloop()

def addButton(database, root, name, start, end, date):
    database.addingToDatabase(name, start, end, date)
    root.destroy()