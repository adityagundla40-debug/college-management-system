import tkinter as tk
from tkinter import ttk, messagebox

BG_MAIN = "#f2f2f2"
BG_CARD = "#ffffff"
PRIMARY = "#2b6cb0"

TITLE_FONT = ("Segoe UI", 20, "bold")
LABEL_FONT = ("Segoe UI", 11)
ENTRY_FONT = ("Segoe UI", 11)
BUTTON_FONT = ("Segoe UI", 11, "bold")

def create(parent):
    frame = tk.Frame(parent, bg=BG_MAIN)

    # ================= TITLE =================
    tk.Label(
        frame,
        text="Issued Books",
        font=TITLE_FONT,
        bg=BG_MAIN
    ).pack(pady=(20, 10))

    # ================= SEARCH CARD =================
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
        search_card,
        text="Student Roll No",
        bg=BG_CARD,
        font=LABEL_FONT
    ).grid(row=0, column=0, sticky="w")

    roll_entry = tk.Entry(
        search_card,
        font=ENTRY_FONT,
        width=30
    )
    roll_entry.grid(row=0, column=1, padx=15)

    search_btn = tk.Button(
        search_card,
        text="Search",
        font=BUTTON_FONT,
        bg=PRIMARY,
        fg="white",
        padx=18,
        pady=6
    )
    search_btn.grid(row=0, column=2)

    # ================= TABLE CARD =================
    table_card = tk.Frame(
        frame,
        bg=BG_CARD,
        padx=20,
        pady=20,
        relief="solid",
        borderwidth=1
    )
    table_card.pack(fill="both", expand=True, padx=50, pady=15)

    columns = ("Book ID", "Book Name", "Roll No", "Issue Date", "Return Status")

    tree = ttk.Treeview(
        table_card,
        columns=columns,
        show="headings"
    )

    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, width=200, anchor="center")

    tree.pack(fill="both", expand=True)

    # ================= SAMPLE DATA (DB LATER) =================
    issued_books_data = [
        ("B101", "Python Basics", "23CE01", "01-08-2025", "Not Returned"),
        ("B102", "DBMS", "23CE02", "03-08-2025", "Returned"),
        ("B103", "OS Concepts", "23CE01", "05-08-2025", "Not Returned"),
        ("B104", "Data Structures", "23CE03", "07-08-2025", "Returned"),
    ]

    # ================= SEARCH LOGIC =================
    def search_by_roll():
        roll = roll_entry.get().strip()

        if not roll:
            messagebox.showwarning(
                "Input Required",
                "Please enter Roll No"
            )
            return

        # Clear table before showing results
        tree.delete(*tree.get_children())

        found = False
        for row in issued_books_data:
            if row[2] == roll:
                tree.insert("", "end", values=row)
                found = True

        if not found:
            messagebox.showinfo(
                "No Records",
                f"No issued books found for Roll No: {roll}"
            )

    search_btn.config(command=search_by_roll)

    # ================= RESET =================
    def reset():
        roll_entry.delete(0, tk.END)
        tree.delete(*tree.get_children())  # ✅ keep table empty

    frame.reset = reset
    return frame
