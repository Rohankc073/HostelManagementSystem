

import sqlite3
import tkinter.messagebox
from tkinter import messagebox
from tkinter import *

def verify():
    conn = sqlite3.connect('signup.db')
    c = conn.cursor()

    email = entry1.get()
    password = entry2.get()

    if email == '' or password == '':
        messagebox.showinfo('Incomplete Information', 'Enter all the given credentials')
        return

    c.execute('SELECT * FROM users WHERE email = ? AND pass = ?', (email, password))
    user = c.fetchone()

    if user:
        messagebox.showinfo('Login Successful', 'Login Successfully')
        a.destroy()
        import dashboard
    else:
        messagebox.showinfo('Incorrect Information', 'Invalid username or password')

    conn.commit()
    conn.close()

#===================================UI DESIGN===================================
a=Tk()
a.title('Login')
a.configure(bg='White')
a.iconbitmap('H:\\My Drive\\a\\icon.ico')
a.maxsize(width=1000,height=660)
a.minsize(width=1000,height=660)
canvas=Canvas(a,bg='#06518d',height=1000,width=500).place(x=500,y=0)
ig1=PhotoImage(file='graphic5 (3).png')
#===================================LABEL AND ENTRY FOR LOGIN PAGE=================================================
image=Label(a,image=ig1,bg='White').place(x=95,y=200)
label1=Label(a,text=' Hostel Management System -\n All in one Application!',font=('Times New Roman',24,'bold'),fg='#06518d',bg='White').place(x=50,y=50)
label2=Label(a,text='One place for all your needs.',font=('Calisto MT Bold',18),bg='White',fg='#06518d').place(x=100,y=125)
label4=Label(a,text='_______',bg='#06518d',font=('Calisto MT Bold',14,'bold'),fg='White').place(x=600,y=195)
label3=Label(a,text='Login',bg='#06518d',font=('Calisto MT Bold',18,'bold'),fg='White').place(x=600,y=180)
label5=Label(a,text='Email :',bg='#06518d',font=('Calisto MT Bold',14,'bold'),fg='White').place(x=600,y=230)
entry1=Entry(a,borderwidth=1,bg='White')
entry1.config(width=30)
entry1.place(x=710,y=235)
label6=Label(a,text='Password :',bg='#06518d',font=('Calisto MT Bold',14,'bold'),fg='White').place(x=600,y=270)
entry2=Entry(a,borderwidth=1,bg='White',show='*')
entry2.config(width=30)
entry2.place(x=710,y=275)
#==============================================Button=============================
def admin():
    a.destroy()
    import Adminlogin
button1=Button(a,text='Login As Admin',fg='#06518d',bg='White',font=('Calisto MT Bold',14,'bold'),height=1,width=12,command=admin).place(x=750,y=360)

#=========================================Checkbox========================================
show_pass = IntVar()
def show_pass_check():
    if show_pass.get():
        entry2.config(show='')
    else:
        entry2.config(show='*')

C1=Checkbutton(a,text='Show Password',bg='#06518d',fg='White',font=('Calisto MT Bold',10),command=show_pass_check,variable=show_pass,offvalue=0,onvalue=1)
C1.place(x=600,y=310)

# def invalid():
#     invalid=tkinter.messagebox.Message('Invalid','Invalid Crediantials')


def me():
    a.destroy()
    import dashboard
button1=Button(a,text='Login',fg='#06518d',bg='White',font=('Calisto MT Bold',14,'bold'),height=1,width=7,command=verify).place(x=600,y=360)

# def forget():
#     a.destroy()
#     import fpas

# label7=Button(a,text='Forgot Password?',bg='White',fg='#06518d',font=('Roboto ',10),command=forget).place(x=780,y=300)

label8=Label(a,text=' * By Login means you are agreeing to our \n Tearms Of Service and Privacy Policy.',bg='#06518d',fg='White',font=('Roboto ',10,'bold')).place(x=600,y=420)


img3=PhotoImage(file='add-on-services.png')
image=Label(a,image=img3,bg='White').place(x=300,y=500)


a.mainloop()
#

