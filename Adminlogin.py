from tkinter import *
import sys
# import tkinter as Tk
from tkinter import messagebox
from PIL import ImageTk,Image

#=============================Verify the admin=====================
def command1():
    if entry1.get()=='admin'and entry2.get()=='password'or  entry1.get()=='test'and entry2.get()=='pass':
        messagebox.showinfo('Valid','Login Successfull')
        # root.deiconify()
        a.destroy()
        import ADash

    elif entry1.get() == '' or entry2.get() == '':
        messagebox.showinfo('Incomplete Information', 'Enter all the given credientials')

    else:
        entry1.get()!='admin' or 'test' and entry2.get()!='password' or 'pass'
        messagebox.showinfo('Incorrect Information', 'Invalid username or password')

def command2():
    a.destroy()
    # root.destroy()
    sys.exit()

#================================UI DESIGN=================================
a=Tk()
a.title('Admin Login')
a.minsize(height=500,width=500)
a.maxsize(height=500,width=500)
path = "H:\\My Drive\\a\\images (1).jpg"
img1 = ImageTk.PhotoImage(Image.open(path))
l1 = Label(a, image=img1, height=500, width=500, bg='blue')
l1.image = img1
l1.place(x=0, y=0)
frame1=Frame(height=400,width=300,bg='#06518d')
frame1.place(x=100,y=50)
path1="H:\\My Drive\\a\\5138226-1024x1024.jpg"
img2=ImageTk.PhotoImage(Image.open(path1))
l2=Label(a,image=img2,height=80,width=100,bg='#06518d')
l2.image=img2
l2.place(x=100,y=250)
# path2="H:\\My Drive\\a\\066962700_1627031568-Admin_1.jpg"
# img3=ImageTk.PhotoImage(Image.open(path2))
# l3=Label(a,image=img3,height=100,width=280)
# l3.image=img3
# l3.place(x=110,y=340)

#====================================Label and Entry for admin login========================

lal=Label(a,text='ADMIN LOGIN',font=('Calisto MT Bold',16),fg='white',bg='#06518d')
lal.place(x=160,y=70)
lbl1=Label(a,text='Username:',font=('Calisto MT Bold',12),fg='white',bg='#06518d')
lbl1.place(x=120,y=130)
entry1=Entry(a,width=25)
entry1.place(x=210,y=135)
lbl2=Label(a,text='Password: ',font=('Calisto MT Bold',12),fg='white',bg='#06518d')
lbl2.place(x=120,y=180)
entry2=Entry(a,width=25,show='*')
entry2.place(x=210,y=180)
lbl3=Label(a,text='Copyright Login Screen 2023',font=('Calisto MT Bold',10),fg='white',bg='#06518d')
lbl3.place(x=160,y=220)
button1=Button(a,text='Login',bg='white',fg='#06518d',font=('Calisto MT Bold',10),width=10,command=command1)
button1.place(x=200,y=260)
button2=Button(a,text='Cancel',bg='white',fg='#06518d',font=('Calisto MT Bold',10),width=10,command=command2)
button2.place(x=200,y=300)

a.mainloop()