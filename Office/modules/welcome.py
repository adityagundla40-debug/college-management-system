import tkinter as tk

def create(parent):
    frame = tk.Frame(parent, bg="#eeeeee")

    tk.Label(
        frame,
        text="Welcome to Office Software",
        font=("Arial", 20, "bold"),
        bg="#eeeeee"
    ).pack(expand=True)

    # reset function (required by main)
    frame.reset = lambda: None
    return frame
