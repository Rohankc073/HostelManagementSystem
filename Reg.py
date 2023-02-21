from tkinter import *
import sqlite3
from tkinter import messagebox
# from PIL import image ,ImageTk
root = Tk()
root.title('Registration')

#Opening data base
#===============================CREATING TABLE============================================================

conn=sqlite3.connect('signup.db')
c=conn.cursor()
#Creating a table
c.execute("""CREATE TABLE users (
    fullname text,
    ph_num text,
    email text,
    pass text,
    newpas text
)""")
print('Table created successfully')

root.iconbitmap('H:\\My Drive\\a\\icon.ico')
root.maxsize(width=900,height=650)
root.minsize(width=900,height=650)
root.configure(bg='#fff')
image_1=PhotoImage(file='WhatsApp Image 2023-01-29 at 11.27.52.png')
Label(root,image=image_1,bg='white').place(x=400,y=100)

def register():
    conn=sqlite3.connect('signup.db')
    c=conn.cursor()
    c.execute("INSERT INTO users VALUES(:fullname, :ph_num, :email, :pass, :newpas)",{
        'fullname':FullName.get(),
        'ph_num': phone1.get(),
        'email': email.get(),
        'pass': pas.get(),
        'newpas':newpas.get()
    })
#IF FullNmae .get is ==" "
    #clear text box
    FullName.delete(0,END)
    phone1.delete(0,END)
    email.delete(0,END)
    pas.delete(0,END)
    newpas.delete(0,END)

    messagebox.showinfo('Registration Information','Registered Successfully')

    conn.commit()
    conn.close()

    root.destroy()
    import Login

#=================================LABEL and ENTRY FOR REGISTRATION UI===================================
header=Label(root,text='Register Now',fg='#06518d', bg='white',font=('Calisto MT Bold',26,'bold'))
header.place(x=50,y=50)

para=Label(root,text='Please input your information on fields.',fg='#404040', bg='white',font=('Calisto MT Bold',12,'bold'))
para.place(x=50,y=100)

para1=Label(root,text='Full Name*',fg='black', bg='white',font=('Calisto MT ',12))
para1.place(x=50,y=170)
FullName=Entry(root,width=32,fg='black',border=2,highlightthickness=1,highlightbackground='#F1F0FD',font=('Calisto MT ',10))
FullName.place(x=50,y=190,height=25)

para2=Label(root,text='Phone Number*',fg='black',bg='white',font=('Calisto MT ',12))
para2.place(x=50,y=230)
phone1=Entry(root,width=25,fg='black',border=2,highlightthickness=1,highlightbackground='#F1F0FD',font=('Calisto MT ',12))
phone1.place(x=50,y=250,height=25)

para4=Label(root,text='Email*',fg='black', bg='white',font=('Calisto MT ',12))
para4.place(x=50,y=290)
email=Entry(root,width=25,fg='black',border=2,highlightthickness=1,highlightbackground='#F1F0FD',font=('Calisto MT ',12))
email.place(x=50,y=310,height=25)

para5=Label(root,text='Create Password*',fg='black', bg='white',font=('Calisto MT ',12))
para5.place(x=50,y=350)
pas=Entry(root,width=25,fg='black',border=2,highlightthickness=1,highlightbackground='#F1F0FD',font=('Calisto MT ',12),show="*")
pas.place(x=50,y=370,height=25)

para6=Label(root,text='Confirm Password*',fg='black', bg='white',font=('Calisto MT ',12))
para6.place(x=50,y=420)
newpas=Entry(root,width=25,fg='black',border=2,highlightthickness=1,highlightbackground='#F1F0FD',font=('Calisto MT ',12),show='*')
newpas.place(x=50,y=440,height=25)

#===========================================CHECK BOX======================================
show_pass = IntVar()
def show_pass_check():
    if show_pass.get():
        pas.config(show='')
        newpas.config(show='')
    else:
        pas.config(show='*')
        newpas.config(show='*')

c1 = Checkbutton(root,fg='black',border=0,text ="Show",bg='white',font=('Calisto MT ',8),command=show_pass_check,variable=show_pass,onvalue=1,offvalue=0).place(x=50,y=465)


button1=Button(root,width=10,pady=7,text='Sign up',bg='#06518d',fg='white',border=0,command=register,font=('Calisto MT Bold ',10)).place(x=50,y=520)

def have_acc():
    root.destroy()
    import Login
para3=Button(root,text='Already have an account? ',fg='white', bg='#06518d',font=('Calisto MT ',10),command=have_acc)
para3.place(x=100,y=590)


conn.commit()
conn.close()

root.mainloop()