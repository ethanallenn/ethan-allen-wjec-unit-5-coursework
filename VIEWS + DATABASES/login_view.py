import tkinter as tk
import sqlite3
from tkinter import messagebox
from tkinter import *


def create_database():
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users
                 (username TEXT PRIMARY KEY, password TEXT, first_name TEXT, last_name TEXT, access_level TEXT)''')
    # Insert admin credentials if they don't exist
    c.execute("INSERT OR IGNORE INTO users (username, password, first_name, last_name, access_level) VALUES (?, ?, ?, ?, ?)", ('admin', 'password1', 'Admin', 'User', 'admin'))
    conn.commit()
    conn.close()

create_database()

def check_credentials():
    username = username_entry.get()
    password = password_entry.get()
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
    result = c.fetchone()
    conn.close()
    if result:
        root.destroy()  # Close the login window
        import main_view # Launch the other file
    else:
        messagebox.showerror("Login Failed", "Invalid credentials. Please try again.")

# Create the main window
root = tk.Tk()
root.title("Calle Pharmacy Login")
root.geometry("1280x720")
root.config(bg="white")
logo = PhotoImage(file='Logo.png')

# Configure grid to center widgets
for i in range(7):
    root.rowconfigure(i, weight=1)
    root.columnconfigure(0, weight=1)
    root.columnconfigure(1, weight=1)

# Create and place the username label and entry
username_label = tk.Label(root, text="Username:", bg="white", fg="black")
username_label.grid(row=2, column=0, padx=10, pady=10, sticky=tk.E)
username_entry = tk.Entry(root)
username_entry.grid(row=2, column=1, padx=10, pady=10, sticky=tk.W)

# Create and place the password label and entry
password_label = tk.Label(root, text="Password:", bg="white", fg="black")
password_label.grid(row=3, column=0, padx=10, pady=10, sticky=tk.E)
password_entry = tk.Entry(root, show="*")
password_entry.grid(row=3, column=1, padx=10, pady=10, sticky=tk.W)

# Create and place the login button
login_button = tk.Button(root, text="Login", command=check_credentials)
login_button.grid(row=4, column=0, columnspan=2, pady=20, padx=10, sticky=tk.N)

# Run the application

root.mainloop()
