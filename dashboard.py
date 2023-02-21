from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image
import sqlite3
from tkinter import ttk
a=Tk()
a.title('Dash Board')
a.geometry('2000x2000')
a.iconbitmap('H:\\My Drive\\a\\icon.ico')
ig1=PhotoImage(file='white-elegant-powerpoint-background-27.png')
image=Label(a,image=ig1,bg='white')\
    .place(x=0,y=0)
canvas=Canvas(a,bg='#06518d',height=1000,width=300)\
    .place(x=0,y=0)
import sqlite3

# Connect to the database and create a new table called "students"
# conn = sqlite3.connect('students.db')
# c = conn.cursor()
# c.execute('''CREATE TABLE booking
#              (name TEXT,
#               p_number INTEGER,
#               parent_name TEXT,
#               school_name TEXT,
#               email TEXT)''')
# conn.commit()
# conn.close()


path1="C:\\Users\\Dell\\Downloads\\aebda5a3ba478eda1324412ff14b38f1.jpg"
img1=ImageTk.PhotoImage(Image.open(path1))
l1=Label(a,image=img1,height=400,width=790,bg='white')
l1.image=img1
l1.place(x=390,y=90)
#======================================================LABEL============================================================
label1=Label(a,text='Hostel Management System',font=('Calisto MT Bold',26),bg='white',fg='#06518d')
label1.place(x=560,y=20)
Frame(a, height=550, width=250, bg='white')\
    .place(x=27, y=80)
label2=Label(a,text='DASHBOARD',font=('Calisto MT Bold',18),bg='#06518d',fg='white')
label2.place(x=55,y=40)

