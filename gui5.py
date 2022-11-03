from tkinter import *
from tkinter import ttk
# choice box 
gui5 = Tk()
gui5.title("chatbox")

gui5.maxsize(width=1000,height=1000)
gui5.minsize(width=1000,height=1000)

tophader = Frame(gui5)
tophader.pack(side=LEFT)

bottem = Frame(gui5)
bottem.pack(side= BOTTOM)

label = Label(tophader,text = 'this is hader').pack()

label = Label(bottem,text = 'this is bottem').pack()



gui5.mainloop()
