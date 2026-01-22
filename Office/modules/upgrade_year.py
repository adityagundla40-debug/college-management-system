import tkinter as tk
from tkinter import messagebox

# ================= THEME =================
BG_MAIN = "#f2f2f2"
BG_CARD = "#ffffff"
PRIMARY = "#2b6cb0"
DANGER = "#c53030"
SUCCESS = "#2f855a"
TEXT = "#1f2937"

TITLE_FONT = ("Segoe UI", 20, "bold")
LABEL_FONT = ("Segoe UI", 11)
ENTRY_FONT = ("Segoe UI", 11)
BUTTON_FONT = ("Segoe UI", 11, "bold")
STATUS_FONT = ("Segoe UI", 11, "bold")

def create(parent):
    frame = tk.Frame(parent, bg=BG_MAIN)

    # ================= TITLE =================
    tk.Label(
        frame,
        text="Upgrade To Next Year",
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

    # ================= INPUT =================
    tk.Label(
        card,
        text="Roll No",
        bg=BG_CARD,
        fg=TEXT,
        font=LABEL_FONT
    ).grid(row=0, column=0, sticky="w", pady=10)

    roll_entry = tk.Entry(card, font=ENTRY_FONT, width=35)
    roll_entry.grid(row=0, column=1, sticky="w", padx=20, pady=10)

    # ================= STATUS =================
    status_label = tk.Label(
        card,
        text="",
        bg=BG_CARD,
        font=STATUS_FONT,
        anchor="w"
    )
    status_label.grid(row=1, column=0, columnspan=2, sticky="w", pady=15)

    card.grid_columnconfigure(1, weight=1)

    # ================= LOGIC =================
    def check_dues():
        roll = roll_entry.get().strip()
        if not roll:
            messagebox.showwarning("Input Required", "Please enter Roll No")
            return

        # 🔹 Placeholder logic (DB later)
        fees_pending = False      # change when DB added
        books_pending = False    # change when DB added

        if fees_pending or books_pending:
            msg = "Cannot upgrade:\n"
            if fees_pending:
                msg += "• Fees are pending\n"
            if books_pending:
                msg += "• Library books not returned\n"

            status_label.config(text=msg, fg=DANGER)
            upgrade_btn.config(state="disabled")
        else:
            status_label.config(
                text="All clear ✔ Student eligible for upgrade",
                fg=SUCCESS
            )
            upgrade_btn.config(state="normal")

    def upgrade_student():
        roll = roll_entry.get().strip()
        if not roll:
            return

        # 🔹 DB update will go here later
        messagebox.showinfo(
            "Success",
            f"Student (Roll No: {roll}) upgraded to next year"
        )

        # lock again after upgrade
        upgrade_btn.config(state="disabled")
        status_label.config(
            text="Upgrade completed successfully ✔",
            fg=SUCCESS
        )

    # ================= BUTTONS =================
    btn_frame = tk.Frame(frame, bg=BG_MAIN)
    btn_frame.pack(fill="x", padx=50, pady=20)

    check_btn = tk.Button(
        btn_frame,
        text="Check Dues",
        font=BUTTON_FONT,
        bg=PRIMARY,
        fg="white",
        padx=20,
        pady=8,
        relief="flat",
        command=check_dues
    )
    check_btn.pack(side="right", padx=10)

    upgrade_btn = tk.Button(
        btn_frame,
        text="Upgrade",
        font=BUTTON_FONT,
        bg=SUCCESS,
        fg="white",          # ✅ TEXT COLOR FIXED
        activeforeground="white",
        padx=20,
        pady=8,
        relief="flat",
        state="disabled",
        command=upgrade_student   # ✅ FUNCTIONABLE
    )
    upgrade_btn.pack(side="right")

    # ================= RESET =================
    def reset():
        roll_entry.delete(0, tk.END)
        status_label.config(text="")
        upgrade_btn.config(state="disabled")

    frame.reset = reset
    return frame
