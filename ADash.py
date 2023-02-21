            from tkinter import *
            from PIL import ImageTk,Image
            import sqlite3
            from tkinter import messagebox
            a=Tk()
            a.title('Admin Dashboard')
            a.minsize(width=1000,height=600)
            a.maxsize(width=1000,height=600)
            # a.iconbitmap('H:\\My Drive\\a\\icon.ico')
            # ig1=PhotoImage(file='white-elegant-powerpoint-background-27.png')
            # image=Label(a,image=ig1,bg='white')\
            #     .place(x=0,y=0)
            path="C:\\Users\\Dell\\Downloads\\Hostel-Management-System-e1569593417580.jpg"
            img = ImageTk.PhotoImage(Image.open(path))
            label = Label(a, image=img, height=600, width=1080)
            label.image = img
            label.place(x=0, y=0)
            canvas=Canvas(a,bg='#06518d',height=1000,width=300)
            canvas.place(x=0,y=0)
            Frame(a, height=500, width=250, bg='white')\
                .place(x=27, y=80)
            label1=Label(a,text='ADMIN DASHBOARD',bg='#06518d',fg='white',font=('Calisto MT Bold',18))
            label1.place(x=14,y=10)
            label2=Label(a,text='HOSTEL MANAGEMENT SYSTEM',fg='#06518d',font=('Calisto MT Bold',18),bd=1)
            # a.attributes('-alpha',0.5)
            label2.place(x=400,y=10)


            def student():
                frame1=Frame(a, height=500, width=600, bg='#06518d') \
                    .place(x=330, y=50)
                frame2=Frame(a,height=450,width=550,bg='white').place(x=355,y=75)

                def add():
                    f_name = Entry(frame2, width=30,border=2)
                    f_name.place(x=550, y=200)

                    l_name = Entry(frame2, width=30,border=2)
                    l_name.place(x=550,y=240)

                    address = Entry(frame2, width=30,border=2)
                    address.place(x=550, y=280)

                    p_name = Entry(frame2, width=30,border=2)
                    p_name.place(x=550,y=320)

                    p_number = Entry(frame2, width=30,border=2)
                    p_number.place(x=550, y=360)

                    s_name = Entry(frame2, width=30,border=2)
                    s_name.place(x=550, y=400)

                    age = Entry(frame2, width=30,border=2)
                    age.place(x=550, y=440)



                    # Create textbox labels
                    f_name_label = Label(frame2, text='First Name: ',fg='#06518d',bg='white',font=('Calisto MT Bold',12)).place(x=450,y=196)

                    l_name_label = Label(frame2, text='Last Name: ',fg='#06518d',bg='white',font=('Calisto MT Bold',12)).place(x=450,y=236)

                    address_label = Label(frame2, text='Address: ',fg='#06518d',bg='white',font=('Calisto MT Bold',12)).place(x=450,y=276)

                    p_name_label = Label(frame2, text='Parents Name: ',fg='#06518d',bg='white',font=('Calisto MT Bold',12)).place(x=450,y=316)

                    p_number_label = Label(frame2, text='Parents No.: ',fg='#06518d',bg='white',font=('Calisto MT Bold',12)).place(x=450,y=356)

                    s_name_label = Label(frame2, text='School Name: ',fg='#06518d',bg='white',font=('Calisto MT Bold',12)).place(x=450,y=396)

                    age_label = Label(frame2, text='Age: ',fg='#06518d',bg='white',font=('Calisto MT Bold',12)).place(x=450,y=436)





                    def add_rec():
                        conn=sqlite3.connect('student.db')
                        c=conn.cursor()
                        c.execute('INSERT INTO student VALUES (:f_name, :l_name, :address, :parents_name, :parents_number, :school_name, :age)',{
                        'f_name':f_name.get(),
                        'l_name':l_name.get(),
                        'address':address.get(),
                        'parents_name':p_name.get(),
                        'parents_number':p_number.get(),
                        'school_name':s_name.get(),
                        'age':age.get()
                         })
                        messagebox.showinfo('students', 'Inserted Successfully ')
                        conn.commit()
                        conn.close()

                        # showinfo message box

                        f_name.delete(0, END)
                        l_name.delete(0, END)
                        address.delete(0, END)
                        p_name.delete(0, END)
                        p_number.delete(0, END)
                        s_name.delete(0, END)
                        age.delete(0, END)

                    submit_btn = Button(frame2, text='AddRecords', command=add_rec, font=('Calisto MT Bold', 12), fg='white',
                                        bg='#06518d')
                    submit_btn.config( pady=2, padx=10)
                    submit_btn.place(x=750,y=480)


                def edit():
                    # frame1 = Frame(a, height=500, width=600, bg='#06518d') \
                    #     .place(x=330, y=50)
                    frame2 = Frame(a, height=450, width=550, bg='white').place(x=355, y=75)


                    def query():
                        conn = sqlite3.connect('student.db')
                        c = conn.cursor()
                        c.execute('SELECT *, oid FROM student')

                        records = c.fetchall()
                        print_record = ''

                        for record in records:
                            print_record += str(record[7]) + '.' + str(record[0]) + '' + '\t'+str(record[1])+'' +'\t'+ str(record[2]) + '\n'

                        def delete():
                            conn = sqlite3.connect('student.db')
                            c = conn.cursor()
                            c.execute('DELETE from student WHERE oid=' + delete_box.get())
                            print('Delete Successfully')
                            conn.commit()
                            conn.close()
                        global delete_box

                        delete_box = Entry(frame2, width=20)
                        delete_box.place(x=550,y=420)
                        delete_box_label = Label(a, text='Delete ID/Update :',font=('Calisto MT Bold', 12),bg='white',fg='#06518d')
                        delete_box_label.place(x=400,y=420)
                        delete_btn = Button(a, text='Delete', command=delete,font=('Calisto MT Bold', 12),bg='#06518d',fg='white')
                        delete_btn.place(x=460,y=460)

                        query_label = Label(a, text=print_record)
                        query_label.config(width=50,height=20)
                        query_label.place(x=450,y=100)
                    query_btn = Button(a, text='Show Record', command=query, font=('Calisto MT Bold', 12), fg='white',
                                           bg='#06518d').place(x=750, y=440)


                    def update():
                        # Creating an update function
                        conn = sqlite3.connect('student.db')
                        c = conn.cursor()
                        global delete_box
                        record_id = delete_box.get()

                        c.execute("""UPDATE student SET
                        first_name=:first_name,
                        last_name=:last_name,
                        address=:address,
                        parents_name=:parents_name,
                        parents_number=:parents_number,
                        school_name=:school_name,
                        age=:age
                        WHERE oid =:oid""",
                                    {'first_name': first_name_editor.get(),
                                    'last_name': last_name_editor.get(),
                                     'address':address_editor.get(),
                                     'parents_name':p_name_editor.get(),
                                     'parents_number':p_number_editor.get(),
                                     'school_name':s_name_editor.get(),
                                     'age':age_editor.get(),
                                     'oid': record_id

                                    }
                                    )
                        conn.commit()
                        conn.close()
                        editor.destroy()

                    def edit():
                        global delete_box
                        global editor
                        editor = Tk()

                        editor.title('Update data')
                        editor.geometry('500x500')



                        conn = sqlite3.connect('student.db')
                        c=conn.cursor()

                        record_id =delete_box.get()

                        c.execute('SELECT * FROM student WHERE oid =' + record_id)
                        records = c.fetchall()

                        global first_name_editor
                        global last_name_editor
                        global address_editor
                        global p_name_editor
                        global p_number_editor
                        global s_name_editor
                        global age_editor


                        first_name_editor = Entry(editor, width=30)
                        first_name_editor.grid(row=0, column=1)

                        last_name_editor = Entry(editor, width=30)
                        last_name_editor.grid(row=1, column=1)

                        address_editor=Entry(editor,width=30)
                        address_editor.grid(row=2,column=1)

                        p_name_editor=Entry(editor,width=30)
                        p_name_editor.grid(row=3,column=1)

                        p_number_editor=Entry(editor,width=30)
                        p_number_editor.grid(row=4,column=1)

                        s_name_editor=Entry(editor,width=30)
                        s_name_editor.grid(row=5,column=1)

                        age_editor=Entry(editor,width=30)
                        age_editor.grid(row=6,column=1)


                        first_name_editor_label = Label(editor, text='First Name')
                        first_name_editor_label.grid(row=0, column=0, pady=(10, 0))

                        last_name_editor_label = Label(editor, text="Last Name")
                        last_name_editor_label.grid(row=1, column=0)

                        address_editor_label=Label(editor,text='Address')
                        address_editor_label.grid(row=2,column=0)

                        p_name_editor_label=Label(editor,text='Parents Name')
                        p_name_editor_label.grid(row=3,column=0)

                        p_number_editor_label=Label(editor,text='Parents Number')
                        p_number_editor_label.grid(row=4,column=0)

                        s_name_editor_label=Label(editor,text='School Name')
                        s_name_editor_label.grid(row=5,column=0)

                        age_editor_label=Label(editor,text='Age')
                        age_editor_label.grid(row=6,column=0)



                        for record in records:
                            first_name_editor.insert(0, record[0])
                            last_name_editor.insert(0, record[1])
                            address_editor.insert(0,record[2])
                            p_name_editor.insert(0,record[3])
                            p_number_editor.insert(0,record[4])
                            s_name_editor.insert(0,record[5])
                            age_editor.insert(0,record[6])

                        edit_btnn = Button(editor, text='Save', command=update)
                        edit_btnn.grid(row=7, column=0, columnspan=2, pady=10, padx=10, ipadx=125)

                    edit_btn = Button(a, text='Update', command=edit,font=('Calisto MT Bold', 12), fg='white',
                                           bg='#06518d')
                    edit_btn.place(x=600,y=460)



                sbtn2=Button(frame2,text='Add Student',pady=1,padx=10,fg='white',bg='#06518d',font=('Calisto MT Bold',16),command=add)
                sbtn2.place(x=380,y=100)
                sbtn3=Button(frame2,text='Delete Student',pady=1,padx=10,fg='white',bg='#06518d',font=('Calisto MT Bold',16),command=edit)
                sbtn3.place(x=580,y=100)
                # sbtn4=Button(a,text='Update',pady=1,padx=10,fg='white',bg='#06518d',font=('Calisto MT Bold',16),command=)
                # sbtn4.place(x=780,y=100)

            #==================================ROOM==========================
            #=============================CRUD============================

            def room():
                def add():
                    room_no = Entry(frame2, width=30,border=2)
                    room_no.place(x=550, y=200)

                    beds = Entry(frame2, width=30,border=2)
                    beds.place(x=550,y=240)

                    price = Entry(frame2, width=30,border=2)
                    price.place(x=550, y=280)

                    students_name = Entry(frame2, width=30,border=2)
                    students_name.place(x=550,y=320)

                    no_students = Entry(frame2, width=30,border=2)
                    no_students.place(x=550, y=360)

                    wifi = Entry(frame2, width=30,border=2)
                    wifi.place(x=550, y=400)



                    # Create textbox labels
                    f_name_label = Label(frame2, text='First Name: ',fg='#06518d',bg='white',font=('Calisto MT Bold',12)).place(x=450,y=196)

                    l_name_label = Label(frame2, text='Last Name: ',fg='#06518d',bg='white',font=('Calisto MT Bold',12)).place(x=450,y=236)

                    address_label = Label(frame2, text='Address: ',fg='#06518d',bg='white',font=('Calisto MT Bold',12)).place(x=450,y=276)

                    p_name_label = Label(frame2, text='Parents Name: ',fg='#06518d',bg='white',font=('Calisto MT Bold',12)).place(x=450,y=316)

                    p_number_label = Label(frame2, text='Parents No.: ',fg='#06518d',bg='white',font=('Calisto MT Bold',12)).place(x=450,y=356)

                    s_name_label = Label(frame2, text='School Name: ',fg='#06518d',bg='white',font=('Calisto MT Bold',12)).place(x=450,y=396)

                    age_label = Label(frame2, text='Age: ',fg='#06518d',bg='white',font=('Calisto MT Bold',12)).place(x=450,y=436)

                    def add_rec():
                        conn=sqlite3.connect('student.db')
                        c=conn.cursor()
                        c.execute('INSERT INTO student VALUES (:f_name, :l_name, :address, :parents_name, :parents_number, :school_name, :age)',{
                        'f_name':f_name.get(),
                        'l_name':l_name.get(),
                        'address':address.get(),
                        'parents_name':p_name.get(),
                        'parents_number':p_number.get(),
                        'school_name':s_name.get(),
                        'age':age.get()
                         })
                        messagebox.showinfo('students', 'Inserted Successfully ')
                        conn.commit()
                        conn.close()

                        # showinfo message box

                        f_name.delete(0, END)
                        l_name.delete(0, END)
                        address.delete(0, END)
                        parents_name.delete(0, END)
                        parents_number.delete(0, END)
                        school_name.delete(0, END)
                        age.delete(0, END)

                    submit_btn = Button(frame2, text='AddRecords', command=add_rec, font=('Calisto MT Bold', 12), fg='white',
                                        bg='#06518d')
                    submit_btn.config( pady=2, padx=10)
                    submit_btn.place(x=750,y=480)

                frame1=Frame(a, height=500, width=600, bg='#06518d') \
                    .place(x=330, y=50)
                frame2=Frame(a,height=450,width=550,bg='white').place(x=355,y=75)

                rbtn2=Button(a,text='Add Rooms',pady=1,padx=10,fg='white',bg='#06518d',font=('Calisto MT Bold',16),command=add)
                rbtn2.place(x=380,y=100)
                rbtn3=Button(a,text='Edit Rooms',pady=1,padx=10,fg='white',bg='#06518d',font=('Calisto MT Bold',16))
                rbtn3.place(x=560,y=100)
                rbtn4=Button(a,text='Delete Rooms',pady=1,padx=1,fg='white',bg='#06518d',font=('Calisto MT Bold',16))
                rbtn4.place(x=740,y=100)


            btn1=Button(a,text='Student Information',pady=3,padx=2,fg='white',bg='#06518d',font=('Calisto MT Bold',16),command=student)
            btn1.place(x=50,y=100)
            btn2=Button(a,text='Rooms',pady=3,padx=63,fg='white',bg='#06518d',font=('Calisto MT Bold',16),command=room)
            btn2.place(x=50,y=160)


            a.mainloop()
