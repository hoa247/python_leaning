from tkinter import *
import os
from tkinter import messagebox, filedialog

class FileHelper():
    def __init__(self):
        self.root = Tk()

        #inputFolderFrame
        self.inputFolderFrame = LabelFrame(self.root, text="Input folder")
        self.inputFolderFrame.grid(row=0, column=0, sticky=N+S+W+E, padx=5, pady=5)

        #files in folder Frame
        self.filesInFolderFrame = LabelFrame(self.root, text="Files")
        self.filesInFolderFrame.grid( row=0, column=1, sticky=N+S+W+E, padx=5, pady=5)
        
        self.files = [1,2];
        self.filesScrollbar = Scrollbar(self.filesInFolderFrame)
        self.filesScrollbar.pack(side=RIGHT, fill=Y)
        self.loadScroll(self.files)

        #inputFolderFrame #inputFolderType
        self.inputFolderType = StringVar(None, 'choose')
        self.inputFolderRadio1 = Radiobutton(self.inputFolderFrame, text="Choose", variable=self.inputFolderType, command=self.inputFolderTypeHandel, value='choose')
        self.inputFolderRadio1.grid(row=0, column=0)
        self.inputFolderRadio2 = Radiobutton(self.inputFolderFrame, text="Enter", variable=self.inputFolderType, command=self.inputFolderTypeHandel, value='enter')
        self.inputFolderRadio2.grid(row=0, column=1, padx=(20, 5))

        #inputFolderFrame #inputFolderType #chooseBtn
        self.inputFolderChooseBtn = Button(self.inputFolderFrame, text="choose", command=self.chooseFolder)
        self.inputFolderChooseBtn.grid(row=1, column=0, padx=5, pady=5, sticky=W+E)
        
        #inputFolderFrame #inputFolderType #enter frame
        self.enterFrame = LabelFrame(self.inputFolderFrame, borderwidth=0)
        self.inputFolderEnterEntry = Entry(self.enterFrame)
        self.inputFolderEnterEntry.grid(row=1, column=0, columnspan=2, padx=5, sticky=W+E)
        self.inputFolderEnterBtn = Button( self.enterFrame, text="enter", command=self.enterFolder)
        self.inputFolderEnterBtn.grid(row=2, column=0, columnspan=2, padx=5, pady=5, sticky=W+E)
    

        
       
    
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
        print("You choose:" + self.folder)
    
    def enterFolder(self):
        self.loadScroll([3,6])

        self.folder = self.inputFolderEnterEntry.get()
        if not os.path.isdir(self.folder):
            return messagebox.showerror("Warning", "Folder does not exist!")
        print(self.folder)

    def loadScroll(self, files):
        
        self.filesListBox = Listbox(
        self.filesInFolderFrame, yscrollcommand=self.filesScrollbar)
        for file in files:
            self.filesListBox.insert(END, file)

        self.filesListBox.pack(side=LEFT, fill=BOTH)
        self.filesScrollbar.config(command=self.filesListBox.yview)



fileHelper = FileHelper()

fileHelper.root.title('File Helper')
fileHelper.root.mainloop()
