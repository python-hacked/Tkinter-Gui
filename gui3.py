from tkinter import *
from tkinter import ttk
# choice box 
gui3 = Tk()
gui3.title("chatbox")

gui3.maxsize(width=1000,height=1000)
gui3.minsize(width=1000,height=1000)
def func():
    print(check1.get())
    print(check2.get())
    
check1 =  IntVar()
check2 =  IntVar()

select = Checkbutton(gui3,text = "male",variable= check1,onvalue=1,offvalue=0)
select.pack()

select = Checkbutton(gui3,text = "female",variable = check2,onvalue=1,offvalue=0)
select.pack()
btn = Button(gui3,text="data get",command=func).pack()


gui3.mainloop()
