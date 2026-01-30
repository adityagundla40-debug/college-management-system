import tkinter as tk
from tkinter import messagebox

from modules import (
    welcome,
    year_wise_admission,
    fees_pending_students,
    staff_data_list,
    all_student_data
)

root = tk.Tk()
root.title("HOD Management System")
root.geometry("1366x768")
root.minsize(1366, 768)

# ================= MENU BAR =================
menubar = tk.Menu(root)

def show_settings():
    settings_window = tk.Toplevel(root)
    settings_window.title("HOD Settings")
    settings_window.geometry("600x600")
    settings_window.resizable(False, False)
    settings_window.grab_set()  # Make it modal
    
    # Center the window
    settings_window.transient(root)
    
    # Main frame
    main_frame = tk.Frame(settings_window, bg="#f2f2f2", padx=20, pady=20)
    main_frame.pack(fill="both", expand=True)
    
    # Title
    tk.Label(main_frame, text="HOD Management Settings", 
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
    
    # Department Settings
    dept_frame = tk.LabelFrame(main_frame, text="Department Settings", 
                              font=("Segoe UI", 11, "bold"), bg="#f2f2f2", padx=10, pady=10)
    dept_frame.pack(fill="x", pady=(0, 15))
    
    tk.Label(dept_frame, text="Department Name:", bg="#f2f2f2", font=("Segoe UI", 10)).grid(row=0, column=0, sticky="w", pady=5)
    dept_entry = tk.Entry(dept_frame, width=25, font=("Segoe UI", 10))
    dept_entry.insert(0, "Computer Engineering")
    dept_entry.grid(row=0, column=1, padx=(10, 0), pady=5)
    
    tk.Label(dept_frame, text="Total Intake:", bg="#f2f2f2", font=("Segoe UI", 10)).grid(row=1, column=0, sticky="w", pady=5)
    intake_entry = tk.Entry(dept_frame, width=10, font=("Segoe UI", 10))
    intake_entry.insert(0, "120")
    intake_entry.grid(row=1, column=1, sticky="w", padx=(10, 0), pady=5)
    
    # Buttons
    button_frame = tk.Frame(main_frame, bg="#f2f2f2")
    button_frame.pack(fill="x", pady=(20, 0))
    
    def save_settings():
        messagebox.showinfo("Settings", f"Settings saved successfully!\nDepartment: {dept_entry.get()}")
        settings_window.destroy()
    
    def reset_settings():
        rpc_ip_entry.delete(0, tk.END)
        rpc_ip_entry.insert(0, "192.168.1.100")
        dept_entry.delete(0, tk.END)
        dept_entry.insert(0, "Computer Engineering")
        intake_entry.delete(0, tk.END)
        intake_entry.insert(0, "120")
    
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
    label="About HOD Software",
    command=lambda: messagebox.showinfo(
        "About",
        "HOD Management System\nVersion 1.0\n© 2026 AK Softwares"
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
    "year_wise_admission": year_wise_admission.create(content),
    "fees_pending_students": fees_pending_students.create(content),
    "staff_data_list": staff_data_list.create(content),
    "all_student_data": all_student_data.create(content)
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
tk.Label(sidebar, text="HOD Management", bg="#dcdcdc", font=("Segoe UI", 12, "bold"), fg="#333333").pack(pady=(15, 10))

sidebar_buttons["year_wise_admission"] = create_sidebar_button("Year-wise Admission Data", lambda: show("year_wise_admission"), "year_wise_admission")
sidebar_buttons["year_wise_admission"].pack(pady=(20, 2))

sidebar_buttons["fees_pending_students"] = create_sidebar_button("Fees Pending Students", lambda: show("fees_pending_students"), "fees_pending_students")
sidebar_buttons["fees_pending_students"].pack(pady=2)

sidebar_buttons["staff_data_list"] = create_sidebar_button("Staff Data List", lambda: show("staff_data_list"), "staff_data_list")
sidebar_buttons["staff_data_list"].pack(pady=2)

sidebar_buttons["all_student_data"] = create_sidebar_button("All Student Data List", lambda: show("all_student_data"), "all_student_data")
sidebar_buttons["all_student_data"].pack(pady=2)

show("welcome")
root.mainloop()