def room():

    frame1 = Frame(a, height=450, width=800, bg='#06518d')\
        .place(x=390, y=90)
    frame2=Frame(frame1,height=400,width=740,bg='white')\
        .place(x=420,y=120)
    path="C:\\Users\\Dell\\Downloads\\hroom (2).jpg"
    img=ImageTk.PhotoImage(Image.open(path))
    label=Label(frame2,image=img,height=250,width=450,bg='white')
    label.image=img
    label.place(x=700,y=150)
    rlabel=Label(frame2,text='*All prices are encluxive of all taxes',fg='#06518d',bg='white',font=('Calisto MT Bold',14))
    rlabel.place(x=700,y=480)
    rlabel1=Label(frame2,text='ROOM DETAILS:',fg='#06518d',bg='white',font=('Calisto MT Bold',14))
    rlabel1.place(x=430,y=120)

    #===============================================Button For Every Room================================================

    def room1():
        rframe=Frame(frame2,height=320,width=300,bg='#06518d')
        rframe.place(x=800,y=150)
        rframe1=Frame(frame2,height=280,width=260,bg='white')
        rframe1.place(x=820,y=170)
        rlabel1=Label(frame2,text='Total Beds:',bg='white',fg='#06518d',font=('Calisto MT Bold',14))
        rlabel1.place(x=830,y=200)
        rlabel2=Label(frame2,text='4',bg='white',fg='#06518d',font=('Calisto MT Bold',14))
        rlabel2.place(x=940,y=200)
        rlabel3=Label(frame2,text='WiFi Available:',bg='white',fg='#06518d',font=('Calisto MT Bold',14))
        rlabel3.place(x=830,y=230)
        rlabel4=Label(frame2,text='Yes',bg='white',fg='#06518d',font=('Calisto MT Bold',14))
        rlabel4.place(x=980,y=230)
        rlabel5=Label(frame2,text='Price:',bg='white',fg='#06518d',font=('Calisto MT Bold',14))
        rlabel5.place(x=830,y=260)
        rlabel6=Label(frame2,text='NRP 16,000',bg='white',fg='#06518d',font=('Calisto MT Bold',14))
        rlabel6.place(x=885,y=260)
        rlabel7=Label(frame2,text='Status :',bg='white',fg='#06518d',font=('Calisto MT Bold',14))
        rlabel7.place(x=830,y=290)
        rlabel8=Label(frame2,text='Available',bg='white',fg='#06518d',font=('Calisto MT Bold',14))
        rlabel8.place(x=900,y=290)

    def room2():
        rframe=Frame(frame2,height=320,width=300,bg='#06518d')
        rframe.place(x=800,y=150)
        rframe1=Frame(frame2,height=280,width=260,bg='white')
        rframe1.place(x=820,y=170)
        rlabel1=Label(frame2,text='Total Beds:',bg='white',fg='#06518d',font=('Calisto MT Bold',14))\
            .place(x=830,y=200)
        rlabel2=Label(frame2,text='3',bg='white',fg='#06518d',font=('Calisto MT Bold',14))\
            .place(x=940,y=200)
        rlabel3=Label(frame2,text='WiFi Available:',bg='white',fg='#06518d',font=('Calisto MT Bold',14))\
            .place(x=830,y=230)
        rlabel4=Label(frame2,text='No',bg='white',fg='#06518d',font=('Calisto MT Bold',14))\
            .place(x=980,y=230)
        rlabel5=Label(frame2,text='Price:',bg='white',fg='#06518d',font=('Calisto MT Bold',14))\
            .place(x=830,y=260)
        rlabel6=Label(frame2,text='NRP 18,000',bg='white',fg='#06518d',font=('Calisto MT Bold',14))\
            .place(x=885,y=260)
        rlabel7=Label(frame2,text='Status :',bg='white',fg='#06518d',font=('Calisto MT Bold',14))\
            .place(x=830,y=290)
        rlabel8=Label(frame2,text=' Not Available',bg='white',fg='#06518d',font=('Calisto MT Bold',14))\
            .place(x=900,y=290)

    def room3():
        rframe=Frame(frame2,height=320,width=300,bg='#06518d')\
            .place(x=800,y=150)
        rframe1=Frame(frame2,height=280,width=260,bg='white')\
            .place(x=820,y=170)
        rlabel1=Label(frame2,text='Total Beds:',bg='white',fg='#06518d',font=('Calisto MT Bold',14))\
            .place(x=830,y=200)
        rlabel2=Label(frame2,text='2',bg='white',fg='#06518d',font=('Calisto MT Bold',14))\
            .place(x=940,y=200)
        rlabel3=Label(frame2,text='WiFi Available:',bg='white',fg='#06518d',font=('Calisto MT Bold',14))\
            .place(x=830,y=230)
        rlabel4=Label(frame2,text='Yes',bg='white',fg='#06518d',font=('Calisto MT Bold',14))\
            .place(x=980,y=230)
        rlabel5=Label(frame2,text='Price:',bg='white',fg='#06518d',font=('Calisto MT Bold',14))\
            .place(x=830,y=260)
        rlabel6=Label(frame2,text='NRP 20,000',bg='white',fg='#06518d',font=('Calisto MT Bold',14))\
            .place(x=885,y=260)
        rlabel7=Label(frame2,text='Status :',bg='white',fg='#06518d',font=('Calisto MT Bold',14))\
            .place(x=830,y=290)
        rlabel8=Label(frame2,text=' Not Available',bg='white',fg='#06518d',font=('Calisto MT Bold',14))\
            .place(x=900,y=290)

    def room4():
        rframe=Frame(frame2,height=320,width=300,bg='#06518d')\
            .place(x=800,y=150)
        rframe1=Frame(frame2,height=280,width=260,bg='white')\
            .place(x=820,y=170)
        rlabel1=Label(frame2,text='Total Beds:',bg='white',fg='#06518d',font=('Calisto MT Bold',14))\
            .place(x=830,y=200)
        rlabel2=Label(frame2,text='4',bg='white',fg='#06518d',font=('Calisto MT Bold',14))\
            .place(x=940,y=200)
        rlabel3=Label(frame2,text='WiFi Available:',bg='white',fg='#06518d',font=('Calisto MT Bold',14))\
            .place(x=830,y=230)
        rlabel4=Label(frame2,text='No',bg='white',fg='#06518d',font=('Calisto MT Bold',14))\
            .place(x=980,y=230)
        rlabel5=Label(frame2,text='Price:',bg='white',fg='#06518d',font=('Calisto MT Bold',14))\
            .place(x=830,y=260)
        rlabel6=Label(frame2,text='NRP 15,000',bg='white',fg='#06518d',font=('Calisto MT Bold',14))\
            .place(x=885,y=260)
        rlabel7=Label(frame2,text='Status :',bg='white',fg='#06518d',font=('Calisto MT Bold',14))\
            .place(x=830,y=290)
        rlabel8=Label(frame2,text='Available',bg='white',fg='#06518d',font=('Calisto MT Bold',14))\
            .place(x=900,y=290)

    def room5():
        rframe=Frame(frame2,height=320,width=300,bg='#06518d')\
            .place(x=800,y=150)
        rframe1=Frame(frame2,height=280,width=260,bg='white')\
            .place(x=820,y=170)
        rlabel1=Label(frame2,text='Total Beds:',bg='white',fg='#06518d',font=('Calisto MT Bold',14))\
            .place(x=830,y=200)
        rlabel2=Label(frame2,text='1',bg='white',fg='#06518d',font=('Calisto MT Bold',14))\
            .place(x=940,y=200)
        rlabel3=Label(frame2,text='WiFi Available:',bg='white',fg='#06518d',font=('Calisto MT Bold',14))\
            .place(x=830,y=230)
        rlabel4=Label(frame2,text='Yes',bg='white',fg='#06518d',font=('Calisto MT Bold',14))\
            .place(x=980,y=230)
        rlabel5=Label(frame2,text='Price:',bg='white',fg='#06518d',font=('Calisto MT Bold',14))\
            .place(x=830,y=260)
        rlabel6=Label(frame2,text='NRP 22,000',bg='white',fg='#06518d',font=('Calisto MT Bold',14))\
            .place(x=885,y=260)
        rlabel7=Label(frame2,text='Status :',bg='white',fg='#06518d',font=('Calisto MT Bold',14))\
            .place(x=830,y=290)
        rlabel8=Label(frame2,text='Available',bg='white',fg='#06518d',font=('Calisto MT Bold',14))\
            .place(x=900,y=290)

    def room6():
        rframe=Frame(frame2,height=320,width=300,bg='#06518d')\
            .place(x=800,y=150)
        rframe1=Frame(frame2,height=280,width=260,bg='white')\
            .place(x=820,y=170)
        rlabel1=Label(frame2,text='Total Beds:',bg='white',fg='#06518d',font=('Calisto MT Bold',14))\
            .place(x=830,y=200)
        rlabel2=Label(frame2,text='2',bg='white',fg='#06518d',font=('Calisto MT Bold',14))\
            .place(x=940,y=200)
        rlabel3=Label(frame2,text='WiFi Available:',bg='white',fg='#06518d',font=('Calisto MT Bold',14))\
            .place(x=830,y=230)
        rlabel4=Label(frame2,text='Yes',bg='white',fg='#06518d',font=('Calisto MT Bold',14))\
            .place(x=980,y=230)
        rlabel5=Label(frame2,text='Price:',bg='white',fg='#06518d',font=('Calisto MT Bold',14))\
            .place(x=830,y=260)
        rlabel6=Label(frame2,text='NRP 20,000',bg='white',fg='#06518d',font=('Calisto MT Bold',14))\
            .place(x=885,y=260)
        rlabel7=Label(frame2,text='Status :',bg='white',fg='#06518d',font=('Calisto MT Bold',14))\
            .place(x=830,y=290)
        rlabel8=Label(frame2,text='Available',bg='white',fg='#06518d',font=('Calisto MT Bold',14))\
            .place(x=900,y=290)

    def room7():
        rframe=Frame(frame2,height=320,width=300,bg='#06518d')\
            .place(x=800,y=150)
        rframe1=Frame(frame2,height=280,width=260,bg='white')\
            .place(x=820,y=170)
        rlabel1=Label(frame2,text='Total Beds:',bg='white',fg='#06518d',font=('Calisto MT Bold',14))\
            .place(x=830,y=200)
        rlabel2=Label(frame2,text='3',bg='white',fg='#06518d',font=('Calisto MT Bold',14))\
            .place(x=940,y=200)
        rlabel3=Label(frame2,text='WiFi Available:',bg='white',fg='#06518d',font=('Calisto MT Bold',14))\
            .place(x=830,y=230)
        rlabel4=Label(frame2,text='Yes',bg='white',fg='#06518d',font=('Calisto MT Bold',14))\
            .place(x=980,y=230)
        rlabel5=Label(frame2,text='Price:',bg='white',fg='#06518d',font=('Calisto MT Bold',14))\
            .place(x=830,y=260)
        rlabel6=Label(frame2,text='NRP 15,000',bg='white',fg='#06518d',font=('Calisto MT Bold',14))\
            .place(x=885,y=260)
        rlabel7=Label(frame2,text='Status :',bg='white',fg='#06518d',font=('Calisto MT Bold',14))\
            .place(x=830,y=290)
        rlabel8=Label(frame2,text='Not Available',bg='white',fg='#06518d',font=('Calisto MT Bold',14))\
            .place(x=900,y=290)

    def room8():
        rframe=Frame(frame2,height=320,width=300,bg='#06518d')\
            .place(x=800,y=150)
        rframe1=Frame(frame2,height=280,width=260,bg='white')\
            .place(x=820,y=170)
        rlabel1=Label(frame2,text='Total Beds:',bg='white',fg='#06518d',font=('Calisto MT Bold',14))\
            .place(x=830,y=200)
        rlabel2=Label(frame2,text='1',bg='white',fg='#06518d',font=('Calisto MT Bold',14))\
            .place(x=940,y=200)
        rlabel3=Label(frame2,text='WiFi Available:',bg='white',fg='#06518d',font=('Calisto MT Bold',14))\
            .place(x=830,y=230)
        rlabel4=Label(frame2,text='No',bg='white',fg='#06518d',font=('Calisto MT Bold',14))\
            .place(x=980,y=230)
        rlabel5=Label(frame2,text='Price:',bg='white',fg='#06518d',font=('Calisto MT Bold',14))\
            .place(x=830,y=260)
        rlabel6=Label(frame2,text='NRP 21,000',bg='white',fg='#06518d',font=('Calisto MT Bold',14))\
            .place(x=885,y=260)
        rlabel7=Label(frame2,text='Status :',bg='white',fg='#06518d',font=('Calisto MT Bold',14))\
            .place(x=830,y=290)
        rlabel8=Label(frame2,text='Not Available',bg='white',fg='#06518d',font=('Calisto MT Bold',14))\
            .place(x=900,y=290)


    fbutton1=Button(frame2,text='Room 1',bg='white',fg='#06518d',borderwidth=2,width=15,font=('Calisto MT Bold',14),command=room1)\
        .place(x=460,y=160)
    fbutton2=Button(frame2,text='Room 2',bg='white',fg='#06518d',borderwidth=2,width=15,font=('Calisto MT Bold',14),command=room2)\
        .place(x=460,y=200)
    fbutton3=Button(frame2,text='Room 3',bg='white',fg='#06518d',borderwidth=2,width=15,font=('Calisto MT Bold',14),command=room3)\
        .place(x=460,y=240)
    fbutton4=Button(frame2,text='Room 4',bg='white',fg='#06518d',borderwidth=2,width=15,font=('Calisto MT Bold',14),command=room4)\
        .place(x=460,y=280)
    fbutton5=Button(frame2,text='Room 5',bg='white',fg='#06518d',borderwidth=2,width=15,font=('Calisto MT Bold',14),command=room5)\
        .place(x=460,y=320)
    fbutton6=Button(frame2,text='Room 6',bg='white',fg='#06518d',borderwidth=2,width=15,font=('Calisto MT Bold',14),command=room6)\
        .place(x=460,y=360)
    fbutton7=Button(frame2,text='Room 7',bg='white',fg='#06518d',borderwidth=2,width=15,font=('Calisto MT Bold',14),command=room7)\
        .place(x=460,y=400)
    fbutton8=Button(frame2,text='Room 8',fg='#06518d',borderwidth=2,width=15,font=('Calisto MT Bold',14),bg='white',command=room8)\
        .place(x=460,y=440)

