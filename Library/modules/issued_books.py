import tkinter as tk
from tkinter import ttk

BG_MAIN = "#f2f2f2"
BG_CARD = "#ffffff"

TITLE_FONT = ("Segoe UI", 20, "bold")

def create(parent):
    frame = tk.Frame(parent, bg=BG_MAIN)

    tk.Label(
        frame,
        text="Issued Books",
        font=TITLE_FONT,
        bg=BG_MAIN
    ).pack(pady=20)

    card = tk.Frame(
        frame,
        bg=BG_CARD,
        padx=20,
        pady=20,
        relief="solid",
        borderwidth=1
    )
    card.pack(fill="both", expand=True, padx=40, pady=10)

    columns = ("Book ID", "Book Name", "Roll No", "Student Name", "Issue Date")

    tree = ttk.Treeview(card, columns=columns, show="headings")

    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, width=200)

    tree.pack(fill="both", expand=True)

    # Placeholder data (DB later)
    sample_data = [
        ("B101", "Python Basics", "23CE01", "Rahul Patil", "01-08-2025"),
        ("B102", "DBMS", "23CE02", "Amit Shah", "03-08-2025"),
    ]

    for row in sample_data:
        tree.insert("", "end", values=row)

    frame.reset = lambda: None
    return frame
