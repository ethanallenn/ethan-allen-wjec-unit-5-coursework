import tkinter as tk
from tkinter import ttk

def back_button_mm_1():
    root.destroy()
    import main_view

def open_user_add_form():
    root.destroy()
    import add_system_user

def delete_system_user():
    root.destroy()
    import delete_system_user

def edit_system_user():
    root.destroy()
    import edit_system_user

# Create the main window with modern dark theme
root = tk.Tk()
root.title("User Management")
root.geometry("1400x720")
root.config(bg="#1A1A1A")  # Darker background for modern look
root.resizable(False, False)

# Configure modern styles
style = ttk.Style()
style.theme_use('clam')

# Modern button styles with material design colors
style.configure('Menu.TButton',
                padding=20,
                font=('Segoe UI', 16),
                background='#2196F3',  # Material Blue
                foreground='white',
                width=25,
                relief='flat',
                borderwidth=0)

style.configure('Menu.TButton.Hover',
                background='#1976D2',  # Darker Material Blue
                relief='flat')

style.configure('Back.TButton',
                padding=10,
                font=('Segoe UI', 12),
                background='#FF5252',  # Material Red A200
                foreground='white',
                relief='flat',
                borderwidth=0)

style.configure('Back.TButton.Hover',
                background='#FF1744',  # Material Red A400
                relief='flat')

style.configure('Title.TLabel',
                font=('Segoe UI', 36, 'bold'),
                background='#1A1A1A',
                foreground='#FFFFFF')

# Create main frame with modern elevation effect
main_frame = ttk.Frame(root, style='Card.TFrame')
main_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

style.configure('Card.TFrame',
                background='#2D2D2D',
                relief='solid',
                borderwidth=0,
                padding=20)

# Modern title with subtle shadow
title_label = ttk.Label(root,
                       text="User Management",
                       style='Title.TLabel')
title_label.pack(pady=50)

# Modern material design buttons with consistent spacing
add_user_button = ttk.Button(main_frame,
                            text="Add User",
                            style='Menu.TButton',
                            command=open_user_add_form)
add_user_button.pack(pady=25, padx=50)

edit_user_button = ttk.Button(main_frame,
                             text="Edit User",
                             style='Menu.TButton',
                             command=edit_system_user)
edit_user_button.pack(pady=25, padx=50)

delete_user_button = ttk.Button(main_frame,
                               text="View/Delete Users",
                               style='Menu.TButton',
                               command=delete_system_user)
delete_user_button.pack(pady=25, padx=50)

# Modern floating back button
back_button = ttk.Button(root,
                        text="Back",
                        style='Back.TButton',
                        command=back_button_mm_1)
back_button.place(x=30, y=30)

# Smooth hover transitions
def on_enter(e):
    if e.widget['style'] == 'Menu.TButton':
        e.widget.configure(style='Menu.TButton.Hover')
    elif e.widget['style'] == 'Back.TButton':
        e.widget.configure(style='Back.TButton.Hover')

def on_leave(e):
    if e.widget['style'] == 'Menu.TButton.Hover':
        e.widget.configure(style='Menu.TButton')
    elif e.widget['style'] == 'Back.TButton.Hover':
        e.widget.configure(style='Back.TButton')

# Bind hover effects for interactive feedback
for button in [add_user_button, edit_user_button, delete_user_button, back_button]:
    button.bind('<Enter>', on_enter)
    button.bind('<Leave>', on_leave)

root.mainloop()