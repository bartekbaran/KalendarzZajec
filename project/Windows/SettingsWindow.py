import tkinter as tk
import PIL.Image
import PIL.ImageTk


class SettingsWindow():
    def __init__(self, root, application):
        self.root = root
        self.root.config(background="#FFFFFF")

        self.application = application

        self.defaultBrowserPath = tk.StringVar()

    def settingUpView(self):
        self.root.geometry('270x230+800+350')

        self.settingsLabel = tk.Label(self.root, text="Settings", font=("Helvetica", 24), bg="#FFFFFF").grid(row=0, columnspan=2, pady=20, padx=10)

        self.urlEntry = tk.Entry(self.root, textvariable=self.defaultBrowserPath, width=40)
        self.urlEntry.insert(0, "--Insert default browser URL here--")
        self.urlEntry.grid(row=1, columnspan=2, pady=15, padx=10)

        self.brightMode = tk.Checkbutton(self.root, text="Bright mode", bg="#FFFFFF", padx=10, pady=16).grid(row=2, column=0)
        self.darkMode = tk.Checkbutton(self.root, text="Dark mode", bg="#FFFFFF").grid(row=2, column=1)

        self.decriptionLabel = tk.Label(self.root, text="Save changes and go back: ", bg="#FFFFFF").grid(row=3, column=0)

        self.backIcon = self.creatingIconImage("smallBackIcon.png")
        self.backButton = tk.Button(self.root, image=self.backIcon, bg="#FFFFFF", bd=0,
                                    command=lambda : self.saveChangesAndClearWindow())
        self.backButton.grid(row=3, column=1)

    def gettingStrings(self):
        self.defaultBrowserPath = self.urlEntry.get()
        self.settingsFile = open("settings.txt", "a+")
        self.settingsFile.write(str("Path:"+f'{self.defaultBrowserPath}\n'))


    def creatingIconImage(self, imagePath):
        self.icon = PIL.ImageTk.PhotoImage(PIL.Image.open(f"images/{imagePath}"))
        return self.icon

    def saveChangesAndClearWindow(self):
        self.gettingStrings()
        for child in self.root.winfo_children():
            child.destroy()
        self.application.refreshingWindow(self.root)