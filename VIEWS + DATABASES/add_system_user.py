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

# Create the main window
root = tk.Tk()
root.title("Calle Pharmacy - Add Staff Member")
root.geometry("1280x720")
root.config(bg="#f0f0f0")
root.resizable(True, True)

# Create main frame as a container
main_frame = tk.Frame(root, bg="#f0f0f0")
main_frame.place(relx=0.5, rely=0.5, anchor="center")

# Create a horizontal container frame
container_frame = tk.Frame(main_frame, bg="#f0f0f0")
container_frame.pack()

# Create form frame
form_frame = tk.Frame(container_frame, bg="white", padx=40, pady=40)
form_frame.pack(pady=20)

# Add shadow effect
shadow_frame = tk.Frame(container_frame, bg="#d0d0d0")
shadow_frame.place(in_=form_frame, x=5, y=5, relwidth=1, relheight=1)
form_frame.lift()

# Add Staff header
header_label = tk.Label(form_frame, text="Add Staff Member", font=("Helvetica", 24, "bold"), bg="white", fg="#333333")
header_label.pack(pady=(0, 20))

# Function to add user to the database
def add_user():
    username = username_entry.get()
    password = password_entry.get()
    first_name = first_name_entry.get()
    last_name = last_name_entry.get()
    access_level = access_level_combo.get()

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
        root.destroy()
        import user_menu_view
    except sqlite3.IntegrityError:
        messagebox.showerror("Error", "Username already exists")
    finally:
        conn.close()

def back_to_menu():
    root.destroy()
    import user_menu_view

# Create entry fields with consistent styling
entry_style = {"bg": "white", "fg": "#333333", "font": ("Helvetica", 12), "width": 30}
label_style = {"bg": "white", "fg": "#666666", "font": ("Helvetica", 12)}

# Username
username_frame = tk.Frame(form_frame, bg="white")
username_frame.pack(fill="x", pady=10)
username_label = tk.Label(username_frame, text="Username", **label_style)
username_label.pack(anchor="w")
username_entry = tk.Entry(username_frame, **entry_style)
username_entry.pack(fill="x", pady=(5, 0))

# Password
password_frame = tk.Frame(form_frame, bg="white")
password_frame.pack(fill="x", pady=10)
password_label = tk.Label(password_frame, text="Password", **label_style)
password_label.pack(anchor="w")
password_entry = tk.Entry(password_frame, show="•", **entry_style)
password_entry.pack(fill="x", pady=(5, 0))

# First Name
first_name_frame = tk.Frame(form_frame, bg="white")
first_name_frame.pack(fill="x", pady=10)
first_name_label = tk.Label(first_name_frame, text="First Name", **label_style)
first_name_label.pack(anchor="w")
first_name_entry = tk.Entry(first_name_frame, **entry_style)
first_name_entry.pack(fill="x", pady=(5, 0))

# Last Name
last_name_frame = tk.Frame(form_frame, bg="white")
last_name_frame.pack(fill="x", pady=10)
last_name_label = tk.Label(last_name_frame, text="Last Name", **label_style)
last_name_label.pack(anchor="w")
last_name_entry = tk.Entry(last_name_frame, **entry_style)
last_name_entry.pack(fill="x", pady=(5, 0))

# Access Level
access_level_frame = tk.Frame(form_frame, bg="white")
access_level_frame.pack(fill="x", pady=10)
access_level_label = tk.Label(access_level_frame, text="Access Level", **label_style)
access_level_label.pack(anchor="w")
access_level_combo = ttk.Combobox(access_level_frame, 
                                 values=["Administrator", "Manager", "Pharmacist", "Team Member"],
                                 font=("Helvetica", 12),
                                 state='readonly',
                                 width=29)
access_level_combo.pack(fill="x", pady=(5, 0))
access_level_combo.set("Select Access Level")

# Button style
button_style = {
    "font": ("Helvetica", 12),
    "borderwidth": 0,
    "padx": 20,
    "pady": 10,
    "cursor": "hand2",
    "width": 15
}

# Buttons frame
button_frame = tk.Frame(form_frame, bg="white")
button_frame.pack(pady=(20, 0))

# Submit button
submit_button = tk.Button(button_frame, text="Add Staff", bg="#2ecc71", fg="white",
                         activebackground="#27ae60", activeforeground="white",
                         command=add_user, **button_style)
submit_button.pack(side=tk.LEFT, padx=5)

# Back button
back_button = tk.Button(button_frame, text="Back", bg="#95a5a6", fg="white",
                       activebackground="#7f8c8d", activeforeground="white",
                       command=back_to_menu, **button_style)
back_button.pack(side=tk.LEFT, padx=5)

# Run the application
root.mainloop()
