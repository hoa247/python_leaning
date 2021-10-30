from tkinter import *
import os
from tkinter import messagebox, filedialog

class FileHelper():
    def __init__(self):
        self.root = Tk()
        self.folder = ''
        #inputFolderFrame
        self.inputFolderFrame = LabelFrame(self.root, text="Input folder", height=10)
        self.inputFolderFrame.grid(row=0, column=0, sticky=N+S+W+E, padx=5, pady=5)
        
        #options Frame
        self.optionsFrame = LabelFrame(self.root, text="Options")
        self.optionsFrame.grid(row=0, column=1, sticky=N+S+W+E, padx=5, pady=5)

        #childs in folder Frame
        self.childFoldersInFolderFrame = LabelFrame(self.root, text="Folders")
        self.childFoldersInFolderFrame.grid( row=1, column=0, sticky=N+S+W+E, padx=5, pady=5)
        
        self.childFilesInFolderFrame = LabelFrame(self.root, text="Files")
        self.childFilesInFolderFrame.grid(row=1, column=1, sticky=N+S+W+E, padx=5, pady=5)
        
        
        
        #checkbox file folder
        self.fileCheckboxValue = IntVar(None, 1)
        Checkbutton(self.optionsFrame, text="File", command=self.handleFilterFileOrFolder,
                    variable=self.fileCheckboxValue).grid(row=0, sticky=W)
        self.folderCheckboxValue = IntVar(None, 1)
        Checkbutton(self.optionsFrame, text="Folder", command=self.handleFilterFileOrFolder,
                    variable=self.folderCheckboxValue).grid(row=1, sticky=W)


        #scroll Folder and file
        
        self.childFoldersScrollbarX = Scrollbar( self.childFoldersInFolderFrame, orient=HORIZONTAL)
        self.childFoldersScrollbarY = Scrollbar(self.childFoldersInFolderFrame)
        self.childFoldersScrollbarX.grid(row=1, column=0, sticky=N+S+E+W)
        self.childFoldersScrollbarY.grid(row=0, column=1, sticky=N+S+E+W)
        self.childFoldersListBox = Listbox(self.childFoldersInFolderFrame)
        self.childFoldersListBox.grid(row=0, column=0, sticky=N+S+E+W)
        
        self.childFilesScrollbarX = Scrollbar(self.childFilesInFolderFrame,  orient=HORIZONTAL)
        self.childFilesScrollbarY = Scrollbar(self.childFilesInFolderFrame)
        self.childFilesScrollbarX.grid(row=1, column=0, sticky=N+S+E+W)
        self.childFilesScrollbarY.grid(row=0, column=1, sticky=N+S+E+W)
        self.childFilesListBox = Listbox(self.childFilesInFolderFrame)
        self.childFilesListBox.grid(row=0, column=0, sticky=N+S+E+W)
        
        self.childs = []
        self.loadScroll()

        #inputFolderFrame #inputFolderType
        self.inputFolderType = StringVar(None, 'choose')
        self.inputFolderRadio1 = Radiobutton(self.inputFolderFrame, text="Choose", variable=self.inputFolderType, command=self.inputFolderTypeHandel, value='choose')
        self.inputFolderRadio1.grid(row=0, column=0)
        self.inputFolderRadio2 = Radiobutton(self.inputFolderFrame, text="Enter", variable=self.inputFolderType, command=self.inputFolderTypeHandel, value='enter')
        self.inputFolderRadio2.grid(row=0, column=1, padx=(20, 5))

        #inputFolderFrame #inputFolderType #chooseBtn
        self.inputFolderChooseBtn = Button(self.inputFolderFrame, text="choose", command=self.chooseFolder)
        self.inputFolderChooseBtn.grid(row=1, column=0, padx=5, pady=(5, 34), sticky=W+E)
        
        #inputFolderFrame #inputFolderType #enter frame
        self.enterFrame = LabelFrame(self.inputFolderFrame, borderwidth=0)
        self.inputFolderEnterEntry = Entry(self.enterFrame)
        self.inputFolderEnterEntry.grid(row=1, column=0, columnspan=2, padx=5, sticky=W+E)
        self.inputFolderEnterBtn = Button( self.enterFrame, text="enter", command=self.enterFolder)
        self.inputFolderEnterBtn.grid(row=2, column=0, columnspan=2, padx=5, pady=5, sticky=W+E)
        

    def handleFilterFileOrFolder(self):
        if self.folder:
            self.loadScroll(1)
    
    def inputFolderTypeHandel(self):
        inputFolderType = self.inputFolderType.get()
        if inputFolderType == 'choose':
            self.enterFrame.grid_remove()
            self.inputFolderChooseBtn.grid(row=1, column=0, padx=5, pady=(5, 34), sticky=W+E)
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
        if not self.folder:
            return messagebox.showerror("Warning", "Please enter folder path!")
        if not os.path.isdir(self.folder):
            return messagebox.showerror("Warning", "Folder does not exist!")
        self.loadScroll(1)

    def loadScroll(self, isChoosed = 0):
        self.childFoldersListBox.delete(0, END)
        self.childFilesListBox.delete(0, END)
        if isChoosed:
            self.childs = os.listdir(self.folder)
            self.childFoldersListBox.insert(END, '../')
        self.filteredChildFolders = []
        self.filteredChildFiles = []
        self.filter()
        
        for childFolder in self.filteredChildFolders:
            self.childFoldersListBox.insert(END, childFolder)
        
        for childFile in self.filteredChildFiles:
            self.childFilesListBox.insert(END, childFile)
            
        self.childFoldersListBox.config(xscrollcommand=self.childFoldersScrollbarX.set, yscrollcommand=self.childFoldersScrollbarY.set)
        self.childFoldersScrollbarX.config(command=self.childFoldersListBox.xview)
        self.childFoldersScrollbarY.config(command=self.childFoldersListBox.yview)
        
        self.childFilesListBox.config(xscrollcommand=self.childFilesScrollbarX.set, yscrollcommand=self.childFilesScrollbarY.set)
        self.childFilesScrollbarX.config(command=self.childFilesListBox.xview)
        self.childFilesScrollbarY.config(command=self.childFilesListBox.yview)
    
    def filter(self):
        isFile = self.fileCheckboxValue.get()
        isFolder = self.folderCheckboxValue.get()
        for child in self.childs:
            path = self.folder + '/' + child
            if isFile and os.path.isfile(path):
                self.filteredChildFiles.append(child)
                continue
            if isFolder and os.path.isdir(path):
                self.filteredChildFolders.append(child)


fileHelper = FileHelper()

fileHelper.root.title('File Helper')
fileHelper.root.mainloop()
