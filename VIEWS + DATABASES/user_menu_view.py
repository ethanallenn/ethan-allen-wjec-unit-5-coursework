import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import os

# Create the main window
root = tk.Tk()
root.title("Calle Pharmacy - Staff Management")
root.geometry("1280x720")
root.config(bg="#f0f0f0")
root.resizable(True, True)

# Create main frame as a container
main_frame = tk.Frame(root, bg="#f0f0f0")
main_frame.place(relx=0.5, rely=0.5, anchor="center")

# Add logout button to top left
logout_button = tk.Button(root, text="Logout", bg="#3498db", fg="white",
                         activebackground="#2980b9", activeforeground="white",
                         font=("Helvetica", 10),
                         borderwidth=0,
                         padx=15,
                         pady=5,
                         cursor="hand2",
                         command=lambda: [root.destroy(), __import__('VIEWS + DATABASES.login_view.py')])
logout_button.place(x=20, y=20)

# Create a horizontal container frame
container_frame = tk.Frame(main_frame, bg="#f0f0f0")
container_frame.pack()



# Create menu frame
menu_frame = tk.Frame(container_frame, bg="white", padx=40, pady=40)
menu_frame.pack(pady=20)

# Add shadow effect
shadow_frame = tk.Frame(container_frame, bg="#d0d0d0")
shadow_frame.place(in_=menu_frame, x=5, y=5, relwidth=1, relheight=1)
menu_frame.lift()

# Staff Management header
header_label = tk.Label(menu_frame, text="Staff Management", font=("Helvetica", 24, "bold"), bg="white", fg="#333333")
header_label.pack(pady=(0, 20))

# Button style
button_style = {
    "font": ("Helvetica", 12),
    "borderwidth": 0,
    "padx": 20,
    "pady": 10,
    "cursor": "hand2",
    "width": 20
}

def add_staff():
    import add_system_user
    pass

def search_staff():
    messagebox.showinfo("Search Staff", "This feature is not available yet.")
    pass

def back_to_main():
    root.destroy()
    import main_view

# Add Staff button
add_button = tk.Button(menu_frame, text="Add Staff Member", bg="#2ecc71", fg="white",
                      activebackground="#27ae60", activeforeground="white",
                      command=add_staff, **button_style)
add_button.pack(pady=(20, 10), fill="x")

# Search Staff button
search_button = tk.Button(menu_frame, text="Manage Staff Member", bg="#3498db", fg="white",
                         activebackground="#2980b9", activeforeground="white",
                         command=search_staff, **button_style)
search_button.pack(pady=10, fill="x")

# Back to Main Menu button
back_button = tk.Button(menu_frame, text="Back to Main Menu", bg="#95a5a6", fg="white",
                       activebackground="#7f8c8d", activeforeground="white",
                       command=back_to_main, **button_style)
back_button.pack(pady=10, fill="x")

# Run the application
root.mainloop()
