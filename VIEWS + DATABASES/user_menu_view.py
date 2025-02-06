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


# Create the main window
root = tk.Tk()
root.title("User Management")
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

style.configure('Back.TButton',
                padding=10,
                font=('Helvetica', 12),
                background='#f44336',
                foreground='white')

# Create main frame
main_frame = ttk.Frame(root, style='Main.TFrame')
main_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

# Create logo frame
logo_frame = ttk.Frame(main_frame, style='Logo.TFrame')
logo_frame.pack(pady=(0, 30))

# Title/Logo
title_label = ttk.Label(logo_frame,
                       text="User Management",
                       font=('Helvetica', 32, 'bold'),
                       background='#f0f0f0')
title_label.pack()

subtitle_label = ttk.Label(logo_frame,
                          text="Calle Pharmacy Management System",
                          font=('Helvetica', 16),
                          background='#f0f0f0')
subtitle_label.pack(pady=(10, 0))

# Button frame
button_frame = ttk.Frame(main_frame, style='Buttons.TFrame')
button_frame.pack(pady=30)

# Menu buttons with consistent spacing
add_user_button = ttk.Button(button_frame,
                            text="Add User",
                            style='Menu.TButton',
                            command=open_user_add_form)
add_user_button.pack(pady=20)

edit_user_button = ttk.Button(button_frame,
                             text="Edit User",
                             style='Menu.TButton',
                             command=edit_system_user)
edit_user_button.pack(pady=20)

delete_user_button = ttk.Button(button_frame,
                               text="View/Delete Users",
                               style='Menu.TButton',
                               command=delete_system_user)
delete_user_button.pack(pady=20)

# Back button
back_button = ttk.Button(root,
                        text="Back",
                        style='Back.TButton',
                        command=back_button_mm_1)
back_button.pack(anchor='nw', padx=20, pady=20)

# Configure frame styles
style.configure('Main.TFrame', background='#f0f0f0')
style.configure('Logo.TFrame', background='#f0f0f0')
style.configure('Buttons.TFrame', background='#f0f0f0')

# Add hover effects
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

style.configure('Menu.TButton.Hover',
                background='#357abd')  # Darker blue on hover
style.configure('Back.TButton.Hover',
                background='#d32f2f')  # Darker red on hover

# Bind hover effects for interactive feedback
for button in [add_user_button, edit_user_button, delete_user_button, back_button]:
    button.bind('<Enter>', on_enter)
    button.bind('<Leave>', on_leave)

root.mainloop()