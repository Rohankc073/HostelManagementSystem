from tkinter import *
import sys
# import tkinter as Tk
from tkinter import messagebox
from PIL import ImageTk,Image

def command1(event):
    if entry1.get()=='admin'and entry2.get()=='password'or  entry1.get()=='test'and entry2.get()=='pass':
        messagebox.showinfo('Valid','Login Successfull')
        root.deiconify()
        top.destroy()

def command2():
    top.destroy()
    root.destroy()
    sys.exit()

root=Tk()
top=Toplevel()
top.geometry('500x500')
top.title("LOGIN SCREEN")
# path = "H:\\My Drive\\a\\images (1).jpg"
# img1 = ImageTk.PhotoImage(Image.open(path))
# l1 = Label(top, image=img1, height=500, width=500, bg='blue')
# l1.image = img1
# l1.place(x=0, y=0)
frame1=Frame(height=100,width=100,bg='#06518d')
frame1.place(x=50,y=50)
# top.configure(bg='white')

lbl1=Label(root,text='Username:',font={'Helvetica',10},fg='white')
entry1=Entry(top)
lbl2=Label(top,text='Password:',font={'Helvetica',10})
entry2=Entry(top,show='*')
button2=Button(top,text='Cancel',command=lambda:command2())
entry2.bind('<Return>', command1)
lbl3= Label(top,text='Copyright Login Screen 2023',font={'Arial',9})
lbl1.place(x=5,y=10)
entry1.pack()
lbl2.pack()
entry2.pack()
button2.pack()
lbl3.pack()
root.title('Main Screen')
root.configure(bg='white')
root.geometry("850x650")
root.withdraw()
root.mainloop()