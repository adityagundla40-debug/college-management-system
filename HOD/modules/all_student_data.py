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
        text="All Student Data List",
        font=("Segoe UI", 18, "bold"),
        bg=BG_MAIN,
        fg="#2b6cb0"
    ).pack(side="left")
    
    # Filter frame
    filter_frame = tk.LabelFrame(frame, text="Search", font=("Segoe UI", 11, "bold"), 
                                bg=BG_MAIN, padx=10, pady=10)
    filter_frame.pack(fill="x", padx=20, pady=(0, 10))
    
    # Search box
    tk.Label(filter_frame, text="Search:", bg=BG_MAIN, font=("Segoe UI", 10)).grid(row=0, column=0, sticky="w", padx=(0, 10))
    search_var = tk.StringVar()
    search_entry = tk.Entry(filter_frame, textvariable=search_var, width=30, font=("Segoe UI", 10))
    search_entry.insert(0, "Enter roll no")
    search_entry.config(fg="gray")
    search_entry.grid(row=0, column=1, sticky="ew", padx=(0, 15))
    
    # Placeholder functionality
    def on_focus_in(event):
        if search_entry.get() == "Enter roll no":
            search_entry.delete(0, tk.END)
            search_entry.config(fg="black")
    
    def on_focus_out(event):
        if search_entry.get() == "":
            search_entry.insert(0, "Enter roll no")
            search_entry.config(fg="gray")
    
    search_entry.bind("<FocusIn>", on_focus_in)
    search_entry.bind("<FocusOut>", on_focus_out)
    
    # Search button
    def search_data():
        # Clear existing data
        for item in tree.get_children():
            tree.delete(item)
        
        # Sample comprehensive student data (only CM students)
        sample_data = [
            ("2025001", "Rahul Sharma", "CM", "First Year", "Male", "01-05-2007", "9876543210", "rahul.sharma@student.edu", "Mumbai", "Active", "15-07-2025"),
            ("2025002", "Priya Patel", "CM", "First Year", "Female", "15-03-2007", "9876543211", "priya.patel@student.edu", "Pune", "Active", "16-07-2025"),
            ("2025003", "Amit Kumar", "CM", "First Year", "Male", "22-08-2006", "9876543212", "amit.kumar@student.edu", "Nashik", "Active", "17-07-2025"),
            ("2024001", "Sneha Singh", "CM", "Second Year", "Female", "10-12-2005", "9876543213", "sneha.singh@student.edu", "Nagpur", "Active", "15-07-2024"),
            ("2024002", "Vikram Joshi", "CM", "Second Year", "Male", "25-09-2005", "9876543214", "vikram.joshi@student.edu", "Aurangabad", "Inactive", "16-07-2024"),
            ("2023001", "Anita Desai", "CM", "Third Year", "Female", "18-06-2004", "9876543215", "anita.desai@student.edu", "Kolhapur", "Active", "15-07-2023"),
            ("2023002", "Ravi Gupta", "CM", "Third Year", "Male", "30-11-2004", "9876543216", "ravi.gupta@student.edu", "Solapur", "Active", "16-07-2023")
        ]
        
        # Filter data based on search
        filtered_data = []
        search_term = search_var.get().lower().strip()
        
        # Skip search if placeholder text is still there
        if search_term == "" or search_term == "enter roll no":
            filtered_data = sample_data
        else:
            # Search by Student ID (roll number)
            for row in sample_data:
                if search_term in row[0].lower():  # Search in Student ID
                    filtered_data.append(row)
        
        # Insert filtered data
        for i, row in enumerate(filtered_data, 1):
            # Color code based on status
            tags = ()
            if row[9] == "Inactive":
                tags = ("inactive",)
            elif row[9] == "Passed Out":
                tags = ("passed_out",)
            elif row[9] == "Dropped":
                tags = ("dropped",)
            
            tree.insert("", "end", values=(i,) + row, tags=tags)
        
        status_label.config(text=f"Found {len(filtered_data)} student records")
        
        # Update statistics
        active_count = len([row for row in filtered_data if row[9] == "Active"])
        inactive_count = len([row for row in filtered_data if row[9] == "Inactive"])
        passed_out_count = len([row for row in filtered_data if row[9] == "Passed Out"])
        stats_label.config(text=f"Total Students: {len(filtered_data)} | Active: {active_count} | Inactive: {inactive_count} | Passed Out: {passed_out_count}")
    
    tk.Button(filter_frame, text="Search", command=search_data, 
              bg="#2b6cb0", fg="white", font=("Segoe UI", 10, "bold"), 
              padx=15).grid(row=0, column=2, padx=(10, 0))
    
    # Bind Enter key to search
    search_entry.bind("<Return>", lambda event: search_data())
    
    # Load initial data
    def load_initial_data():
        search_data()  # Load all data initially
    
    # Call initial data load after a short delay
    frame.after(100, load_initial_data)
    
    # Statistics frame
    stats_frame = tk.Frame(frame, bg=BG_MAIN)
    stats_frame.pack(fill="x", padx=20, pady=(0, 10))
    
    stats_label = tk.Label(stats_frame, text="Total Students: 0 | Active: 0 | Inactive: 0 | Passed Out: 0", 
                          bg=BG_MAIN, font=("Segoe UI", 11, "bold"), fg="#2b6cb0")
    stats_label.pack(side="left")
    
    # Data display frame
    data_frame = tk.Frame(frame, bg=BG_MAIN)
    data_frame.pack(fill="both", expand=True, padx=20, pady=(0, 20))
    
    # Treeview for data display
    columns = ("Sr No", "Student ID", "Name", "Branch", "Year", "Gender", "DOB", "Phone", "Email", "Address", "Status", "Admission Date")
    tree = ttk.Treeview(data_frame, columns=columns, show="headings", height=10)
    
    # Define column headings and widths
    tree.heading("Sr No", text="Sr No")
    tree.heading("Student ID", text="Student ID")
    tree.heading("Name", text="Name")
    tree.heading("Branch", text="Branch")
    tree.heading("Year", text="Year")
    tree.heading("Gender", text="Gender")
    tree.heading("DOB", text="Date of Birth")
    tree.heading("Phone", text="Phone")
    tree.heading("Email", text="Email")
    tree.heading("Address", text="Address")
    tree.heading("Status", text="Status")
    tree.heading("Admission Date", text="Admission Date")
    
    tree.column("Sr No", width=50, anchor="center")
    tree.column("Student ID", width=90, anchor="center")
    tree.column("Name", width=130, anchor="w")
    tree.column("Branch", width=70, anchor="center")
    tree.column("Year", width=90, anchor="center")
    tree.column("Gender", width=70, anchor="center")
    tree.column("DOB", width=100, anchor="center")
    tree.column("Phone", width=100, anchor="center")
    tree.column("Email", width=180, anchor="w")
    tree.column("Address", width=120, anchor="w")
    tree.column("Status", width=80, anchor="center")
    tree.column("Admission Date", width=110, anchor="center")
    
    # Configure tags for color coding
    tree.tag_configure("inactive", background="#fff3e0", foreground="#ef6c00")
    tree.tag_configure("passed_out", background="#e8f5e8", foreground="#2e7d32")
    tree.tag_configure("dropped", background="#ffebee", foreground="#c62828")
    
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
    
    def view_student():
        selected = tree.selection()
        if not selected:
            messagebox.showwarning("Selection", "Please select a student to view details.")
            return
        messagebox.showinfo("Student Details", "Student details view will be implemented here.")
    
    def edit_student():
        selected = tree.selection()
        if not selected:
            messagebox.showwarning("Selection", "Please select a student to edit.")
            return
        messagebox.showinfo("Edit Student", "Student edit functionality will be implemented here.")
    
    tk.Button(action_frame, text="View Details", command=view_student, 
              bg="#17a2b8", fg="white", font=("Segoe UI", 10, "bold"), 
              padx=15).pack(side="left", padx=(0, 10))
    
    tk.Button(action_frame, text="Edit Student", command=edit_student, 
              bg="#ffc107", fg="black", font=("Segoe UI", 10, "bold"), 
              padx=15).pack(side="left", padx=(0, 10))
    
    # Status bar
    status_frame = tk.Frame(frame, bg=BG_MAIN)
    status_frame.pack(fill="x", padx=20, pady=(0, 10))
    
    status_label = tk.Label(status_frame, text="Ready", bg=BG_MAIN, font=("Segoe UI", 10))
    status_label.pack(side="left")
    
    def reset():
        # Clear all data
        for item in tree.get_children():
            tree.delete(item)
        search_var.set("")
        search_entry.delete(0, tk.END)
        search_entry.insert(0, "Enter roll no")
        search_entry.config(fg="gray")
        status_label.config(text="Ready")
        stats_label.config(text="Total Students: 0 | Active: 0 | Inactive: 0 | Passed Out: 0")
    
    frame.reset = reset
    return frame