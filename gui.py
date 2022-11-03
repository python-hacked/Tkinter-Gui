from tkinter import *
 
 
gui = Tk ()
gui.title("imegnus")

# gui.iconbitmap('icon.ico')
# gui.geometry('600*300')
#window size min and max

gui.maxsize(width=1000,height=1000)
gui.minsize(width=1000,height=1000)

#funcation
def func():
    x=var.get()
    lbl.config(text = x,bg = "green")
    
# create label
lbl = Label(gui,text = "username",bg="red",fg="black")#use funcation opctionl
# first opctionl(pack,gride,place)

lbl.place(x= 10,y=10)
# con = StringVar()
lbl = Label(gui,text = "nathing",bg="black",fg="white")#show data on display
lbl.place(x= 40,y=120)

#entrybox
var = StringVar()
ent = Entry(gui,bg = "red",fg = "black",bd = "5",textvariable=var)
ent.place(x=80,y=10)

# buttion
btn = Button(gui,text="submit",bg = "green",command=func) 
btn.place(x=60,y=60)

gui.mainloop()