import tkinter as tk
from tkinter import messagebox, ttk
import sqlite3
import os

# Database setup
conn = sqlite3.connect('users.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS users
             (username TEXT PRIMARY KEY, password TEXT, first_name TEXT, last_name TEXT, access_level TEXT)''')
conn.commit()
conn.close()

# Function to add user to the database
def add_user():
    username = entry_username.get()
    password = entry_password.get()
    first_name = entry_first_name.get()
    last_name = entry_last_name.get()
    access_level = combo_access_level.get()

    if not username or not password or not first_name or not last_name or not access_level:
        messagebox.showerror("Error", "All fields are required")
        return

    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    try:
        c.execute("INSERT INTO users (username, password, first_name, last_name, access_level) VALUES (?, ?, ?, ?, ?)",
                  (username, password, first_name, last_name, access_level))
        conn.commit()
        messagebox.showinfo("Success", "User added successfully")
        root.destroy()  # Close the current window
        os.system('python login_view.py')  # Open the login_view.py window
    except sqlite3.IntegrityError:
        messagebox.showerror("Error", "Username already exists")
    finally:
        conn.close()

def mv_open() -> None:
    root.destroy()
    import main_view

# Tkinter setup
root = tk.Tk()
root.title("Add New User")
root.geometry("1400x720")
root.config(bg="#f0f0f0")
root.resizable(False, False)

# Create a style for ttk widgets
style = ttk.Style()
style.theme_use('clam')
style.configure('TFrame', background='#f0f0f0')
style.configure('TButton', 
                padding=10,
                font=('Helvetica', 12),
                background='#4a90e2',
                foreground='white')
style.configure('TEntry',
                padding=5,
                font=('Helvetica', 12))
style.configure('TLabel',
                font=('Helvetica', 12),
                background='#f0f0f0')

# Create main frame
main_frame = ttk.Frame(root)
main_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

# Title
title_label = ttk.Label(main_frame, 
                        text="Add New User",
                        font=('Helvetica', 20, 'bold'),
                        background='#f0f0f0')
title_label.grid(row=0, column=0, columnspan=2, pady=(0, 30))

# Form fields
fields = [
    ("Username:", "entry_username"),
    ("Password:", "entry_password", "*"),
    ("First Name:", "entry_first_name"),
    ("Last Name:", "entry_last_name"),
    ("Access Level:", "combo_access_level")
]

for i, field in enumerate(fields):
    label = ttk.Label(main_frame, text=field[0])
    label.grid(row=i+1, column=0, padx=15, pady=10, sticky='e')
    
    if field[0] == "Access Level:":
        combo_access_level = ttk.Combobox(main_frame, 
                                         values=["Administrator", "Manager", "Pharmacist", "Team Member"],
                                         font=('Helvetica', 12),
                                         state='readonly')
        combo_access_level.grid(row=i+1, column=1, padx=15, pady=10, sticky='w')
        combo_access_level.set("Select Access Level")
    else:
        if len(field) == 3:  # Password field
            globals()[field[1]] = ttk.Entry(main_frame, show=field[2], font=('Helvetica', 12))
        else:
            globals()[field[1]] = ttk.Entry(main_frame, font=('Helvetica', 12))
        globals()[field[1]].grid(row=i+1, column=1, padx=15, pady=10, sticky='w')

# Buttons
button_frame = ttk.Frame(main_frame)
button_frame.grid(row=6, column=0, columnspan=2, pady=30)

submit_button = ttk.Button(button_frame, text="Submit", command=add_user, style='TButton')
submit_button.pack(side=tk.LEFT, padx=10)

back_button = ttk.Button(button_frame, text="Back", command=mv_open, style='TButton')
back_button.pack(side=tk.LEFT, padx=10)

root.mainloop()
