import tkinter as tk
from tkinter import messagebox
import sqlite3
import main_view

def delete_user(username):
    def confirm_delete():
        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()
        cursor.execute("DELETE FROM users WHERE first_name || ' ' || last_name=?", (username,))
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", f"User {username} deleted successfully.")
        root.destroy()

    if messagebox.askyesno("Confirm Delete", f"Are you sure you want to delete {username}?"):
        confirm_delete()
    else:
        root.destroy()

def fetch_users():
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute("SELECT first_name, last_name, access_level FROM users")
    users = cursor.fetchall()
    conn.close()
    return users

root = tk.Tk()
root.title("User Management")

users = fetch_users()

for user in users:
    first_name, last_name, access_level = user
    user_info = f"{first_name} {last_name} - Access Level: {access_level}"
    user_label = tk.Label(root, text=user_info)
    user_label.pack()

    delete_button = tk.Button(root, text="Delete", command=lambda uname=f"{first_name} {last_name}": delete_user(uname))
    delete_button.pack()

root.mainloop()
