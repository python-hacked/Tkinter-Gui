from tkinter import *
from tkinter import ttk
from tkinter import messagebox


gui6 = Tk()
gui6.title("chatbox")

gui6.maxsize(width=1000,height=1000)
gui6.minsize(width=1000,height=1000)
def func():
    if var.get()=="":
        messagebox.showwarning("WARNING", "Empty box")
    else:
        messagebox.askyesno("Title","Do you want to Exit")
        gui6.destroy()
        # messagebox.showinfo("success", var.get())    

var = StringVar()
ent = Entry(gui6,textvariable = var)
ent.pack()

btn = Button(gui6,text="Cleck Me",bg = "green",command=func).pack()

gui6.mainloop()