def contacts():


    frame1 = Frame(a, height=440, width=800, bg='#06518d')
    frame1.place(x=390, y=95)
    frame2 = Frame(frame1, height=400, width=740, bg='white')
    frame2.place(x=30, y=20)
    frame3=Frame(frame2,height=100,width=300,bg='#06518d')
    frame3.place(x=30,y=25)
    label=Label(frame2,text='Important Contact Details',bg='white',fg='#06518d',font=('Calisto MT Bold',24))
    label.place(x=160,y=330)
    clabel=Label(frame3,text='Hostel Warden:',bg='#06518d',fg='White',font=('Calisto MT Bold',14))
    clabel.place(x=10,y=10)
    clabel1=Label(frame3,text='Phone No. +9779827904325',fg='White',font=('Calisto MT Bold',14),bg='#06518d')
    clabel1.place(x=10,y=35)
    clabel2=Label(frame3,text='Wardens Name: Rohan KC',fg='white',font=('Calisto MT Bold',14),bg='#06518d')
    clabel2.place(x=10,y=60)
    frame4=Frame(frame2,height=100,width=300,bg='#06518d')
    frame4.place(x=400,y=25)
    clabel3=Label(frame4,text='Hostel Security:',bg='#06518d',fg='White',font=('Calisto MT Bold',14))
    clabel3.place(x=10,y=10)
    clabel4=Label(frame4,text='Phone No: +9779801011034',bg='#06518d',fg='White',font=('Calisto MT Bold',14))
    clabel4.place(x=10,y=35)
    clabel5=Label(frame4,text='Securitys Name: Yanish Singh',bg='#06518d',fg='White',font=('Calisto MT Bold',14))
    clabel5.place(x=10,y=60)
    frame5=Frame(frame2,height=100,width=300,bg='#06518d')
    frame5.place(x=30,y=200)
    frame6=Frame(frame2,height=100,width=300,bg='#06518d')
    frame6.place(x=400,y=200)
    clabel6=Label(frame5,text='Hostel DI:',bg='#06518d',fg='White',font=('Calisto MT Bold',14))
    clabel6.place(x=10,y=10)
    clabel7=Label(frame5,text='Phone No: +9779708345666',bg='#06518d',fg='White',font=('Calisto MT Bold',14))
    clabel7.place(x=10,y=35)
    clabel8=Label(frame5,text='DIs Name : Sagar Adhikari',bg='#06518d',fg='White',font=('Calisto MT Bold',14))
    clabel8.place(x=10,y=60)
    clabel9=Label(frame6,text='Hostel Mess Manager :',bg='#06518d',fg='White',font=('Calisto MT Bold',14))
    clabel9.place(x=10,y=10)
    clabel10=Label(frame6,text='Phone No. +9779823173786',bg='#06518d',fg='White',font=('Calisto MT Bold',14))
    clabel10.place(x=10,y=35)
    clabel11=Label(frame6,text='Mess Managers Name: Siyata D',bg='#06518d',fg='White',font=('Calisto MT Bold',14))
    clabel11.place(x=10,y=60)

