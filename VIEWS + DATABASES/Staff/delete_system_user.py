import tkinter as tk
from tkinter import messagebox, ttk
import sqlite3
import main_view

def open_delete_user_window(main_view_window):
    root = tk.Tk()
    root.title("User Management")
    root.geometry("1400x720")
    root.config(bg="#f0f0f0")
    root.resizable(False, False)

    # Create a style for ttk widgets
    style = ttk.Style()
    style.theme_use('clam')
    style.configure('TFrame', background='#f0f0f0')
    style.configure('TButton', 
                    padding=10,
                    font=('Helvetica', 12),
                    background='#4a90e2',
                    foreground='white')
    style.configure('TLabel',
                    font=('Helvetica', 12),
                    background='#f0f0f0')

    users = fetch_users()

    main_frame = ttk.Frame(root)
    main_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    # Title
    title_label = ttk.Label(main_frame, 
                           text="User Management",
                           font=('Helvetica', 24, 'bold'))
    title_label.pack(pady=(0, 30))

    # Create scrollable frame for users
    canvas = tk.Canvas(main_frame, bg='#f0f0f0', highlightthickness=0)
    scrollbar = ttk.Scrollbar(main_frame, orient="vertical", command=canvas.yview)
    scrollable_frame = ttk.Frame(canvas)

    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
    )

    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    for user in users:
        first_name, last_name, access_level = user
        user_frame = ttk.Frame(scrollable_frame)
        user_frame.pack(pady=10, padx=20, fill="x")

        user_info = f"{first_name} {last_name} - Access Level: {access_level}"
        user_label = ttk.Label(user_frame, 
                              text=user_info,
                              font=('Helvetica', 12))
        user_label.pack(side="left", padx=(0, 20))

        delete_button = ttk.Button(user_frame, 
                                 text="Delete",
                                 command=lambda uname=f"{first_name} {last_name}": delete_user(uname, main_view_window, root))
        delete_button.pack(side="right")

    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    button_frame = ttk.Frame(root)
    button_frame.pack(side="bottom", pady=20)

    menu_button = ttk.Button(button_frame,
                            text="Back to Main Menu",
                            command=lambda: [root.destroy(), main_view.main()])
    menu_button.pack(side="left", padx=10)

    exit_button = ttk.Button(button_frame,
                            text="Exit",
                            command=root.quit)
    exit_button.pack(side="left", padx=10)

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