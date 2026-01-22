import tkinter as tk

BG_MAIN = "#f2f2f2"

def create(parent):
    frame = tk.Frame(parent, bg=BG_MAIN)

    tk.Label(
        frame,
        text="Welcome to Library Management System",
        font=("Segoe UI", 22, "bold"),
        bg=BG_MAIN
    ).pack(expand=True)

    frame.reset = lambda: None
    return frame
