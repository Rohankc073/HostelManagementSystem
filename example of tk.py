# import tkinter
# from tkinter import*
# a=Tk()
# a.title('GUI')
# a.configure(bg='sky blue')
# user_name=Label(a,text='User Name',font='Arial').place(x=30,y=50)
# password=Label(a,text='Password',font='Arial').place(x=30,y=90)
# email=Label(a,text='Email',font='Ariel').place(x=30,y=130)
# myLabel=Label(a,text='Tkinter')
# button1=tkinter.Button(a,text='Login')
# button1.place(x=70,y=170)
# myLabel.pack()
# a.mainloop()


# #TO click a button
# from tkinter import *
# a=Tk()
# def fun():
#     print("jhedgcusdjv")
# a.maxsize(width=300,height=300)
# a.minsize(width=300,height=300)
#
#
# btn=Button(a,text="Login",command=fun)
# btn.pack(side='top')
# a.mainloop()

# #Creating Button
# from tkinter import*
# a=Tk()
# def myClick():
#     myLabel=Label(a,text="Look I clicked the button",fg='red',font=('Ariel',13))
#     myLabel.pack()
#
# my_button=Button(a,text='Click me',padx=10,pady=10,command=myClick,fg='red',bg='blue')
# my_button.pack()
# a.mainloop()
#
# #Disabling a button
# from tkinter import*
# a=Tk()
# def myClick():
#     myLabel=Label(a,text="Look I clicked the button",fg='red',font=('Ariel',13))
#     myLabel.pack()
#
# my_button=Button(a,text='Click me',padx=10,pady=10,command=myClick,fg='red',bg='blue')
# my_button1=Button(a,text='Click me',padx=10,pady=10,command=myClick,fg='red',bg='blue',state=DISABLED)
# my_button.pack()
# my_button1.pack()
# a.mainloop()

# from tkinter import *
# a=Tk()
#
# e=Entry(a,width=50,bg='blue',fg='white',borderwidth=5,font=20)
# e.pack()
#
# def myClick():
#     myLabel=Label(a,text='Hi ' + e.get())
#     myLabel.pack()
#     e.delete(0,END)
#
# btn=Button(a,text='click me',padx=10,pady=10,command=myClick)
# btn.pack()
# a.mainloop()

# #Getting entry
# from tkinter import *
# a=Tk()
# a.title('GUI')
# a.maxsize(width=600,height=300)
# a.minsize(width=600,height=300)
# #function
# def add():
#     x=var.get()
#
#     mylabel.config(text=x,bg='green')
# #label1
# mylabel=Label(a,text='User Name',fg='red',bg='yellow')
# mylabel.place(x=10,y=120)
# #label2
# mylabel1=Label(a,text='User Name',fg='red',bg='yellow')
# mylabel1.place(x=40,y=120)
# #entry
# var=StringVar()
# ent=Entry(a,bg='black',fg='white',textvariable=var)
# ent.place(x=80,y=10)
# #button
# btn=Button(a,text='Submit',bg='green',fg='white',command=add)
# btn.place(x=20,y=80)
# a.mainloop()

# #Text Widget
# from tkinter import*
# a=Tk()
#
# def click():
#     text1='Address: '+ mytext.get('1.0',END)
#     lbl.config(text=str(text1))
#
# mytext=Text(a,font=20,width=20,height=10)
# mytext.place(x=0,y=50)
#
# btn=Button(root,text='Click Me',font=30,command=click)

#
# from tkinter import*
# a=Tk()
# a.geometry('500x500')
# a.title('Hostel Management System')
# label=Label(a,text='Welcome!',font=('Algerian',18))
# label.pack(padx=20,pady=20)
#Using Entry to leave a space using entry.This is more useful then text in making login and registration
# e1=Entry(a).pack()
#Using Text
# e2=Text(a,height=3,font=('Arial',16))
# e2.pack()
#add a button
# button=Button(a,text='Click me!',font=('Algerian',14))
# button.pack(padx=20,pady=20)

# #This is from youtube
# buttonframe=Frame(a)
# buttonframe.columnconfigure(0,weight=1)
# buttonframe.columnconfigure(1,weight=1)
# buttonframe.columnconfigure(2,weight=1)
#
# btn1=Button(buttonframe,text='1',font=('Arial',18))
# btn1.grid(row=0,column=0)
#
# btn2=Button(buttonframe,text='2',font=('Arial',18))
# btn2.grid(row=0,column=1)
#
# btn3=Button(buttonframe,text='3',font=('Arial',18))
# btn3.grid(row=0,column=2)
#
# buttonframe.pack()

#Frame using sir methods
# from tkinter import*
# a=Tk()
# a.geometry('500x500')
# a.title('Hostel Management System')
# label=Label(a,text='Welcome!',font=('Algerian',18))
# label.pack(padx=20,pady=20)
# Frame=LabelFrame(a,text="My Frame",padx=5,pady=5,bg='Black')
# Frame.pack(padx=10,pady=10)
# b=Button(Frame,text="Dont click here")
# b2=Button(Frame,text='...here')
# b.grid(row=0,column=0)
# b2.grid(row=1,column=1)

#Radio Button# using this the output is printed in the termianal
# def add():
#     selection = 'You have selected option' + str(var.get())
#     label.config(text=selection)
     # print(var.get())

# var=IntVar()
# r1=Radiobutton(a,text='Male',variable=var,value=1,command=add)
# r1.pack(anchor=W)
# r2=Radiobutton(a,text='Female',variable=var,value=2,command=add)
# r2.pack(anchor=W)
# label=Label(a)
# label.pack()


