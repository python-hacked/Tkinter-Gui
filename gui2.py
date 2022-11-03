from tkinter import *
from tkinter import ttk
# choice box 
gui2 = Tk()
gui2.title("chatbox")

gui2.maxsize(width=1000,height=1000)
gui2.minsize(width=1000,height=1000)

var = StringVar()
com = ttk.Combobox(gui2,width=27)
com["state"]="readonly"
com['values']=('jan','feb',)
com.current(0)
com.place(x=20,y=20)



gui2.mainloop()
