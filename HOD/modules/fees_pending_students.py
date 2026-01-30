import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime, timedelta

BG_MAIN = "#f2f2f2"

def create(parent):
    frame = tk.Frame(parent, bg=BG_MAIN)
    
    # Title
    title_frame = tk.Frame(frame, bg=BG_MAIN)
    title_frame.pack(fill="x", padx=20, pady=(20, 10))
    
    tk.Label(
        title_frame,
        text="Fees Pending Student List",
        font=("Segoe UI", 18, "bold"),
        bg=BG_MAIN,
        fg="#dc2626"
    ).pack(side="left")
    
    # Filter frame
    filter_frame = tk.LabelFrame(frame, text="Filters", font=("Segoe UI", 11, "bold"), 
                                bg=BG_MAIN, padx=10, pady=10)
    filter_frame.pack(fill="x", padx=20, pady=(0, 10))
    
    # Branch selection
    tk.Label(filter_frame, text="Branch:", bg=BG_MAIN, font=("Segoe UI", 10)).grid(row=0, column=0, sticky="w", padx=(0, 10))
    branch_var = tk.StringVar(value="CM")
    branch_combo = ttk.Combobox(filter_frame, textvariable=branch_var, width=15, font=("Segoe UI", 10))
    branch_combo['values'] = ("CM",)
    branch_combo.grid(row=0, column=1, padx=(0, 20))
    
    # Year selection
    tk.Label(filter_frame, text="Year:", bg=BG_MAIN, font=("Segoe UI", 10)).grid(row=0, column=2, sticky="w", padx=(0, 10))
    year_var = tk.StringVar(value="All")
    year_combo = ttk.Combobox(filter_frame, textvariable=year_var, width=15, font=("Segoe UI", 10))
    year_combo['values'] = ("All", "First Year", "Second Year", "Third Year")
    year_combo.grid(row=0, column=3, padx=(0, 20))
    
    # Search button
    def search_data():
        # Clear existing data
        for item in tree.get_children():
            tree.delete(item)
        
        # Sample pending fees data
        sample_data = [
            ("2025001", "Rahul Sharma", "CM", "First Year", "Tuition Fee", "₹25,000", "15-01-2026", "Pending"),
            ("2025002", "Priya Patel", "CM", "First Year", "Exam Fee", "₹2,500", "20-01-2026", "Pending"),
            ("2024001", "Sneha Singh", "CM", "Second Year", "Library Fee", "₹1,000", "10-01-2026", "Overdue"),
            ("2024002", "Vikram Joshi", "CM", "Second Year", "Lab Fee", "₹5,000", "25-01-2026", "Overdue"),
            ("2023001", "Anita Desai", "CM", "Third Year", "Tuition Fee", "₹30,000", "05-01-2026", "Overdue"),
            ("2022001", "Ravi Gupta", "CM", "Third Year", "Exam Fee", "₹3,000", "12-01-2026", "Pending"),
            ("2025003", "Amit Kumar", "CM", "First Year", "Tuition Fee", "₹25,000", "28-01-2026", "Overdue")
        ]
        
        # Filter data based on selection
        filtered_data = []
        for row in sample_data:
            branch_match = branch_var.get() == "CM" or row[2] == branch_var.get()
            year_match = year_var.get() == "All" or row[3] == year_var.get()
            
            if branch_match and year_match:
                filtered_data.append(row)
        
        # Insert filtered data
        for i, row in enumerate(filtered_data, 1):
            # Color code based on overdue status
            tags = ()
            if "Overdue" in row[7]:
                tags = ("overdue",)
            elif "Pending" in row[7]:
                tags = ("pending",)
            
            tree.insert("", "end", values=(i,) + row, tags=tags)
        
        status_label.config(text=f"Found {len(filtered_data)} pending records")
        
        # Update summary
        total_amount = sum([int(row[5].replace("₹", "").replace(",", "")) for row in filtered_data])
        summary_label.config(text=f"Total Pending Amount: ₹{total_amount:,}")
    
    tk.Button(filter_frame, text="Search", command=search_data, 
              bg="#dc2626", fg="white", font=("Segoe UI", 10, "bold"), 
              padx=15).grid(row=0, column=4, padx=(10, 0))
    
    # Summary frame
    summary_frame = tk.Frame(frame, bg=BG_MAIN)
    summary_frame.pack(fill="x", padx=20, pady=(0, 10))
    
    summary_label = tk.Label(summary_frame, text="Total Pending Amount: ₹0", 
                            bg=BG_MAIN, font=("Segoe UI", 12, "bold"), fg="#dc2626")
    summary_label.pack(side="left")
    
    # Data display frame
    data_frame = tk.Frame(frame, bg=BG_MAIN)
    data_frame.pack(fill="both", expand=True, padx=20, pady=(0, 20))
    
    # Treeview for data display
    columns = ("Sr No", "Student ID", "Name", "Branch", "Year", "Fee Type", "Amount", "Due Date", "Status")
    tree = ttk.Treeview(data_frame, columns=columns, show="headings", height=12)
    
    # Define column headings and widths
    tree.heading("Sr No", text="Sr No")
    tree.heading("Student ID", text="Student ID")
    tree.heading("Name", text="Name")
    tree.heading("Branch", text="Branch")
    tree.heading("Year", text="Year")
    tree.heading("Fee Type", text="Fee Type")
    tree.heading("Amount", text="Amount")
    tree.heading("Due Date", text="Due Date")
    tree.heading("Status", text="Status")
    
    tree.column("Sr No", width=60, anchor="center")
    tree.column("Student ID", width=100, anchor="center")
    tree.column("Name", width=150, anchor="w")
    tree.column("Branch", width=80, anchor="center")
    tree.column("Year", width=100, anchor="center")
    tree.column("Fee Type", width=100, anchor="center")
    tree.column("Amount", width=100, anchor="e")
    tree.column("Due Date", width=100, anchor="center")
    tree.column("Status", width=100, anchor="center")
    
    # Configure tags for color coding
    tree.tag_configure("overdue", background="#ffebee", foreground="#c62828")
    tree.tag_configure("pending", background="#fff3e0", foreground="#ef6c00")
    
    # Scrollbars
    v_scrollbar = ttk.Scrollbar(data_frame, orient="vertical", command=tree.yview)
    h_scrollbar = ttk.Scrollbar(data_frame, orient="horizontal", command=tree.xview)
    tree.configure(yscrollcommand=v_scrollbar.set, xscrollcommand=h_scrollbar.set)
    
    # Pack treeview and scrollbars
    tree.pack(side="left", fill="both", expand=True)
    v_scrollbar.pack(side="right", fill="y")
    h_scrollbar.pack(side="bottom", fill="x")
    
    # Action buttons frame
    action_frame = tk.Frame(frame, bg=BG_MAIN)
    action_frame.pack(fill="x", padx=20, pady=(0, 10))
    
    def send_reminder():
        selected = tree.selection()
        if not selected:
            messagebox.showwarning("Selection", "Please select a student to send reminder.")
            return
        messagebox.showinfo("Reminder", "Reminder sent successfully!")
    
    tk.Button(action_frame, text="Send Reminder", command=send_reminder, 
              bg="#f59e0b", fg="white", font=("Segoe UI", 10, "bold"), 
              padx=15).pack(side="left", padx=(0, 10))
    
    # Status bar
    status_frame = tk.Frame(frame, bg=BG_MAIN)
    status_frame.pack(fill="x", padx=20, pady=(0, 10))
    
    status_label = tk.Label(status_frame, text="Ready", bg=BG_MAIN, font=("Segoe UI", 10))
    status_label.pack(side="left")
    
    # Load initial data
    def load_initial_data():
        search_data()  # Load data when frame is first created
    
    # Call initial data load after a short delay to ensure all widgets are created
    frame.after(100, load_initial_data)
    
    def reset():
        # Clear all data
        for item in tree.get_children():
            tree.delete(item)
        branch_var.set("CM")
        year_var.set("All")
        status_label.config(text="Ready")
        summary_label.config(text="Total Pending Amount: ₹0")
    
    frame.reset = reset
    return frame