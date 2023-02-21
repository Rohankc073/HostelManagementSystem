from tkinter import *
import sqlite3
from tkinter import messagebox

a = Tk()
a.title('Forgot Password')
a.maxsize(850, 650)
a.minsize(850, 650)

# Create a function to handle the "Reset Password" functionality
def reset_password():
    conn = sqlite3.connect('signup.db')
    c=conn.cursor()

    # Get the input values
    email = email_entry.get()
    p_number = phone1_entry.get()
    new_password = new_password_entry.get()
    confirm_password = confirm_password_entry.get()

    # Check if the email and phone number exist in the database
    c.execute('SELECT * FROM users WHERE email=? AND ph_num=?', (email, p_number))
    user = c.fetchone()

    if user:
        # If the email and phone number are valid, update the password in the database
        if new_password == confirm_password:
            # Check if the new password meets the requirements
            if len(new_password) >= 8 and any(c.isupper() for c in new_password) and any(c.isdigit() for c in new_password):
                c.execute('UPDATE users SET pass=? WHERE email=?', (new_password, email))
                conn.commit()
                messagebox.showinfo('Success', 'Password reset successfully.')
                a.destroy()
                import Login
            else:
                messagebox.showerror('Error', 'New password must be at least 8 characters long and include at least one uppercase letter and one number.')
        else:
            messagebox.showerror('Error', 'New password and confirm password do not match.')
    else:
        messagebox.showerror('Error', 'Email and phone number do not match.')

    conn.close()

# Create the GUI elements
img1 = PhotoImage(file='istockphoto-1351756759-170667a.png')
image = Label(a, image=img1)
image.place(x=0, y=0)

frame1 = Frame(height=500, width=380, bg='#06518d')
frame1.place(x=250, y=100)

label1 = Label(a, text='Reset Your Password:', bg='#06518d', font=('Calisto MT Bold', 18), fg='white')
label1.place(x=330, y=120)

email_label = Label(a, text='Confirm your email*', bg='#06518d', font=('Calisto MT Bold', 12), fg='White')
email_label.place(x=260, y=165)
email_entry = Entry(a, borderwidth=2, fg='Black', width=50)
email_entry.place(x=260, y=200)

phone1_label = Label(a, text='Phone Number*', bg='#06518d', font=('Calisto MT Bold', 12), fg='White')
phone1_label.place(x=260, y=240)
phone1_entry = Entry(a, borderwidth=2, fg='Black', width=50)
phone1_entry.place(x=260, y=280)

new_password_label = Label(a, text='New Password*', bg='#06518d', fg='white', font=('Calisto MT Bold', 12))
new_password_label.place(x=260, y=320)
new_password_entry = Entry(a, borderwidth=2, fg='Black', width=50, show='*')
new_password_entry.place(x=260, y=360)

confirm_password_label = Label(a, text='Confirm Password*', bg='#06518d', fg='white', font=('Calisto MT Bold', 12))
confirm_password_label.place(x=260, y=400)
confirm_password_entry = Entry(a, borderwidth=2, width=50, fg='black', show='*')
confirm_password_entry.place(x=260, y=450)

confirm_button = Button(a, text='Confirm', bg='White', font=('Calisto MT Bold', 14), padx=20, pady=2, fg='#06518d', command=reset_password).place(x=300,y=520)

a.mainloop()
