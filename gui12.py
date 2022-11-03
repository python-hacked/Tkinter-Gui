from tkinter import *
from tkinter import ttk
from tkinter import messagebox


gui12 = Tk()
gui12.title("Progresbar")

gui12.maxsize(width=1000,height=1000)
gui12.minsize(width=1000,height=1000)


def func():
    import time
    progres ['value'] = 20
    progres.update_idletasks()
    time.sleep(0.5)
    
    progres ['value'] = 50
    progres.update_idletasks()
    time.sleep(0.5)
    
    progres ['value'] = 70
    progres.update_idletasks()
    time.sleep(0.5)
    
    progres ['value'] = 60
    progres.update_idletasks()
    time.sleep(0.5)
    
    
    progres ['value'] = 50
    progres.update_idletasks()
    time.sleep(0.5)
    
    
    progres ['value'] = 20
    progres.update_idletasks()
    time.sleep(0.5)
    
    
    progres ['value'] = 40
    progres.update_idletasks()
    time.sleep(0.5)
    
    
    progres ['value'] = 100
    progres.update_idletasks()
    time.sleep(0.5)
    
    
    progres ['value'] = 50
    progres.update_idletasks()
    time.sleep(0.5)
    
    
    progres ['value'] = 20
    progres.update_idletasks()
    time.sleep(0.5)
    
    
    progres ['value'] = 80
    progres.update_idletasks()
    time.sleep(0.5)
    
    
    progres ['value'] = 40
    progres.update_idletasks()
    time.sleep(0.5)
    
    
    
progres = ttk.Progressbar(gui12, orient=HORIZONTAL, length =100,mode = 'determinate')# secand mood  indeterminate

progres.pack()

btn = Button(gui12,text = "Start",command = func).pack()

gui12.mainloop()
