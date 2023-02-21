from tkinter import *
a=Tk()

a.title("Hostel Management")

a.configure(bg='White')
a.maxsize(width=1000,height=1000)
a.minsize(width=1000,height=1000)
label1=Label(a,text='Hostel Management',font=('Times New Roman',28),fg='Navy Blue',bg='White').place(x=380,y=20)
label2=Label(a,text='The hostel management system is to take care of all the hostel activities such as rooms,fees,and admission and provides reports for \n easy transactions. Additionally, it makes sure the facilities of students are well equipped with private indoor/outdoor bathrooms,\n study rooms, dormitory facilities that are ready-made for all the students. ',font=('Times New Roman',13),bg='White').place(x=30,y=80)
a.iconbitmap('H:\\My Drive\\a\\icon.ico')
# bg=PhotoImage(file='action-dialogue-change-hero-800x450.png')
# label3=Label(a,image=bg).place(x=100,y=200)

Label3=Label(a,text='Login :',font=('Times New Roman',20),bg='White',fg='Navy Blue').place(x=10,y=180)
label3=Label(a,text='Email* : ',font=('Roboto',12),bg='White').place(x=10,y=230)
entry1=Entry(a,borderwidth=5).place(x=100,y=230)
label4=Label(a,text='Password* :',font=('Roboto',12),bg='White').place(x=10,y=280)
entry2=Entry(a,borderwidth=5).place(x=100,y=280)
button1=Button(a,text='Login',bg='White',font=('Times New Roman',12),borderwidth=2,padx=15,pady=5).place(x=80,y=340)
bg=PhotoImage(file='Hostel-Managemen-info_474x397 (3).png')
image=Label(a,image=bg).place(x=450,y=180)
bg1=PhotoImage(file='colorfull.png')
image1=Label(a,image=bg1).place(x=0,y=520)

a.mainloop()
