from tkinter import *
from tkinter import ttk
from tkinter import messagebox


gui13 = Tk()
gui13.title("Scroolbar")
gui13.maxsize(width=1000,height=1000)
gui13.minsize(width=1000,height=1000)

scroll = Scrollbar(gui13)
scroll.pack(side = RIGHT,fill=Y)

mylist = Text(gui13,yscrollcommand=Y)

for i in range(8000):
    mylist.insert(END,i)
    
mylist.pack(side=LEFT,fill =Y)    
scroll.config(command = mylist.yview)

gui13.mainloop()
