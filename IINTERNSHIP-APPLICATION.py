import sqlite3
from datetime import datetime

conn = sqlite3.connect('internship_applications.db')
cursor = conn.cursor()

def submit_application(name, email, date_of_birth, university, major, resume_link):
    try:
        cursor.execute("""
            INSERT INTO InternshipApplication 
            (StudentName, Email, DateOfBirth, University, Major, ResumeLink) 
            VALUES (?, ?, ?, ?, ?, ?)
        """, (name, email, date_of_birth, university, major, resume_link))
        conn.commit()
        print("Application submitted successfully.")
    except sqlite3.Error as e:
        print(f"Error submitting application: {e}")

def get_application_by_id(application_id):
    cursor.execute("SELECT * FROM InternshipApplication WHERE ApplicationID=?", (application_id,))
    return cursor.fetchone()

def update_application_status(application_id, new_status):
    try:
        cursor.execute("UPDATE InternshipApplication SET Status=? WHERE ApplicationID=?", (new_status, application_id))
        conn.commit()
        print("Application status updated successfully.")
    except sqlite3.Error as e:
        print(f"Error updating application status: {e}")

def delete_application(application_id):
    try:
        cursor.execute("DELETE FROM InternshipApplication WHERE ApplicationID=?", (application_id,))
        conn.commit()
        print("Application deleted successfully.")
    except sqlite3.Error as e:
        print(f"Error deleting application: {e}")

# Example Usage
submit_application("John Doe", "john.doe@example.com", "1998-05-15", "Example University", "Computer Science", "resume_link_here")
application = get_application_by_id(1)
print("Retrieved Application:", application)

update_application_status(1, "Approved")
application = get_application_by_id(1)
print("Updated Application:", application)

delete_application(1)
