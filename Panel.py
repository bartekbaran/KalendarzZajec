from tkinter import *

class Panel:
    def __init__(self, root, frame):
        self.root = root
        self.frame = frame

        Label(self.frame, text="Instructions: ").grid(row=0, column=0, padx=0, pady=0)

        self.instruct = Label(self.frame, text="1\n2\n2\n3\n4\n5\n6\n7\n8\n9\n")
        self.instruct.grid(row=1, column=0, padx=0, pady=0)