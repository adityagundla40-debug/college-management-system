import tkinter as tk
from tkinter import messagebox

BG_MAIN = "#f2f2f2"
BG_CARD = "#ffffff"
PRIMARY = "#2b6cb0"
TEXT = "#1f2937"

TITLE_FONT = ("Segoe UI", 20, "bold")
LABEL_FONT = ("Segoe UI", 11)
ENTRY_FONT = ("Segoe UI", 11)
BUTTON_FONT = ("Segoe UI", 11, "bold")

def create(parent):
    frame = tk.Frame(parent, bg=BG_MAIN)

    # TITLE
    tk.Label(
        frame, text="Add Student",
        font=TITLE_FONT,
        bg=BG_MAIN, fg=TEXT
    ).pack(pady=(20, 10))

    # CARD (fills width nicely)
    card = tk.Frame(
        frame,
        bg=BG_CARD,
        padx=40,
        pady=30,
        relief="solid",
        borderwidth=1
    )
    card.pack(fill="x", padx=50, pady=10)

    fields = [
        "Roll No", "Student Name", "Applying Year", "Branch",
        "Date of Birth", "Address", "Phone Number",
        "Admission Type (CAP / Non-CAP)",
        "Caste", "Mother Tongue", "Aadhar Number"
    ]

    entries = {}

    for i, field in enumerate(fields):
        tk.Label(
            card, text=field,
            bg=BG_CARD, fg=TEXT,
            font=LABEL_FONT,
            anchor="w"
        ).grid(row=i, column=0, sticky="w", pady=8)

        entry = tk.Entry(card, font=ENTRY_FONT, width=40)
        entry.grid(row=i, column=1, sticky="w", pady=8, padx=20)

        entries[field] = entry

    card.grid_columnconfigure(1, weight=1)

    # SUBMIT BUTTON (right aligned)
    btn_frame = tk.Frame(frame, bg=BG_MAIN)
    btn_frame.pack(fill="x", padx=50, pady=20)

    def submit():
        messagebox.showinfo("Saved", "Student added successfully")

    tk.Button(
        btn_frame,
        text="Submit",
        font=BUTTON_FONT,
        bg=PRIMARY,
        fg="white",
        padx=20,
        pady=8,
        relief="flat",
        command=submit
    ).pack(side="right")

    # RESET
    def reset():
        for e in entries.values():
            e.delete(0, tk.END)

    frame.reset = reset
    return frame
