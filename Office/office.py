import tkinter as tk
from tkinter import messagebox

from modules import welcome, add_student, monitor, add_fee, upgrade_year,issue_bonafide,pass_out_students

# ================= ROOT =================
root = tk.Tk()
root.title("AK SOFTWARES")
root.geometry("1366x768")
root.minsize(1366, 768)

root.resizable(False, False)

# ================= MENU BAR =================
menubar = tk.Menu(root)

# Config menu
def show_settings():
    settings_window = tk.Toplevel(root)
    settings_window.title("Office Settings")
    settings_window.geometry("800x700")
    settings_window.resizable(False, False)
    settings_window.grab_set()  # Make it modal
    
    # Center the window
    settings_window.transient(root)
    
    # Main frame
    main_frame = tk.Frame(settings_window, bg="#eeeeee", padx=20, pady=20)
    main_frame.pack(fill="both", expand=True)
    
    # Title
    tk.Label(main_frame, text="Office Management Settings", 
             font=("Segoe UI", 16, "bold"), bg="#eeeeee").pack(pady=(0, 20))
    
    # Settings sections
    # Network Settings
    network_frame = tk.LabelFrame(main_frame, text="Network Settings", 
                                 font=("Segoe UI", 11, "bold"), bg="#eeeeee", padx=10, pady=10)
    network_frame.pack(fill="x", pady=(0, 15))
    
    tk.Label(network_frame, text="RPC IP Address:", bg="#eeeeee", font=("Segoe UI", 10)).grid(row=0, column=0, sticky="w", pady=5)
    rpc_ip_entry = tk.Entry(network_frame, width=20, font=("Segoe UI", 10))
    rpc_ip_entry.insert(0, "192.168.1.100")
    rpc_ip_entry.grid(row=0, column=1, padx=(10, 0), pady=5)
    
    # Student Settings
    student_frame = tk.LabelFrame(main_frame, text="Student Settings", 
                                 font=("Segoe UI", 11, "bold"), bg="#eeeeee", padx=10, pady=10)
    student_frame.pack(fill="x", pady=(0, 15))
    
    tk.Label(student_frame, text="Academic Year:", bg="#eeeeee", font=("Segoe UI", 10)).grid(row=0, column=0, sticky="w", pady=5)
    year_entry = tk.Entry(student_frame, width=15, font=("Segoe UI", 10))
    year_entry.insert(0, "2025-2026")
    year_entry.grid(row=0, column=1, sticky="w", padx=(10, 0), pady=5)
    
    tk.Label(student_frame, text="Default Fee Amount (₹):", bg="#eeeeee", font=("Segoe UI", 10)).grid(row=1, column=0, sticky="w", pady=5)
    fee_entry = tk.Entry(student_frame, width=15, font=("Segoe UI", 10))
    fee_entry.insert(0, "50000")
    fee_entry.grid(row=1, column=1, sticky="w", padx=(10, 0), pady=5)
    
    tk.Label(student_frame, text="Late Fee (₹):", bg="#eeeeee", font=("Segoe UI", 10)).grid(row=2, column=0, sticky="w", pady=5)
    late_fee_entry = tk.Entry(student_frame, width=15, font=("Segoe UI", 10))
    late_fee_entry.insert(0, "500")
    late_fee_entry.grid(row=2, column=1, sticky="w", padx=(10, 0), pady=5)
    
    # Branch Settings
    branch_frame = tk.LabelFrame(main_frame, text="Branch Settings", 
                                font=("Segoe UI", 11, "bold"), bg="#eeeeee", padx=10, pady=10)
    branch_frame.pack(fill="x", pady=(0, 15))
    
    tk.Label(branch_frame, text="Available Branches:", bg="#eeeeee", font=("Segoe UI", 10)).grid(row=0, column=0, sticky="w", pady=5)
    
    # Branch selection with checkboxes
    branches = ["CM", "EE", "ENTC", "CE", "ME"]
    branch_vars = {}
    
    for i, branch in enumerate(branches):
        var = tk.BooleanVar(value=True)  # All branches enabled by default
        branch_vars[branch] = var
        cb = tk.Checkbutton(branch_frame, text=branch, variable=var, bg="#eeeeee", font=("Segoe UI", 10))
        cb.grid(row=1 + i//3, column=i%3, sticky="w", padx=(10, 20), pady=2)
    
    # Office Settings
    office_frame = tk.LabelFrame(main_frame, text="Office Settings", 
                                font=("Segoe UI", 11, "bold"), bg="#eeeeee", padx=10, pady=10)
    office_frame.pack(fill="x", pady=(0, 15))
    
    tk.Label(office_frame, text="Institution Name:", bg="#eeeeee", font=("Segoe UI", 10)).grid(row=0, column=0, sticky="w", pady=5)
    inst_entry = tk.Entry(office_frame, width=30, font=("Segoe UI", 10))
    inst_entry.insert(0, "AK Educational Institute")
    inst_entry.grid(row=0, column=1, sticky="w", padx=(10, 0), pady=5)
    
    tk.Label(office_frame, text="Bonafide Fee (₹):", bg="#eeeeee", font=("Segoe UI", 10)).grid(row=1, column=0, sticky="w", pady=5)
    bonafide_fee_entry = tk.Entry(office_frame, width=15, font=("Segoe UI", 10))
    bonafide_fee_entry.insert(0, "100")
    bonafide_fee_entry.grid(row=1, column=1, sticky="w", padx=(10, 0), pady=5)
    
    # Buttons
    button_frame = tk.Frame(main_frame, bg="#eeeeee")
    button_frame.pack(fill="x", pady=(20, 0))
    
    def save_settings():
        enabled_branches = [branch for branch, var in branch_vars.items() if var.get()]
        messagebox.showinfo("Settings", f"Settings saved successfully!\nRPC IP: {rpc_ip_entry.get()}\nEnabled Branches: {', '.join(enabled_branches)}")
        settings_window.destroy()
    
    def reset_settings():
        rpc_ip_entry.delete(0, tk.END)
        rpc_ip_entry.insert(0, "192.168.1.100")
        year_entry.delete(0, tk.END)
        year_entry.insert(0, "2025-2026")
        fee_entry.delete(0, tk.END)
        fee_entry.insert(0, "50000")
        late_fee_entry.delete(0, tk.END)
        late_fee_entry.insert(0, "500")
        inst_entry.delete(0, tk.END)
        inst_entry.insert(0, "AK Educational Institute")
        bonafide_fee_entry.delete(0, tk.END)
        bonafide_fee_entry.insert(0, "100")
        # Reset all branches to enabled
        for var in branch_vars.values():
            var.set(True)
    
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
config_menu.add_command(label="Settings", command=show_settings)  # Now functional
config_menu.add_separator()
config_menu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="Config", menu=config_menu)

