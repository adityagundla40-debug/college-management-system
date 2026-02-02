# College Management System

A comprehensive college management system built with Python and Tkinter, featuring separate modules for different administrative functions.

## Modules

### 1. Library Management System
Located in `Library/` folder
- **Main File**: `library.py`
- **Features**:
  - Add Books
  - Issue Books
  - Remove Books
  - Scrap Books
  - Issued Books Management

### 2. Office Management System
Located in `Office/` folder
- **Main File**: `office.py`
- **Features**:
  - Add Student
  - Monitor Students
  - Add Student Fee
  - Upgrade To Next Year
  - Issue Bonafide
  - Pass Out Students

### 3. HOD Management System
Located in `HOD/` folder
- **Main File**: `hod.py`
- **Features**:
  - Year-wise Student Admission Data
  - Fees Pending Student List
  - Staff Data List
  - All Student Data List

## How to Run

### Library Management System
```bash
cd Library
python library.py
```

### Office Management System
```bash
cd Office
python office.py
```

### HOD Management System
```bash
cd HOD
python hod.py
```

## System Requirements
- Python 3.x
- Tkinter (usually comes with Python)
- SQLite3 (for database operations)

## Features
- Modern GUI with consistent styling
- Menu bar with settings and about options
- Sidebar navigation with hover effects
- Data filtering and search capabilities
- Export functionality
- Database integration for data persistence

## Project Structure
```
college-management-system/
├── Library/
│   ├── library.py
│   └── modules/
│       ├── __init__.py
│       ├── welcome.py
│       ├── add_books.py
│       ├── issue_books.py
│       ├── remove_books.py
│       ├── scrap_books.py
│       └── issued_books.py
├── Office/
│   ├── office.py
│   ├── database/
│   │   └── db.py
│   └── modules/
│       ├── __init__.py
│       ├── welcome.py
│       ├── add_student.py
│       ├── monitor.py
│       ├── add_fee.py
│       ├── upgrade_year.py
│       ├── issue_bonafide.py
│       └── pass_out_students.py
├── HOD/
│   ├── hod.py
│   ├── database/
│   │   └── db.py
│   └── modules/
│       ├── __init__.py
│       ├── welcome.py
│       ├── year_wise_admission.py
│       ├── fees_pending_students.py
│       ├── staff_data_list.py
│       └── all_student_data.py
└── README.md
```

## Contributing
Feel free to contribute to this project by submitting pull requests or reporting issues.

## License
This project is open source and available under the MIT License.

##Team Members
1.Aditya Kolhapure 
2.Aditya Gundla
3.Shreyash Kabane