#==============================================STUDENT INFORMATION=============================================

def student():
    frame1 = Frame(a, height=450, width=800, bg='#06518d')\
        .place(x=390, y=90)
    frame2=Frame(frame1,height=400,width=740,bg='white')\
        .place(x=420,y=120)
    slabel=Label(frame1,text='Student Information:',fg='#06518d',bg='white',font=('Calisto MT Bold',18))
    slabel.place(x=430,y=122)

    conn=sqlite3.connect('student.db')
    c=conn.cursor()
    # # CREATE A NEW TABLE
    # c.execute("""CREATE TABLE student(
    #         first_name text,
    #         last_name text,
    #         address text,
    #         parents_name text,
    #         parents_number integer,
    #         school_name text,
    #         age integer
    # )""")
    # print('Table created successfully')
    # conn.commit()
    # conn.close()
    def query():
        conn = sqlite3.connect('student.db')
        c = conn.cursor()
        c.execute('SELECT *, oid FROM student')

        records = c.fetchall()

        # Create a new Treeview widget to display the query result
        tree = ttk.Treeview(a)
        tree["columns"] = ("Name", "Phone No.", "Address", "School Name")
        tree.column("#0", width=0, stretch=NO)
        tree.column("Name", width=100, anchor=W)
        tree.column("Phone No.", width=100, anchor=W)
        tree.column("Address", width=100, anchor=W)
        tree.column("School Name", width=100, anchor=W)
        tree.heading("#0", text="", anchor=W)
        tree.heading("Name", text="Name", anchor=W)
        tree.heading("Phone No.", text="Phone No.", anchor=W)
        tree.heading("Address", text="Address", anchor=W)
        tree.heading("School Name", text="School Name", anchor=W)
        tree.place(x=600, y=200)

        # Insert the query result into the Treeview widget
        for record in records:
            tree.insert("", END, text="", values=(record[0], record[4], record[2], record[5]))



    btn = Button(a, text='Student Information', command=query,font=('Calisto MT Bold',12))
    btn.place(x=420, y=170)


#============================================PAYMENT==============================================================

def payment():

    def esewa():
        eframe=Frame(a,height=320,width=300,bg='#06518d')\
            .place(x=800,y=150)
        eframe1=Frame(a,height=280,width=260,bg='white')\
            .place(x=820,y=170)
        eimage="C:\\Users\\Dell\\Downloads\\WhatsApp Image 2023-02-03 at 21.06.00.jpg"
        img = ImageTk.PhotoImage(Image.open(eimage))
        l = Label(a,image=img, bg='white')
        l.image = img
        l.place(x=845, y=205)
        elabel1=Label(eframe1,text='*Scan QR to send money',bg='white',fg='#06518d',font=('Calisto MT ',12))\
            .place(x=863,y=420)
        eimage1="C:\\Users\\Dell\\Downloads\\esewa11.jpg"
        img1=ImageTk.PhotoImage(Image.open(eimage1))
        l1=Label(a,image=img1,bg='white',height=30)
        l1.image=img1
        l1.place(x=860,y=175)


    def fonepay():
        fframe=Frame(a,height=320,width=300,bg='#06518d')\
            .place(x=800,y=150)

    def visa():
        vframe=Frame(a,height=320,width=300,bg='#06518d')\
            .place(x=800,y=150)
        vframe1=Frame(vframe,height=285,width=270,bg='white')\
            .place(x=815,y=170)
        vlabel1=Label(vframe1,text='Add Your Card Details:',bg='white',fg='#06518d',font=('Calisto MT Bold',12))\
            .place(x=830,y=180)
        vlabel2=Label(vframe1,text='Cardholders Name: ',bg='white',fg='#06518d',font=('Calisto MT ',10))\
            .place(x=830,y=210)
        ventry=Entry(vframe1,width=30,borderwidth=2,bg='white',fg='#06518d')\
            .place(x=830,y=240)
        vlabel3=Label(vframe1,text='Card Number: ',bg='white',fg='#06518d',font=('Calisto MT ',10))\
            .place(x=830,y=270)
        ventry1=Entry(vframe1,width=30,borderwidth=2,bg='white',fg='#06518d')\
            .place(x=830,y=300)
        vlabel4=Label(vframe1,text='Exipry Date:',bg='white',fg='#06518d',font=('Calisto MT ',10))\
            .place(x=830,y=330)
        ventry2=Entry(vframe1,borderwidth=2,width=20,bg='white',fg='#06518d')\
            .place(x=830,y=350)
        vlabel4=Label(vframe1,text='CVV:',bg='white',fg='#06518d',font=('Calisto MT ',10))\
            .place(x=830,y=380)
        ventry3=Entry(vframe1,bg='white',fg='#06518d',width=15,borderwidth=2)\
            .place(x=830,y=400)
        vbutton=Button(vframe1,text='Pay',fg='#06518d',bg='white',width=15,font=('Calisto MT ',8))\
            .place(x=950,y=420)




    frame1 = Frame(a, height=450, width=800, bg='#06518d',borderwidth=10)\
        .place(x=390, y=90)
    frame2=Frame(frame1,height=390,width=740,bg='white',borderwidth=10)\
        .place(x=420,y=120)
    frame3=Frame(frame2,height=450,width=300,bg='#06518d',borderwidth=10)\
        .place(x=420,y=90)
    eimage2 = "C:\\Users\\Dell\\Downloads\\pay1.jpg"
    img2 = ImageTk.PhotoImage(Image.open(eimage2))
    e1 = Label(frame1, image=img2, bg='white', height=250,width=250)
    e1.image = img2
    e1.place(x=810, y=160)
    label1=Label(frame2,text='Payment Options: ',bg='#06518d',fg='white',font=('Calisto MT Bold',20))\
        .place(x=440,y=140)
    button1=Button(frame3,padx=40,pady=5,height=0,text='Esewa',bg='#06518d',fg='white',font=('Calisto MT Bold',18),borderwidth=2,command=esewa)\
        .place(x=475,y=207)
    button2=Button(frame3,padx=28,pady=5,text='FonePay',bg='#06518d',fg='white',font=('Calisto MT Bold',18),borderwidth=2,command=fonepay)\
        .place(x=475,y=290)
    button3=Button(frame3,padx=48,pady=5,text='Card',bg='#06518d',fg='white',font=('Calisto MT Bold',18),borderwidth=2,command=visa)\
        .place(x=475,y=370)
