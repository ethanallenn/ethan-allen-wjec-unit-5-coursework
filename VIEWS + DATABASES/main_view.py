import tkinter as tk
from tkinter import ttk

def clear_frame(frame):
    for widget in frame.winfo_children():
        widget.destroy()

def logout():
    root.destroy()
    import login_view

def open_user_menu():
    import user_menu_view
    user_menu_view

def open_stock_menu():
    import stock_menu_view
    stock_menu_view

# Create the main window
root = tk.Tk()
root.title29("Calle Pharmacy Management System")
root.geometry("1400x720")
root.config(bg="#f0f0f0")
root.resizable(False, False)

# Create styles
style = ttk.Style()
style.theme_use('clam')
style.configure('Menu.TButton',
                padding=20,
                font=('Helvetica', 16),
                background='#4a90e2',
                foreground='white',
                width=25)
style.configure('Logout.TButton',
                padding=10,
                font=('Helvetica', 12),
                background='#f44336',
                foreground='white')

# Create main frame
main_frame = ttk.Frame(root)
main_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

# Title
title_label = ttk.Label(root,
                       text="Main Menu",
                       font=('Helvetica', 32, 'bold'),
                       background='#f0f0f0')
title_label.pack(pady=50)

# Menu buttons frame
button_frame = ttk.Frame(main_frame)
button_frame.pack(pady=20)

# User Menu Button
user_menu_btn = ttk.Button(button_frame,
                          text="User Management",
                          style='Menu.TButton',
                          command=open_user_menu)
user_menu_btn.pack(side=tk.LEFT, padx=20, pady=10)

# Stock Menu Button
stock_menu_btn = ttk.Button(button_frame,
                           text="Stock Management",
                           style='Menu.TButton',
                           command=open_stock_menu)
stock_menu_btn.pack(side=tk.LEFT, padx=20, pady=10)

# Logout Button
logout_btn = ttk.Button(root,
                       text="Logout",
                       style='Logout.TButton',
                       command=logout)
logout_btn.place(relx=0.95, rely=0.05, anchor='ne')

root.mainloop()