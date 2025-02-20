import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import os
import sqlite3

# Create the main window
root = tk.Tk()
root.title("Calle Pharmacy - Search Staff")
root.geometry("1280x720")
root.config(bg="#f0f0f0")
root.resizable(True, True)

# Create main frame as a container
main_frame = tk.Frame(root, bg="#f0f0f0")
main_frame.place(relx=0.5, rely=0.5, anchor="center")

# Add back button to top left
back_button = tk.Button(root, text="Back", bg="#3498db", fg="white",
                       activebackground="#2980b9", activeforeground="white",
                       font=("Helvetica", 10),
                       borderwidth=0,
                       padx=15, 
                       pady=5,
                       cursor="hand2",
                       command=root.destroy)
back_button.place(x=20, y=20)

# Create a horizontal container frame
container_frame = tk.Frame(main_frame, bg="#f0f0f0")
container_frame.pack()

# Load and display the logo image
script_dir = os.path.dirname(os.path.abspath(__file__))
logo_path = os.path.join(script_dir, "..", "Logo_new.png")
logo_image = tk.PhotoImage(file=logo_path)
logo_image = logo_image.subsample(2, 2)  # Resize logo
logo_label = tk.Label(container_frame, image=logo_image, bg="#f0f0f0")
logo_label.pack(pady=20)

# Create search frame
search_frame = tk.Frame(container_frame, bg="white", padx=40, pady=40)
search_frame.pack(pady=20)

# Add shadow effect
shadow_frame = tk.Frame(container_frame, bg="#d0d0d0")
shadow_frame.place(in_=search_frame, x=5, y=5, relwidth=1, relheight=1)
search_frame.lift()

# Search header
header_label = tk.Label(search_frame, text="Search Staff Member", font=("Helvetica", 24, "bold"), bg="white", fg="#333333")
header_label.pack(pady=(0, 20))

# Search entry
search_entry = ttk.Entry(search_frame, font=("Helvetica", 12), width=30)
search_entry.pack(pady=10)

# Results treeview
tree = ttk.Treeview(search_frame, columns=("Username", "First Name", "Last Name", "Access Level", "Edit", "Delete"), show="headings")
tree.heading("Username", text="Username")
tree.heading("First Name", text="First Name")
tree.heading("Last Name", text="Last Name")
tree.heading("Access Level", text="Access Level")
tree.heading("Edit", text="Edit")
tree.heading("Delete", text="Delete")
tree.pack(pady=20)

def edit_user(username):
    edit_window = tk.Toplevel(root)
    edit_window.title("Edit User")
    edit_window.geometry("400x300")
    
    # Get user details
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE username=?", (username,))
    user = c.fetchone()
    conn.close()
    
    # Create entry fields
    tk.Label(edit_window, text="Username:").pack(pady=5)
    username_entry = ttk.Entry(edit_window)
    username_entry.insert(0, user[0])
    username_entry.pack()
    
    tk.Label(edit_window, text="Password:").pack(pady=5)
    password_entry = ttk.Entry(edit_window)
    password_entry.insert(0, user[1])
    password_entry.pack()
    
    tk.Label(edit_window, text="First Name:").pack(pady=5)
    firstname_entry = ttk.Entry(edit_window)
    firstname_entry.insert(0, user[2])
    firstname_entry.pack()
    
    tk.Label(edit_window, text="Last Name:").pack(pady=5)
    lastname_entry = ttk.Entry(edit_window)
    lastname_entry.insert(0, user[3])
    lastname_entry.pack()
    
    tk.Label(edit_window, text="Access Level:").pack(pady=5)
    access_entry = ttk.Entry(edit_window)
    access_entry.insert(0, user[4])
    access_entry.pack()
    
    def save_changes():
        conn = sqlite3.connect('users.db')
        c = conn.cursor()
        c.execute("""UPDATE users 
                    SET username=?, password=?, first_name=?, last_name=?, access_level=?
                    WHERE username=?""",
                 (username_entry.get(), password_entry.get(), firstname_entry.get(),
                  lastname_entry.get(), access_entry.get(), username))
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "User details updated successfully")
        edit_window.destroy()
        search_staff()  # Refresh the results
        
    tk.Button(edit_window, text="Save Changes", command=save_changes).pack(pady=20)

def delete_user(username):
    if messagebox.askyesno("Confirm Delete", "Are you sure you want to delete this user?"):
        conn = sqlite3.connect('users.db')
        c = conn.cursor()
        c.execute("DELETE FROM users WHERE username=?", (username,))
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "User deleted successfully")
        search_staff()  # Refresh the results

def binary_search(arr, target, low, high):
    if low > high:
        return None
    
    mid = (low + high) // 2
    if arr[mid][1].lower() == target.lower():
        return arr[mid]
    elif arr[mid][1].lower() > target.lower():
        return binary_search(arr, target, low, mid - 1)
    else:
        return binary_search(arr, target, mid + 1, high)

def search_staff():
    search_term = search_entry.get()
    if not search_term:
        messagebox.showwarning("Warning", "Please enter a search term")
        return
        
    # Clear previous results
    for item in tree.get_children():
        tree.delete(item)
        
    # Get staff data from database
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute("SELECT username, first_name, last_name, access_level FROM users ORDER BY first_name")
    staff_list = c.fetchall()
    conn.close()
    
    if not staff_list:
        messagebox.showinfo("Info", "No staff members found")
        return
        
    # Perform binary search
    result = binary_search(staff_list, search_term, 0, len(staff_list)-1)
    
    if result:
        # Create edit and delete buttons
        edit_button = tk.Button(tree, text="Edit", bg="#f39c12", fg="white",
                              activebackground="#d68910", activeforeground="white",
                              font=("Helvetica", 8),
                              borderwidth=0,
                              padx=10,
                              pady=2)
        delete_button = tk.Button(tree, text="Delete", bg="#e74c3c", fg="white",
                                activebackground="#c0392b", activeforeground="white",
                                font=("Helvetica", 8),
                                borderwidth=0,
                                padx=10,
                                pady=2)
        
        # Insert result with buttons
        item = tree.insert("", "end", values=(result[0], result[1], result[2], result[3], 
                                     "", ""))
        
        # Place buttons in the tree
        tree.update()
        bbox = tree.bbox(item, "#5")  # Get bbox of edit column
        if bbox:
            x, y, w, h = bbox
            edit_button.place(x=x, y=y, width=w, height=h)
            
        bbox = tree.bbox(item, "#6")  # Get bbox of delete column
        if bbox:
            x, y, w, h = bbox
            delete_button.place(x=x, y=y, width=w, height=h)
            
        # Configure button commands
        edit_button.configure(command=lambda u=result[0]: edit_user(u))
        delete_button.configure(command=lambda u=result[0]: delete_user(u))
    else:
        messagebox.showinfo("Info", "No matching staff member found")

# Search button
search_button = tk.Button(search_frame, text="Search", bg="#3498db", fg="white",
                         activebackground="#2980b9", activeforeground="white",
                         font=("Helvetica", 12),
                         borderwidth=0,
                         padx=20,
                         pady=10,
                         cursor="hand2",
                         command=search_staff)
search_button.pack(pady=10)

# Run the application
root.mainloop()
