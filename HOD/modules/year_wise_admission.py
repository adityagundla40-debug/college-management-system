import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime

BG_MAIN = "#f2f2f2"

def create(parent):
    frame = tk.Frame(parent, bg=BG_MAIN)
    
    # Title
    title_frame = tk.Frame(frame, bg=BG_MAIN)
    title_frame.pack(fill="x", padx=20, pady=(20, 10))
    
    tk.Label(
        title_frame,
        text="Year-wise Student Admission Data",
        font=("Segoe UI", 18, "bold"),
        bg=BG_MAIN,
        fg="#2b6cb0"
    ).pack(side="left")
    
    # Filter frame
    filter_frame = tk.LabelFrame(frame, text="Filters", font=("Segoe UI", 11, "bold"), 
                                bg=BG_MAIN, padx=10, pady=10)
    filter_frame.pack(fill="x", padx=20, pady=(0, 10))
    
    # Year selection
    tk.Label(filter_frame, text="Academic Year:", bg=BG_MAIN, font=("Segoe UI", 10)).grid(row=0, column=0, sticky="w", padx=(0, 10))
    year_var = tk.StringVar(value="2025-2026")
    year_combo = ttk.Combobox(filter_frame, textvariable=year_var, width=15, font=("Segoe UI", 10))
    year_combo['values'] = ("2025-2026", "2024-2025", "2023-2024", "2022-2023", "2021-2022")
    year_combo.grid(row=0, column=1, padx=(0, 20))
    
    # Branch selection
    tk.Label(filter_frame, text="Branch:", bg=BG_MAIN, font=("Segoe UI", 10)).grid(row=0, column=2, sticky="w", padx=(0, 10))
    branch_var = tk.StringVar(value="CM")
    branch_combo = ttk.Combobox(filter_frame, textvariable=branch_var, width=15, font=("Segoe UI", 10))
    branch_combo['values'] = ("CM",)
    branch_combo.grid(row=0, column=3, padx=(0, 20))
    
    # Search button
    def search_data():
        # Clear existing data
        for item in tree.get_children():
            tree.delete(item)
        
        # Sample data based on filters
        year = year_var.get()
        branch = branch_var.get()
        
        sample_data = [
            ("2025001", "Rahul Sharma", "CM", "First Year", "15-07-2025", "Active"),
            ("2025002", "Priya Patel", "EE", "First Year", "16-07-2025", "Active"),
            ("2025003", "Amit Kumar", "ENTC", "First Year", "17-07-2025", "Active"),
            ("2024001", "Sneha Singh", "CE", "Second Year", "15-07-2024", "Active"),
            ("2024002", "Vikram Joshi", "ME", "Second Year", "16-07-2024", "Active"),
            ("2023001", "Anita Desai", "CM", "Third Year", "15-07-2023", "Active"),
            ("2022001", "Ravi Gupta", "EE", "Final Year", "15-07-2022", "Active")
        ]
        
        # Filter data based on selection
        filtered_data = []
        for row in sample_data:
            if branch == "CM" or row[2] == branch:
                if year in row[0]:  # Simple year matching
                    filtered_data.append(row)
        
        # Insert filtered data
        for i, row in enumerate(filtered_data, 1):
            tree.insert("", "end", values=(i,) + row)
        
        status_label.config(text=f"Found {len(filtered_data)} records")
    
    tk.Button(filter_frame, text="Search", command=search_data, 
              bg="#2b6cb0", fg="white", font=("Segoe UI", 10, "bold"), 
              padx=15).grid(row=0, column=4, padx=(10, 0))
    
    # Data display frame
    data_frame = tk.Frame(frame, bg=BG_MAIN)
    data_frame.pack(fill="both", expand=True, padx=20, pady=(0, 20))
    
    # Treeview for data display
    columns = ("Sr No", "Student ID", "Name", "Branch", "Year", "Admission Date", "Status")
    tree = ttk.Treeview(data_frame, columns=columns, show="headings", height=15)
    
    # Define column headings and widths
    tree.heading("Sr No", text="Sr No")
    tree.heading("Student ID", text="Student ID")
    tree.heading("Name", text="Name")
    tree.heading("Branch", text="Branch")
    tree.heading("Year", text="Year")
    tree.heading("Admission Date", text="Admission Date")
    tree.heading("Status", text="Status")
    
    tree.column("Sr No", width=60, anchor="center")
    tree.column("Student ID", width=100, anchor="center")
    tree.column("Name", width=150, anchor="w")
    tree.column("Branch", width=80, anchor="center")
    tree.column("Year", width=100, anchor="center")
    tree.column("Admission Date", width=120, anchor="center")
    tree.column("Status", width=80, anchor="center")
    
    # Scrollbars
    v_scrollbar = ttk.Scrollbar(data_frame, orient="vertical", command=tree.yview)
    h_scrollbar = ttk.Scrollbar(data_frame, orient="horizontal", command=tree.xview)
    tree.configure(yscrollcommand=v_scrollbar.set, xscrollcommand=h_scrollbar.set)
    
    # Pack treeview and scrollbars
    tree.pack(side="left", fill="both", expand=True)
    v_scrollbar.pack(side="right", fill="y")
    h_scrollbar.pack(side="bottom", fill="x")
    
    # Status bar
    status_frame = tk.Frame(frame, bg=BG_MAIN)
    status_frame.pack(fill="x", padx=20, pady=(0, 10))
    
    status_label = tk.Label(status_frame, text="Ready", bg=BG_MAIN, font=("Segoe UI", 10))
    status_label.pack(side="left")
    
    def reset():
        # Clear all data
        for item in tree.get_children():
            tree.delete(item)
        year_var.set("2025-2026")
        branch_var.set("CM")
        status_label.config(text="Ready")
    
    frame.reset = reset
    return frame