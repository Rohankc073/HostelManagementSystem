from tkinter import*
import sqlite3
from tkinter import messagebox
a=Tk()
a.title('Message Box')
a.geometry('500x500')

#Database
#create a database or connect to one
conn=sqlite3.connect('address_book.db')
#Create cursor
c=conn.cursor()
# Create tabel
# c.execute("""CREATE TABLE addresses(
#         first_name text,
#         last_name text,
#         address text,
#         city text,
#         state text,
#         zipcode integer
# )""")
# print('Table created successfully')

#Commit change
conn.commit()

#Close connection
conn.close()

def submit():
    #Create a databases or connect to one
    conn=sqlite3.connect('address_book.db')
    #Create cursor
    c=conn.cursor()
    #Insert into table
    c.execute('INSERT INTO addresses VALUES(:f_name, :l_name, :address, :city, :state, :zipcode)',{
        'f_name':f_name.get(),
        'l_name':l_name.get(),
        'address':address.get(),
        'city':city.get(),
        'state':state.get(),
        'zipcode':zipcode.get()
    })
    #showinfo message box
    messagebox.showinfo('Addresses','Inserted Successfully ')
    conn.commit()
    conn.close()
    f_name.delete(0,END)
    l_name.delete(0,END)
    address.delete(0,END)
    city.delete(0,END)
    state.delete(0,END)
    zipcode.delete(0,END)
    #clear the text box

#Creating table in database
#create tesxt box
f_name=Entry(a,width=30)
f_name.grid(row=0,column=1,padx=20)

l_name=Entry(a,width=30)
l_name.grid(row=1,column=1)

address=Entry(a,width=30)
address.grid(row=2,column=1)

city=Entry(a,width=30)
city.grid(row=3,column=1)

state=Entry(a,width=30)
state.grid(row=4,column=1)

zipcode=Entry(a,width=30)
zipcode.grid(row=5,column=1)

#Create textbox labels
f_name_label=Label(a,text='First Name').grid(row=0,column=0)

l_name_label=Label(a,text='Last Name').grid(row=1,column=0)

address_label=Label(a,text='Address').grid(row=2,column=0)

city_label=Label(a,text='City').grid(row=3,column=0)

state_label=Label(a,text='State').grid(row=4,column=0)

zipcode_label=Label(a,text='Zipcode').grid(row=5,column=0)

#Create submit button
submit_btn=Button(a,text='AddRecords',command=submit)
submit_btn.grid(row=6,column=0,columnspan=2,pady=10,padx=10,ipadx=100)


def query():
    conn=sqlite3.connect('address_book.db')

    #Create Cursor
    c=conn.cursor()

    #query of gthe address
    c.execute('SELECT *,oid FROM addresses')

    records=c.fetchall()
    # print(records)
    print_record = ''
    for record in records:
        print_record += str(record[0]) + ' ' + str(record[1]) + ' ' + '\t' + str(record[6]) + '\n'

    query_label = Label(a, text=print_record)
    query_label.grid(row=8, column=0, columnspan=2)

    conn.commit()
    conn.close()
query_btn=Button(a,text='Show Record',command=query).grid(row=7,column=0,columnspan=2,pady=10,padx=10,ipadx=10)

def delete():
    conn=sqlite3.connect('address_book.db')
    c=conn.cursor()
    c.execute('DELETE from addresses WHERE oid= '+delete_box.get())
    print('Delete Successfully')
    conn.commit()
    conn.close()
    # c.execute('SELECT*,oid FROM addresses')
    # records=c.fetchall()
    # print_record+=str(record[0])
delete_box = Entry(a, width=30)
delete_box.grid(row=9, column=1, pady=5)
delete_box_label = Label(a, text='Delete ID')
delete_box_label.grid(row=9, column=0, pady=5)
delete_btn = Button(a, text='Delete', command=delete)
delete_btn.grid(row=10, columnspan=2, pady=10, padx=10, ipadx=20)


#creating an update function
def update():
    #Create A database or connect to one
    conn=sqlite3.connect('address_book.db')
    # Create Cursor
    c=conn.cursor()
    record_id=delete_box.get()


    c.execute("""UPDATE addresses SET
    first_name=:first,
    last_name=:last,
    address=:address,
    city=:city,
    state=:state,
    zipcode=:zipcode
    WHERE oid=:oid""",
              {'first':f_name_editor.get(),
               'last':l_name_editor.get(),
               'address':address_editor.get(),
               'city':city_editor.get(),
               'state':state_editor.get(),
               'zipcode':zipcode_editor.get(),
               'oid':record_id
               }
    )
    conn.commit()
    conn.close()

    editor.destroy()

def edit():
    global editor

    editor=Tk()
    editor.title('Update data')
    editor.geometry('500x500')
    conn=sqlite3.connect('address_book.db')
    c=conn.cursor()

    record_id=delete_box.get()

    c.execute('SELECT * FROM addresses WHERE oid='+record_id)
    records=c.fetchall()

    global f_name_editor
    global l_name_editor
    global address_editor
    global city_editor
    global state_editor
    global zipcode_editor

    f_name_editor=Entry(editor,width=30)
    f_name_editor.grid(row=0,column=1)

    l_name_editor=Entry(editor,width=30)
    l_name_editor.grid(row=1,column=1)

    address_editor=Entry(editor,width=30)
    address_editor.grid(row=2,column=1)

    city_editor = Entry(editor, width=30)
    city_editor.grid(row=3, column=1)

    state_editor = Entry(editor, width=30)
    state_editor.grid(row=4, column=1)

    zipcode_editor = Entry(editor, width=30)
    zipcode_editor.grid(row=5, column=1)

    f_name_label=Label(editor,text='First Name')
    f_name_label.grid(row=0,column=0,pady=(10,0))

    l_name_label = Label(editor, text="Last Name")
    l_name_label.grid(row=1, column=0)

    address_label = Label(editor, text='Address')
    address_label.grid(row=2, column=0)

    city_label = Label(editor, text='City')
    city_label.grid(row=3, column=0)

    state_label = Label(editor, text='State')
    state_label.grid(row=4, column=0)

    zipcode_label =Label(editor, width=30)
    zipcode_label.grid(row=5, column=0)

    #Loop through the results
    for record in records:
        f_name_editor.insert(0,record[0])
        l_name_editor.insert(0,record[1])
        address_editor.insert(0,record[2])
        city_editor.insert(0,record[3])
        state_editor.insert(0,record[4])
        zipcode_editor.insert(0,record[5])



    #CREATE A UPDATE BUTTON
    edit_btnn=Button(editor,text='Save',command=update)
    edit_btnn.grid(row=6,column=0,columnspan=2,pady=10,padx=10,ipadx=125)

edit_btn=Button(a,text='Update',command=edit)
edit_btn.grid(row=11,column=0,columnspan=2,padx=10,pady=10,ipadx=120)


a.mainloop()

