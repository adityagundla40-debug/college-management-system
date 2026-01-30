import tkinter as tk
from tkinter import messagebox

from modules import (
    welcome,
    add_books,
    issue_books,
    remove_books,
    scrap_books,
    issued_books
)

root = tk.Tk()
root.title("Library Management System")
root.geometry("1366x768")
root.minsize(1366, 768)

# ================= MENU BAR =================
menubar = tk.Menu(root)

def show_settings():
    settings_window = tk.Toplevel(root)
    settings_window.title("Library Settings")
    settings_window.geometry("500x500")
    settings_window.resizable(False, False)
    settings_window.grab_set()  # Make it modal
    
    # Center the window
    settings_window.transient(root)
    
    # Main frame
    main_frame = tk.Frame(settings_window, bg="#f2f2f2", padx=20, pady=20)
    main_frame.pack(fill="both", expand=True)
    
    # Title
    tk.Label(main_frame, text="Library Management Settings", 
             font=("Segoe UI", 16, "bold"), bg="#f2f2f2").pack(pady=(0, 20))
    
    # Settings sections
    # Network Settings
    network_frame = tk.LabelFrame(main_frame, text="Network Settings", 
                                 font=("Segoe UI", 11, "bold"), bg="#f2f2f2", padx=10, pady=10)
    network_frame.pack(fill="x", pady=(0, 15))
    
    tk.Label(network_frame, text="RPC IP Address:", bg="#f2f2f2", font=("Segoe UI", 10)).grid(row=0, column=0, sticky="w", pady=5)
    rpc_ip_entry = tk.Entry(network_frame, width=20, font=("Segoe UI", 10))
    rpc_ip_entry.insert(0, "192.168.1.100")
    rpc_ip_entry.grid(row=0, column=1, padx=(10, 0), pady=5)
    
    # Library Settings
    lib_frame = tk.LabelFrame(main_frame, text="Library Settings", 
                             font=("Segoe UI", 11, "bold"), bg="#f2f2f2", padx=10, pady=10)
    lib_frame.pack(fill="x", pady=(0, 15))
    
    tk.Label(lib_frame, text="Max Books Per Student:", bg="#f2f2f2", font=("Segoe UI", 10)).grid(row=0, column=0, sticky="w", pady=5)
    max_books_entry = tk.Entry(lib_frame, width=10, font=("Segoe UI", 10))
    max_books_entry.insert(0, "3")
    max_books_entry.grid(row=0, column=1, sticky="w", padx=(10, 0), pady=5)
    
    tk.Label(lib_frame, text="Issue Duration (days):", bg="#f2f2f2", font=("Segoe UI", 10)).grid(row=1, column=0, sticky="w", pady=5)
    duration_entry = tk.Entry(lib_frame, width=10, font=("Segoe UI", 10))
    duration_entry.insert(0, "14")
    duration_entry.grid(row=1, column=1, sticky="w", padx=(10, 0), pady=5)
    
    tk.Label(lib_frame, text="Fine Per Day (₹):", bg="#f2f2f2", font=("Segoe UI", 10)).grid(row=2, column=0, sticky="w", pady=5)
    fine_entry = tk.Entry(lib_frame, width=10, font=("Segoe UI", 10))
    fine_entry.insert(0, "2")
    fine_entry.grid(row=2, column=1, sticky="w", padx=(10, 0), pady=5)
    
    # Buttons
    button_frame = tk.Frame(main_frame, bg="#f2f2f2")
    button_frame.pack(fill="x", pady=(20, 0))
    
    def save_settings():
        messagebox.showinfo("Settings", f"Settings saved successfully!\nRPC IP: {rpc_ip_entry.get()}")
        settings_window.destroy()
    
    def reset_settings():
        rpc_ip_entry.delete(0, tk.END)
        rpc_ip_entry.insert(0, "192.168.1.100")
        max_books_entry.delete(0, tk.END)
        max_books_entry.insert(0, "3")
        duration_entry.delete(0, tk.END)
        duration_entry.insert(0, "14")
        fine_entry.delete(0, tk.END)
        fine_entry.insert(0, "2")
    
    tk.Button(button_frame, text="Save", command=save_settings, 
              bg="#2b6cb0", fg="white", font=("Segoe UI", 10, "bold"), 
              padx=20, pady=5).pack(side="right", padx=(10, 0))
    
    tk.Button(button_frame, text="Reset", command=reset_settings, 
              bg="#6b7280", fg="white", font=("Segoe UI", 10, "bold"), 
              padx=20, pady=5).pack(side="right")
    
    tk.Button(button_frame, text="Cancel", command=settings_window.destroy, 
              bg="#dc2626", fg="white", font=("Segoe UI", 10, "bold"), 
              padx=20, pady=5).pack(side="right", padx=(0, 10))

