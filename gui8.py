from tkinter import *
from tkinter import ttk
from tkinter import messagebox
# choice box 
gui8 = Tk()
gui8.title("chatbox")

gui8.maxsize(width=1000,height=1000)
gui8.minsize(width=1000,height=1000)
canvas = Canvas()
card = 10,10,200,100
canvas.create_arc(card,start =0,extent = 150 ,fill = "red")
canvas.create_line(card)
canvas.create_oval(card)
canvas.pack()


# btn = Button(gui8,text="Cleck Me",bg = "green",command=func).pack()
    

# lst.pack()








gui8.mainloop()
