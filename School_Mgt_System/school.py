class School:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.student = []
        self.teacher = []
        self.classroom = []
        self.timetable = []

    def add_student(self, student):
        self.student.append(student)
        print(f"Success : Student Added {student.name}")

    def add_teacher(self, teacher):
        self.teacher.append(teacher)
        print(f"Success : Teacher Added {teacher.name}")

    def add_classroom(self, classroom):
        self.classroom.append(classroom)
        print(f"Success : Classroom Added {classroom.class_id}") 
    
    def add_timetable(self, timetable):
        self.timetable.append(timetable)
        print(f"Success : Timetable Added {timetable.day} {timetable.timing}")
        
            
    
        
