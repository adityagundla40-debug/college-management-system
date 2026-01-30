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
        text="Staff Data List",
        font=("Segoe UI", 18, "bold"),
        bg=BG_MAIN,
        fg="#2b6cb0"
    ).pack(side="left")
    
    # Data display frame
    data_frame = tk.Frame(frame, bg=BG_MAIN)
    data_frame.pack(fill="both", expand=True, padx=20, pady=(0, 20))
    
    # Treeview for data display
    columns = ("Sr No", "Staff ID", "Name", "Department", "Designation", "Qualification", "Experience", "Salary", "Phone", "Email", "Address", "Status")
    tree = ttk.Treeview(data_frame, columns=columns, show="headings", height=12)
    
    # Define column headings and widths
    tree.heading("Sr No", text="Sr No")
    tree.heading("Staff ID", text="Staff ID")
    tree.heading("Name", text="Name")
    tree.heading("Department", text="Department")
    tree.heading("Designation", text="Designation")
    tree.heading("Qualification", text="Qualification")
    tree.heading("Experience", text="Experience")
    tree.heading("Salary", text="Salary")
    tree.heading("Phone", text="Phone")
    tree.heading("Email", text="Email")
    tree.heading("Address", text="Address")
    tree.heading("Status", text="Status")
    
    tree.column("Sr No", width=50, anchor="center")
    tree.column("Staff ID", width=80, anchor="center")
    tree.column("Name", width=130, anchor="w")
    tree.column("Department", width=120, anchor="w")
    tree.column("Designation", width=120, anchor="w")
    tree.column("Qualification", width=130, anchor="w")
    tree.column("Experience", width=80, anchor="center")
    tree.column("Salary", width=80, anchor="e")
    tree.column("Phone", width=100, anchor="center")
    tree.column("Email", width=180, anchor="w")
    tree.column("Address", width=150, anchor="w")
    tree.column("Status", width=80, anchor="center")
    
    # Configure tags for color coding
    tree.tag_configure("on_leave", background="#fff3e0", foreground="#ef6c00")
    tree.tag_configure("retired", background="#f3e5f5", foreground="#7b1fa2")
    tree.tag_configure("resigned", background="#ffebee", foreground="#c62828")
    
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
    
    def view_details():
        selected = tree.selection()
        if not selected:
            messagebox.showwarning("Selection", "Please select a staff member to view details.")
            return
        messagebox.showinfo("Details", "Staff details view will be implemented here.")
    
    def edit_staff():
        selected = tree.selection()
        if not selected:
            messagebox.showwarning("Selection", "Please select a staff member to edit.")
            return
        messagebox.showinfo("Edit", "Staff edit functionality will be implemented here.")
    
    tk.Button(action_frame, text="View Details", command=view_details, 
              bg="#17a2b8", fg="white", font=("Segoe UI", 10, "bold"), 
              padx=15).pack(side="left", padx=(0, 10))
    
    tk.Button(action_frame, text="Edit Staff", command=edit_staff, 
              bg="#ffc107", fg="black", font=("Segoe UI", 10, "bold"), 
              padx=15).pack(side="left", padx=(0, 10))
    
    # Status bar
    status_frame = tk.Frame(frame, bg=BG_MAIN)
    status_frame.pack(fill="x", padx=20, pady=(0, 10))
    
    status_label = tk.Label(status_frame, text="Ready", bg=BG_MAIN, font=("Segoe UI", 10))
    status_label.pack(side="left")
    
    # Load staff data function
    def load_staff_data():
        # Clear existing data
        for item in tree.get_children():
            tree.delete(item)
        
        # Sample staff data with addresses
        sample_data = [
            ("STF001", "Dr. Rajesh Kumar", "Computer Engineering", "Professor", "PhD Computer Science", "15 years", "₹85,000", "9876543210", "rajesh.kumar@college.edu", "Mumbai, Maharashtra", "Active"),
            ("STF002", "Prof. Sunita Sharma", "Computer Engineering", "Associate Professor", "ME Computer Engineering", "12 years", "₹75,000", "9876543211", "sunita.sharma@college.edu", "Pune, Maharashtra", "Active"),
            ("STF003", "Mr. Amit Patel", "Computer Engineering", "Assistant Professor", "BE Computer Engineering", "8 years", "₹65,000", "9876543212", "amit.patel@college.edu", "Nashik, Maharashtra", "Active"),
            ("STF004", "Dr. Priya Singh", "Computer Engineering", "Professor", "PhD Computer Science", "18 years", "₹90,000", "9876543213", "priya.singh@college.edu", "Thane, Maharashtra", "Active"),
            ("STF005", "Mr. Vikram Joshi", "Computer Engineering", "Assistant Professor", "ME Computer Science", "6 years", "₹60,000", "9876543214", "vikram.joshi@college.edu", "Aurangabad, Maharashtra", "On Leave"),
            ("STF006", "Ms. Anita Desai", "Computer Engineering", "Lecturer", "BE Computer Engineering", "4 years", "₹45,000", "9876543215", "anita.desai@college.edu", "Kolhapur, Maharashtra", "Active"),
            ("STF007", "Mr. Ravi Gupta", "Computer Engineering", "Lab Assistant", "Diploma Computer Engineering", "10 years", "₹35,000", "9876543216", "ravi.gupta@college.edu", "Solapur, Maharashtra", "Active"),
            ("STF008", "Dr. Neha Agarwal", "Computer Engineering", "HOD", "PhD Computer Science", "20 years", "₹1,20,000", "9876543217", "neha.agarwal@college.edu", "Navi Mumbai, Maharashtra", "Active")
        ]
        
        # Insert all staff data (no filtering needed since we removed filters)
        for i, row in enumerate(sample_data, 1):
            # Color code based on status
            tags = ()
            if row[10] == "On Leave":
                tags = ("on_leave",)
            elif row[10] == "Retired":
                tags = ("retired",)
            elif row[10] == "Resigned":
                tags = ("resigned",)
            
            tree.insert("", "end", values=(i,) + row, tags=tags)
        
        status_label.config(text=f"Total {len(sample_data)} staff records")
    
    # Load initial data
    load_staff_data()
    
    def reset():
        # Clear all data and reload
        load_staff_data()
        status_label.config(text="Ready")
    
    frame.reset = reset
    return frame