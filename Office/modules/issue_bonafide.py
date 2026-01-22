import tkinter as tk
from tkinter import messagebox

# ================= THEME =================
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

    # ================= TITLE =================
    tk.Label(
        frame,
        text="Issue Bonafide Certificate",
        font=TITLE_FONT,
        bg=BG_MAIN,
        fg=TEXT
    ).pack(pady=(20, 10))

    # ================= CARD =================
    card = tk.Frame(
        frame,
        bg=BG_CARD,
        padx=40,
        pady=30,
        relief="solid",
        borderwidth=1
    )
    card.pack(fill="x", padx=50, pady=10)

    # ================= FIELDS =================
    fields = [
        "Student Name",
        "Roll No",
        "Year",
        "Department",
        "Student Address"
    ]

    entries = {}

    for i, field in enumerate(fields):
        tk.Label(
            card,
            text=field,
            bg=BG_CARD,
            fg=TEXT,
            font=LABEL_FONT,
            anchor="w"
        ).grid(row=i, column=0, sticky="w", pady=10)

        if field == "Student Address":
            entry = tk.Text(card, height=3, width=42, font=ENTRY_FONT)
            entry.grid(row=i, column=1, sticky="w", padx=20, pady=10)
        else:
            entry = tk.Entry(card, font=ENTRY_FONT, width=42)
            entry.grid(row=i, column=1, sticky="w", padx=20, pady=10)

        entries[field] = entry

    card.grid_columnconfigure(1, weight=1)

    # ================= BUTTON =================
    btn_frame = tk.Frame(frame, bg=BG_MAIN)
    btn_frame.pack(fill="x", padx=50, pady=20)

    def issue_bonafide():
        data = {}
        for key, widget in entries.items():
            if isinstance(widget, tk.Text):
                data[key] = widget.get("1.0", tk.END).strip()
            else:
                data[key] = widget.get().strip()

        if not data["Student Name"] or not data["Roll No"]:
            messagebox.showwarning(
                "Missing Data",
                "Student Name and Roll No are required"
            )
            return

        # 🔹 DB / PDF generation later
        messagebox.showinfo(
            "Bonafide Issued",
            "Bonafide certificate issued successfully"
        )

    tk.Button(
        btn_frame,
        text="Issue Bonafide",
        font=BUTTON_FONT,
        bg=PRIMARY,
        fg="white",
        padx=24,
        pady=8,
        relief="flat",
        command=issue_bonafide
    ).pack(side="right")

    # ================= RESET =================
    def reset():
        for widget in entries.values():
            if isinstance(widget, tk.Text):
                widget.delete("1.0", tk.END)
            else:
                widget.delete(0, tk.END)

    frame.reset = reset
    return frame
