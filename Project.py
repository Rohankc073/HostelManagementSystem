# from tkinter import *
# from PIL import Image,ImageTk
# a=Tk()
# a.title('Hostel Management System')
# a.geometry('500x500')
# a.configure(bg='white')
# a.anchor('center')
# Intro=Label(a,text='Online Hostel\n Management System',bg='White',fg='Black',font=('Bold',16)).place(x=10,y=20)
# # Login=Label(a,text='Email\\Phone number').place(x=1,y=)
# bg=PhotoImage(file='Project.png')
# my_label1=Label(a,image=bg).place(x=10,y=130)
# my_image=Image.open('Spider.png')
# resized_image=my_image.resize((10,10))
# my_label2=Label(a,text='Student ID',image='')
#
# from PIL import Image
#
# # Open the original image
# original_image = Image.open("Project.png")
#
# # Resize the image to a width of 300 and a height of 200
# resized_image = original_image.resize((100, 100))
#
# # Save the resized image
# resized_image.save("resized.png")
# # resized_image.show()
#
#
# a.mainloop()



from tkinter import*

root =Tk()
bg=PhotoImage(file='financial-forecastt-hostel.png')
my_label=Label(root,image=bg).place(x=0,y=0)
root.maxsize(width=700,height=450)
root.minsize(width=700,height=450)

# root.geometry("400x300")
root.title("Hostel Management Login")
root.configure(bg='Grey')
label=Label(root,text='Welcome',fg='Black',font=('Algerian',16)).place(x=320,y=80)

username_label =Label(root, text="Username:",borderwidth=3)
username_label.place(x=250, y=150)
root.iconbitmap('H:\\My Drive\\a\\icon.ico')#to change the application icon

username_entry =Entry(root,borderwidth=3)
username_entry.place(x=320, y=150)

password_label = Label(root, text="Password:")
password_label.place(x=250, y=200)

password_entry = Entry(root, show="*",borderwidth=3)
password_entry.place(x=320, y=200)

login_button = Button(root, text="Login", width=10, height=1,borderwidth=3)
login_button.place(x=320, y=250)


root.mainloop()



