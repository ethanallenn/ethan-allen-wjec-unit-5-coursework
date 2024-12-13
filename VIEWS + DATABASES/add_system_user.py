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
root.geometry("1280x720")
root.config(bg="light blue")
root.resizable(False, False)

font_style = ("Helvetica", 16)

tk.Label(root, text="Add New User:", font=("Helvetica", 20, "bold"), bg="light blue").grid(row=0, column=0, columnspan=2, pady=10)

tk.Label(root, text="Username:", font=font_style, bg="light blue").grid(row=1, column=0, padx=10, pady=5, sticky="e")
entry_username = tk.Entry(root, font=font_style)
entry_username.grid(row=1, column=1, padx=10, pady=5, sticky="w")

tk.Label(root, text="Password:", font=font_style, bg="light blue").grid(row=2, column=0, padx=10, pady=5, sticky="e")
entry_password = tk.Entry(root, show="*", font=font_style)
entry_password.grid(row=2, column=1, padx=10, pady=5, sticky="w")

tk.Label(root, text="First Name", font=font_style, bg="light blue").grid(row=3, column=0, padx=10, pady=5, sticky="e")
entry_first_name = tk.Entry(root, font=font_style)
entry_first_name.grid(row=3, column=1, padx=10, pady=5, sticky="w")

tk.Label(root, text="Last Name", font=font_style, bg="light blue").grid(row=4, column=0, padx=10, pady=5, sticky="e")
entry_last_name = tk.Entry(root, font=font_style)
entry_last_name.grid(row=4, column=1, padx=10, pady=5, sticky="w")

tk.Label(root, text="Access Level", font=font_style, bg="light blue").grid(row=5, column=0, padx=10, pady=5, sticky="e")
combo_access_level = ttk.Combobox(root, values=["Administrator", "Manager", "Pharmacist", "Team Member"], font=font_style)
combo_access_level.grid(row=5, column=1, padx=10, pady=5, sticky="w")

submit_button = tk.Button(root, text="Submit", command=add_user, font=font_style)
submit_button.grid(row=6, column=0, columnspan=2, pady=20)

back_button = tk.Button(root, text="Back", command=mv_open, font=font_style)
back_button.grid(row=7, column=0, columnspan=2, pady=20)

root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)
root.grid_rowconfigure(2, weight=1)
root.grid_rowconfigure(3, weight=1)
root.grid_rowconfigure(4, weight=1)
root.grid_rowconfigure(5, weight=1)
root.grid_rowconfigure(6, weight=1)

root.mainloop()
