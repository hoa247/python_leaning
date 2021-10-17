from tkinter import *

class Caculation():
    def __init__(self):
        self.root = Tk()
        self.inputFrame = LabelFrame(self.root, text="Input")
        self.inputFrame.grid(row=0, column=0, padx=10, pady=10, sticky=E+W+N+S)

        self.outputFrame = LabelFrame(self.root, text="Output")
        self.outputFrame.grid(row=0, column=2, padx=10, pady=10, sticky=E+W+N+S)

        self.label1 = Label(self.inputFrame, text="Number 1:")
        self.label1.grid(row=0, column=0)

        self.input1Value = StringVar()

        self.input1 = Entry(self.inputFrame, width=25,
                            textvariable=self.input1Value)
        self.input1.grid(row=0, column=1)
        self.inputFrame.grid(row=0, column=0, padx=5)

        self.label2 = Label(self.inputFrame, text="Number 2:")
        self.label2.grid(row=1, column=0)

        self.input2Value = StringVar()
        self.input2 = Entry(self.inputFrame, width=25,
                            textvariable=self.input2Value)
        self.input2.grid(row=1, column=1, padx=5)

        self.calculateBtn = Button(self.inputFrame, text='Calculate',
                              command=self.calculate)
        self.calculateBtn.grid(row=2, column=1, sticky=W, pady=5)

        self.clearBtn = Button(self.inputFrame, text='clear',
                              command=self.clear)
        self.clearBtn.grid(row=2, column=1, sticky=N, pady=5)

        self.font = ("Arial", 14)
        self.operater = StringVar(None, '+')
        self.radio1 = Radiobutton(self.inputFrame, text="+", variable=self.operater, value='+', font=self.font)
        self.radio1.grid(row=3, column=0)
 
        self.radio2 = Radiobutton(self.inputFrame, text="-", variable=self.operater, value='-', font=self.font)
        self.radio2.grid(row=3, column=1)

        self.radio3 = Radiobutton(self.inputFrame, text="*", variable=self.operater, value='*', font=self.font)
        self.radio3.grid(row=4, column=0)

        self.radio4 = Radiobutton(self.inputFrame, text="/", variable=self.operater, value='/', font=self.font)
        self.radio4.grid(row=4, column=1)

        self.label3 = Label(self.outputFrame, text="Result")
        self.label3.grid(row=0, column=0, padx=80)

        self.result = StringVar(None, '')
        self.resultLabel = Label(self.outputFrame, textvariable=self.result)
        self.resultLabel.grid(row=2, column=0, padx=5)

    def calculate(self):
        input1 = self.input1.get()
        input2 = self.input2.get()
        operater = self.operater.get()
        
        if not input1 and not input2:
            return self.result.set('Please enter values!')
        operater = self.operater.get()
        
        if not input1:
            return self.result.set('Please enter first input!')
        operater = self.operater.get()
        
        if not input2:
            return self.result.set('Please enter second input!')

        if not input1.isdigit():
            return self.result.set('The first input must be a number!')
        operater = self.operater.get()
        
        if not input2.isdigit():
            return self.result.set('The second input must be a number!')
            
        input1 = int(input1)
        input2 = int(input2)
        
        return self.result.set(eval(f'{input1} {operater} {input2}'))

    def clear(self):
        self.result.set('cleared!')
        self.input1Value.set('')
        self.input2Value.set('')

caculation = Caculation()
caculation.root.mainloop()
