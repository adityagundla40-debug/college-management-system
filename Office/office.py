import tkinter as tk
from tkinter import messagebox

from modules import welcome, add_student, monitor, add_fee, upgrade_year,issue_bonafide

# ================= ROOT =================
root = tk.Tk()
root.title("AK SOFTWARES")
root.geometry("1366x768")
root.minsize(1366, 768)

root.resizable(False, False)

# ================= MENU BAR =================
menubar = tk.Menu(root)

# Config menu
config_menu = tk.Menu(menubar, tearoff=0)
config_menu.add_command(label="Settings")  # later
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
}

def show_frame(name):
    for frame in frames.values():
        frame.pack_forget()

    # reset module data (important)
    frames[name].reset()
    frames[name].pack(fill="both", expand=True)

# ================= LEFT PANEL BUTTONS =================
btn_cfg = {
    "width": 22,
    "anchor": "w",
    "padx": 10,
    "pady": 6
}

tk.Button(
    sidebar, text="Add Student",
    command=lambda: show_frame("add_student"),
    **btn_cfg
).pack()

tk.Button(
    sidebar, text="Monitor",
    command=lambda: show_frame("monitor"),
    **btn_cfg
).pack()

tk.Button(
    sidebar, text="Add Student Fee",
    command=lambda: show_frame("add_fee"),
    **btn_cfg
).pack()

tk.Button(
    sidebar, text="Upgrade To Next Year",
    command=lambda: show_frame("upgrade"),
    **btn_cfg
).pack()

tk.Button(
    sidebar,
    text="Issue Bonafide",
    command=lambda: show_frame("bonafide"),
    **btn_cfg
).pack()

# ================= STARTUP SCREEN =================
show_frame("welcome")

root.mainloop()
