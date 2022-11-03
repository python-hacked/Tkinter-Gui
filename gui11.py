import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter.filedialog import askopenfile
from PIL import Image, ImageTk
from tkinter import ttk


my_w = tk.Tk()
my_w.geometry("410x300")  # Size of the window 
my_w.title('www.plus2net.com')
my_font1=('times', 18, 'bold')
l1 = tk.Label(my_w,text='Upload Files & display',width=35,font=my_font1)  
l1.grid(row=1,column=1,columnspan=4)
b1 = tk.Button(my_w, text='Upload Files', 
   width=20,command = lambda:upload_file())
b1.grid(row=2,column=1,columnspan=4)

#this is Thumbnail
# my_font1=('times', 18, 'bold')
# l2 = tk.Label(my_w,text='Upload Files & display',width=35,font=my_font1)  
# l2.grid(row=1,column=1,columnspan=4)
# b2 = tk.Button(my_w, text='Upload Thumbnal', 
#    width=20,command = lambda:upload_file())
# b2.grid(row=2,column=1,columnspan=4)

# this is a title of cource
lbl = Label(my_w,text = "Title",fg="black")
lbl.place(x= 10,y=80)
ent = Entry(my_w,fg = "black",bd = "3", width=29)
ent.place(x=90,y=70)

# this is a cource dicraption
T = Label(my_w,text = "Dicraption",fg="black")
T.place(x= 10,y=120)
T = tk.Text(my_w,height=2, width=30)
T.place(x = 90, y = 110)

# this is a cource choice
com = Label(my_w,text = "Cource",fg="black")
com.place(x= 10,y=160)
com = ttk.Combobox(my_w,width=28)
com["state"]="readonly"
com['values']=('English','Hindi',)
com.current(0)
com.place(x=90,y=160)

#this is a cource category
com = Label(my_w,text = "Category",fg="black")
com.place(x= 10,y=190)
com = ttk.Combobox(my_w,width=28)
com["state"]="readonly"
com['values']=('jan','feb',)
com.current(0)
com.place(x=90,y=190)

# this is Teacher
com = Label(my_w,text = "Teacher",fg="black")
com.place(x= 10,y=220)
com = ttk.Combobox(my_w,width=28)
com["state"]="readonly"
com['values']=('Rahul','satish',)
com.current(0)
com.place(x=90,y=220)

btn = Button(my_w,text = "Upload")
btn.place(x = 150, y=250)

def upload_file():
    f_types = [
        # ('Jpg Files', '*.jpg'),
    # ('PNG Files','*.png'),
    ('video Files', '*.mp3')]   # type of files to select 
    filename = tk.filedialog.askopenfilename(multiple=True,filetypes=f_types)
    col=1 # start from column 1
    row=3 # start from row 3 
    for f in filename:
        img=Image.open(f) # read the image file
        img=img.resize((100,100)) # new width & height
        img=ImageTk.PhotoImage(img)
        e1 =tk.Label(my_w)
        e1.grid(row=row,column=col)
        e1.image = img
        e1['image']=img # garbage collection 
        if(col==3): # start new line after third column
            row=row+1# start wtih next row
            col=1    # start with first column
        else:       # within the same row 
            col=col+1 # increase to next column  
            
                           
my_w.mainloop()  # Keep the window open
