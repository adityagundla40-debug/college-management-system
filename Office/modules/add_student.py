import tkinter as tk
from tkinter import messagebox

# ================= THEME =================
BG_MAIN = "#f2f2f2"
BG_CARD = "#ffffff"
PRIMARY = "#2b6cb0"
TEXT = "#1f2937"
DANGER = "#c53030"

TITLE_FONT = ("Segoe UI", 20, "bold")
LABEL_FONT = ("Segoe UI", 11)
ENTRY_FONT = ("Segoe UI", 11)
BUTTON_FONT = ("Segoe UI", 11, "bold")
NOTE_FONT = ("Segoe UI", 9, "italic")

def create(parent):
    frame = tk.Frame(parent, bg=BG_MAIN)

    # ================= TITLE =================
    tk.Label(
        frame,
        text="Add Student",
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
        ("Roll No", "entry"),
        ("Student Name", "entry"),
        ("Admission Year", "entry_with_note"),   # 👈 changed
        ("Branch", "dropdown", ["CM", "ENTC", "EE", "CE", "ME"]),
        ("Admission Entry Level","dropdown",[" 1st Year "," Direct 2nd Year" ]),
        ("Date of Birth", "entry"),
        ("Address", "entry"),
        ("Phone Number", "entry"),
        ("Admission Type", "dropdown", ["CAP", "NON-CAP"]),
        ("Caste", "entry"),
        ("Mother Tongue", "entry"),
        ("Aadhar Number", "entry")
    ]

    widgets = {}

    row = 0
    for field in fields:
        label = field[0]
        field_type = field[1]

        tk.Label(
            card,
            text=label,
            bg=BG_CARD,
            fg=TEXT,
            font=LABEL_FONT,
            anchor="w"
        ).grid(row=row, column=0, sticky="w", pady=6)

        # ---------- ENTRY ----------
        if field_type == "entry":
            widget = tk.Entry(card, font=ENTRY_FONT, width=40)
            widget.grid(row=row, column=1, sticky="w", padx=20, pady=6)

        # ---------- ENTRY + NOTE ----------
        elif field_type == "entry_with_note":
            widget = tk.Entry(card, font=ENTRY_FONT, width=40)
            widget.grid(row=row, column=1, sticky="w", padx=20, pady=(6, 2))

            tk.Label(
                card,
                text="Format: 2026-2027",
                font=NOTE_FONT,
                fg=DANGER,
                bg=BG_CARD,
                anchor="w"
            ).grid(row=row + 1, column=1, sticky="w", padx=20)

            widgets[label] = widget
            row += 1  # extra row used by note
            row += 1
            continue

        # ---------- DROPDOWN ----------
        elif field_type == "dropdown":
            options = field[2]
            var = tk.StringVar(value=options[0])

            widget = tk.OptionMenu(card, var, *options)
            widget.config(
                font=ENTRY_FONT,
                width=37,
                bg="white",
                anchor="w"
            )
            widget.grid(row=row, column=1, sticky="w", padx=20, pady=6)
            widget.var = var

        widgets[label] = widget
        row += 1

    card.grid_columnconfigure(1, weight=1)

    # ================= SUBMIT =================
    btn_frame = tk.Frame(frame, bg=BG_MAIN)
    btn_frame.pack(fill="x", padx=50, pady=20)

    def submit_student():
        data = {}

        for key, widget in widgets.items():
            if hasattr(widget, "var"):
                data[key] = widget.var.get()
            else:
                data[key] = widget.get().strip()

        if not data["Roll No"] or not data["Student Name"]:
            messagebox.showwarning(
                "Missing Data",
                "Roll No and Student Name are required"
            )
            return

        print(data)  # DB later
        messagebox.showinfo("Success", "Student added successfully")

    tk.Button(
        btn_frame,
        text="Submit",
        font=BUTTON_FONT,
        bg=PRIMARY,
        fg="white",
        padx=24,
        pady=8,
        relief="flat",
        command=submit_student
    ).pack(side="right")

    # ================= RESET =================
    def reset():
        for widget in widgets.values():
            if hasattr(widget, "var"):
                widget.var.set(widget.var.get())
            else:
                widget.delete(0, tk.END)

    frame.reset = reset
    return frame
