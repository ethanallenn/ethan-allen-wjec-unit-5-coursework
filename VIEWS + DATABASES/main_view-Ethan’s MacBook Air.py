import tkinter as tk
from tkinter import messagebox
import sqlite3

def logout():
    root.destroy()
    import login_view

def add_system_stock():
    import add_system_stock
    root.destroy()

def open_user_menu():
    import user_menu_view
    root.destroy()
    

# Create the main window
root = tk.Tk()
root.title("Main Menu")
root.geometry("1400x720")
root.config(bg="light blue")
root.resizable(False, False)  # Set the width and height of the window

button_width = 20
button_height = 7

# Create a frame to center the buttons
frame = tk.Frame(root, bg="light blue")
frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

font_style = ("Helvetica", 16)

# Add User Button
uMenu_button = tk.Button(frame, text="User Menu", font=font_style, command=open_user_menu, width=button_width, height=button_height
                         _button.pack(side=tk.LEFT, padx=10)



root.mainloop()