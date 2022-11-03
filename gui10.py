import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
from tkinter import *


gui6 = Tk()
gui6.title("chatbox")

gui6.maxsize(width=1000,height=1000)
gui6.minsize(width=1000,height=1000)
def UploadAction(event=None):
    filename = filedialog.askopenfilename()
    print('Selected:', filename)

# gui6 = tk.Tk()
button = tk.Button(gui6, text='Open', command=UploadAction)
button.pack()

gui6.mainloop()