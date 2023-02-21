from tkinter import*
import sqlite3
from tkinter import messagebox
# import Reg
a=Tk()
a.title('Forgot Password')
a.maxsize(850,650)
a.minsize(850,650)
def verfity():
    conn = sqlite3.connect('signup.db')
    c = conn.cursor()

    email = email.get()
    p_number = phone1.get()
img1=PhotoImage(file='istockphoto-1351756759-170667a.png')
image=Label(a,image=img1).place(x=0,y=0)
frame1=Frame(height=500,width=380,bg='#06518d').place(x=250,y=100)
label1=Label(a,text='Reset Your Password : ',bg='#06518d',font=('Calisto MT Bold',18),fg='white').place(x=330,y=120)
label2=Label(a,text='Confirm your email*',bg='#06518d',font=('Calisto MT Bold',12),fg='White').place(x=260,y=165)
entry1=Entry(a,borderwidth=2,fg='Black',width=50).place(x=260,y=200)
label4=Label(a,text='Phone Number*',bg='#06518d',font=('Calisto MT Bold',12),fg='White').place(x=260,y=240)
entry3=Entry(a,borderwidth=2,fg='Black',width=50).place(x=260,y=280)
label5=Label(a,text='New Password*',bg='#06518d',fg='white',font=('Calisto MT Bold',12)).place(x=260,y=320)
entry4=Entry(a,borderwidth=2,fg='Black',width=50).place(x=260,y=360)
label6=Label(a,text='Confirm Password*',bg='#06518d',fg='white',font=('Calisto MT Bold',12)).place(x=260,y=400)
entry5=Entry(a,borderwidth=2,width=50,fg='black').place(x=260,y=450)
def confirm():
    a.destroy()
    import Login
button1=Button(a,text='Confirm',bg='White',font=('Calisto MT Bold',14),padx=20,pady=2,fg='#06518d').place(x=360,y=520)
a.mainloop()

# a=Tk()
# a.title('Message Box')
# conn=sqlite3.connect('signup.db')
# c=conn.cursor()
# def submit():
#
#     conn=sqlite3.connect('signup.db')
#     c=conn.cursor()
#     c.execute("INSERT INTO users VALUES(:FullName, :phone1, :email, :pas, :newpas)",{
#         'FullName':FullName.get(),
#         'phone1':phone1.get(),
#         'email':email.get(),
#         'pas':pas.get(),
#         'newpas':newpas.get()
#     })
#     messagebox.showinfo('users','Inserted successfully')
#
#     conn.commit()
#     conn.close()
#     # global FullName
#     # global phone1
#     # global email
#     # global pas
#     # global newpas
#
#
#
#     FullName.delete(0,END)
#     phone1.delete(0,END)
#     email.delete(0,END)
#     pas.delete(0,END)
#     newpas.delete(0,END)
#
# FullName=Entry(a,width=30)
# FullName.grid(row=0,column=1,padx=20)
#
# phone1=Entry(a,width=30)
# phone1.grid(row=1,column=1)
#
# email=Entry(a,width=30)
# email.grid(row=2,column=1)
#
# pas=Entry(a,width=30)
# pas.grid(row=3,column=1)
#
# newpas=Entry(a,width=30)
# newpas.grid(row=4,column=1)
#
#
# FullName_label=Label(a,text='Full Name')
# FullName_label.grid(row=0,column=0)
#
# phone1_label=Label(a,text='Phone Number')
# phone1_label.grid(row=1,column=0)
#
# email_label=Label(a,text='Email')
# email_label.grid(row=2,column=0)
#
# pas_label=Label(a,text='Password')
# pas_label.grid(row=3,column=0)
#
# newpas_label=Label(a,text='Confirm Password')
# newpas_label.grid(row=4,column=0)
#
# submit_btn=Button(a,text='Add record',command=submit)
# submit_btn.grid(row=6,column=0,columnspan=2,padx=10,pady=10,ipadx=1)
#
# def query():
#     conn=sqlite3.connect('signup.db')
#     c=conn.cursor()
#
#     c.execute('SELECT *, oid FROM users')
#
#     records=c.fetchall()
#     print_record=''
#     for record in records:
#         print_record+=str(record[0]) + ' ' + str(record[1]) + ' ' + '\t' + str(record[5]) + '\n'
#
#
#     query_label=Label(a,text=print_record)
#     query_label.grid(row=6,column=0,columnspan=2)
#
#     conn.commit()
#     conn.close()
# query_btn=Button(a,text='Show Records',command=query).grid(row=7,column=0,columnspan=2,pady=10,padx=10,ipadx=10)
#
#
# def delete():
#     conn=sqlite3.connect('signup.db')
#     c=conn.cursor()
#     c.execute('DELETE from users WHERE oid='+delete_box.get())
#     print('Delete Successfully')
#     conn.commit()
#     conn.close()
#
#
# delete_box = Entry(a, width=30)
# delete_box.grid(row=9, column=1, pady=5)
# delete_box_label = Label(a, text='Delete ID')
# delete_box_label.grid(row=9, column=0, pady=5)
# delete_btn = Button(a, text='Delete', command=delete)
# delete_btn.grid(row=10, columnspan=2, pady=10, padx=10, ipadx=20)
# conn.commit()
# conn.close()
#
# def update():
#     conn=sqlite3.connect('signup.db')
#     c=conn.cursor()
#     record_id=delete_box.get()
#     c.execute("""UPDATE users SET
#     FullName=:FullName,
#     phone1=:phone1,
#     email=:email,
#     pas=:pas,
#     newpas=:newpas
#     WHERE oid=:oid""",
#               {'FullName':FullName_editor.get(),
#                'phone1':phone1_editor.get(),
#                'email':email_editor.get(),
#                'pas':pas_editor.get(),
#                'newpas':newpas_editor.get(),
#                'oid':record_id
#
#               }
#     )
#     conn.commit()
#     conn.close()
#
# def edit():
#     global editor
#
#     editor=Tk()
#     editor.title('Update data')
#     editor.geometry('500x500')
#     conn=sqlite3.connect('signup.db')
#     c=conn.cursor()
#
#     record_id=delete_box.get()
#
#     c.execute('SELECT * FROM users WHERE oid='+record_id)
#     records=c.fetchall()
#
#     global FullName_editor
#     global phone1_editor
#     global email_editor
#     global pas_editor
#     global newpas_editor
#
#     FullName_editor=Entry(editor,width=30)
#     FullName_editor.grid(row=0,column=1)
#
#     phone1_editor=Entry(editor,width=30)
#     phone1_editor.grid(row=1,column=1)
#
#     email_editor=Entry(editor,width=30)
#     email_editor.grid(row=2,column=1)
#
#     pas_editor= Entry(editor, width=30)
#     pas_editor.grid(row=3, column=1)
#
#     newpas_editor = Entry(editor, width=30)
#     newpas_editor.grid(row=4, column=1)
#
#     for record in records:
#         FullName_editor.insert(0,record[0])
#         phone1_editor.insert(0,record[1])
#         email_editor.insert(0,record[2])
#         pas_editor.insert(0,record[3])
#         newpas_editor.insert(0,record[4])
#
#         # CREATE A UPDATE BUTTON
#     edit_btnn = Button(editor, text='Save', command=update)
#     edit_btnn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=125)
#
# edit_btn = Button(a, text='Update', command=edit)
# edit_btn.grid(row=11, column=0, columnspan=2, padx=10, pady=10, ipadx=120)