#=========================================Photo for all the payment optins ==============================================
    esewa1 = "C:\\Users\\Dell\\Downloads\\732-7320315_esewa-logo-hd-png-download.png"
    img1 = ImageTk.PhotoImage(Image.open(esewa1))
    l1 = Label(a, image=img1, bg='#06518d',height=100)
    l1.image = img1
    l1.place(x=410, y=185)

    fonepay1="C:\\Users\\Dell\\Downloads\\unnamed.jpg"
    img2=ImageTk.PhotoImage(Image.open(fonepay1))
    l2=Label(a,image=img2,bg='#06518d',height=80)
    l2.image=img2
    l2.place(x=410,y=278)

    visa1="C:\\Users\\Dell\\Downloads\\visa-logo-800x450.jpg"
    img3=ImageTk.PhotoImage(Image.open(visa1))
    l3=Label(a,image=img3,bg='#06518d',height=60,width=60)
    l3.image=img3
    l3.place(x=410,y=368)

#==============================================FOOD=======================================================

def food():
    frame1 = Frame(a, height=450, width=800, bg='#06518d', borderwidth=10)\
        .place(x=390, y=90)
    frame2 = Frame(frame1, height=390, width=740, bg='white', borderwidth=10)\
        .place(x=420, y=120)


    def sunday():
        rframe = Frame(frame2, height=400, width=300, bg='#06518d')
        rframe.place(x=800, y=120)
        rframe1 = Frame(frame2, height=390, width=260, bg='white')
        rframe1.place(x=820, y=120)
        folabel=Label(rframe1,text='BREAKFAST:',bg='white',fg='#06518d',font=('Calisto MT Bold',14))
        folabel.place(x=10,y=10)
        folabel1=Label(rframe1,text='Time 6 AM to 8AM:',bg='white',fg='#06518d',font=('Calisto MT Bold',12))
        folabel1.place(x=10,y=35)
        folabel2=Label(rframe1,text='Bread/Butter with Milk and Egg.',bg='white',fg='#06518d',font=('Calisto MT Bold',12))
        folabel2.place(x=10,y=60)
        folabel3=Label(rframe1,text='LUNCH',bg='white',fg='#06518d',font=('Calisto MT Bold',14))
        folabel3.place(x=10,y=95)
        folabel4=Label(rframe1,text='Time 11 PM to 1 PM:',bg='white',fg='#06518d',font=('Calisto MT Bold',12))
        folabel4.place(x=10,y=120)
        folabel5=Label(rframe1,text='Rice, Daal, Curry(Potatoe \n and Vegies) and Egg',bg='white',fg='#06518d',font=('Calisto MT Bold',12))
        folabel5.place(x=10,y=145)
        folabel6=Label(rframe1,text='SNACKS',bg='white',fg='#06518d',font=('Calisto MT Bold',14))
        folabel6.place(x=10,y=197)
        folabel7=Label(rframe1,text='Time 2 PM to 4 PM:',bg='white',fg='#06518d',font=('Calisto MT Bold',12))
        folabel7.place(x=10,y=225)
        folabel8=Label(rframe1,text='Chowmin',bg='white',fg='#06518d',font=('Calisto MT Bold',12))
        folabel8.place(x=10,y=250)
        folabel9=Label(rframe1,text='DINNER',bg='white',fg='#06518d',font=('Calisto MT Bold',14))
        folabel9.place(x=10,y=285)
        folabel10=Label(rframe1,text='Time 7 PM to 9 PM:',bg='white',fg='#06518d',font=('Calisto MT Bold',12))
        folabel10.place(x=10,y=313)
        folabel11=Label(rframe1,text='Roti and Curry',bg='white',fg='#06518d',font=('Calisto MT Bold',12))
        folabel11.place(x=10,y=340)


    def monday():
        rframe = Frame(frame2, height=400, width=300, bg='#06518d')
        rframe.place(x=800, y=120)
        rframe1 = Frame(frame2, height=390, width=260, bg='white')
        rframe1.place(x=820, y=120)
        folabel=Label(rframe1,text='BREAKFAST:',bg='white',fg='#06518d',font=('Calisto MT Bold',14))
        folabel.place(x=10,y=10)
        folabel1=Label(rframe1,text='Time 6 AM to 8AM:',bg='white',fg='#06518d',font=('Calisto MT Bold',12))
        folabel1.place(x=10,y=35)
        folabel2=Label(rframe1,text='Biscuits with Milk and Egg.',bg='white',fg='#06518d',font=('Calisto MT Bold',12))
        folabel2.place(x=10,y=60)
        folabel3=Label(rframe1,text='LUNCH',bg='white',fg='#06518d',font=('Calisto MT Bold',14))
        folabel3.place(x=10,y=95)
        folabel4=Label(rframe1,text='Time 11 PM to 1 PM:',bg='white',fg='#06518d',font=('Calisto MT Bold',12))
        folabel4.place(x=10,y=120)
        folabel5=Label(rframe1,text='Rice, Daal, Curry(Mushroom \n and Vegies) and Salad',bg='white',fg='#06518d',font=('Calisto MT Bold',12))
        folabel5.place(x=10,y=145)
        folabel6=Label(rframe1,text='SNACKS',bg='white',fg='#06518d',font=('Calisto MT Bold',14))
        folabel6.place(x=10,y=197)
        folabel7=Label(rframe1,text='Time 2 PM to 4 PM:',bg='white',fg='#06518d',font=('Calisto MT Bold',12))
        folabel7.place(x=10,y=225)
        folabel8=Label(rframe1,text='Pasta',bg='white',fg='#06518d',font=('Calisto MT Bold',12))
        folabel8.place(x=10,y=250)
        folabel9=Label(rframe1,text='DINNER',bg='white',fg='#06518d',font=('Calisto MT Bold',14))
        folabel9.place(x=10,y=285)
        folabel10=Label(rframe1,text='Time 7 PM to 9 PM:',bg='white',fg='#06518d',font=('Calisto MT Bold',12))
        folabel10.place(x=10,y=313)
        folabel11=Label(rframe1,text='Puri and Curry',bg='white',fg='#06518d',font=('Calisto MT Bold',12))
        folabel11.place(x=10,y=340)


    def tuesday():
        rframe = Frame(frame2, height=400, width=300, bg='#06518d')
        rframe.place(x=800, y=120)
        rframe1 = Frame(frame2, height=390, width=260, bg='white')
        rframe1.place(x=820, y=120)
        folabel=Label(rframe1,text='BREAKFAST:',bg='white',fg='#06518d',font=('Calisto MT Bold',14))
        folabel.place(x=10,y=10)
        folabel1=Label(rframe1,text='Time 6 AM to 8AM:',bg='white',fg='#06518d',font=('Calisto MT Bold',12))
        folabel1.place(x=10,y=35)
        folabel2=Label(rframe1,text='Paratha with Milk and Egg.',bg='white',fg='#06518d',font=('Calisto MT Bold',12))
        folabel2.place(x=10,y=60)
        folabel3=Label(rframe1,text='LUNCH',bg='white',fg='#06518d',font=('Calisto MT Bold',14))
        folabel3.place(x=10,y=95)
        folabel4=Label(rframe1,text='Time 11 PM to 1 PM:',bg='white',fg='#06518d',font=('Calisto MT Bold',12))
        folabel4.place(x=10,y=120)
        folabel5=Label(rframe1,text='Rice, Daal, Curry(Chicken \n and Vegies) and Chips',bg='white',fg='#06518d',font=('Calisto MT Bold',12))
        folabel5.place(x=10,y=145)
        folabel6=Label(rframe1,text='SNACKS',bg='white',fg='#06518d',font=('Calisto MT Bold',14))
        folabel6.place(x=10,y=197)
        folabel7=Label(rframe1,text='Time 2 PM to 4 PM:',bg='white',fg='#06518d',font=('Calisto MT Bold',12))
        folabel7.place(x=10,y=225)
        folabel8=Label(rframe1,text='Fried Rice',bg='white',fg='#06518d',font=('Calisto MT Bold',12))
        folabel8.place(x=10,y=250)
        folabel9=Label(rframe1,text='DINNER',bg='white',fg='#06518d',font=('Calisto MT Bold',14))
        folabel9.place(x=10,y=285)
        folabel10=Label(rframe1,text='Time 7 PM to 9 PM:',bg='white',fg='#06518d',font=('Calisto MT Bold',12))
        folabel10.place(x=10,y=313)
        folabel11=Label(rframe1,text='Rice, Dal, and Fish',bg='white',fg='#06518d',font=('Calisto MT Bold',12))
        folabel11.place(x=10,y=340)

    def wednesday():
        rframe = Frame(frame2, height=400, width=300, bg='#06518d')
        rframe.place(x=800, y=120)
        rframe1 = Frame(frame2, height=390, width=260, bg='white')
        rframe1.place(x=820, y=120)
        folabel=Label(rframe1,text='BREAKFAST:',bg='white',fg='#06518d',font=('Calisto MT Bold',14))
        folabel.place(x=10,y=10)
        folabel1=Label(rframe1,text='Time 6 AM to 8AM:',bg='white',fg='#06518d',font=('Calisto MT Bold',12))
        folabel1.place(x=10,y=35)
        folabel2=Label(rframe1,text='American Breakfast.',bg='white',fg='#06518d',font=('Calisto MT Bold',12))
        folabel2.place(x=10,y=60)
        folabel3=Label(rframe1,text='LUNCH',bg='white',fg='#06518d',font=('Calisto MT Bold',14))
        folabel3.place(x=10,y=95)
        folabel4=Label(rframe1,text='Time 11 PM to 1 PM:',bg='white',fg='#06518d',font=('Calisto MT Bold',12))
        folabel4.place(x=10,y=120)
        folabel5=Label(rframe1,text='Rice, Daal, Curry(Paneer \n and Vegies).',bg='white',fg='#06518d',font=('Calisto MT Bold',12))
        folabel5.place(x=10,y=145)
        folabel6=Label(rframe1,text='SNACKS',bg='white',fg='#06518d',font=('Calisto MT Bold',14))
        folabel6.place(x=10,y=197)
        folabel7=Label(rframe1,text='Time 2 PM to 4 PM:',bg='white',fg='#06518d',font=('Calisto MT Bold',12))
        folabel7.place(x=10,y=225)
        folabel8=Label(rframe1,text='Wai Wai.',bg='white',fg='#06518d',font=('Calisto MT Bold',12))
        folabel8.place(x=10,y=250)
        folabel9=Label(rframe1,text='DINNER',bg='white',fg='#06518d',font=('Calisto MT Bold',14))
        folabel9.place(x=10,y=285)
        folabel10=Label(rframe1,text='Time 7 PM to 9 PM:',bg='white',fg='#06518d',font=('Calisto MT Bold',12))
        folabel10.place(x=10,y=313)
        folabel11=Label(rframe1,text='Rice, Dal and Chicken with Salad.',bg='white',fg='#06518d',font=('Calisto MT Bold',12))
        folabel11.place(x=10,y=340)

    def thursday():
        rframe = Frame(frame2, height=400, width=300, bg='#06518d')
        rframe.place(x=800, y=120)
        rframe1 = Frame(frame2, height=390, width=260, bg='white')
        rframe1.place(x=820, y=120)
        folabel=Label(rframe1,text='BREAKFAST:',bg='white',fg='#06518d',font=('Calisto MT Bold',14))
        folabel.place(x=10,y=10)
        folabel1=Label(rframe1,text='Time 6 AM to 8AM:',bg='white',fg='#06518d',font=('Calisto MT Bold',12))
        folabel1.place(x=10,y=35)
        folabel2=Label(rframe1,text='Biscuits with Milk.',bg='white',fg='#06518d',font=('Calisto MT Bold',12))
        folabel2.place(x=10,y=60)
        folabel3=Label(rframe1,text='LUNCH',bg='white',fg='#06518d',font=('Calisto MT Bold',14))
        folabel3.place(x=10,y=95)
        folabel4=Label(rframe1,text='Time 11 PM to 1 PM:',bg='white',fg='#06518d',font=('Calisto MT Bold',12))
        folabel4.place(x=10,y=120)
        folabel5=Label(rframe1,text='Rice, Daal, Curry(Soyabeans \n and Vegies) and Egg',bg='white',fg='#06518d',font=('Calisto MT Bold',12))
        folabel5.place(x=10,y=145)
        folabel6=Label(rframe1,text='SNACKS',bg='white',fg='#06518d',font=('Calisto MT Bold',14))
        folabel6.place(x=10,y=197)
        folabel7=Label(rframe1,text='Time 2 PM to 4 PM:',bg='white',fg='#06518d',font=('Calisto MT Bold',12))
        folabel7.place(x=10,y=225)
        folabel8=Label(rframe1,text='Burger',bg='white',fg='#06518d',font=('Calisto MT Bold',12))
        folabel8.place(x=10,y=250)
        folabel9=Label(rframe1,text='DINNER',bg='white',fg='#06518d',font=('Calisto MT Bold',14))
        folabel9.place(x=10,y=285)
        folabel10=Label(rframe1,text='Time 7 PM to 9 PM:',bg='white',fg='#06518d',font=('Calisto MT Bold',12))
        folabel10.place(x=10,y=313)
        folabel11=Label(rframe1,text='Chicken Momo',bg='white',fg='#06518d',font=('Calisto MT Bold',12))
        folabel11.place(x=10,y=340)

    def friday():
        rframe = Frame(frame2, height=400, width=300, bg='#06518d')
        rframe.place(x=800, y=120)
        rframe1 = Frame(frame2, height=390, width=260, bg='white')
        rframe1.place(x=820, y=120)
        folabel=Label(rframe1,text='BREAKFAST:',bg='white',fg='#06518d',font=('Calisto MT Bold',14))
        folabel.place(x=10,y=10)
        folabel1=Label(rframe1,text='Time 6 AM to 8AM:',bg='white',fg='#06518d',font=('Calisto MT Bold',12))
        folabel1.place(x=10,y=35)
        folabel2=Label(rframe1,text='Bread/Butter with Milk and Egg.',bg='white',fg='#06518d',font=('Calisto MT Bold',12))
        folabel2.place(x=10,y=60)
        folabel3=Label(rframe1,text='LUNCH',bg='white',fg='#06518d',font=('Calisto MT Bold',14))
        folabel3.place(x=10,y=95)
        folabel4=Label(rframe1,text='Time 11 PM to 1 PM:',bg='white',fg='#06518d',font=('Calisto MT Bold',12))
        folabel4.place(x=10,y=120)
        folabel5=Label(rframe1,text='Rice, Daal, Curry\n and Egg',bg='white',fg='#06518d',font=('Calisto MT Bold',12))
        folabel5.place(x=10,y=145)
        folabel6=Label(rframe1,text='SNACKS',bg='white',fg='#06518d',font=('Calisto MT Bold',14))
        folabel6.place(x=10,y=197)
        folabel7=Label(rframe1,text='Time 2 PM to 4 PM:',bg='white',fg='#06518d',font=('Calisto MT Bold',12))
        folabel7.place(x=10,y=225)
        folabel8=Label(rframe1,text='Puri and Curry',bg='white',fg='#06518d',font=('Calisto MT Bold',12))
        folabel8.place(x=10,y=250)
        folabel9=Label(rframe1,text='DINNER',bg='white',fg='#06518d',font=('Calisto MT Bold',14))
        folabel9.place(x=10,y=285)
        folabel10=Label(rframe1,text='Time 7 PM to 9 PM:',bg='white',fg='#06518d',font=('Calisto MT Bold',12))
        folabel10.place(x=10,y=313)
        folabel11=Label(rframe1,text='Roti and Curry',bg='white',fg='#06518d',font=('Calisto MT Bold',12))
        folabel11.place(x=10,y=340)

    def saturday():
        rframe = Frame(frame2, height=400, width=300, bg='#06518d')
        rframe.place(x=800, y=120)
        rframe1 = Frame(frame2, height=390, width=260, bg='white')
        rframe1.place(x=820, y=120)
        folabel=Label(rframe1,text='BREAKFAST:',bg='white',fg='#06518d',font=('Calisto MT Bold',14))
        folabel.place(x=10,y=10)
        folabel1=Label(rframe1,text='Time 6 AM to 8AM:',bg='white',fg='#06518d',font=('Calisto MT Bold',12))
        folabel1.place(x=10,y=35)
        folabel2=Label(rframe1,text='European Breakfast.',bg='white',fg='#06518d',font=('Calisto MT Bold',12))
        folabel2.place(x=10,y=60)
        folabel3=Label(rframe1,text='LUNCH',bg='white',fg='#06518d',font=('Calisto MT Bold',14))
        folabel3.place(x=10,y=95)
        folabel4=Label(rframe1,text='Time 11 PM to 1 PM:',bg='white',fg='#06518d',font=('Calisto MT Bold',12))
        folabel4.place(x=10,y=120)
        folabel5=Label(rframe1,text='Rice, Daal, Curry(Chicken \n and Vegies) and Egg',bg='white',fg='#06518d',font=('Calisto MT Bold',12))
        folabel5.place(x=10,y=145)
        folabel6=Label(rframe1,text='SNACKS',bg='white',fg='#06518d',font=('Calisto MT Bold',14))
        folabel6.place(x=10,y=197)
        folabel7=Label(rframe1,text='Time 2 PM to 4 PM:',bg='white',fg='#06518d',font=('Calisto MT Bold',12))
        folabel7.place(x=10,y=225)
        folabel8=Label(rframe1,text='Chowmin',bg='white',fg='#06518d',font=('Calisto MT Bold',12))
        folabel8.place(x=10,y=250)
        folabel9=Label(rframe1,text='DINNER',bg='white',fg='#06518d',font=('Calisto MT Bold',14))
        folabel9.place(x=10,y=285)
        folabel10=Label(rframe1,text='Time 7 PM to 9 PM:',bg='white',fg='#06518d',font=('Calisto MT Bold',12))
        folabel10.place(x=10,y=313)
        folabel11=Label(rframe1,text='Rice, Daal and Curry(Mutton\n and Salad)',bg='white',fg='#06518d',font=('Calisto MT Bold',12))
        folabel11.place(x=10,y=340)



    fobutton1=Button(frame2,text='Sunday',bg='white',fg='#06518d',borderwidth=2,width=15,font=('Calisto MT Bold',14),command=sunday)\
        .place(x=460,y=160)
    fobutton2=Button(frame2,text='Monday',bg='white',fg='#06518d',borderwidth=2,width=15,font=('Calisto MT Bold',14),command=monday)\
        .place(x=460,y=200)
    fobutton3=Button(frame2,text='Tuesday',bg='white',fg='#06518d',borderwidth=2,width=15,font=('Calisto MT Bold',14),command=tuesday)\
        .place(x=460,y=240)
    fobutton4=Button(frame2,text='Wednesday',bg='white',fg='#06518d',borderwidth=2,width=15,font=('Calisto MT Bold',14),command=wednesday)\
        .place(x=460,y=280)
    fobutton5=Button(frame2,text='Thursday',bg='white',fg='#06518d',borderwidth=2,width=15,font=('Calisto MT Bold',14),command=thursday)\
        .place(x=460,y=320)
    fobutton6=Button(frame2,text='Friday',bg='white',fg='#06518d',borderwidth=2,width=15,font=('Calisto MT Bold',14),command=friday)\
        .place(x=460,y=360)
    fobutton7=Button(frame2,text='Saturday',bg='white',fg='#06518d',borderwidth=2,width=15,font=('Calisto MT Bold',14),command=saturday)\
        .place(x=460,y=400)



