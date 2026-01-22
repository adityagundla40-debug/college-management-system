import tkinter as tk
from tkinter import messagebox
from .theme import *

def create(parent):
    frame = tk.Frame(parent, bg=BG_MAIN)

    tk.Label(frame, text="Issue Book", font=TITLE_FONT, bg=BG_MAIN).pack(pady=20)

    card = tk.Frame(frame, bg=BG_CARD, padx=40, pady=30, relief="solid", borderwidth=1)
    card.pack(fill="x", padx=60)

    fields = [
        "Book ID",
        "Student Roll No",
        "Student Name",
        "Issue Date"
    ]

    entries = {}

    for i, f in enumerate(fields):
        tk.Label(card, text=f, bg=BG_CARD).grid(row=i, column=0, pady=8, sticky="w")
        e = tk.Entry(card, width=40)
        e.grid(row=i, column=1, pady=8, padx=20)
        entries[f] = e

    tk.Button(frame, text="Issue Book", font=BUTTON_FONT,
              bg=PRIMARY, fg="white", padx=20, pady=8,
              command=lambda: messagebox.showinfo("Issued", "Book issued")).pack(pady=20)

    frame.reset = lambda: [e.delete(0, tk.END) for e in entries.values()]
    return frame
