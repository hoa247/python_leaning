from tkinter import *
import os
from tkinter import messagebox, filedialog

class FileHelper():
    def __init__(self):
        self.root = Tk()
        self.folder = 'root'
        #inputFolderFrame
        self.inputFolderFrame = LabelFrame(self.root, text="Input folder", height=10)
        self.inputFolderFrame.grid(row=0, column=0, sticky=N+S+W+E, padx=5, pady=5)
        
        #options Frame
        self.optionsFrame = LabelFrame(self.root, text="Options")
        self.optionsFrame.grid(row=0, column=1, sticky=N+S+W+E, padx=5, pady=5)

        #actions Frame
        self.actionsFrame = LabelFrame(self.root, text="Actions")
        self.actionsFrame.grid(row=1, column=0, columnspan=2, sticky=N+S+W+E, padx=5, pady=5)

        #childs in folder Frame
        self.childFoldersInFolderFrame = LabelFrame(self.root, text="Folders")
        self.childFoldersInFolderFrame.grid( row=2, column=0, sticky=N+S+W+E, padx=5, pady=5)
        
        self.childFilesInFolderFrame = LabelFrame(self.root, text="Files")
        self.childFilesInFolderFrame.grid(row=2, column=1, sticky=N+S+W+E, padx=5, pady=5)
        
        
        
        #checkbox file folder
        self.fileCheckboxValue = IntVar(None, 1)
        Checkbutton(self.optionsFrame, text="File", command=self.handleFilterFileOrFolder, variable=self.fileCheckboxValue).grid(row=0, sticky=W)
        self.folderCheckboxValue = IntVar(None, 1)
        Checkbutton(self.optionsFrame, text="Folder", command=self.handleFilterFileOrFolder, variable=self.folderCheckboxValue).grid(row=1, sticky=W)
        
        self.filterNameLabel = Label(self.optionsFrame, text="name")
        self.filterNameLabel.grid(row=2, column=0,sticky=W+E)
        self.filterNameEntry = Entry(self.optionsFrame)
        self.filterNameEntry.grid(row=2, column=1, padx=5, sticky=W+E)
        self.searchBtn = Button(self.optionsFrame, text="search", command=self.loadScroll, width=10)
        self.searchBtn.grid(row=3, column=1, padx=5, pady=5, sticky=W)


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
        self.childFilesListBox = Listbox(self.childFilesInFolderFrame, width=30)
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
        self.inputFolderEnterBtn = Button(self.enterFrame, text="enter", command=self.enterFolder)
        self.inputFolderEnterBtn.grid(row=2, column=0, columnspan=2, padx=5, pady=5, sticky=W+E)
        
        #actions Frame #Delimiter
        self.delimiterLabel = Label(self.actionsFrame, text="Delimiter")
        self.delimiterLabel.grid(row=0, column=0, sticky=W)
        
        self.delimiter = StringVar(None, '_')
        self.inputFolderRadio1 = Radiobutton( self.actionsFrame, text="_(name_order)", variable=self.delimiter, command=self.delimiterHandel, value='_')
        self.inputFolderRadio1.grid(row=1, column=0, sticky=W)
        self.inputFolderRadio2 = Radiobutton( self.actionsFrame, text="-(name-order)", variable=self.delimiter, command=self.delimiterHandel, value='-')
        self.inputFolderRadio2.grid(row=2, column=0, sticky=W)
        self.inputFolderRadio2 = Radiobutton( self.actionsFrame, text="space(name order)", variable=self.delimiter, command=self.delimiterHandel, value=' ')
        self.inputFolderRadio2.grid(row=3, column=0, sticky=W)
        
        #actions Frame #New name
        self.newNameLabel = Label(self.actionsFrame, text="New name(*)")
        self.newNameLabel.grid(row=4, column=0, sticky=W)
        self.newNameEntry = Entry(self.actionsFrame)
        self.newNameEntry.grid(row=5, column=0, padx=5, sticky=W+E)
        
        #actions Frame #Checkbutton New extension
        self.changeExtensionValue = IntVar(None, 0)
        Checkbutton(self.actionsFrame, text="Change extension", command=self.handleChangeExtensionValue,
                    variable=self.changeExtensionValue).grid(row=6, sticky=W)

        
        #actions Frame #New extension
        self.newExtensionFrame = LabelFrame(self.actionsFrame, borderwidth=0)
        self.newExtensionLabel = Label( self.newExtensionFrame, text="New file extension")
        self.newExtensionLabel.grid(row=0, column=0, sticky=W)
        self.newExtensionEntry = Entry(self.newExtensionFrame)
        self.newExtensionEntry.grid(row=1, column=0, padx=5, sticky=W+E)

        #actions Frame #btn rename
        self.renameBtn = Button(self.actionsFrame, text="rename folders", command=self.renameFolders)
        self.renameBtn.grid(row=8, column=0, padx=3, pady=5, sticky=W)
        self.renameBtn = Button( self.actionsFrame, text="rename files", command=self.renameFiles)
        self.renameBtn.grid(row=8, column=2, padx=30, pady=5, sticky=E)

    def handleChangeExtensionValue(self):
        if (self.changeExtensionValue.get() == 1):
            self.newExtensionFrame.grid(row=7, column=0, sticky=W)
        else:
            self.newExtensionFrame.grid_remove()

    def validNewNameFormat(self, name):
        notAllowedCharacters = ['/', '<', '>',
                                ':', '"', '/', '\\', '|', '?', ' *']
        for notAllowedCharacter in notAllowedCharacters:
            if notAllowedCharacter in name:
                messagebox.showerror("Warning", "Name must not include characters / <  >  :  \" / |  ? *")
                return False
        return True
    
    def validNewNameLength(self, name):
        maxLength = 255
        if (len(name) > maxLength):
            messagebox.showerror( "Warning", "Name length must not greater than 255")
            return False
        if (len(name) == 0):
            messagebox.showerror(
                "Warning", "Please enter new name")
            return False
        return True
        
    
    def renameFiles(self):
        if (self.folder == 'root'):
            return messagebox.showerror("Warning", "Can not rename in root folder")
        newName = self.newNameEntry.get()
        print()
        if (not self.validNewNameFormat(newName) or not self.validNewNameLength(newName)):
            return
        answer = messagebox.askyesno(title='Confirmation', message='Are you sure that you want to rename FILES?')
        if answer:
            self.loadScroll()
            try:
                self.doRenameFiles(newName)
            except Exception as e:
                messagebox.showerror('Error', e)
            self.filterNameEntry.delete(0, END)
            self.loadScroll()
            
    def doRenameFiles(self, newName):
        order = 1
        delimiter = self.delimiter.get()
        for childFile in self.filteredChildFiles:
            fullPathFile = os.path.join(self.folder, childFile)
            pathname, extension = os.path.splitext(fullPathFile)
            if (self.changeExtensionValue.get() == 1):
                extension = self.newExtensionEntry.get()
            else:
                extension = extension[1:]
            newPathname = os.path.join( self.folder, newName) + delimiter + str(order)
            if (extension):
                os.rename(fullPathFile, newPathname + "." + extension)
            else:
                os.rename(fullPathFile, newPathname)
            order += 1
        return messagebox.showinfo("Info", "Rename " + str(order) + " files successfully")

    def renameFolders(self):
        if (self.folder == 'root'):
            return messagebox.showerror( "Warning", "Can not rename in root folder")
        newName = self.newNameEntry.get()
        if (not self.validNewNameFormat(newName) or not self.validNewNameLength(newName)):
            return
        answer = messagebox.askyesno(
            title='Confirmation', message='Are you sure that you want to rename FOLDERS?')
        if answer:
            self.loadScroll()
            self.filterNameEntry.delete(0, END)
            try:
                self.doRenameFolders(newName)
            except Exception as e:
                messagebox.showerror('Error', e)
            self.loadScroll()

    def doRenameFolders(self, newName):
        order = 1
        delimiter = self.delimiter.get()
        for childFolder in self.filteredChildFolders:
            fullPathFolder = os.path.join(self.folder, childFolder)
            newPathname = os.path.join(
                self.folder, newName) + delimiter + str(order)
            os.rename(fullPathFolder, newPathname)
            order += 1
        return messagebox.showinfo("Info", "Rename " + str(order) + " folders successfully")

    def handleFilterFileOrFolder(self):
        if self.folder:
            self.loadScroll()
    
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
        self.filterNameEntry.delete(0, END)
        self.folder = filedialog.askdirectory()
        if (not self.folder):
            return print('not choose folder')
        self.loadScroll()
    
    def enterFolder(self):
        self.folder = self.inputFolderEnterEntry.get()
        if not self.folder:
            return messagebox.showerror("Warning", "Please enter folder path!")
        if not os.path.isdir(self.folder):
            return messagebox.showerror("Warning", "Folder does not exist!")
        self.loadScroll()

    def loadScroll(self):
        self.childFoldersListBox.delete(0, END)
        self.childFilesListBox.delete(0, END)
        if self.folder == 'root':
            dl = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
            self.childs = ['%s:/' % d for d in dl if os.path.exists('%s:' % d)]
        else:
            try:
                self.childs = os.listdir(self.folder)
            except Exception as e:
                messagebox.showerror('Error', e)
            self.childFoldersListBox.insert(END, '../')
                
        self.filteredChildFolders = []
        self.filteredChildFiles = []
        self.filter()
        
        for childFolder in self.filteredChildFolders:
            self.childFoldersListBox.insert(END, childFolder)
            
        self.childFoldersListBox.bind('<Double-Button>', self.doubleClickFolder)
        
        for childFile in self.filteredChildFiles:
            self.childFilesListBox.insert(END, childFile)
            
        self.childFoldersListBox.config(xscrollcommand=self.childFoldersScrollbarX.set, yscrollcommand=self.childFoldersScrollbarY.set)
        self.childFoldersScrollbarX.config(command=self.childFoldersListBox.xview)
        self.childFoldersScrollbarY.config(command=self.childFoldersListBox.yview)
        
        self.childFilesListBox.config(xscrollcommand=self.childFilesScrollbarX.set, yscrollcommand=self.childFilesScrollbarY.set)
        self.childFilesScrollbarX.config(command=self.childFilesListBox.xview)
        self.childFilesScrollbarY.config(command=self.childFilesListBox.yview)
    
    def doubleClickFolder(self, event):
        selection = event.widget.curselection()
        if selection:
            index = selection[0]
            clickFolder = event.widget.get(index)
            if clickFolder == '../' :
                if (len(self.folder) == 3):
                    self.folder = 'root'
                else:
                    self.folder = os.path.dirname(self.folder)
            else:
                self.folder = os.path.join(self.folder, clickFolder)
        self.loadScroll()
    def filter(self):
        isFile = self.fileCheckboxValue.get()
        isFolder = self.folderCheckboxValue.get()
        for child in self.childs:
            filterName = self.filterNameEntry.get()
            if filterName.lower() not in child.lower():
                continue
            path = self.folder + '/' + child
            if isFile and os.path.isfile(path):
                self.filteredChildFiles.append(child)
                continue
            if (isFolder and os.path.isdir(path)) or self.folder == 'root':
                self.filteredChildFolders.append(child)

    def delimiterHandel(self):
        print(self.delimiter)

fileHelper = FileHelper()

fileHelper.root.title('File Helper')
fileHelper.root.mainloop()
