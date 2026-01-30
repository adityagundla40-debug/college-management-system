# HOD Management System Database Module
# This module handles all database operations for the HOD system

import sqlite3
import os
from datetime import datetime

class HODDatabase:
    def __init__(self):
        self.db_path = "hod_management.db"
        self.init_database()
    
    def init_database(self):
        """Initialize the database with required tables"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        # Students table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS students (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                student_id TEXT UNIQUE NOT NULL,
                name TEXT NOT NULL,
                branch TEXT NOT NULL,
                year TEXT NOT NULL,
                gender TEXT,
                dob TEXT,
                phone TEXT,
                email TEXT,
                address TEXT,
                status TEXT DEFAULT 'Active',
                admission_date TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        
        # Staff table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS staff (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                staff_id TEXT UNIQUE NOT NULL,
                name TEXT NOT NULL,
                department TEXT NOT NULL,
                designation TEXT NOT NULL,
                qualification TEXT,
                experience TEXT,
                salary TEXT,
                phone TEXT,
                email TEXT,
                status TEXT DEFAULT 'Active',
                joining_date TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        
        # Fees table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS fees (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                student_id TEXT NOT NULL,
                fee_type TEXT NOT NULL,
                amount REAL NOT NULL,
                due_date TEXT,
                paid_date TEXT,
                status TEXT DEFAULT 'Pending',
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (student_id) REFERENCES students (student_id)
            )
        ''')
        
        # Admission data table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS admissions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                student_id TEXT NOT NULL,
                academic_year TEXT NOT NULL,
                admission_date TEXT NOT NULL,
                branch TEXT NOT NULL,
                year TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (student_id) REFERENCES students (student_id)
            )
        ''')
        
        conn.commit()
        conn.close()
    
    def get_connection(self):
        """Get database connection"""
        return sqlite3.connect(self.db_path)
    
    # Student operations
    def add_student(self, student_data):
        """Add a new student"""
        conn = self.get_connection()
        cursor = conn.cursor()
        
        try:
            cursor.execute('''
                INSERT INTO students (student_id, name, branch, year, gender, dob, 
                                    phone, email, address, admission_date)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', student_data)
            conn.commit()
            return True
        except sqlite3.IntegrityError:
            return False
        finally:
            conn.close()
    
    def get_students(self, filters=None):
        """Get students with optional filters"""
        conn = self.get_connection()
        cursor = conn.cursor()
        
        query = "SELECT * FROM students WHERE 1=1"
        params = []
        
        if filters:
            if filters.get('branch') and filters['branch'] != 'All':
                query += " AND branch = ?"
                params.append(filters['branch'])
            if filters.get('year') and filters['year'] != 'All':
                query += " AND year = ?"
                params.append(filters['year'])
            if filters.get('status') and filters['status'] != 'All':
                query += " AND status = ?"
                params.append(filters['status'])
        
        cursor.execute(query, params)
        results = cursor.fetchall()
        conn.close()
        return results
    
    # Staff operations
    def add_staff(self, staff_data):
        """Add a new staff member"""
        conn = self.get_connection()
        cursor = conn.cursor()
        
        try:
            cursor.execute('''
                INSERT INTO staff (staff_id, name, department, designation, 
                                 qualification, experience, salary, phone, email, joining_date)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', staff_data)
            conn.commit()
            return True
        except sqlite3.IntegrityError:
            return False
        finally:
            conn.close()
    
    def get_staff(self, filters=None):
        """Get staff with optional filters"""
        conn = self.get_connection()
        cursor = conn.cursor()
        
        query = "SELECT * FROM staff WHERE 1=1"
        params = []
        
        if filters:
            if filters.get('department') and filters['department'] != 'All':
                query += " AND department = ?"
                params.append(filters['department'])
            if filters.get('designation') and filters['designation'] != 'All':
                query += " AND designation = ?"
                params.append(filters['designation'])
            if filters.get('status') and filters['status'] != 'All':
                query += " AND status = ?"
                params.append(filters['status'])
        
        cursor.execute(query, params)
        results = cursor.fetchall()
        conn.close()
        return results
    
    # Fees operations
    def add_fee_record(self, fee_data):
        """Add a fee record"""
        conn = self.get_connection()
        cursor = conn.cursor()
        
        cursor.execute('''
            INSERT INTO fees (student_id, fee_type, amount, due_date, status)
            VALUES (?, ?, ?, ?, ?)
        ''', fee_data)
        conn.commit()
        conn.close()
        return True
    
    def get_pending_fees(self, filters=None):
        """Get pending fees with student details"""
        conn = self.get_connection()
        cursor = conn.cursor()
        
        query = '''
            SELECT f.*, s.name, s.branch, s.year 
            FROM fees f 
            JOIN students s ON f.student_id = s.student_id 
            WHERE f.status = 'Pending'
        '''
        params = []
        
        if filters:
            if filters.get('branch') and filters['branch'] != 'All':
                query += " AND s.branch = ?"
                params.append(filters['branch'])
            if filters.get('year') and filters['year'] != 'All':
                query += " AND s.year = ?"
                params.append(filters['year'])
            if filters.get('fee_type') and filters['fee_type'] != 'All':
                query += " AND f.fee_type = ?"
                params.append(filters['fee_type'])
        
        cursor.execute(query, params)
        results = cursor.fetchall()
        conn.close()
        return results
    
    # Admission operations
    def get_year_wise_admissions(self, filters=None):
        """Get year-wise admission data"""
        conn = self.get_connection()
        cursor = conn.cursor()
        
        query = '''
            SELECT s.student_id, s.name, s.branch, s.year, s.admission_date, s.status
            FROM students s
            WHERE 1=1
        '''
        params = []
        
        if filters:
            if filters.get('academic_year'):
                query += " AND s.admission_date LIKE ?"
                params.append(f"%{filters['academic_year'][:4]}%")
            if filters.get('branch') and filters['branch'] != 'All':
                query += " AND s.branch = ?"
                params.append(filters['branch'])
        
        cursor.execute(query, params)
        results = cursor.fetchall()
        conn.close()
        return results

# Global database instance
hod_db = HODDatabase()