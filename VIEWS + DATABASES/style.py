import tkinter as tk
from tkinter import ttk

def apply_modern_style():
    # Create style object
    style = ttk.Style()
    style.theme_use('clam')

    # Configure common styles
    style.configure('Main.TFrame',
                   background='#f0f0f0')
    
    # Modern button style
    style.configure('Modern.TButton',
                   padding=10,
                   font=('Helvetica', 12),
                   background='#4a90e2',
                   foreground='white')
    
    # Hover effect for buttons
    style.map('Modern.TButton',
             background=[('active', '#357abd')])
    
    # Large menu button style
    style.configure('Menu.TButton',
                   padding=20,
                   font=('Helvetica', 16),
                   background='#4a90e2', 
                   foreground='white',
                   width=25)
    
    # Danger/logout button style  
    style.configure('Danger.TButton',
                   padding=10,
                   font=('Helvetica', 12),
                   background='#f44336',
                   foreground='white')
    
    # Label styles
    style.configure('Title.TLabel',
                   font=('Helvetica', 32, 'bold'),
                   background='#f0f0f0')
    
    style.configure('Header.TLabel',
                   font=('Helvetica', 24, 'bold'),
                   background='#f0f0f0')
    
    style.configure('Normal.TLabel',
                   font=('Helvetica', 12),
                   background='#f0f0f0')
    
    # Entry style
    style.configure('Modern.TEntry',
                   padding=5,
                   font=('Helvetica', 12))
    
    # Combobox style
    style.configure('Modern.TCombobox',
                   padding=5,
                   font=('Helvetica', 12))

def create_modern_window(title, size="1400x720"):
    """Creates a modern styled root window"""
    root = tk.Tk()
    root.title(title)
    root.geometry(size)
    root.config(bg="#f0f0f0")
    root.resizable(False, False)
    apply_modern_style()
    return root

def create_main_frame(root):
    """Creates a centered main frame with modern styling"""
    main_frame = ttk.Frame(root, style='Main.TFrame')
    main_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
    return main_frame
