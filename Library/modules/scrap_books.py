import tkinter as tk
from tkinter import messagebox

BG_MAIN = "#f2f2f2"
BG_CARD = "#ffffff"
PRIMARY = "#805ad5"

TITLE_FONT = ("Segoe UI", 20, "bold")
LABEL_FONT = ("Segoe UI", 11)
ENTRY_FONT = ("Segoe UI", 11)
BUTTON_FONT = ("Segoe UI", 11, "bold")

def create(parent):
    frame = tk.Frame(parent, bg=BG_MAIN)

    tk.Label(
        frame,
        text="Scrap Books",
        font=TITLE_FONT,
        bg=BG_MAIN
    ).pack(pady=20)

    card = tk.Frame(
        frame,
        bg=BG_CARD,
        padx=40,
        pady=30,
        relief="solid",
        borderwidth=1
    )
    card.pack(fill="x", padx=60)

    fields = [
        "Book ID",
        "Reason for Scrap",
        "Scrap Date"
    ]

    entries = {}

    for i, field in enumerate(fields):
        tk.Label(card, text=field, bg=BG_CARD, font=LABEL_FONT)\
            .grid(row=i, column=0, sticky="w", pady=10)

        entry = tk.Entry(card, font=ENTRY_FONT, width=40)
        entry.grid(row=i, column=1, padx=20, pady=10)
        entries[field] = entry

    def scrap_book():
        messagebox.showinfo("Scrapped", "Book scrapped successfully")

    tk.Button(
        frame,
        text="Scrap Book",
        font=BUTTON_FONT,
        bg=PRIMARY,
        fg="white",
        padx=22,
        pady=8,
        command=scrap_book
    ).pack(pady=20)

    def reset():
        for e in entries.values():
            e.delete(0, tk.END)

    frame.reset = reset
    return frame