label3=Button(a,text='Rooms',bg='#06518d',font=('Calisto MT Bold',18),fg='white',pady=3,padx=30,command=room)
label3.place(x=100,y=100)
label4=Button(a,text='Contacts',bg='#06518d',font=('Calisto MT Bold',18),fg='White',padx=19,pady=3,borderwidth=2,command=contacts)
label4.place(x=100,y=180)

label5=Button(a,text='Students \n Information',bg='#06518d',font=('Calisto MT Bold',18),fg='White',padx=0,pady=0,borderwidth=2,command=student)
label5.place(x=95,y=260)
label6=Button(a,text='Payment',bg='#06518d',font=('Calisto MT Bold',18),fg='White',padx=20,pady=3,borderwidth=2,highlightbackground='white',command=payment)
label6.place(x=100,y=360)
label7=Button(a,text='Food',bg='#06518d',font=('Calisto MT Bold',18),fg='white',padx=40,pady=3,borderwidth=2,command=food)
label7.place(x=100,y=440)

#====================================Icon Image=========================================================================

img2=PhotoImage(file='images (1).png')
image1=Label(a,image=img2,bg='white')
image1.place(x=35,y=100)
img3=PhotoImage(file='contacts.png')
image2=Label(a,image=img3,bg='white')
image2.place(x=30,y=180)
img4=PhotoImage(file='student id (1).png')
image3=Label(a,image=img4,bg='white')
image3.place(x=30,y=265)
img5=PhotoImage(file='payment (1).png')
image4=Label(a,image=img5,bg='white')
image4.place(x=30,y=360)
img6=PhotoImage(file='food (1).png')
image5=Label(a,image=img6,bg='white')
image5.place(x=30,y=440)
img7=PhotoImage(file='exit (1).png')
image6=Label(a,image=img7,bg='white')
image6.place(x=30,y=520)
img8=PhotoImage(file='colorfull (2) (1).png')
image7=Label(a,image=img8,bg='white')
image7.place(x=330,y=565)

