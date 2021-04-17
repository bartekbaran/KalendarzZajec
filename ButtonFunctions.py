import tkinter as tk
from tkinter import ttk
from Database import *

def addClass(database):
    root = tk.Tk()
    root.title("Add new class")

    n = tk.StringVar()

    eventNameLabel = tk.Label(root, text="Event name: ")
    eventNameLabel.grid(row=0, column=0)
    eventNameEntry = tk.Entry(root)
    eventNameEntry.grid(row=0, column=1)

    eventStartLabel = tk.Label(root, text="Time of start: ")
    eventStartLabel.grid(row=1, column=0)
    eventStartEntry = tk.Entry(root)
    eventStartEntry.grid(row=1, column=1)

    eventEndLabel = tk.Label(root, text="End: ")
    eventEndLabel.grid(row=2, column=0)
    eventEndEntry = tk.Entry(root)
    eventEndEntry.grid(row=2, column=1)

    eventDateLabel = tk.Label(root, text="Day of the Week: ")
    eventDateLabel.grid(row=3, column=0)
    eventDateCombo = ttk.Combobox(root, textvariable=n)
    eventDateCombo['values'] = ('Monday',
                                'Tuesday',
                                'Wednesday',
                                'Thursday',
                                'Friday')
    eventDateCombo.grid(row=3, column=1)

    # addToDatabaseButton = Button(root, text="Add", command=database.addingToDatabase("Math", "14:40", "16:10", "Wednesday"))
    addToDatabaseButton = tk.Button(root, text="Add", bd=1, bg='#b7c8c9', activebackground='#94a0a1')
    addToDatabaseButton.grid(row=4,column=0)

    root.mainloop()