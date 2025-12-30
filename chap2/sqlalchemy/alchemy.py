from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///school.db')
Base = declarative_base()

class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    marks = Column(Integer)

Base.metadata.create_all(engine)
print("Table created successfully")

# Create a session to interact with the database
Session = sessionmaker(bind=engine)
session = Session()

# Insert a single student
student1 = Student(name='Sita', marks=85)
session.add(student1)
session.commit()
print("Single record inserted successfully")

# Insert multiple students
students = [
    Student(name='Ram', marks=78),
    Student(name='Hari', marks=92),
    Student(name='Suman', marks=88)
]
session.add_all(students)
session.commit()
print("Multiple records inserted successfully")

# Query all students
all_students = session.query(Student).all()
print("\nAll Students:")
for student in all_students:
    print(f"ID: {student.id}, Name: {student.name}, Marks: {student.marks}")

# Query a specific student by name
student = session.query(Student).filter(Student.name == "Sita").first()
if student:
    print(f"\nFound Student - ID: {student.id}, Name: {student.name}, Marks: {student.marks}")
else:
    print("Record not found")

# to delete record
student_to_delete = session.query(Student).filter(Student.name == "Ram").first()
if student_to_delete:
    session.delete(student_to_delete)
    session.commit()
    print("Record deleted successfully")
else:
    print("Record not found")


session.close()

