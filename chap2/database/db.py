import sqlite3
conn = sqlite3.connect('school1.db') # Database file is created if not exists
cursor = conn.cursor()
print("Database created successfully")

# create table
cursor.execute('''
CREATE TABLE IF NOT EXISTS students (
id INTEGER PRIMARY KEY,
name TEXT,
marks INTEGER
)
''')
print("Table created successfully")

# to insert single record
cursor.execute("""INSERT INTO students (id, name, marks) VALUES (?, ?, ?)""", (1, 'Sita', 85))
print("Record inserted successfully")

# to insert multiple record
students = [
(2, 'Ram', 78),
(3, 'Hari', 92),
(4, 'Suman', 88)
]
cursor.executemany("""INSERT INTO students (id, name, marks) VALUES (?, ?, ?)""", students)
print("Multiple records inserted successfully")

# to select all data from table
cursor.execute("SELECT * FROM students")
rows = cursor.fetchall()
for row in rows:
    print(f"ID: {row[0]}, Name: {row[1]}, Marks: {row[2]}")

# to print specific row only 
cursor.execute("SELECT * FROM students WHERE name = ?",("Sita",))
row = cursor.fetchone()
if row:
    print(f"ID: {row[0]}, Name: {row[1]}, Marks: {row[2]}")
else:
    print("Record not found")

# to delete data from table
cursor.execute("DELETE FROM students WHERE name = ?", ("Ram",))
conn.commit()
print("Record deleted successfully")

conn.commit()

conn.close()