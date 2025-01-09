import tkinter as tk

def logout():
    root.destroy()
    import login_view

    import login_view
    login_view
    import add_system_stock
    import add_system_stock
    add_system_stock

def open_user_menu():
    import user_menu_view
    user_menu_view

def open_stock_menu():
    import stock_menu_view
    stock_menu_view

# Create the main window
root = tk.Tk()
root.title("Main Menu")
root.geometry("1400x720")
root.config(bg="light blue")
root.resizable(False, False)  # Set the width and height of the window

button_width = 20
button_height = 7

# Create a frame to center the buttons
frame = tk.Frame(root, bg="light blue")
frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

font_style = ("Helvetica", 16)

# Add User Button
uMenu_button = tk.Button(frame, text="User Menu", font=font_style, command=open_user_menu, width=button_width, height=button_height)
uMenu_button.pack(side=tk.LEFT, padx=10)

# Add Stock Button
sMenu = tk.Button(frame, text="Stock Menu", font=font_style, command=open_stock_menu, width=button_width, height=button_height)
sMenu.pack(side=tk.RIGHT, padx=10)

# Logout Button
logout_button = tk.Button(root, text="Logout", font=font_style, command=logout)
logout_button.place(relx=1.0, rely=0.0, anchor='ne', x=-10, y=10)

root.mainloop()