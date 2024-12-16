import tkinter as tk
from tkinter import *

def logout_button():
    root.destroy()
    import login_view

def open_add_stock():
    root.destroy()
    import add_system_stock


root = tk.Tk()
root.title("User Menu")
root.geometry("1400x720")
root.config(bg="light blue")
root.resizable(False, False)  # Set the width and height of the window
Frame = tk.Frame(root, bg="light blue")
Frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
font_style = ("Helvetica", 16)

add_stock_button = tk.Button(Frame, text="Add Stock", font=font_style, command=open_add_stock, width=20, height=7)
add_stock_button.pack(side=tk.LEFT, padx=10)

logout_button_add = tk.Button(root, text="Logout", font=font_style, command=logout_button)
logout_button_add.place(relx=1.0, rely=0.0, anchor='ne', x=-10, y=10)
logout_button_add.pack(side=tk.LEFT, padx=10)

root.mainloop()
