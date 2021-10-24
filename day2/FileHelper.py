from tkinter import *
import os
from tkinter import messagebox, filedialog

class FileHelper():
    def __init__(self):
        self.root = Tk()

        #inputFolderFrame
        self.inputFolderFrame = LabelFrame(self.root, text="Input folder").grid(row=0, column=0, sticky=N+S+W+E, padx=5, pady=5)

        #files in folder Frame
        self.filesInFolderFrame = LabelFrame(self.root, text="Files").grid( row=0, column=1, sticky=N+S+W+E, padx=5, pady=5)
        
        self.filesScrollbar = Scrollbar(self.filesInFolderFrame)
        self.filesListBox = Listbox(self.filesInFolderFrame, yscrollcommand=self.filesScrollbar)
        self.files = []
        self.loadScroll()

        #inputFolderFrame #inputFolderType
        self.inputFolderType = StringVar(None, 'choose')
        self.inputFolderRadio1 = Radiobutton(self.inputFolderFrame, text="Choose", variable=self.inputFolderType, command=self.inputFolderTypeHandel, value='choose')
                                .grid(row=0, column=0)
        self.inputFolderRadio2 = Radiobutton(self.inputFolderFrame, text="Enter", variable=self.inputFolderType, command=self.inputFolderTypeHandel, value='enter')
                                .grid(row=0, column=1, padx=(20, 5))

        #inputFolderFrame #inputFolderType #chooseBtn
        self.inputFolderChooseBtn = Button(self.inputFolderFrame, text="choose", command=self.chooseFolder).grid(row=1, column=0, padx=5, pady=5, sticky=W+E)
        
        #inputFolderFrame #inputFolderType #enter frame
        self.enterFrame = LabelFrame(self.inputFolderFrame, borderwidth=0)
        self.inputFolderEnterEntry = Entry(self.enterFrame).grid(row=1, column=0, columnspan=2, padx=5, sticky=W+E)
        self.inputFolderEnterBtn = Button( self.enterFrame, text="enter", command=self.enterFolder).grid(row=2, column=0, columnspan=2, padx=5, pady=5, sticky=W+E)
    
    def inputFolderTypeHandel(self):
        inputFolderType = self.inputFolderType.get()
        if inputFolderType == 'choose':
            self.enterFrame.grid_remove()
            self.inputFolderChooseBtn.grid(row=1, column=0, padx=5, pady=5, sticky=W+E)
        else:
            self.inputFolderChooseBtn.grid_remove()
            self.enterFrame.grid(row=1, column=0, columnspan=3, padx=5, pady=5, sticky=W+E)
            self.inputFolderEnterEntry.delete(0, END)

    def chooseFolder(self):
        self.folder = filedialog.askdirectory()
        if (not self.folder):
            return print('not choose folder')
        self.loadScroll(1)
    
    def enterFolder(self):
        self.folder = self.inputFolderEnterEntry.get()
        if not os.path.isdir(self.folder):
            return messagebox.showerror("Warning", "Folder does not exist!")
        self.loadScroll(1)

    def loadScroll(self, loadFiles = 0):
        if loadFiles:
            self.files = os.listdir(self.folder)
        self.filesListBox.delete(0, END)
        lengMax = 0
        for file in self.files:
            if len(file) > lengMax:
                lengMax = len(file)
            self.filesListBox.insert(END, file)
        
        if lengMax != 0:
            self.filesListBox.config(width=(lengMax + 2))
        self.filesListBox.grid(row=0, column=1, sticky=N+S+W+E, padx=5, pady=5)
       



fileHelper = FileHelper()

fileHelper.root.title('File Helper')
fileHelper.root.mainloop()
