import tkinter as tk

def switch_mode():
    global mode
    mode = "dark" if mode == "light" else "light"
    color = "black" if mode == "dark" else "white"
    background_color = "grey12" if mode == "dark" else "white"
    label.config(fg=color, bg=background_color)
    button.config(fg=color, bg=background_color)

root = tk.Tk()
root.geometry("200x100")

mode = "light"

label = tk.Label(root, text="Hello, World!", font=("TkDefaultFont", 16))
label.pack(pady=10)

button = tk.Button(root, text="Switch Mode", command=switch_mode)
button.pack()

root.mainloop()
