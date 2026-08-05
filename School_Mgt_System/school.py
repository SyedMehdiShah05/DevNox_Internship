from pathlib import Path


class School:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.students = []
        self.teachers = []
        self.classrooms = []
        self.timetables = []

    def save_to_file(self, record_type, item):
        data_file = Path(__file__).resolve().with_name("school_data.txt")
        data_file.parent.mkdir(parents=True, exist_ok=True)
        with data_file.open("a", encoding="utf-8") as file:
            file.write(f"{record_type} | {item.display()}\n")

    # --- ADD METHODS (Now with auto-save) ---
    def add_student(self, student):
        self.students.append(student)
        self.save_to_file("STUDENT", student)   
        print(f"Success: Added student {student.name}")

    def add_teacher(self, teacher):
        self.teachers.append(teacher)
        self.save_to_file("TEACHER", teacher) 
        print(f"Success: Added teacher {teacher.name}")
        
    def add_classroom(self, classroom):
        self.classrooms.append(classroom)
        self.save_to_file("CLASSROOM", classroom) 
        print(f"Success: Added classroom {classroom.class_id}")
        
    def add_timetable(self, timetable):
        self.timetables.append(timetable)
        self.save_to_file("TIMETABLE", timetable)  
        print(f"Success: Added timetable for {timetable.subject}")


    def delete_student(self, student_id):
        for student in self.students:
            if student.student_id == student_id:
                self.students.remove(student)
                print(f"Success: Deleted student with ID {student_id}")
                return 
        print(f"Error: No student found with ID {student_id}")

    def delete_teacher(self, teacher_name):
        for teacher in self.teachers:
            if teacher.name.lower() == teacher_name.lower():
                self.teachers.remove(teacher)
                print(f"Success: Deleted teacher {teacher.name}")
                return
        print(f"Error: No teacher found named {teacher_name}")
            
    
        
