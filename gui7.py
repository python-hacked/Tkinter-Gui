from tkinter import *
from tkinter import ttk
from tkinter import messagebox
# choice box 
gui7 = Tk()
gui7.title("chatbox")

gui7.maxsize(width=1000,height=1000)
gui7.minsize(width=1000,height=1000)

def func():
    lst.delete(ANCHOR)

lst = Listbox(gui7, width =27)
itmes = ["Apple", "Banana", "Mango"]

for i in itmes:
    lst.insert(END,i)
btn = Button(gui7,text="Cleck Me",bg = "green",command=func).pack()
    

lst.pack()








gui7.mainloop()
