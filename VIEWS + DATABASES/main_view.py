import tkinter as tk
from tkinter import messagebox
import sqlite3

def logout():
    import login_view
    root.destroy()

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
root.geometry("500x500")  # Set the width and height of the window

# Add User Button
def open_user_add_form():
    root.destroy()
    import user_add_form  # Assuming user_add_form.py is in the same directory

# Add User Button
add_user_button = tk.Button(root, text="Add User", command=open_user_add_form)
add_user_button.grid(row=0, column=0, pady=10)

# Edit User Button
edit_user_button = tk.Button(root, text="Edit User", command=edit_system_user)
edit_user_button.grid(row=1, column=0, pady=10)

# Delete User Button
delete_user_button = tk.Button(root, text="Delete User", command=delete_system_user)
delete_user_button.grid(row=2, column=0, pady=10)

# Add Stock Button
add_stock_button = tk.Button(root, text="Add Stock", command=add_system_stock)
add_stock_button.grid(row=3, column=0, pady=10)

# Logout Button
logout_button = tk.Button(root, text="Logout", command=logout)
logout_button.grid(row=4, column=0, pady=10)

root.mainloop()