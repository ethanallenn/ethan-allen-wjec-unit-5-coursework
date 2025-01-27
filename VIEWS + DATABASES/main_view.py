import tkinter as tk
from tkinter import messagebox


def logout():
    """Function to handle logout."""
    confirm = messagebox.askyesno("Confirm Logout", "Are you sure you want to logout?")
    if confirm:
        root.destroy()  # Close current window
        import login_view  # Redirect to login_view


def user_management():
    """Navigate to User Management."""
    root.destroy()
    import user_menu_view  # Redirect to user_menu_view


def staff_management():
    """Function handling Staff Management."""
    root.destroy()
    import staff_menu_view  # Redirect to staff_menu_view


def stock_management():
    """Function handling Stock Management."""
    root.destroy()
    import stock_menu_view  # Redirect to stock_menu_view


def prescription_management():
    """Function handling Prescription Management."""
    root.destroy()
    import prescription_menu_view  # Redirect to prescription_menu_view


def administrative_tools():
    """Function handling Administrative Tools."""
    root.destroy()
    import admin_tools_view  # Redirect to admin_tools_view


# Create main Tkinter window
root = tk.Tk()
root.title("Calle Pharmacy - Home Screen")
root.configure(bg="#ffffff")
root.geometry("400x500")  # Updated size to match user_menu_view
root.resizable(False, False)

# Create Frames for layout organization
frame = tk.Frame(root, bg="#e0f7fa", bd=2, relief="flat", padx=20, pady=20)
frame.pack(pady=10)

# Heading
heading = tk.Label(frame, text="Calle Pharmacy Management System", font=("Helvetica", 16, "bold"), bg="#e0f7fa",
                   fg="#00695c")
heading.pack(pady=15)

# Buttons
button_style = {"font": ("Helvetica", 12), "bg": "#00695c", "fg": "#ffffff", "activebackground": "#004d40",
                "activeforeground": "#ffffff", "width": 25, "relief": "flat", "bd": 0}

btn_user_management = tk.Button(frame, text="User Management", command=user_management, **button_style)
btn_user_management.pack(pady=8)

btn_staff_management = tk.Button(frame, text="Staff Management", command=staff_management, **button_style)
btn_staff_management.pack(pady=8)

btn_stock_management = tk.Button(frame, text="Stock Management", command=stock_management, **button_style)
btn_stock_management.pack(pady=8)

btn_prescription_management = tk.Button(frame, text="Prescription Management", command=prescription_management,
                                        **button_style)
btn_prescription_management.pack(pady=8)

btn_administrative_tools = tk.Button(frame, text="Administrative Tools", command=administrative_tools, **button_style)
btn_administrative_tools.pack(pady=8)

# Logout Button
btn_logout = tk.Button(frame, text="Logout", command=logout, font=("Helvetica", 12), bg="#d32f2f", fg="#ffffff",
                       activebackground="#b71c1c", activeforeground="#ffffff", width=25, relief="flat", bd=0)
btn_logout.pack(pady=8)

# Run the application
root.mainloop()
