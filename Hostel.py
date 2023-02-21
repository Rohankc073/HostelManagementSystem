# import email
from tkinter import *
import sqlite3
from tkinter import messagebox

root = Tk()
root.geometry('800x500')
root.title("Database Connection")

conn = sqlite3.connect('sql.db')
c = conn.cursor()


# c.execute ("""CREATE TABLE addresses (
#     email text,
#     password text
# )""")
#
# print ("Table created successfully")

def delete():
    conn = sqlite3.connect('sql.db')
    c = conn.cursor()
    c.execute("DELETE from addresses WHERE oid = " + delete_box.get())
    print('Deleted Successfully')

    c.execute("SELECT *, oid FROM addresses")
    records = c.fetchall()

    delete_box.delete(0, END)

    conn.commit()
    conn.close()


def update():
    conn = sqlite3.connect('sql.db')
    c = conn.cursor()

    record_id = delete_box.get()

    c.execute("""UPDATE addresses SET
        email=:email,
        password = :password,
        WHERE oid = :oid""",
              {'email': email_editor.get(),
               'password': password_editor.get(),
               # 'address': address_editor.get(),
               # 'city': city_editor.get(),
               # 'state': state_editor.get(),
               # 'zipcode': zipcode_editor.get(),
               'oid': record_id
               })
    conn.commit()
    conn.close()
    editor.destroy()


def query():
    conn = sqlite3.connect('sql.db')
    c = conn.cursor()
    c.execute("SELECT *, oid FROM addresses")

    records = c.fetchall()
    # print (records)
    print_record = ''
    for record in records:
        print_record += str(record[0]) + ' ' + str(record[1]) + ' ' + '\t' + str(record[6]) + "\n"
    query_label = Label(root, text=print_record)
    query_label.grid(row=15, column=0, columnspan=2)

    conn.commit()
    conn.close()


def submit():
    conn = sqlite3.connect('sql.db')
    c = conn.cursor()
    c.execute("INSERT INTO addresses VALUES (:email, :password)", {
        'email': email.get(),
        'password': password.get()
        # 'address': address.get(),
        # 'city': city.get(),
        # 'state': state.get(),
        # 'zipcode': zipcode.get(),

    })

    messagebox.showinfo("Info", "Inserted Successfully")

    conn.commit()
    conn.close()

    # clear text boxes
    email.delete(0, END)
    password.delete(0, END)
    # address.delete(0, END)
    # city.delete(0, END)
    # state.delete(0, END)
    # zipcode.delete(0, END)



def edit():
    global editor
    editor = Tk()
    editor.title('Update Data')
    editor.geometry('300x480')

    conn = sqlite3.connect('sql.db')
    c = conn.cursor()

    global email_editor
    global password_editor

    email_editor = Entry(editor, width=30)
    email_editor.grid(row=0, column=1, padx=20, pady=(10, 0))

    password_editor = Entry(editor, width=30)
    password_editor.grid(row=1, column=1)

    # address_editor = Entry(editor, width=30)
    # address_editor.grid(row=2, column=1)
    #
    # city_editor = Entry(editor, width=30)
    # city_editor.grid(row=3, column=1)
    #
    # state_editor = Entry(editor, width=30)
    # state_editor.grid(row=4, column=1)
    #
    # zipcode_editor = Entry(editor, width=30)
    # zipcode_editor.grid(row=5, column=1)

    delete_box_editor = Entry(editor, width=30)
    delete_box_editor.grid(row=6, column=1)

    email_label = Label(editor, text='Email')
    email_label.grid(row=0, column=0)

    password_label = Label(editor, text='Password')
    password_label.grid(row=1, column=0)

    # address_label = Label(editor, text='Address')
    # address_label.grid(row=2, column=0)
    #
    # city_label = Label(editor, text='City')
    # city_label.grid(row=3, column=0)
    #
    # state_label = Label(editor, text='State')
    # state_label.grid(row=4, column=0)
    #
    # zipcode_label = Label(editor, text='Zip Code')
    # zipcode_label.grid(row=5, column=0)

    # create Submit Button
    submit_button_editor = Button(editor, text="Add Record", command=submit)
    submit_button_editor.grid(row=7, column=0, columnspan=2, pady=5, padx=10, ipadx=100)

    # create a query button
    query_button = Button(editor, text="Show Records", command=query)
    query_button.grid(row=8, column=0, columnspan=2, pady=5, padx=10, ipadx=95)

    btn_save = Button(editor, text='Save', command=update)
    btn_save.grid(row=11, column=0, columnspan=2, pady=10, padx=10, ipadx=125)

    record_id = delete_box.get()

    c.execute('SELECT * FROM addresses WHERE oid='+record_id)
    records = c.fetchall()

    for record in records:
        email_editor.insert(0, record[0])
        password_editor.insert(1, record[1])
        # address_editor.insert(2, record[2])
        # city_editor.insert(3, record[3])
        # state_editor.insert(4, record[4])
        # zipcode_editor.insert(5, record[5])

    conn.commit()
    conn.close()


email1 = Entry(root, width=30)
email1.grid(row=0, column=1, padx=20)

password1 = Entry(root, width=30)
password1.grid(row=1, column=1)

# address = Entry(root, width=30)
# address.grid(row=2, column=1)
#
# city = Entry(root, width=30)
# city.grid(row=3, column=1)
#
# state = Entry(root, width=30)
# state.grid(row=4, column=1)
#
# zipcode = Entry(root, width=30)
# zipcode.grid(row=5, column=1)

email_label = Label(root, text='Email')
email_label.grid(row=0, column=0)

password1_label = Label(root, text='Password')
password1_label.grid(row=1, column=0)

# address_label = Label(root, text='Address')
# address_label.grid(row=2, column=0)
#
# city_label = Label(root, text='City')
# city_label.grid(row=3, column=0)
#
# state_label = Label(root, text='State')
# state_label.grid(row=4, column=0)
#
# zipcode_label = Label(root, text='Zip Code')
# zipcode_label.grid(row=5, column=0)

submit_btn = Button(root, text="Add Records", command=submit)
submit_btn.grid(row=7, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

query_btn = Button(root, text="Show Records", command=query)
query_btn.grid(row=8, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

delete_box = Entry(root, width=30)
delete_box.grid(row=9, column=1, pady=5)

delete_box_label = Label(root, text="Delete/Update ID")
delete_box_label.grid(row=9, column=0, pady=5)

delrecord_btn = Button(root, text="Delete Record", command=delete)
delrecord_btn.grid(row=11, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

edit_btn = Button(root, text="Update", command=edit)
edit_btn.grid(row=12, column=0, columnspan=2, pady=10, padx=10, ipadx=120)

conn.commit()
conn.close()

# conn = sqlite3.connect('sql.db')
# c = conn.cursor()
#
#
# c.execute ("""CREATE TABLE login (
#     email text,
#     password text,
# )""")
#
# print ("Table created successfully")


root.mainloop()