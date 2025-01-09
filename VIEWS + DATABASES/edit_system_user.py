import tkinter as tk
from tkinter import messagebox, ttk
import sqlite3

def fetch_users():
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute("SELECT username FROM users")
    users = cursor.fetchall()
    conn.close()
    return users

def update_user(new_username, new_password, old_username):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute("UPDATE users SET username = ?, password = ? WHERE username = ?", (new_username, new_password, old_username))
    conn.commit()
    conn.close()

def authenticate_admin(username, password):
    return username == "admin-update" and password == "admin-update*"

def apply_changes(new_username, new_password, old_username):
    def on_authenticate():
        admin_username = admin_username_entry.get()
        admin_password = admin_password_entry.get()
        if authenticate_admin(admin_username, admin_password):
            update_user(new_username, new_password, old_username)
            messagebox.showinfo("Success", "User details updated successfully")
            auth_popup.destroy()
            root.destroy()
            main()
        else:
            messagebox.showerror("Error", "Invalid admin credentials")

    auth_popup = tk.Toplevel(root)
    auth_popup.title("Admin Authentication")
    auth_popup.geometry("400x300")
    auth_popup.config(bg="#f0f0f0")
    
    style = ttk.Style()
    style.configure('Auth.TLabel', font=('Helvetica', 12), background='#f0f0f0')
    style.configure('Auth.TEntry', font=('Helvetica', 12), padding=5)
    style.configure('Auth.TButton', font=('Helvetica', 12), padding=10, background='#4a90e2')

    frame = ttk.Frame(auth_popup, style='Auth.TFrame')
    frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    ttk.Label(frame, text="Admin Username:", style='Auth.TLabel').pack(pady=5)
    admin_username_entry = ttk.Entry(frame, style='Auth.TEntry')
    admin_username_entry.pack(pady=5)
    
    ttk.Label(frame, text="Admin Password:", style='Auth.TLabel').pack(pady=5)
    admin_password_entry = ttk.Entry(frame, show="*", style='Auth.TEntry')
    admin_password_entry.pack(pady=5)
    
    ttk.Button(frame, text="Authenticate", command=on_authenticate, style='Auth.TButton').pack(pady=20)

def edit_user(username):
    edit_popup = tk.Toplevel(root)
    edit_popup.title("Edit User")
    edit_popup.geometry("400x300")
    edit_popup.config(bg="#f0f0f0")

    style = ttk.Style()
    style.configure('Edit.TLabel', font=('Helvetica', 12), background='#f0f0f0')
    style.configure('Edit.TEntry', font=('Helvetica', 12), padding=5)
    style.configure('Edit.TButton', font=('Helvetica', 12), padding=10, background='#4a90e2')

    frame = ttk.Frame(edit_popup)
    frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    ttk.Label(frame, text="New Username:", style='Edit.TLabel').pack(pady=5)
    new_username_entry = ttk.Entry(frame, style='Edit.TEntry')
    new_username_entry.insert(0, username)
    new_username_entry.pack(pady=5)

    ttk.Label(frame, text="New Password:", style='Edit.TLabel').pack(pady=5)
    new_password_entry = ttk.Entry(frame, show="*", style='Edit.TEntry')
    new_password_entry.pack(pady=5)

    ttk.Button(frame, text="Apply Changes", 
              command=lambda: apply_changes(new_username_entry.get(), new_password_entry.get(), username),
              style='Edit.TButton').pack(pady=20)

def main():
    global root
    root = tk.Tk()
    root.title("User Management")
    root.geometry("800x600")
    root.config(bg="#f0f0f0")

    style = ttk.Style()
    style.theme_use('clam')
    style.configure('Main.TFrame', background='#f0f0f0')
    style.configure('Main.TLabel', font=('Helvetica', 12), background='#f0f0f0')
    style.configure('Main.TButton', font=('Helvetica', 12), padding=10, background='#4a90e2')

    main_frame = ttk.Frame(root, style='Main.TFrame')
    main_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    title_label = ttk.Label(main_frame, text="User Management", 
                           font=('Helvetica', 24, 'bold'),
                           background='#f0f0f0')
    title_label.pack(pady=(0, 30))

    users = fetch_users()
    for username in users:
        frame = ttk.Frame(main_frame)
        frame.pack(fill="x", pady=5)
        ttk.Label(frame, text=username[0], style='Main.TLabel').pack(side="left", padx=10)
        ttk.Button(frame, text="Edit", 
                  command=lambda uname=username[0]: edit_user(uname),
                  style='Main.TButton').pack(side="right", padx=10)

    root.mainloop()

if __name__ == "__main__":
    main()
