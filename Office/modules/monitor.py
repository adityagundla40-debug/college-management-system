import tkinter as tk

BG_MAIN = "#f2f2f2"
BG_CARD = "#ffffff"
PRIMARY = "#2b6cb0"
TEXT = "#1f2937"

TITLE_FONT = ("Segoe UI", 20, "bold")
LABEL_FONT = ("Segoe UI", 11)
LABEL_BOLD = ("Segoe UI", 11, "bold")
ENTRY_FONT = ("Segoe UI", 11)
BUTTON_FONT = ("Segoe UI", 11, "bold")


def create(parent):
    frame = tk.Frame(parent, bg=BG_MAIN)

    # TITLE
    tk.Label(
        frame, text="Monitor Student",
        font=TITLE_FONT,
        bg=BG_MAIN, fg=TEXT
    ).pack(pady=(20, 10))

    # SEARCH CARD
    search_card = tk.Frame(
        frame,
        bg=BG_CARD,
        padx=30,
        pady=20,
        relief="solid",
        borderwidth=1
    )
    search_card.pack(fill="x", padx=50, pady=10)

    tk.Label(
        search_card, text="Roll No:",
        bg=BG_CARD, font=LABEL_FONT
    ).grid(row=0, column=0, pady=5)

    roll_entry = tk.Entry(search_card, font=LABEL_FONT, width=30)
    roll_entry.grid(row=0, column=1, padx=15, pady=5)

    search_btn = tk.Button(
        search_card,
        text="Search",
        font=BUTTON_FONT,
        bg=PRIMARY,
        fg="white",
        padx=16,
        pady=6,
        relief="flat"
    )
    search_btn.grid(row=0, column=2)

    # DETAILS CARD
    details_card = tk.Frame(
        frame,
        bg=BG_CARD,
        padx=40,
        pady=25,
        relief="solid",
        borderwidth=1
    )
    details_card.pack(fill="both", expand=True, padx=50, pady=15)

    fields = [
        "Student Name", "Branch", "Current Year",
        "Admission Date", "Admission Type",
        "Caste", "Scholarship Filled",
        "Fees Paid", "Fees Pending",
        "Contact No", "Aadhar No",
        "Enrollment No", "Address",
        "Documents Submitted"
    ]

    labels = {}

    for i, field in enumerate(fields):
        tk.Label(
            details_card, text=f"{field}:",
            bg=BG_CARD, font=LABEL_BOLD,
            anchor="w"
        ).grid(row=i, column=0, sticky="w", pady=6)

        val = tk.Label(
            details_card, text="",
            bg=BG_CARD, font=LABEL_FONT,
            anchor="w"
        )
        val.grid(row=i, column=1, sticky="w", pady=6)

        labels[field] = val

    details_card.grid_columnconfigure(1, weight=1)

    # SEARCH LOGIC (placeholder)
    def search_student():
        data = {
            "Student Name": "Rahul Patil",
            "Branch": "Computer Engineering",
            "Current Year": "Second Year",
            "Admission Date": "15-08-2024",
            "Admission Type": "CAP",
            "Caste": "OBC",
            "Scholarship Filled": "Yes",
            "Fees Paid": "₹45,000",
            "Fees Pending": "₹15,000",
            "Contact No": "9876543210",
            "Aadhar No": "1234-5678-9012",
            "Enrollment No": "ENR2024CSE102",
            "Address": "Pune, Maharashtra",
            "Documents Submitted": "10th, 12th, LC, Caste Certificate"
        }

        for k, lbl in labels.items():
            lbl.config(text=data.get(k, "-"))

    search_btn.config(command=search_student)

    # RESET
    def reset():
        roll_entry.delete(0, tk.END)
        for lbl in labels.values():
            lbl.config(text="")

    frame.reset = reset
    return frame
