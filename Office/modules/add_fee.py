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
        text="Add Student Fee",
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
        ("Amount to be Paid", "entry"),
        ("Transaction Type", "dropdown"),
        ("Transaction ID", "entry"),
        ("Bank Name", "entry"),
        ("Account Type", "entry")
    ]

    widgets = {}

    for i, (label, field_type) in enumerate(fields):
        tk.Label(
            card,
            text=label,
            bg=BG_CARD,
            fg=TEXT,
            font=LABEL_FONT,
            anchor="w"
        ).grid(row=i, column=0, sticky="w", pady=8)

        if field_type == "entry":
            widget = tk.Entry(card, font=ENTRY_FONT, width=40)
            widget.grid(row=i, column=1, sticky="w", pady=8, padx=20)

        elif field_type == "dropdown":
            var = tk.StringVar(value="Select")
            widget = tk.OptionMenu(
                card,
                var,
                "Cash",
                "UPI",
                "Bank Transfer"
            )
            widget.config(
                font=ENTRY_FONT,
                width=36,
                bg="white"
            )
            widget.grid(row=i, column=1, sticky="w", pady=8, padx=20)
            widget.var = var

        widgets[label] = widget

    card.grid_columnconfigure(1, weight=1)

    # ================= BUTTON =================
    btn_frame = tk.Frame(frame, bg=BG_MAIN)
    btn_frame.pack(fill="x", padx=50, pady=20)

    def submit_fee():
        data = {}

        for key, widget in widgets.items():
            if hasattr(widget, "var"):
                data[key] = widget.var.get()
            else:
                data[key] = widget.get()

        print(data)  # DB later
        messagebox.showinfo("Success", "Fee added successfully")

    tk.Button(
        btn_frame,
        text="Add Fee",
        font=BUTTON_FONT,
        bg=PRIMARY,
        fg="white",
        padx=22,
        pady=8,
        relief="flat",
        command=submit_fee
    ).pack(side="right")

    # ================= RESET =================
    def reset():
        for widget in widgets.values():
            if hasattr(widget, "var"):
                widget.var.set("Select")
            else:
                widget.delete(0, tk.END)

    frame.reset = reset
    return frame
