from tkinter import*
import sqlite3
from tkinter import messagebox
a=Tk()
a.title('Hostel Management System')
a.geometry('500x500')

#Creatind a new database
conn=sqlite3.connect('Hostel_book.db')
c=conn.cursor()

# #Creating a table
# c.execute("""CREATE TABLE hostel(
#       email text,
#       password text
# )""")
# print('Table created successfully')
# conn.commit()
# conn.close()

# defien the first function submit so that the button add record actually adds records
def submit():
    conn=sqlite3.connect('Hostel_book.db')
    c=conn.cursor()
    c.execute('INSERT INTO hostel VALUES (:email_btn,:password_btn)',{
        'email_btn':email_btn.get(),
        'password_btn':password_btn.get()

    })
    messagebox.showinfo('hostel','Inserted Successfully')
    conn.commit()
    conn.close()

    
    email_btn.delete(0,END)
    password_btn.delete(0,END)

#Creating text boxes
email_btn=Entry(a,width=30)
email_btn.grid(row=0,column=1,padx=20)
password_btn=Entry(a,width=30)
password_btn.grid(row=1,column=1)
# address=Entry(a,width=30)
# address.grid(row=2,column=1)
# school_name=Entry(a,width=30)
# school_name.grid(row=3,column=1)
# parent_name=Entry(a,width=30)
# parent_name.grid(row=4,column=1)
# parent_number=Entry(a,width=30)
# parent_number.grid(row=5,column=1)
# room_number=Entry(a,width=30)
# room_number.grid(row=6,column=1)

#Creating text label
email_btn_label=Label(a,text='Email: ')
email_btn_label.grid(row=0,column=0)
password_btn_label=Label(a,text='Password: ')
password_btn_label.grid(row=1,column=0)
# address_label=Label(a,text='Address: ')
# address_label.grid(row=2,column=0)
# school_name_label=Label(a,text='School Name: ')
# school_name_label.grid(row=3,column=0)
# parent_name_label=Label(a,text='Parents Name: ')
# parent_name_label.grid(row=4,column=0)
# parent_number_label=Label(a,text='Parents No.: ')
# parent_number_label.grid(row=5,column=0)
# room_number_label=Label(a,text='Roon No.:')
# room_number_label.grid(row=6,column=0)

#Create submit button
submit_btn=Button(a,text='Add Record',command=submit)
submit_btn.grid(row=3,column=0,columnspan=2,padx=10,pady=10,ipadx=100)

def query():
    conn=sqlite3.connect('Hostel_book.db')
    c = conn.cursor()
    c.execute('SELECT *, oid FROM hostel')

    records = c.fetchall()
    print_record=''

    for record in records:
        print_record += str(record[0]) + ' ' + str(record[1]) + ' ' + '\t' + str(record[2]) + '\n'

    query_label=Label(a,text=print_record)
    query_label.grid(row=4, column=0,columnspan=2)

    # conn.commit()
    # conn.close()
query_btn=Button(a,text='Show Record',command=query).grid(row=5,column=0,columnspan=2,pady=10,padx=10,ipadx=10)

def delete():
    conn=sqlite3.connect('Hostel_book.db')
    c=conn.cursor()
    c.execute('DELETE from hostel WHERE oid='+delete_box.get())
    # conn.commit()
    # conn.close()

delete_box=Entry(a,width=30)
delete_box.grid(row=7,column=1,pady=5)
delete_box_label = Label(a, text='Delete ID')
delete_box_label.grid(row=8, column=0, pady=5)
delete_btn = Button(a, text='Delete', command=delete)
delete_btn.grid(row=10, columnspan=2, pady=10, padx=10, ipadx=20)

#Creating an update function
def update():
    conn=sqlite3.connect('Hostel_book.db')
    c=conn.cursor()
    record_id=delete_box.get()


    c.execute("""UPDATE hostel SET
    email=:email,
    password=:password
    WHERE oid=:oid""",
              {'email':email_btn_editor.get(),
               'password':password_btn_editor.get()
               }
    )
    # conn.commit()
    # conn.close()
    editor.destroy()

def edit():
    global editor
    editor=Tk()
    editor.title('Update data')
    editor.geometry('500x500')
    conn=sqlite3.connect('Hostel_book.db')
    conn.cursor()

    record_id=delete_box.get()

    c.execute('SELECT * FROM hostel WHERE oid ='+record_id)
    records=c.fetchall()

    global email_btn_editor
    global password_btn_editor

    email_btn_editor = Entry(editor, width=30)
    email_btn_editor.grid(row=0, column=1)

    password_btn_editor = Entry(editor, width=30)
    password_btn_editor.grid(row=1, column=1)

    email_btn_label=Label(editor,text='Email')
    email_btn_label.grid(row=0,column=0,pady=(10,0))

    password_btn_label = Label(editor, text="Password")
    password_btn_label.grid(row=1, column=0)


    for record in records:
        email_btn_editor.insert(0, record[0])
        password_btn_editor.insert(0, record[1])

    edit_btnn = Button(editor, text='Save', command=update)
    edit_btnn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=125)

edit_btn = Button(a, text='Update', command=edit)
edit_btn.grid(row=11, column=0, columnspan=2, padx=10, pady=10, ipadx=120)

# #A new table for sign up
#
# conn=sqlite3.connect('Hostel_book.db')
# conn.cursor()
# c.execute("""CREATE TABLE registration (
#         first_name text,
#         last_name text,
#         email text,
#         phone_number integer,
#         password text
#
# )""")
#
# conn.commit()
# conn.close()
#
# def submit1():
#     conn=sqlite3.connect('Hostel_book.db')
#     c=conn.cursor()
#     c.execute('INSERT INTO registration VALUES(:first_name, :last_name, :email, :phone_number, :password)',{
#         'first_name':first_name.get(),
#         'last_name':last_name.get(),
#         'email':email.get(),
#         'password':password.get()
#     })
#
#     messagebox.showinfo('')






a.mainloop()