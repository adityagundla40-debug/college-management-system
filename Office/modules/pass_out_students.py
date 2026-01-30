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
        text="Pass Out Students",
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

    fields = [
        "Roll No / Enrollment No",
        "Aggregate Percentage (3rd Year)",
        "Mark List ID"
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

        entry = tk.Entry(card, font=ENTRY_FONT, width=40)
        entry.grid(row=i, column=1, sticky="w", padx=20, pady=10)

        entries[field] = entry

    card.grid_columnconfigure(1, weight=1)

    # ================= BUTTON =================
    btn_frame = tk.Frame(frame, bg=BG_MAIN)
    btn_frame.pack(fill="x", padx=50, pady=20)

    def save_pass_out():
        roll_or_enroll = entries["Roll No / Enrollment No"].get().strip()
        percentage = entries["Aggregate Percentage (3rd Year)"].get().strip()
        marklist_id = entries["Mark List ID"].get().strip()

        if not roll_or_enroll or not percentage:
            messagebox.showwarning(
                "Missing Data",
                "Roll/Enrollment No and Percentage are required"
            )
            return

        # DB logic later
        print({
            "roll_or_enroll": roll_or_enroll,
            "percentage": percentage,
            "marklist_id": marklist_id
        })

        messagebox.showinfo(
            "Saved",
            "Pass out student details saved successfully"
        )

    tk.Button(
        btn_frame,
        text="Save",
        font=BUTTON_FONT,
        bg=PRIMARY,
        fg="white",
        padx=24,
        pady=8,
        relief="flat",
        command=save_pass_out
    ).pack(side="right")

    # ================= RESET =================
    def reset():
        for e in entries.values():
            e.delete(0, tk.END)

    frame.reset = reset
    return frame
