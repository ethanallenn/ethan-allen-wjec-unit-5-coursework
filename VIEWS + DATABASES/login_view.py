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
root.config(bg="light blue")
root.resizable(False, False)

# Configure grid to center widgets
for i in range(7):
    root.rowconfigure(i, weight=1)
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.columnconfigure(2, weight=1)

# Load and display the logo image
logo_image = tk.PhotoImage(file="c:/Users/ethan/OneDrive - C2k/Year 14_24_25/Computer Science/A2 - Coursework/SoftwareDevelopment/ethan-allen-wjec-unit-5-coursework/VIEWS + DATABASES/Logo_new.png")
logo_label = tk.Label(root, image=logo_image, bg="light blue")
logo_label.grid(row=0, column=0, rowspan=7, pady=20, padx=20, sticky=tk.NS)

font_style = ("Helvetica", 16)

text_label = tk.Label(root, text="Login", bg="light blue", fg="black", font=("Helvetica", 16, "bold"))
text_label.grid(row=1, column=1, columnspan=2, pady=10, sticky=tk.EW)

# Create and place the username label and entry
username_label = tk.Label(root, text="Username:", font=font_style, bg="light blue", fg="black")
username_label.grid(row=2, column=1, padx=10, pady=2, sticky=tk.E)
username_entry = tk.Entry(root, font=font_style)
username_entry.grid(row=2, column=2, padx=10, pady=2, sticky=tk.W)

# Create and place the password label and entry
password_label = tk.Label(root, text="Password:", font=font_style, bg="light blue", fg="black")
password_label.grid(row=3, column=1, padx=10, pady=2, sticky=tk.E)
password_entry = tk.Entry(root, show="*", font=font_style)
password_entry.grid(row=3, column=2, padx=10, pady=2, sticky=tk.W)

# Create and place the login button
login_button = tk.Button(root, text="Login", command=check_credentials, font=font_style)
login_button.grid(row=4, column=1, columnspan=2, pady=20, padx=10, sticky=tk.N)

# Run the application
root.mainloop()
