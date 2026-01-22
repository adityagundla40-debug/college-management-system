import tkinter as tk
from tkinter import messagebox

BG_MAIN = "#f2f2f2"
BG_CARD = "#ffffff"
PRIMARY = "#c53030"

TITLE_FONT = ("Segoe UI", 20, "bold")
LABEL_FONT = ("Segoe UI", 11)
ENTRY_FONT = ("Segoe UI", 11)
BUTTON_FONT = ("Segoe UI", 11, "bold")

def create(parent):
    frame = tk.Frame(parent, bg=BG_MAIN)

    tk.Label(
        frame,
        text="Remove Books",
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

    tk.Label(card, text="Book ID", bg=BG_CARD, font=LABEL_FONT)\
        .grid(row=0, column=0, sticky="w", pady=10)

    book_id = tk.Entry(card, font=ENTRY_FONT, width=40)
    book_id.grid(row=0, column=1, padx=20, pady=10)

    tk.Label(card, text="Quantity to Remove", bg=BG_CARD, font=LABEL_FONT)\
        .grid(row=1, column=0, sticky="w", pady=10)

    qty = tk.Entry(card, font=ENTRY_FONT, width=40)
    qty.grid(row=1, column=1, padx=20, pady=10)

    def remove_book():
        messagebox.showinfo("Removed", "Book removed successfully")

    tk.Button(
        frame,
        text="Remove Book",
        font=BUTTON_FONT,
        bg=PRIMARY,
        fg="white",
        padx=22,
        pady=8,
        command=remove_book
    ).pack(pady=20)

    def reset():
        book_id.delete(0, tk.END)
        qty.delete(0, tk.END)

    frame.reset = reset
    return frame
