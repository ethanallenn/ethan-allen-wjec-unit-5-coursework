import tkinter as tk
from tkinter import messagebox
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
    auth_popup.geometry("200x200")
    tk.Label(auth_popup, text="Admin Username:").pack()
    admin_username_entry = tk.Entry(auth_popup)
    admin_username_entry.pack()
    tk.Label(auth_popup, text="Admin Password:").pack()
    admin_password_entry = tk.Entry(auth_popup, show="*")
    admin_password_entry.pack()
    tk.Button(auth_popup, text="Authenticate", command=on_authenticate).pack()

def edit_user(username):
    edit_popup = tk.Toplevel(root)
    edit_popup.title("Edit User")
    edit_popup.geometry("200x200")

    tk.Label(edit_popup, text="New Username:").pack()
    new_username_entry = tk.Entry(edit_popup)
    new_username_entry.insert(0, username)
    new_username_entry.pack()

    tk.Label(edit_popup, text="New Password:").pack()
    new_password_entry = tk.Entry(edit_popup, show="*")
    new_password_entry.pack()

    tk.Button(edit_popup, text="Apply Changes", command=lambda: apply_changes(new_username_entry.get(), new_password_entry.get(), username)).pack()

def main():
    global root
    root = tk.Tk()
    root.title("User Editor")
    root.geometry("200x200")

    users = fetch_users()
    for username in users:
        frame = tk.Frame(root)
        frame.pack(fill="x")
        tk.Label(frame, text=username).pack(side="left")
        tk.Button(frame, text="Edit", command=lambda uname=username[0]: edit_user(uname)).pack(side="right")

    root.mainloop()

if __name__ == "__main__":
    main()
