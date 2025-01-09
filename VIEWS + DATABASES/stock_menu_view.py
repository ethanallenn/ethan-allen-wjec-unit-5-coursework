import tkinter as tk
from tkinter import ttk

def logout_button():
    root.destroy()
    import login_view

def open_add_stock():
    root.destroy()
    import add_system_stock

# Create the main window
root = tk.Tk()
root.title("Stock Management")
root.geometry("1400x720")
root.config(bg="#1e1e1e")  # Dark background
root.resizable(False, False)

# Create styles
style = ttk.Style()
style.theme_use('clam')
style.configure('Menu.TButton',
                padding=20,
                font=('Roboto', 16),
                background='#2196F3',  # Material blue
                foreground='white',
                width=25)
style.configure('Logout.TButton',
                padding=10,
                font=('Roboto', 12),
                background='#f44336',  # Material red
                foreground='white')
style.configure('Title.TLabel',
                font=('Roboto', 32, 'bold'),
                background='#1e1e1e',
                foreground='white')

# Create main frame with shadow effect
main_frame = ttk.Frame(root, style='Card.TFrame')
main_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

style.configure('Card.TFrame',
                background='#2d2d2d',  # Slightly lighter than background
                relief='solid',
                borderwidth=1)

# Title with modern font
title_label = ttk.Label(root,
                       text="Stock Management",
                       style='Title.TLabel')
title_label.pack(pady=50)

# Add Stock Button with hover effect
add_stock_btn = ttk.Button(main_frame,
                          text="Add Stock",
                          style='Menu.TButton',
                          command=open_add_stock)
add_stock_btn.pack(pady=20)

# Logout Button with hover effect
logout_btn = ttk.Button(root,
                       text="Logout",
                       style='Logout.TButton',
                       command=logout_button)
logout_btn.pack(anchor='ne', padx=20, pady=20)

# Add hover effects
def on_enter(e):
    e.widget.configure(style='Menu.TButton.Hover')
def on_leave(e):
    e.widget.configure(style='Menu.TButton')

style.configure('Menu.TButton.Hover',
                background='#1976D2')  # Darker blue on hover

add_stock_btn.bind('<Enter>', on_enter)
add_stock_btn.bind('<Leave>', on_leave)

root.mainloop()
