import tkinter as tk
from tkinter import ttk, messagebox
import re

BG_MAIN = "#eeeeee"

def create(parent):
    frame = tk.Frame(parent, bg=BG_MAIN)
    
    # Title
    title_frame = tk.Frame(frame, bg=BG_MAIN)
    title_frame.pack(fill="x", padx=20, pady=(20, 10))
    
    tk.Label(
        title_frame,
        text="Add New Staff",
        font=("Segoe UI", 18, "bold"),
        bg=BG_MAIN,
        fg="#28a745"
    ).pack(side="left")
    
    # Main content frame with scrollable area
    main_content = tk.Frame(frame, bg=BG_MAIN)
    main_content.pack(fill="both", expand=True, padx=20, pady=(0, 20))
    
    # Form frame
    form_frame = tk.LabelFrame(main_content, text="Staff Information", 
                              font=("Segoe UI", 12, "bold"), bg=BG_MAIN, padx=20, pady=20)
    form_frame.pack(fill="x", pady=(0, 20))
    
    # Input variables
    name_var = tk.StringVar()
    phone_var = tk.StringVar()
    address_var = tk.StringVar()
    qualification_var = tk.StringVar()
    experience_var = tk.StringVar()
    email_var = tk.StringVar()
    department_var = tk.StringVar(value="CM")
    designation_var = tk.StringVar(value="Assistant Professor")
    
    # Name field
    tk.Label(form_frame, text="Full Name *", bg=BG_MAIN, font=("Segoe UI", 11, "bold")).grid(
        row=0, column=0, sticky="w", padx=(0, 10), pady=(10, 5))
    name_entry = tk.Entry(form_frame, textvariable=name_var, width=40, font=("Segoe UI", 11))
    name_entry.grid(row=0, column=1, sticky="ew", padx=(0, 20), pady=(10, 5))
    
    # Phone field
    tk.Label(form_frame, text="Phone Number *", bg=BG_MAIN, font=("Segoe UI", 11, "bold")).grid(
        row=1, column=0, sticky="w", padx=(0, 10), pady=5)
    phone_entry = tk.Entry(form_frame, textvariable=phone_var, width=40, font=("Segoe UI", 11))
    phone_entry.grid(row=1, column=1, sticky="ew", padx=(0, 20), pady=5)
    
    # Email field
    tk.Label(form_frame, text="Email Address *", bg=BG_MAIN, font=("Segoe UI", 11, "bold")).grid(
        row=2, column=0, sticky="w", padx=(0, 10), pady=5)
    email_entry = tk.Entry(form_frame, textvariable=email_var, width=40, font=("Segoe UI", 11))
    email_entry.grid(row=2, column=1, sticky="ew", padx=(0, 20), pady=5)
    
    # Department field
    tk.Label(form_frame, text="Department *", bg=BG_MAIN, font=("Segoe UI", 11, "bold")).grid(
        row=3, column=0, sticky="w", padx=(0, 10), pady=5)
    department_combo = ttk.Combobox(form_frame, textvariable=department_var, width=37, font=("Segoe UI", 11))
    department_combo['values'] = ("CM", "ME", "CE", "EE", "ENTC")
    department_combo['state'] = 'readonly'
    department_combo.grid(row=3, column=1, sticky="ew", padx=(0, 20), pady=5)
    
    # Designation field
    tk.Label(form_frame, text="Designation *", bg=BG_MAIN, font=("Segoe UI", 11, "bold")).grid(
        row=4, column=0, sticky="w", padx=(0, 10), pady=5)
    designation_combo = ttk.Combobox(form_frame, textvariable=designation_var, width=37, font=("Segoe UI", 11))
    designation_combo['values'] = ("Professor", "Associate Professor", "Assistant Professor", "Lecturer", "Lab Assistant", "HOD", "Principal", "Admin Staff", "Clerk", "Librarian", "Lab Technician")
    designation_combo['state'] = 'readonly'
    designation_combo.grid(row=4, column=1, sticky="ew", padx=(0, 20), pady=5)
    
    # Address field
    tk.Label(form_frame, text="Address *", bg=BG_MAIN, font=("Segoe UI", 11, "bold")).grid(
        row=5, column=0, sticky="nw", padx=(0, 10), pady=5)
    address_text = tk.Text(form_frame, width=40, height=3, font=("Segoe UI", 11))
    address_text.grid(row=5, column=1, sticky="ew", padx=(0, 20), pady=5)
    
    # Qualification field
    tk.Label(form_frame, text="Qualification *", bg=BG_MAIN, font=("Segoe UI", 11, "bold")).grid(
        row=6, column=0, sticky="w", padx=(0, 10), pady=5)
    qualification_entry = tk.Entry(form_frame, textvariable=qualification_var, width=40, font=("Segoe UI", 11))
    qualification_entry.grid(row=6, column=1, sticky="ew", padx=(0, 20), pady=5)
    
    # Experience field
    tk.Label(form_frame, text="Experience (Years) *", bg=BG_MAIN, font=("Segoe UI", 11, "bold")).grid(
        row=7, column=0, sticky="w", padx=(0, 10), pady=5)
    experience_entry = tk.Entry(form_frame, textvariable=experience_var, width=40, font=("Segoe UI", 11))
    experience_entry.grid(row=7, column=1, sticky="ew", padx=(0, 20), pady=5)
    
    # Configure grid weights for responsive design
    form_frame.grid_columnconfigure(1, weight=1)
    
    # Validation functions
    def validate_email(email):
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(pattern, email) is not None
    
    def validate_phone(phone):
        # Remove any spaces or special characters
        phone_clean = re.sub(r'[^\d]', '', phone)
        return len(phone_clean) == 10 and phone_clean.isdigit()
    
    def validate_experience(exp):
        try:
            exp_num = float(exp)
            return 0 <= exp_num <= 50
        except ValueError:
            return False
    
    # Button frame
    button_frame = tk.Frame(main_content, bg=BG_MAIN)
    button_frame.pack(fill="x", pady=(10, 0))
    
    def clear_form():
        """Clear all form fields"""
        name_var.set("")
        phone_var.set("")
        email_var.set("")
        department_var.set("CM")
        designation_var.set("Assistant Professor")
        address_text.delete("1.0", tk.END)
        qualification_var.set("")
        experience_var.set("")
        status_label.config(text="Form cleared", fg="#6c757d")
    
    def save_staff():
        """Save staff information"""
        # Get values
        name = name_var.get().strip()
        phone = phone_var.get().strip()
        email = email_var.get().strip()
        department = department_var.get().strip()
        designation = designation_var.get().strip()
        address = address_text.get("1.0", tk.END).strip()
        qualification = qualification_var.get().strip()
        experience = experience_var.get().strip()
        
        # Validation
        errors = []
        
        if not name:
            errors.append("Name is required")
        elif len(name) < 2:
            errors.append("Name must be at least 2 characters")
        
        if not phone:
            errors.append("Phone number is required")
        elif not validate_phone(phone):
            errors.append("Phone number must be 10 digits")
        
        if not email:
            errors.append("Email is required")
        elif not validate_email(email):
            errors.append("Invalid email format")
        
        if not department:
            errors.append("Department is required")
        
        if not designation:
            errors.append("Designation is required")
        
        if not address:
            errors.append("Address is required")
        elif len(address) < 10:
            errors.append("Address must be at least 10 characters")
        
        if not qualification:
            errors.append("Qualification is required")
        elif len(qualification) < 2:
            errors.append("Qualification must be at least 2 characters")
        
        if not experience:
            errors.append("Experience is required")
        elif not validate_experience(experience):
            errors.append("Experience must be a number between 0 and 50")
        
        if errors:
            error_msg = "Please fix the following errors:\n\n" + "\n".join(f"• {error}" for error in errors)
            messagebox.showerror("Validation Error", error_msg)
            status_label.config(text="Please fix validation errors", fg="#dc3545")
            return
        
        # If validation passes, show success message
        success_msg = f"""Staff member added successfully!
        
Name: {name}
Phone: {phone}
Email: {email}
Department: {department}
Designation: {designation}
Address: {address[:50]}{'...' if len(address) > 50 else ''}
Qualification: {qualification}
Experience: {experience} years"""
        
        messagebox.showinfo("Success", success_msg)
        status_label.config(text="Staff member added successfully!", fg="#28a745")
        
        # Clear form after successful save
        clear_form()
    
    # Buttons
    tk.Button(button_frame, text="Save Staff", command=save_staff,
              bg="#28a745", fg="white", font=("Segoe UI", 11, "bold"),
              padx=20, pady=8).pack(side="left", padx=(0, 10))
    
    tk.Button(button_frame, text="Clear Form", command=clear_form,
              bg="#6c757d", fg="white", font=("Segoe UI", 11, "bold"),
              padx=20, pady=8).pack(side="left")
    
    # Status label
    status_frame = tk.Frame(main_content, bg=BG_MAIN)
    status_frame.pack(fill="x", pady=(20, 0))
    
    status_label = tk.Label(status_frame, text="Ready to add new staff member", 
                           bg=BG_MAIN, font=("Segoe UI", 10), fg="#6c757d")
    status_label.pack(side="left")
    
    # Instructions
    instructions_frame = tk.LabelFrame(main_content, text="Instructions", 
                                     font=("Segoe UI", 11, "bold"), bg=BG_MAIN, padx=15, pady=10)
    instructions_frame.pack(fill="x", pady=(20, 0))
    
    instructions_text = """• All fields marked with * are required
• Phone number should be 10 digits
• Email must be in valid format (example@domain.com)
• Select appropriate department from dropdown (CM, ME, CE, EE, ENTC)
• Select appropriate designation from dropdown
• Address should be detailed and at least 10 characters
• Experience should be in years (can include decimals like 2.5)
• Click 'Save Staff' to add the staff member
• Click 'Clear Form' to reset all fields"""
    
    tk.Label(instructions_frame, text=instructions_text, bg=BG_MAIN, 
             font=("Segoe UI", 10), justify="left", fg="#495057").pack(anchor="w")
    
    def reset():
        """Reset the form"""
        clear_form()
        status_label.config(text="Ready to add new staff member", fg="#6c757d")
    
    frame.reset = reset
    return frame