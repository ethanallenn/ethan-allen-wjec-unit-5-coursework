import tkinter as tk
from tkinter import messagebox
import sqlite3
from tkinter import ttk
import os

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

def exit_program():
    root.destroy()

def check_credentials():
    username = username_entry.get()
    password = password_entry.get()
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
    result = c.fetchone()
    conn.close()
    if result:
        root.destroy()
        import main_view
    else:
        messagebox.showerror("Login Failed", "Invalid credentials. Please try again.")

# Create the main window
root = tk.Tk()
root.title("Calle Pharmacy Login")
root.geometry("1280x720")
root.config(bg="#f0f0f0")  # Light gray background
root.resizable(True, True)

# Create main frame as a container for logo and login
main_frame = tk.Frame(root, bg="#f0f0f0")
main_frame.place(relx=0.5, rely=0.5, anchor="center")

# Create a horizontal container frame
container_frame = tk.Frame(main_frame, bg="#f0f0f0")
container_frame.pack()

# Load and display the logo image on the left
script_dir = os.path.dirname(os.path.abspath(__file__))
logo_path = os.path.join(script_dir, "Logo_new.png")
logo_image = tk.PhotoImage(file=logo_path)
# Resize logo to fit nicely
logo_image = logo_image.subsample(2, 2)  # Adjust subsample values as needed
logo_label = tk.Label(container_frame, image=logo_image, bg="#f0f0f0")
logo_label.pack(side="left", padx=(0, 40))

# Create login frame on the right
login_frame = tk.Frame(container_frame, bg="white", padx=40, pady=40)
login_frame.pack(side="left", pady=20)

# Add shadow effect
shadow_frame = tk.Frame(container_frame, bg="#d0d0d0")
shadow_frame.place(in_=login_frame, x=5, y=5, relwidth=1, relheight=1)
login_frame.lift()

# Login header
header_label = tk.Label(login_frame, text="Login", font=("Helvetica", 24, "bold"), bg="white", fg="#333333")
header_label.pack(pady=(0, 20))

# Style for entry fields
style = ttk.Style()
style.configure("Custom.TEntry", padding=10)

# Username entry
username_frame = tk.Frame(login_frame, bg="white")
username_frame.pack(fill="x", pady=10)
username_label = tk.Label(username_frame, text="Username", font=("Helvetica", 12), bg="white", fg="#666666")
username_label.pack(anchor="w")
username_entry = ttk.Entry(username_frame, font=("Helvetica", 12), style="Custom.TEntry", width=30)
username_entry.pack(fill="x", pady=(5, 0))

# Password entry
password_frame = tk.Frame(login_frame, bg="white")
password_frame.pack(fill="x", pady=10)
password_label = tk.Label(password_frame, text="Password", font=("Helvetica", 12), bg="white", fg="#666666")
password_label.pack(anchor="w")
password_entry = ttk.Entry(password_frame, font=("Helvetica", 12), show="•", style="Custom.TEntry", width=30)
password_entry.pack(fill="x", pady=(5, 0))

# Button style
button_style = {
    "font": ("Helvetica", 12),
    "borderwidth": 0,
    "padx": 20,
    "pady": 10,
    "cursor": "hand2"
}

# Login button
login_button = tk.Button(login_frame, text="Login", bg="#4CAF50", fg="black",
                        activebackground="#45a049", **button_style,
                        command=check_credentials)
login_button.pack(pady=(20, 10), fill="x")

# Exit button
exit_button = tk.Button(login_frame, text="Exit", bg="#f44336", fg="black",
                       activebackground="#da190b", **button_style,
                       command=exit_program)
exit_button.pack(fill="x")

# Bind Enter key to login
root.bind('<Return>', lambda event: check_credentials())

# Run the application
root.mainloop()
