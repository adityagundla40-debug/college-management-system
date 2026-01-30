import tkinter as tk
from tkinter import messagebox, ttk
from datetime import datetime

from .theme import *

# Sample book data - replace with actual database connection
SAMPLE_BOOKS = [
    {"id": "B001", "name": "Python Programming", "author": "John Doe", "quantity": 5},
    {"id": "B002", "name": "Data Structures", "author": "Jane Smith", "quantity": 3},
    {"id": "B003", "name": "Machine Learning", "author": "Bob Johnson", "quantity": 7},
    {"id": "B004", "name": "Web Development", "author": "Alice Brown", "quantity": 2},
    {"id": "B005", "name": "Database Systems", "author": "Charlie Wilson", "quantity": 4},
]

def create(parent):
    frame = tk.Frame(parent, bg=BG_MAIN)

    tk.Label(frame, text="Scrap Books", font=TITLE_FONT, bg=BG_MAIN).pack(pady=20)

    # Search section
    search_card = tk.Frame(frame, bg=BG_CARD, padx=40, pady=30, relief="solid", borderwidth=1)
    search_card.pack(fill="x", padx=60, pady=(0, 20))

    tk.Label(search_card, text="Search by Book ID or Book Name:", bg=BG_CARD, font=LABEL_FONT).pack(anchor="w", pady=(0, 10))
    
    search_entry = tk.Entry(search_card, font=ENTRY_FONT, width=50)
    search_entry.pack(fill="x", pady=(0, 15))

    # Results section
    results_frame = tk.Frame(frame, bg=BG_MAIN)
    results_frame.pack(fill="both", expand=True, padx=60)

    # Canvas and scrollbar for scrollable results
    canvas = tk.Canvas(results_frame, bg=BG_MAIN, highlightthickness=0)
    scrollbar = ttk.Scrollbar(results_frame, orient="vertical", command=canvas.yview)
    scrollable_frame = tk.Frame(canvas, bg=BG_MAIN)

    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
    )

    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    def search_books():
        # Clear previous results
        for widget in scrollable_frame.winfo_children():
            widget.destroy()

        search_term = search_entry.get().strip().lower()
        if not search_term:
            tk.Label(scrollable_frame, text="Please enter a Book ID or Book Name to search", 
                    bg=BG_MAIN, font=LABEL_FONT, fg="red").pack(pady=20)
            return

        # Filter books based on search term
        matching_books = []
        for book in SAMPLE_BOOKS:
            if (search_term in book["id"].lower() or 
                search_term in book["name"].lower()):
                matching_books.append(book)

        if not matching_books:
            tk.Label(scrollable_frame, text="No books found matching your search", 
                    bg=BG_MAIN, font=LABEL_FONT, fg="red").pack(pady=20)
            return

        # Display matching books
        tk.Label(scrollable_frame, text=f"Found {len(matching_books)} book(s):", 
                bg=BG_MAIN, font=LABEL_FONT, fg=TEXT).pack(anchor="w", pady=(10, 20))

        for book in matching_books:
            create_book_row(scrollable_frame, book)

    def create_book_row(parent, book):
        # Book card
        book_card = tk.Frame(parent, bg=BG_CARD, padx=20, pady=15, relief="solid", borderwidth=1)
        book_card.pack(fill="x", pady=(0, 10))

        # Book info
        info_frame = tk.Frame(book_card, bg=BG_CARD)
        info_frame.pack(fill="x")

        tk.Label(info_frame, text=f"ID: {book['id']}", bg=BG_CARD, font=LABEL_FONT, fg=TEXT).grid(row=0, column=0, sticky="w", padx=(0, 20))
        tk.Label(info_frame, text=f"Name: {book['name']}", bg=BG_CARD, font=LABEL_FONT, fg=TEXT).grid(row=0, column=1, sticky="w", padx=(0, 20))
        tk.Label(info_frame, text=f"Author: {book['author']}", bg=BG_CARD, font=LABEL_FONT, fg=TEXT).grid(row=1, column=0, sticky="w", padx=(0, 20), pady=(5, 0))
        tk.Label(info_frame, text=f"Available: {book['quantity']}", bg=BG_CARD, font=LABEL_FONT, fg=TEXT).grid(row=1, column=1, sticky="w", padx=(0, 20), pady=(5, 0))

        # Controls frame
        controls_frame = tk.Frame(book_card, bg=BG_CARD)
        controls_frame.pack(fill="x", pady=(15, 0))

        # First row of controls
        controls_row1 = tk.Frame(controls_frame, bg=BG_CARD)
        controls_row1.pack(fill="x", pady=(0, 10))

        tk.Label(controls_row1, text="Quantity to scrap:", bg=BG_CARD, font=LABEL_FONT).pack(side="left")
        
        # Quantity dropdown
        quantity_var = tk.StringVar(value="1")
        quantity_dropdown = ttk.Combobox(controls_row1, textvariable=quantity_var, 
                                       values=[str(i) for i in range(1, book['quantity'] + 1)], 
                                       state="readonly", width=5)
        quantity_dropdown.pack(side="left", padx=(10, 0))

        # Second row of controls
        controls_row2 = tk.Frame(controls_frame, bg=BG_CARD)
        controls_row2.pack(fill="x", pady=(0, 10))

        tk.Label(controls_row2, text="Reason for scrap:", bg=BG_CARD, font=LABEL_FONT).pack(side="left")
        
        reason_var = tk.StringVar()
        reason_dropdown = ttk.Combobox(controls_row2, textvariable=reason_var, 
                                     values=["Damaged", "Lost", "Outdated", "Torn Pages", "Water Damage", "Other"], 
                                     state="readonly", width=15)
        reason_dropdown.pack(side="left", padx=(10, 0))
        reason_dropdown.set("Damaged")  # Default value

        # Third row for custom reason (if "Other" is selected)
        custom_reason_frame = tk.Frame(controls_frame, bg=BG_CARD)
        custom_reason_entry = tk.Entry(custom_reason_frame, font=ENTRY_FONT, width=30)

        def on_reason_change(event):
            if reason_var.get() == "Other":
                custom_reason_frame.pack(fill="x", pady=(5, 10))
                tk.Label(custom_reason_frame, text="Custom reason:", bg=BG_CARD, font=LABEL_FONT).pack(side="left")
                custom_reason_entry.pack(side="left", padx=(10, 0))
            else:
                custom_reason_frame.pack_forget()

        reason_dropdown.bind("<<ComboboxSelected>>", on_reason_change)

        # Action buttons frame
        buttons_frame = tk.Frame(controls_frame, bg=BG_CARD)
        buttons_frame.pack(fill="x", pady=(10, 0))

        def scrap_book():
            qty_to_scrap = int(quantity_var.get())
            reason = reason_var.get()
            
            if reason == "Other":
                custom_reason = custom_reason_entry.get().strip()
                if not custom_reason:
                    messagebox.showerror("Error", "Please provide a custom reason for scrapping")
                    return
                reason = custom_reason
            
            if not reason:
                messagebox.showerror("Error", "Please select a reason for scrapping")
                return

            current_date = datetime.now().strftime("%Y-%m-%d")
            
            result = messagebox.askyesno(
                "Confirm Scrap", 
                f"Are you sure you want to scrap {qty_to_scrap} copy(ies) of '{book['name']}'?\n\n"
                f"Reason: {reason}\n"
                f"Date: {current_date}\n\n"
                f"This action cannot be undone."
            )
            
            if result:
                # Update book quantity (in real implementation, update database and log scrap record)
                book['quantity'] -= qty_to_scrap
                if book['quantity'] <= 0:
                    SAMPLE_BOOKS.remove(book)
                    messagebox.showinfo("Success", 
                        f"Book '{book['name']}' completely scrapped from library\n"
                        f"Reason: {reason}\n"
                        f"Date: {current_date}")
                else:
                    messagebox.showinfo("Success", 
                        f"{qty_to_scrap} copy(ies) of '{book['name']}' scrapped. {book['quantity']} remaining.\n"
                        f"Reason: {reason}\n"
                        f"Date: {current_date}")
                
                # Refresh search results
                search_books()

        scrap_btn = tk.Button(buttons_frame, text="Scrap Book", font=BUTTON_FONT,
                             bg=PRIMARY, fg="white", padx=15, pady=5,
                             command=scrap_book)
        scrap_btn.pack(side="right")

    # Search button
    search_btn = tk.Button(search_card, text="Search Books", font=BUTTON_FONT,
                          bg=PRIMARY, fg="white", padx=20, pady=8,
                          command=search_books)
    search_btn.pack(pady=(0, 10))

    # Pack canvas and scrollbar
    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    # Bind mousewheel to canvas
    def _on_mousewheel(event):
        canvas.yview_scroll(int(-1*(event.delta/120)), "units")
    canvas.bind_all("<MouseWheel>", _on_mousewheel)

    # Bind Enter key to search
    search_entry.bind("<Return>", lambda e: search_books())

    def reset():
        search_entry.delete(0, tk.END)
        for widget in scrollable_frame.winfo_children():
            widget.destroy()

    frame.reset = reset
    return frame
