import tkinter as tk
from tkinter import messagebox

from .theme import *

def create(parent):
    frame = tk.Frame(parent, bg=BG_MAIN)

    tk.Label(frame, text="Add Books", font=TITLE_FONT, bg=BG_MAIN).pack(pady=20)

    card = tk.Frame(frame, bg=BG_CARD, padx=40, pady=30, relief="solid", borderwidth=1)
    card.pack(fill="x", padx=60)

    fields = [
        "ISBN",
        "Book Name",
        "Author",
        "Department",
        "Quantity"
    ]

    entries = {}

    for i, f in enumerate(fields):
        tk.Label(card, text=f, bg=BG_CARD, font=LABEL_FONT).grid(row=i, column=0, pady=8, sticky="w")
        e = tk.Entry(card, font=ENTRY_FONT, width=40)
        e.grid(row=i, column=1, pady=8, padx=20)
        entries[f] = e

    def save():
        messagebox.showinfo("Saved", "Book added successfully")

    tk.Button(frame, text="Add Book", font=BUTTON_FONT,
              bg=PRIMARY, fg="white", padx=20, pady=8,
              command=save).pack(pady=20)

    def reset():
        for e in entries.values():
            e.delete(0, tk.END)

    frame.reset = reset
    return frame
