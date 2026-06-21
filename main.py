import sqlite3

def init_db():
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        course TEXT NOT NULL,
        marks INTEGER
    )
    """)

    conn.commit()
    conn.close()


# INITIALIZE DB FIRST
init_db()


def add_student():
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()

    name = input("Enter student name: ").strip()
    course = input("Enter course: ").strip()
    marks = int(input("Enter marks (0-100): "))

    if marks < 0 or marks > 100:
     print("Invalid marks! Must be 0-100")
     return

    cursor.execute("""
    INSERT INTO students (name, course, marks)
    VALUES (?, ?, ?)
    """, (name, course, marks))

    conn.commit()
    conn.close()

    print("Student added successfully!")

def view_students():
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()

    if len(rows) == 0:
        print("No students found")
    else:
        print("\n--- Student List ---")
        for row in rows:
            print(f"\nID: {row[0]}")
            print(f"Name: {row[1]}")
            print(f"Course: {row[2]}")
            print(f"Marks: {row[3]}")
            print("-" * 20)

    conn.close()
def search_student():
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()

    name = input("Enter student name to search: ").strip().lower()

    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()

    found = False

    for row in rows:
        db_name = row[1].strip().lower()

        if db_name == name:
            print("\n--- Result ---")
            print(f"ID: {row[0]}")
            print(f"Name: {row[1]}")
            print(f"Course: {row[2]}")
            print(f"Marks: {row[3]}")
            found = True

    if not found:
        print("Student not found")

    conn.close()
def update_student():
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()

    student_id = input("Enter student ID to update: ")
    new_marks = int(input("Enter new marks: "))

    cursor.execute("""
    UPDATE students
    SET marks = ?
    WHERE id = ?
    """, (new_marks, student_id))

    conn.commit()
    conn.close()

    print("Student updated successfully")
def delete_student():
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()

    student_id = input("Enter student ID to delete: ")

    cursor.execute("DELETE FROM students WHERE id=?", (student_id,))

    conn.commit()
    conn.close()

    print("Student deleted successfully")
while True:
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        update_student()
    elif choice == "5":
        delete_student()
    elif choice == "6":
        print("Exiting system...")
        break
    else:
        print("Invalid choice")