#=========================================Exit==========================================================================

    # q=messagebox.askyesno('Exit','Do you really want to exit ?')
    # if (q):
    #     a.destroy()
def book():
    frame1 = Frame(a, height=450, width=800, bg='#06518d', borderwidth=10)\
        .place(x=390, y=90)
    frame2 = Frame(frame1, height=390, width=740, bg='white', borderwidth=10)\
        .place(x=420, y=120)
    def booking():
        conn = sqlite3.connect('students.db')
        c=conn.cursor()
        c = conn.cursor()
        c.execute("INSERT INTO booking VALUES(:fullname, :ph_num, :email, :p_name, :s_name)", {
            'fullname': f_name.get(),
            'ph_num': p_num.get(),
            'email': e_mail.get(),
            'p_name': parents.get(),
            's_name': school.get()
        })
        # IF FullNmae .get is ==" "
        # clear text box
        f_name.delete(0, END)
        p_num.delete(0, END)
        e_mail.delete(0, END)
        parents.delete(0, END)
        school.delete(0, END)

        messagebox.showinfo('Registration Information', 'Booking Successfully')

        conn.commit()
        conn.close()

    label = Label(a, text='Please input your information on fields to book.', fg='#404040', bg='white',
                 font=('Calisto MT Bold', 12, 'bold'))
    label.place(x=450, y=130)

    f_namel = Label(a, text='Full Name*', fg='black', bg='white', font=('Calisto MT ', 12))
    f_namel.place(x=450, y=180)
    f_name = Entry(a, width=32, fg='black', border=2, highlightthickness=1, highlightbackground='#F1F0FD',
                     font=('Calisto MT ', 10))
    f_name.place(x=450, y=210, height=25)

    ph_num = Label(a, text='Phone Number*', fg='black', bg='white', font=('Calisto MT ', 12))
    ph_num.place(x=450, y=240)
    p_num = Entry(a, width=25, fg='black', border=2, highlightthickness=1, highlightbackground='#F1F0FD',
                   font=('Calisto MT ', 12))
    p_num.place(x=450, y=260, height=25)

    email = Label(a, text='Email*', fg='black', bg='white', font=('Calisto MT ', 12))
    email.place(x=450, y=300)
    e_mail = Entry(a, width=25, fg='black', border=2, highlightthickness=1, highlightbackground='#F1F0FD',
                  font=('Calisto MT ', 12))
    e_mail.place(x=450, y=320, height=25)

    p_name = Label(a, text='Parents Name', fg='black', bg='white', font=('Calisto MT ', 12))
    p_name.place(x=450, y=360)
    parents = Entry(a, width=25, fg='black', border=2, highlightthickness=1, highlightbackground='#F1F0FD',
                font=('Calisto MT ', 12))
    parents.place(x=450, y=380, height=25)

    s_name = Label(a, text='School Name', fg='black', bg='white', font=('Calisto MT ', 12))
    s_name.place(x=450, y=430)
    school = Entry(a, width=25, fg='black', border=2, highlightthickness=1, highlightbackground='#F1F0FD',
                   font=('Calisto MT ', 12))
    school.place(x=450, y=450, height=25)

    btn=Button(a,text='Book',fg='white',bg='#06518d',width=15,font=('Calisto MT ',10),command=booking)
    btn.place(x=800,y=460)

label8=Button(a,text='Booking',bg='#06518d',font=('Calisto MT Bold',18),fg='white',padx=20,pady=2,borderwidth=2,command=book)
label8.place(x=100,y=520)

a.mainloop()