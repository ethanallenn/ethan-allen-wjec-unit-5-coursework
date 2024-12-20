import tkinter as tk
from tkinter import messagebox
from tkinter import *

root = tk.Tk()
root.title("User Menu")
root.geometry("1400x720")
root.config(bg="light blue")
root.resizable(False, False)  # Set the width and height of the window

button_width = 20
button_height = 7

def back_button_mm_1 ():
    root.destroy()
    import main_view

# Create a frame to center the buttons
Frame = tk.Frame(root, bg="light blue")
Frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

font_style = ("Helvetica", 16)

# Add User Button
def open_user_add_form():
    root.destroy()
    import add_system_user  # Assuming user_add_form.py is in the same directory

def delete_system_user():
    import delete_system_user
    root.destroy()

def edit_system_user():
    import edit_system_user
    root.destroy()

# Add User Button
add_user_button = tk.Button(Frame, text="Add User", font=font_style, command=open_user_add_form, width=button_width, height=button_height)
add_user_button.pack(side=tk.LEFT, padx=10)

# Edit User Button
edit_user_button = tk.Button(Frame, text="Edit User", font=font_style, command=edit_system_user, width=button_width, height=button_height)
edit_user_button.pack(side=tk.LEFT, padx=10)

# Delete User Button
delete_user_button = tk.Button(Frame, text="View/Delete Users", font=font_style, command=delete_system_user, width=button_width, height=button_height)
delete_user_button.pack(side=tk.LEFT, padx=10)

# Back Button
back_button = tk.Button(root, text="Back", font=font_style, command=back_button_mm_1)
back_button.place(relx=1.0, rely=0.0, anchor='ne', x=-10, y=10)
back_button.pack(side=tk.LEFT, padx=10)

root.mainloop()