config_menu = tk.Menu(menubar, tearoff=0)
config_menu.add_command(label="Settings", command=show_settings)
config_menu.add_separator()
config_menu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="Config", menu=config_menu)

about_menu = tk.Menu(menubar, tearoff=0)
about_menu.add_command(
    label="About Library Software",
    command=lambda: messagebox.showinfo(
        "About",
        "Library Management System\nVersion 1.0"
    )
)
menubar.add_cascade(label="About", menu=about_menu)

root.config(menu=menubar)

# ================= MAIN LAYOUT =================
main = tk.Frame(root)
main.pack(fill="both", expand=True)

sidebar = tk.Frame(main, width=240, bg="#dcdcdc", relief="sunken")
sidebar.pack(side="left", fill="y")

content = tk.Frame(main, bg="#f2f2f2")
content.pack(side="right", fill="both", expand=True)

# ================= LOAD MODULES =================
frames = {
    "welcome": welcome.create(content),
    "add_books": add_books.create(content),
    "issue_books": issue_books.create(content),
    "remove_books": remove_books.create(content),
    "scrap_books": scrap_books.create(content),
    "issued_books": issued_books.create(content)

}

# ================= BUTTON STYLING =================
# Normal button style
normal_btn_style = {
    "width": 22, 
    "anchor": "w", 
    "padx": 10, 
    "pady": 6,
    "bg": "#e8e8e8",
    "fg": "#333333",
    "relief": "flat",
    "font": ("Segoe UI", 10)
}

# Active button style
active_btn_style = {
    "width": 22, 
    "anchor": "w", 
    "padx": 10, 
    "pady": 6,
    "bg": "#2b6cb0",
    "fg": "white",
    "relief": "flat",
    "font": ("Segoe UI", 10, "bold")
}

# Hover button style
hover_btn_style = {
    "bg": "#d0d0d0",
    "fg": "#333333"
}

# Store references to all buttons
sidebar_buttons = {}
current_active_button = None

def update_button_states(active_button_name):
    global current_active_button
    current_active_button = active_button_name
    
    for btn_name, button in sidebar_buttons.items():
        if btn_name == active_button_name:
            # Apply active style
            button.config(**active_btn_style)
        else:
            # Apply normal style
            button.config(**normal_btn_style)

def show(name):
    for f in frames.values():
        f.pack_forget()
    frames[name].reset()
    frames[name].pack(fill="both", expand=True)
    
    # Update button states
    update_button_states(name)

def create_sidebar_button(text, command, button_name):
    button = tk.Button(sidebar, text=text, command=command, **normal_btn_style)
    
    # Add hover effects
    def on_enter(event):
        if current_active_button != button_name:
            button.config(**hover_btn_style)
    
    def on_leave(event):
        if current_active_button != button_name:
            button.config(bg=normal_btn_style["bg"], fg=normal_btn_style["fg"])
    
    button.bind("<Enter>", on_enter)
    button.bind("<Leave>", on_leave)
    
    return button

# ================= SIDEBAR BUTTONS =================
tk.Label(sidebar, text="Library Management", bg="#dcdcdc", font=("Segoe UI", 12, "bold"), fg="#333333").pack(pady=(15, 10))

sidebar_buttons["add_books"] = create_sidebar_button("Add Books", lambda: show("add_books"), "add_books")
sidebar_buttons["add_books"].pack(pady=(20, 2))

sidebar_buttons["issue_books"] = create_sidebar_button("Issue Books", lambda: show("issue_books"), "issue_books")
sidebar_buttons["issue_books"].pack(pady=2)

sidebar_buttons["remove_books"] = create_sidebar_button("Remove Books", lambda: show("remove_books"), "remove_books")
sidebar_buttons["remove_books"].pack(pady=2)

sidebar_buttons["scrap_books"] = create_sidebar_button("Scrap Books", lambda: show("scrap_books"), "scrap_books")
sidebar_buttons["scrap_books"].pack(pady=2)

sidebar_buttons["issued_books"] = create_sidebar_button("Issued Books", lambda: show("issued_books"), "issued_books")
sidebar_buttons["issued_books"].pack(pady=2)

# Add some spacing at the top of sidebar

show("welcome")
root.mainloop()
