import tkinter as tk
import PIL.Image
import PIL.ImageTk


class SettingsWindow():
    def __init__(self, root, application):
        self.root = root

        self.application = application

        self.colorVersion = application.colorVersion
        self.bgColor = application.bgColor
        self.buttonColor = application.buttonColor
        self.textColor = application.textColor
        self.frameColor = application.frameColor

        self.root.config(background=self.bgColor)
        self.defaultBrowserPath = tk.StringVar()
        self.colorOption = tk.IntVar()

    def settingUpView(self):
        self.root.geometry('270x230+800+350')

        self.settingsLabel = tk.Label(self.root, text="Settings", font=("Helvetica", 24), bg=self.bgColor, fg=self.textColor)
        self.settingsLabel.grid(row=0, columnspan=2, pady=20, padx=10)

        self.urlEntry = tk.Entry(self.root, textvariable=self.defaultBrowserPath, width=40, bg=self.bgColor, fg=self.textColor)
        self.urlEntry.insert(0, "       --Insert default browser URL here--")
        self.urlEntry.grid(row=1, columnspan=2, pady=15, padx=10)

        self.brightMode = tk.Radiobutton(self.root, text="Bright mode", bg=self.bgColor, padx=10, pady=16, fg=self.textColor,
                                         variable=self.colorOption, value=1, command=lambda: self.choosedOption()).grid(
            row=2, column=0)
        self.darkMode = tk.Radiobutton(self.root, text="Dark mode", bg=self.bgColor,  fg=self.textColor,
                                       variable=self.colorOption, value=2, command=lambda: self.choosedOption()).grid(row=2, column=1)

        self.decriptionLabel = tk.Label(self.root, text="Save changes and go back: ", bg=self.bgColor).grid(row=3,
                                                                                                         column=0)

        self.backIcon = self.creatingIconImage(self.colorVersion, "smallBackIcon.png")
        self.backButton = tk.Button(self.root, image=self.backIcon, bg=self.bgColor, bd=0,
                                    command=lambda: self.saveChangesAndClearWindow())
        self.backButton.grid(row=3, column=1)

    def gettingStrings(self):
        self.defaultBrowserPath = self.urlEntry.get()
        self.settingsFile = open("settings.txt", "a+")
        self.settingsFile.write(str("Path:"+f'{self.defaultBrowserPath}\n'))

    def choosedOption(self):
        self.colorChoice = self.colorOption.get()
        if self.colorChoice == 1:
            self.settingsFile = open("colorSettings.txt", "w+")
            self.settingsFile.write(str("bright"))
        if self.colorChoice == 2:
            self.settingsFile = open("colorSettings.txt", "w+")
            self.settingsFile.write(str("dark"))

    def creatingIconImage(self, colorVersion, imagePath):
        self.icon = PIL.ImageTk.PhotoImage(PIL.Image.open(f"images/{colorVersion}/{imagePath}"))
        return self.icon

    def saveChangesAndClearWindow(self):
        self.gettingStrings()
        for child in self.root.winfo_children():
            child.destroy()
        self.application.refreshingWindow(self.root)