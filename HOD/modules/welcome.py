import tkinter as tk

BG_MAIN = "#f2f2f2"

def create(parent):
    frame = tk.Frame(parent, bg=BG_MAIN)

    # Welcome title
    tk.Label(
        frame,
        text="Welcome to HOD Management System",
        font=("Segoe UI", 22, "bold"),
        bg=BG_MAIN,
        fg="#2b6cb0"
    ).pack(expand=True, pady=(0, 20))
    
    # Description
    description = """
    Manage your department efficiently with comprehensive tools for:
    
    • Year-wise Student Admission Data
    • Fees Pending Student Lists
    • Staff Data Management
    • Complete Student Database
    
    Select an option from the sidebar to get started.
    """
    
    tk.Label(
        frame,
        text=description,
        font=("Segoe UI", 12),
        bg=BG_MAIN,
        fg="#333333",
        justify="left"
    ).pack(expand=True)

    frame.reset = lambda: None
    return frame