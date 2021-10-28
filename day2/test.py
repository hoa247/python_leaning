from tkinter import *
from tkinter import scrolledtext


root = Tk()


scroll_x = Scrollbar(root, orient="horizontal")
text = scrolledtext.ScrolledText(root, wrap=NONE)

text.config(xscrollcommand=scroll_x.set)
scroll_x.configure(command=text.xview)
text.pack(fill=X)
scroll_x.pack(fill=X)

root.mainloop()
