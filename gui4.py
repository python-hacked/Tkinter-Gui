from tkinter import *
from tkinter import ttk

# choice box 
gui4 = Tk()
gui4.title("chatbox")

gui4.maxsize(width=1000,height=1000)
gui4.minsize(width=1000,height=1000)

def func():
    if var.get ==0:
        print("female")
    else:
        print("male")
    
var = IntVar()

radio = Radiobutton(gui4,text ="male",value =1,variable= var).pack()
radio = Radiobutton(gui4,text ="female",value = 0,variable =var).pack()
btn = Button(gui4,text = "ok",command =func).pack()

gui4.mainloop()
