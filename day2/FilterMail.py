from tkinter import *
import os
from os.path import dirname, abspath
from tkinter.filedialog import askopenfilename
from tkinter import messagebox, filedialog
import shutil
import subprocess



class FilterMail():
    def __init__(self):
        self.root = Tk()
        self.count = 0
        self.files = []
        #addFrame
        self.addFrame = LabelFrame(self.root, text="ADD", height=10)
        self.addFrame.grid( row=0, column=0, sticky=N+S+W+E, padx=5, pady=5)
        
        #exportFrame
        self.exportFrame = LabelFrame(self.root, text="EXPORT", height=10)
        self.exportFrame.grid(row=0, column=1, sticky=N+S+W+E, padx=5, pady=5)
        
        #addFrame child
        self.mailCountLabel = Label(self.addFrame, text="Mail count")
        self.mailCountLabel.grid(row=0, column=0, sticky=W)
        self.mailCountNumber = Label(self.addFrame, text=self.count)
        self.mailCountNumber.grid(row=0, column=1, sticky=S)
        self.pathLabel = Label(self.addFrame, text="Path: ")
        self.pathLabel.grid(row=1, column=0, sticky=W)
        self.openBtn = Button(self.addFrame, text="Open", command=self.openFile, width=10)
        self.openBtn.grid(row=1, column=1, padx=5, pady=5, sticky=W)
        
        #exportFrame child
        self.fileCountLabel = Label(self.exportFrame, text="File count:")
        self.fileCountLabel.grid(row=0, column=0, sticky=W)
        self.fileCountEntry = Entry(self.exportFrame, width=10)
        self.fileCountEntry.grid(row=0, column=1, sticky=W, padx=5, pady=5)
        self.mailsInAFileLabel = Label(self.exportFrame, text="Mails in a file:")
        self.mailsInAFileLabel.grid(row=1, column=0, sticky=W)
        self.mailsInAFileEntry = Entry(self.exportFrame, width=10)
        self.mailsInAFileEntry.grid(row=1, column=1, sticky=W, padx=5, pady=5)
        
        self.openBtn = Button(self.exportFrame, text="Export", command=self.export, width=10)
        self.openBtn.grid(row=0, column=2, rowspan=2, padx=5, pady=5, sticky=N+S+W+E)
        

    def openFile(self):
        file = askopenfilename()
        if not file in self.files:
            self.files.append(file)
            self.countLineFiles()
    
    def countLineFiles(self):
        self.count = 0
        for file in self.files:
            with open(file) as f:
                self.count += sum(1 for line in f if line.strip())
        self.mailCountNumber.config(text=self.count)
        
    def export(self):
        if (self.count == 0):
            return messagebox.showerror("Warning", "List mail empty!")
        fileCount = self.fileCountEntry.get()
        mailsInAFile = self.mailsInAFileEntry.get()

        if not fileCount:
            return messagebox.showerror("Warning", "Please enter file count!")
        
        if not mailsInAFile:
            return messagebox.showerror("Warning", "Please enter mails in file!")
        
        if (not self.isInt(fileCount)):
            return messagebox.showerror("Warning", "File count must be a number!")
        
        if (not self.isInt(mailsInAFile)):
            return messagebox.showerror("Warning", "Mails in a file must be a number!")
        
        mails = []
        for file in self.files:
            with open(file, 'r') as f:
                lines = f.readlines()
                mails += lines
        
        exportFolder = os.path.join(
            dirname(abspath(__file__)), 'mail', 'export')
        if (os.path.isdir(exportFolder)):
            shutil.rmtree(exportFolder)
        os.makedirs(exportFolder)
        
        count = 0
        for i in range(1, int(fileCount) + 1):
            count += int(mailsInAFile)
            exportMail = mails[count-int(mailsInAFile):count]
            if not exportMail:
                break
            exportFilePath = os.path.join( exportFolder, 'mail' + str(i) + '.txt')
            with open(exportFilePath, 'w+') as f:
                for mail in exportMail:
                    f.write("%s" % mail)
                    
        messagebox.showinfo("Info", "Export mails successfully")
        subprocess.Popen('explorer "' + exportFolder + '"')

    def isInt(self, str):
        try:
            int(str)
            return True
        except ValueError:
            return False

filterMail = FilterMail()

filterMail.root.title('Filter Mail')
filterMail.root.mainloop()
