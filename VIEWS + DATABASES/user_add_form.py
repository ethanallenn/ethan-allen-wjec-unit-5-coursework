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

# Tkinter setup
root = tk.Tk()
root.title("Add New User")

tk.Label(root, text="Username").grid(row=0, column=0)
entry_username = tk.Entry(root)
entry_username.grid(row=0, column=1)

tk.Label(root, text="Password").grid(row=1, column=0)
entry_password = tk.Entry(root, show="*")
entry_password.grid(row=1, column=1)

tk.Label(root, text="First Name").grid(row=2, column=0)
entry_first_name = tk.Entry(root)
entry_first_name.grid(row=2, column=1)

tk.Label(root, text="Last Name").grid(row=3, column=0)
entry_last_name = tk.Entry(root)
entry_last_name.grid(row=3, column=1)

tk.Label(root, text="Access Level").grid(row=4, column=0)
combo_access_level = ttk.Combobox(root, values=["Administrator", "Manager", "Pharmacist", "Team Member"])
combo_access_level.grid(row=4, column=1)

submit_button = tk.Button(root, text="Submit", command=add_user)
submit_button.grid(row=5, column=0, columnspan=2)

root.mainloop()
# Function to validate login
def validate_login():
    username = login_username.get()
    password = login_password.get()

    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute("SELECT access_level FROM users WHERE username=? AND password=?", (username, password))
    result = c.fetchone()
    conn.close()

    if result:
        access_level = result[0]
        if access_level in ["Administrator", "Manager"]:
            login_window.destroy()
            open_add_user_form()
        else:
            messagebox.showerror("Error", "Access denied")
    else:
        messagebox.showerror("Error", "Invalid credentials")

# Function to open the add user form
def open_add_user_form():
    global root
    root = tk.Tk()
    root.title("Add New User")

    tk.Label(root, text="Username").grid(row=0, column=0)
    global entry_username
    entry_username = tk.Entry(root)
    entry_username.grid(row=0, column=1)

    tk.Label(root, text="Password").grid(row=1, column=0)
    global entry_password
    entry_password = tk.Entry(root, show="*")
    entry_password.grid(row=1, column=1)

    tk.Label(root, text="First Name").grid(row=2, column=0)
    global entry_first_name
    entry_first_name = tk.Entry(root)
    entry_first_name.grid(row=2, column=1)

    tk.Label(root, text="Last Name").grid(row=3, column=0)
    global entry_last_name
    entry_last_name = tk.Entry(root)
    entry_last_name.grid(row=3, column=1)

    tk.Label(root, text="Access Level").grid(row=4, column=0)
    global combo_access_level
    combo_access_level = ttk.Combobox(root, values=["Administrator", "Manager", "Pharmacist", "Team Member", "test_user"])
    combo_access_level.grid(row=4, column=1)

    submit_button = tk.Button(root, text="Submit", command=add_user)
    submit_button.grid(row=5, column=0, columnspan=2)

    root.mainloop()

# Login window setup 

login_window = tk.Tk()
login_window.withdraw()  # Hide the login window initially

def validate_login():
    username = login_username.get()
    password = login_password.get()

    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute("SELECT access_level FROM users WHERE username=? AND password=?", (username, password))
    result = c.fetchone()
    conn.close()

    if result:
        access_level = result[0]
        if access_level in ["Administrator", "Manager"]:
            login_window.destroy()
            open_add_user_form()
        else:
            messagebox.showerror("Error", "Access denied")
    else:
        messagebox.showerror("Error", "Invalid credentials")

def show_login_window():
    login_window.deiconify()  # Show the login window

login_window.title("Login")
login_window.geometry("400x400")

infoLabel = tk.Label(login_window, text="Please login with the credentials in which you have just created.")
infoLabel.grid(row=0, column=0, columnspan=3)

tk.Label(login_window, text="Username").grid(row=1, column=0)
login_username = tk.Entry(login_window)
login_username.grid(row=1, column=1)

tk.Label(login_window, text="Password").grid(row=2, column=0)
login_password = tk.Entry(login_window, show="*")
login_password.grid(row=2, column=1)

login_button = tk.Button(login_window, text="Login", command=validate_login)
login_button.grid(row=3, column=0, columnspan=2)

def open_main_view():
    login_window.destroy()
    os.system('python main_view.py')

login_button = tk.Button(login_window, text="Login", command=lambda: [validate_login()])
login_button.grid(row=3, column=0, columnspan=2)
login_window.title("Login")
login_window.geometry("400x400")

infoLabel = tk.Label(login_window, text="Please login with the credentials in which you have just created.")
infoLabel.grid(row=0, column=0, columnspan=3)

tk.Label(login_window, text="Username").grid(row=1, column=0)
login_username = tk.Entry(login_window)
login_username.grid(row=1, column=1)

tk.Label(login_window, text="Password").grid(row=2, column=0)
login_password = tk.Entry(login_window, show="*")
login_password.grid(row=2, column=1)

login_button = tk.Button(login_window, text="Login", command=validate_login)
login_button.grid(row=3, column=0, columnspan=2)

def open_main_view():
    login_window.destroy()
    os.system('python main_view.py')

login_button = tk.Button(login_window, text="Login", command=lambda: [validate_login()])
login_button.grid(row=3, column=0, columnspan=2)
login_window.mainloop()