from tkinter import*
a=Tk()
a.title('Calculator')
a.configure(bg='Navy')
a.maxsize(width=300,height=400)
a.minsize(width=300,height=400)
e=Entry(width=45,borderwidth=10).grid(row=0,column=0,columnspan=3)

def button_click(number):
    current=e.get()
    e.delete(0,END)
    e.insert(0,str(current)+str(number))

def button_clear():
    e.delete(0,END)

def button_add():
    first_number=e.get()
    global f_num
    e.delete(0,END)
    global button_clicked
    button_clicked='+'


a.mainloop()
