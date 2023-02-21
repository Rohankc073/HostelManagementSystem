# from tkinter import *
# import sqlite3
# from tkinter import messagebox
# a=Tk()
# a.title('Facebook')
# a.geometry('500x500')
#
# conn=sqlite3.connect('Facebook.db')
# c=conn.cursor()
#
# #Cresting a table
# c.execute("""CREATE TABLE facebook (
#       username text,
#       first_name text,
#       last_name text,
#       age integer,
#       password text,
#       address text
#       )""")
# print('Table has been created')
#
# conn.commit()
# conn.close()
#
#
# def submit():
#     conn=sqlite3.connect('Facebook.db')
#     c=conn.cursor()
#     c.execute('INSERT INTO facebook VALUES(:username, :first_name, :last_name, :age, :password, :address)',{
#         'username': username.get(),
#         'first_name': first_name.get(),
#         'last_name': last_name.get(),
#         'age': age.get(),
#         'password':password.get(),
#         'address':address.get()
#     })
#
#     messagebox.showinfo('facebook','inserted successfully ')
#     conn.commit()
#     conn.close()
#
#     username.delete(0,END)
#     first_name.delete(0,END)
#     last_name.delete(0,END)
#     age.delete(0,END)
#     password.delete(0,END)
#     address.delete(0,END)
#
# #Creating Table
#
#
#
#
#
#
# mainloop()

a=20
print(b)