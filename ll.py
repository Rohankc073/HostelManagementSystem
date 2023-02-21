from tkinter import *
import sqlite3
from tkinter import messagebox

root = Tk()
root.title('Registration')

try:
    # Opening database
    conn = sqlite3.connect('signup.db')
    c = conn.cursor()

    # Creating a table
    # c.execute("""CREATE TABLE users (
    #     fullname text,
    #     ph_num text,
    #     email text,
    #     pass text,
    #     newpas text
    # )""")
    # print('Table created successfully')

except sqlite3.Error as error:
    print("Error while connecting to sqlite", error)

else:
    root.iconbitmap('H:\\My Drive\\a\\icon.ico')
    root.maxsize(width=900, height=650)
    root.minsize(width=900, height=650)
    root.configure(bg='#fff')
    image_1 = PhotoImage(file='WhatsApp Image 2023-01-29 at 11.27.52.png')
    Label(root, image=image_1, bg='white').place(x=400, y=100)

finally:
    # Closing database connection
    if conn:
        conn.close()

# Registration function
def register():
    try:
        # Get user input
        fullname = FullName.get().strip()
        ph_num = phone1.get().strip()
        email_val = email.get().strip()
        password = pas.get().strip()
        confirm_password = newpas.get().strip()

        # Validate inputs
        if not fullname:
            messagebox.showerror('Error', 'Please enter a valid full name')
            return
        if not ph_num.isdigit() or len(ph_num) != 10:
            messagebox.showerror('Error', 'Please enter a valid 10-digit phone number')
            return
        if not is_valid_email(email_val):
            messagebox.showerror('Error', 'Please enter a valid email')
            return
        if not is_valid_password(password):
            messagebox.showerror('Error', 'Please enter a valid password')
            return
        if password != confirm_password:
            messagebox.showerror('Error', 'Passwords do not match')
            return

        conn = sqlite3.connect('signup.db')
        c = conn.cursor()
        c.execute("INSERT INTO users VALUES(:fullname, :ph_num, :email, :pass, :newpas)",{
            'fullname': fullname,
            'ph_num': ph_num,
            'email': email_val,
            'pass': password,
            'newpas': confirm_password
        })

        # Clear input fields
        FullName.delete(0, END)
        phone1.delete(0, END)
        email.delete(0, END)
        pas.delete(0, END)
        newpas.delete(0, END)

        messagebox.showinfo('Registration Information','Registered Successfully')

        conn.commit()

    except sqlite3.Error as error:
        print("Error while connecting to sqlite", error)

    else:
        if conn:
            conn.close()

        root.destroy()
        import Login

    finally:
        # Closing database connection
        if conn:
            conn.close()

def is_valid_email(email_val):
    if not email_val:
        return False
    parts = email_val.split('@')
    if len(parts) != 2:
        return False
    username, domain = parts
    if not username or not domain:
        return False
    domain_parts = domain.split('.')
    if len(domain_parts) < 2:
        return False
    for part in domain_parts:
        if not part:
            return False
    return True

def is_valid_password(password):
    if not password or len(password) < 8:
        return False
    has_uppercase = False
    has_lowercase = False
    has_digit = False
    for char in password:
        if char.isupper():
            has_uppercase = True
        elif char.islower():
            has_lowercase = True
        elif char.isdigit():
            has_digit = True
    return has_uppercase and has_lowercase and has_digit

#=================================LABEL and ENTRY FOR REGISTRATION UI===================================
header=Label(root,text='Register Now',fg='#06518d', bg='white',font=('Calisto MT Bold',26,'bold'))
header.place(x=50,y=50)

para=Label(root,text='Please input your information on fields.',fg='#404040', bg='white',font=('Calisto MT Bold',12,'bold'))
para.place(x=50,y=100)

para1=Label(root,text='Full Name*',fg='black', bg='white',font=('Calisto MT ',12))
para1.place(x=50,y=170)
FullName=Entry(root,width=32,fg='black',border=2,highlightthickness=1,highlightbackground='#F1F0FD',font=('Calisto MT ',10))
FullName.place(x=50,y=190,height=25)

para2=Label(root,text='Phone Number*',fg='black',bg='white',font=('Calisto MT ',12))
para2.place(x=50,y=230)
phone1=Entry(root,width=25,fg='black',border=2,highlightthickness=1,highlightbackground='#F1F0FD',font=('Calisto MT ',12))
phone1.place(x=50,y=250,height=25)

para4=Label(root,text='Email*',fg='black', bg='white',font=('Calisto MT ',12))
para4.place(x=50,y=290)
email=Entry(root,width=25,fg='black',border=2,highlightthickness=1,highlightbackground='#F1F0FD',font=('Calisto MT ',12))
email.place(x=50,y=310,height=25)

para5=Label(root,text='Create Password*',fg='black', bg='white',font=('Calisto MT ',12))
para5.place(x=50,y=350)
pas=Entry(root,width=25,fg='black',border=2,highlightthickness=1,highlightbackground='#F1F0FD',font=('Calisto MT ',12),show="*")
pas.place(x=50,y=370,height=25)

para6=Label(root,text='Confirm Password*',fg='black', bg='white',font=('Calisto MT ',12))
para6.place(x=50,y=420)
newpas=Entry(root,width=25,fg='black',border=2,highlightthickness=1,highlightbackground='#F1F0FD',font=('Calisto MT ',12),show='*')
newpas.place(x=50,y=440,height=25)

#===========================================CHECK BOX======================================
show_pass = IntVar()
def show_pass_check():
    if show_pass.get():
        pas.config(show='')
        newpas.config(show='')
    else:
        pas.config(show='*')
        newpas.config(show='*')

c1 = Checkbutton(root,fg='black',border=0,text ="Show",bg='white',font=('Calisto MT ',8),command=show_pass_check,variable=show_pass,onvalue=1,offvalue=0).place(x=50,y=465)


button1=Button(root,width=10,pady=7,text='Sign up',bg='#06518d',fg='white',border=0,command=register,font=('Calisto MT Bold ',10)).place(x=50,y=520)

def have_acc():
    root.destroy()
    import Login
para3=Button(root,text='Already have an account? ',fg='white', bg='#06518d',font=('Calisto MT ',10),command=have_acc)
para3.place(x=100,y=590)



conn.close()
root.mainloop()



