import tkinter as tk
from tkinter import messagebox
import sqlite3

def logout():
    root.destroy()
    import login_view

def delete_system_user():
    import delete_system_user
    root.destroy()

def add_system_stock():
    import add_system_stock
    root.destroy()

def edit_system_user():
    import edit_system_user
    root.destroy()

root = tk.Tk()
root.title("Main Menu")
root.geometry("1400x720")
root.config(bg="light blue")
root.resizable(False, False)  # Set the width and height of the window

# Add User Button
def open_user_add_form():
    root.destroy()
    import user_add_form  # Assuming user_add_form.py is in the same directory

button_width = 20
button_height = 7

# Create a frame to center the buttons
frame = tk.Frame(root, bg="light blue")
frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

font_style = ("Helvetica", 16)

# Add User Button
add_user_button = tk.Button(frame, text="Add User", font=font_style, command=open_user_add_form, width=button_width, height=button_height)
add_user_button.pack(side=tk.LEFT, padx=10)

# Edit User Button
edit_user_button = tk.Button(frame, text="Edit User", font=font_style, command=edit_system_user, width=button_width, height=button_height)
edit_user_button.pack(side=tk.LEFT, padx=10)

# Delete User Button
delete_user_button = tk.Button(frame, text="Delete User", font=font_style, command=delete_system_user, width=button_width, height=button_height)
delete_user_button.pack(side=tk.LEFT, padx=10)

# Add Stock Button
add_stock_button = tk.Button(frame, text="Add Stock", font=font_style, command=add_system_stock, width=button_width, height=button_height)
add_stock_button.pack(side=tk.LEFT, padx=10)

# Logout Button
logout_button = tk.Button(frame, text="Logout", font=font_style, command=logout, width=button_width, height=button_height)
logout_button.pack(side=tk.LEFT, padx=10)

root.mainloop()