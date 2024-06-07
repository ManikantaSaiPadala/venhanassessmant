import sqlite3

def insert_student(name: str, grade: float):
    
    conct = sqlite3.connect('students.db')
    cursor = conct.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            grade REAL
        )
    ''')

    cursor.execute('''
        INSERT INTO students (name, grade)
        VALUES (?, ?)
    ''', (name, grade))
    
    conct.commit()
    conct.close()

insert_student('Manikanta Sai', 87.9)