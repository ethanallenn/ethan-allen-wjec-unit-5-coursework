import tkinter as tk
from tkinter import messagebox
import sqlite3
import main_view

def open_delete_user_window(main_view_window):
    root = tk.Tk()
    root.title("User Management")
    root.geometry("1280x720")
    root.config(bg="light blue")
    root.resizable(False, False)

    users = fetch_users()

    frame = tk.Frame(root, bg="light blue")
    frame.pack(expand=True)

    for user in users:
        first_name, last_name, access_level = user
        user_info = f"{first_name} {last_name} - Access Level: {access_level}"
        user_label = tk.Label(frame, text=user_info, font=("Helvetica", 18), bg="light blue")
        user_label.pack(pady=10)

        delete_button = tk.Button(frame, text="Delete", font=("Helvetica", 18), command=lambda uname=f"{first_name} {last_name}": delete_user(uname, main_view_window, root))
        delete_button.pack(pady=10)

    menu_button = tk.Button(root, text="Back to Main Menu", font=("Helvetica", 18), command=lambda: [root.destroy(), main_view.main()])
    menu_button.pack(side="bottom", pady=20)

    exit_button = tk.Button(root, text="Exit", font=("Helvetica", 18), command=root.quit)
    exit_button.pack(side="bottom", pady=20)

    root.mainloop()

def delete_user(username, main_view_window, root):
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

    main_view_window.destroy()

def fetch_users():
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute("SELECT first_name, last_name, access_level FROM users")
    users = cursor.fetchall()
    conn.close()
    return users


# Assuming main_view.main() creates the main_view window and returns it
main_view_window = main_view
open_delete_user_window(main_view_window)