#Check button
from tkinter import*
from PIL import Image,ImageTk
a=Tk()
# a.maxsize(width=280,height=350)
# a.minsize(width=280,height=380)
# a.geometry('500x500')
# a.title('Hostel Management System')
# def add():
#     label.config(text=CheckVar1.get())
# CheckVar1=IntVar()
#
# C1=Checkbutton(a,text='Music',variable=CheckVar1,onvalue=1,offvalue=0,height=5,width=20)
# C1.pack()
# btn=Button(a,text='Click',command=add)
# label=Label(a,text='')
# label.pack()
# btn.pack()

# #Adding message box
# from tkinter import messagebox
# def popup():
#     messagebox.showinfo('This is my popup','HI ROhan')
#
# btn=Button(a,text='Popup',command=popup).pack()

# #Adding image
# bg=PhotoImage(file='Spider.png')
# bg1=PhotoImage(file='Nike.png')
# my_label1=Label(a,image=bg1).place(x=100,y=130)
# my_label=Label(a,image=bg,height=100,width=1000).place(x=50,y=50)#we can even resize like this

# #TO resize the imgae
# my_image=Image.open('Spider.png')
# resized_image=my_image.resize((300,250))
# converted_image=ImageTk.PhotoImage(resized_image)
# mylabel=Label(a,image=converted_image,width=300,height=180).pack()
# btn=Button(a,text='Exit',command=a.quit,width=20).pack()

# #To open another window in with a image in it
# def open():
#     global my_image
#     top=Toplevel()
#     my_image=ImageTk.PhotoImage(Image.open('Nike.png'))
#     my_label=Label(top,image=my_image).pack(pady=10)
#     btn=Button(top,text='Close Window',command=top.destroy).pack()
#
# btn=Button(a,text='Open',command=open).pack()
a.title('Simple Calculator ')
a.configure(bg='Navy')
e=Entry(a,width=35,borderwidth=5)
e.grid(row=0,column=0,columnspan=3,padx=10,pady=10)

def button_click(number):
    current=e.get()
    e.delete(0,END)
    e.insert(0,str(current)+str(number))

def button_clear():
    e.delete(0,END)

def button_add():
    first_number=e.get()
    global f_num
    f_num=int(first_number)
    e.delete(0,END)
    global button_clicked
    button_clicked='+'

def button_multiply():
    first_number=e.get()
    global f_num
    f_num=int(first_number)
    e.delete(0,END)
    global button_clicked
    button_clicked='*'

def button_subtract():
    first_number=e.get()
    global f_num
    f_num=int(first_number)
    e.delete(0,END)
    global button_clicked
    button_clicked='-'

def button_divided():
    first_number=e.get()
    global f_num
    f_num=int(first_number)
    e.delete(0,END)
    global button_clicked
    button_clicked='/'




def button_equal():
    second_number=e.get()
    e.delete(0,END)
    if button_clicked=='+':
     e.insert(0, f_num + int(second_number))
    elif button_clicked=='*':
     e.insert(0, f_num * int(second_number))
    elif button_clicked=='-':
     e.insert(0,f_num-int(second_number))
    elif button_clicked=='/':
     e.insert(0,f_num / int(second_number))


#Defining the buttons
button_1=Button(a,text='1',padx=40,pady=20,bg='Dodgerblue',command=lambda : button_click(1))
button_2=Button(a,text='2',padx=40,pady=20,bg='Dodgerblue',command=lambda : button_click(2))
button_3=Button(a,text='3',padx=40,pady=20,bg='Dodgerblue',command=lambda : button_click(3))
button_4=Button(a,text='4',padx=40,pady=20,bg='Dodgerblue',command=lambda : button_click(4))
button_5=Button(a,text='5',padx=40,pady=20,bg='Dodgerblue',command=lambda : button_click(5))
button_6=Button(a,text='6',padx=40,pady=20,bg='Dodgerblue',command=lambda : button_click(6))
button_7=Button(a,text='7',padx=40,pady=20,bg='Dodgerblue',command=lambda : button_click(7))
button_8=Button(a,text='8',padx=40,pady=20,bg='Dodgerblue',command=lambda : button_click(8))
button_9=Button(a,text='9',padx=40,pady=20,bg='Dodgerblue',command=lambda : button_click(9))
button_0=Button(a,text='0',padx=40,pady=20,bg='Dodgerblue',command=lambda : button_click(0))
button_add=Button(a,text='+',padx=40,pady=20,bg='Dodgerblue',command=button_add)
button_equal=Button(a,text='=',padx=40,pady=20,bg='Dodgerblue',command=button_equal)
button_multiply=Button(a,text='X',padx=40,pady=20,bg='Dodgerblue',command=button_multiply).grid(row=5,column=2)
button_subtract=Button(a,text='-',padx=40,pady=20,bg='Dodgerblue',command=button_subtract).grid(row=4,column=2)
button_clear=Button(a,text='Clear',padx=30,pady=20,bg='Dodgerblue',command=button_clear)
button_divided=Button(a,text='/',padx=40,pady=20,bg='Dodgerblue',command=button_divided).grid(row=6,column=0)


#Putting buttons on the screen
button_1.grid(row=3,column=0)
button_2.grid(row=3,column=1)
button_3.grid(row=3,column=2)
button_4.grid(row=2,column=0)
button_5.grid(row=2,column=1)
button_6.grid(row=2,column=2)
button_7.grid(row=1,column=0)
button_8.grid(row=1,column=1)
button_9.grid(row=1,column=2)
button_0.grid(row=4,column=0)

button_clear.grid(row=4,column=1)
button_add.grid(row=5,column=0)
button_equal.grid(row=5,column=1)


a.mainloop()


