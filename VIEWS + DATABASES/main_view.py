import tkinter as tk
from tkinter import ttk
import os

# Create the main window
root = tk.Tk()
root.title("Calle Pharmacy - Main Menu")
root.geometry("1280x720")
root.config(bg="#f0f0f0")
root.resizable(True, True)

# Create main frame as a container
main_frame = tk.Frame(root, bg="#f0f0f0")
main_frame.place(relx=0.5, rely=0.5, anchor="center")

# Create a horizontal container frame
container_frame = tk.Frame(main_frame, bg="#f0f0f0")
container_frame.pack()

# Load and display the logo image
script_dir = os.path.dirname(os.path.abspath(__file__))
logo_path = os.path.join(script_dir, "Logo_new.png")
logo_image = tk.PhotoImage(file=logo_path)
logo_image = logo_image.subsample(2, 2)  # Resize logo
logo_label = tk.Label(container_frame, image=logo_image, bg="#f0f0f0")
logo_label.pack(pady=20)

# Create menu frame
menu_frame = tk.Frame(container_frame, bg="white", padx=40, pady=40)
menu_frame.pack(pady=20)

# Add shadow effect
shadow_frame = tk.Frame(container_frame, bg="#d0d0d0")
shadow_frame.place(in_=menu_frame, x=5, y=5, relwidth=1, relheight=1)
menu_frame.lift()

# Welcome header
header_label = tk.Label(menu_frame, text="Main Menu", font=("Helvetica", 24, "bold"), bg="white", fg="#333333")
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

def open_staff_menu():
    import user_menu_view
    pass

def logout():
    root.destroy()
    import login_view

# Staff Management button
staff_button = tk.Button(menu_frame, text="Staff Management", bg="#2ecc71", fg="white",
                        activebackground="#27ae60", activeforeground="white",
                        command=open_staff_menu, **button_style)
staff_button.pack(pady=(20, 10), fill="x")

# Logout button
logout_button = tk.Button(menu_frame, text="Logout", bg="#3498db", fg="white",
                         activebackground="#2980b9", activeforeground="white",
                         command=logout, **button_style)
logout_button.pack(fill="x")

# Run the application
root.mainloop()
