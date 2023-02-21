from tkinter import*
a=Tk()
a.title('Hostel Management System')
# a.iconbitmap('H:\\My Drive\\a\\icon.ico')
# a.maxsize(width=300,height=300)
# a.minsize(width=500,height=500)
# a.configure(bg='Sky Blue')
# a.geometry('500x500')
# b1=Button(a,text='Left',fg='green',bg='yellow')
# b1.pack(side=LEFT)
# b2=Button(a,text='Right',fg='blue',bg='Blue')
# b2.pack(side=RIGHT)
# b3=Button(a,text='Top',fg='Green',bg='White')
# b3.pack(side=TOP)
# b4=Button(a,text="Buttom",fg='Black',bg='White')
# b4.pack(side=BOTTOM)
# label=Label(a,text='Welcome!',font=('Algerian',18))
# label.pack(padx=100,pady=90)
#Grid Method
# name=Label(a,text='Name',font=('Algerian',18)).grid(row=0,column=0)
# gu=Label(a,text='Anjali').grid(row=1,column=1)
# ae=Label(a,text='Gu').grid(row=5,column=1)
# b1=Button(a,text='Login',bg='Blue',fg='Black')
# b1.grid(row=10,column=5)
# b2=Button(a,text='Anjali').grid(row=19,column=5)
#PLACE METHOD
# name=Label(a,text='Hi',font=('Algerian')).place(x=10,y=20)
# # b1=Button(a,text='Anjali',font=('Algerian')).place(x=200,y=25)
# e1=Entry(a).place(x=40,y=20)
#To print that i have clicked the button on the termianl
# def func():
#     print('Button is clicked')
# btn=Button(a,text='Login',command=func).pack(side='top')
# def myClick():
#     mylabel=Label(a,text='Look i clicked a button',fg='red',bg='blue',font=50)
#     mylabel.pack()
#
# my_button=Button(a,text='click me',padx=10,pady=10,command=myClick)
# my_button.pack()
#Button with different padding
# mybutton=Button(a,text='Click me').pack()
# mybutton=Button(a,text='Click me',padx=50,pady=50,state=DISABLED).pack()
# mybutton=Button(a,text='Click me').pack()
# mybutton=Button(a,text='Click me',padx=50,pady=50).pack()
#Entry Widegt
# e=Entry(a,width=50,bg='blue',fg='white',font=20)
# e.pack()
# def myClick():
#     myLabel=Label(a,text='Hi ' + e.get())
#     myLabel.pack()
#
# btn=Button(a,text='Click me',command=myClick).pack()


a.mainloop()