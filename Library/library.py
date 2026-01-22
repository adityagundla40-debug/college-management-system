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

config_menu = tk.Menu(menubar, tearoff=0)
config_menu.add_command(label="Settings")
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

def show(name):
    for f in frames.values():
        f.pack_forget()
    frames[name].reset()
    frames[name].pack(fill="both", expand=True)

# ================= SIDEBAR BUTTONS =================
btn_cfg = {"width": 22, "anchor": "w", "padx": 10, "pady": 6}

tk.Button(sidebar, text="Add Books", command=lambda: show("add_books"), **btn_cfg).pack()
tk.Button(sidebar, text="Issue Books", command=lambda: show("issue_books"), **btn_cfg).pack()
tk.Button(sidebar, text="Remove Books", command=lambda: show("remove_books"), **btn_cfg).pack()
tk.Button(sidebar, text="Scrap Books", command=lambda: show("scrap_books"), **btn_cfg).pack()
tk.Button(sidebar, text="Issued Books", command=lambda: show("issued_books"), **btn_cfg).pack()

show("welcome")
root.mainloop()