# delete_box = Entry(a, width=30)
# delete_box.grid(row=9, column=1, pady=5)
# delete_box_label = Label(a, text='Delete ID')
# delete_box_label.grid(row=9, column=0, pady=5)
# delete_btn = Button(a, text='Delete')
# delete_btn.grid(row=10, columnspan=2, pady=10, padx=10, ipadx=20)
# def update():
#     # Create A database or connect to one
#     conn = sqlite3.connect('signup.db')
#     # Create Cursor
#     c = conn.cursor()
#     record_id = delete_box.get()
#
#     c.execute("""UPDATE users SET
#      email=:c_email,
#      phone=:phone_number,
#      pass=:n_password,
#      c_pass=:con_password
#      WHERE oid=:oid""",
#               {'c_email': email_editor.get(),
#                'phone_number': phone_editor.get(),
#                'pass': n_password_editor.get(),
#                'c_pass': con_password_editor.get(),
#                'oid': record_id
#                }
#               )
#     conn.commit()
#     conn.close()
#
# def edit():
#     global editor
#
#     editor=Tk()
#     editor.title('Update data')
#     editor.geometry('500x500')
#     conn=sqlite3.connect('signup.db')
#     c=conn.cursor()
#
#     record_id=delete_box.get()
#
#     c.execute('SELECT * FROM users WHERE oid='+record_id)
#     records=c.fetchall()
#
#     global email_editor
#     global phone_editor
#     global n_password_editor
#     global con_password_editor
#
#
#     email_editor=Entry(editor,width=30)
#     email_editor.grid(row=0,column=1)
#
#     phone_editor=Entry(editor,width=30)
#     phone_editor.grid(row=1,column=1)
#
#     n_password_editor=Entry(editor,width=30)
#     n_password_editor.grid(row=2,column=1)
#
#     con_password_editor = Entry(editor, width=30)
#     con_password_editor.grid(row=3, column=1)
#
#
#     email_editor=Label(editor,text='First Name')
#     email_editor.grid(row=0,column=0,pady=(10,0))
#
#     phone_editor = Label(editor, text="Last Name")
#     phone_editor.grid(row=1, column=0)
#
#     n_password_editor = Label(editor, text='Address')
#     n_password_editor.grid(row=2, column=0)
#
#     con_password_editor = Label(editor, text='City')
#     con_password_editor.grid(row=3, column=0)
#
#
#
#     #Loop through the results
#     for record in records:
#         email_editor.insert(0,record[0])
#         phone_editor.insert(0,record[1])
#         n_password_editor.insert(0,record[2])
#         con_password_editor.insert(0,record[3])
#
#
#
#
#     #CREATE A UPDATE BUTTON
#     edit_btnn=Button(editor,text='Save',command=update)
#     edit_btnn.grid(row=6,column=0,columnspan=2,pady=10,padx=10,ipadx=125)
#
# edit_btn=Button(a,text='Update',command=edit)
# edit_btn.grid(row=11,column=0,columnspan=2,padx=10,pady=10,ipadx=120)