# About menu
def show_about():
    messagebox.showinfo(
        "About Office Software",
        "AK Office Software\n\n"
        "Version: 1.0\n"
        "Developed by: AK Softwares\n"
        "© 2026 AK Softwares"
    )

about_menu = tk.Menu(menubar, tearoff=0)
about_menu.add_command(label="About Office Software", command=show_about)
menubar.add_cascade(label="About", menu=about_menu)

root.config(menu=menubar)

# ================= MAIN LAYOUT =================
main_container = tk.Frame(root)
main_container.pack(fill="both", expand=True)

# LEFT PANEL (AS BEFORE)
sidebar = tk.Frame(
    main_container,
    width=230,
    bg="#dcdcdc",
    relief="sunken",
    borderwidth=1
)
sidebar.pack(side="left", fill="y")

# RIGHT CONTENT AREA
content = tk.Frame(
    main_container,
    bg="#eeeeee",
    relief="sunken",
    borderwidth=1
)
content.pack(side="right", fill="both", expand=True)

# ================= LOAD MODULE FRAMES =================
frames = {
    "welcome": welcome.create(content),
    "add_student": add_student.create(content),
    "monitor": monitor.create(content),
    "add_fee": add_fee.create(content),
    "upgrade": upgrade_year.create(content),
    "bonafide": issue_bonafide.create(content),
    "pass_out": pass_out_students.create(content)
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

def show_frame(name):
    for frame in frames.values():
        frame.pack_forget()

    # reset module data (important)
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

# ================= LEFT PANEL BUTTONS =================
# Add title at the top of sidebar
tk.Label(sidebar, text="Office Management", bg="#dcdcdc", font=("Segoe UI", 12, "bold"), fg="#333333").pack(pady=(15, 10))

sidebar_buttons["add_student"] = create_sidebar_button("Add Student", lambda: show_frame("add_student"), "add_student")
sidebar_buttons["add_student"].pack(pady=(10, 2))

sidebar_buttons["monitor"] = create_sidebar_button("Monitor", lambda: show_frame("monitor"), "monitor")
sidebar_buttons["monitor"].pack(pady=2)

sidebar_buttons["add_fee"] = create_sidebar_button("Add Student Fee", lambda: show_frame("add_fee"), "add_fee")
sidebar_buttons["add_fee"].pack(pady=2)

sidebar_buttons["upgrade"] = create_sidebar_button("Upgrade To Next Year", lambda: show_frame("upgrade"), "upgrade")
sidebar_buttons["upgrade"].pack(pady=2)

sidebar_buttons["bonafide"] = create_sidebar_button("Issue Bonafide", lambda: show_frame("bonafide"), "bonafide")
sidebar_buttons["bonafide"].pack(pady=2)

sidebar_buttons["pass_out"] = create_sidebar_button("Pass Out Students", lambda: show_frame("pass_out"), "pass_out")
sidebar_buttons["pass_out"].pack(pady=2)

# ================= STARTUP SCREEN =================
show_frame("welcome")

root.mainloop()
