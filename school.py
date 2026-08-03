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
        print(f"Succes : Teacher Added {teacher.name}")

    def add_classroom(self, classroom):
            self.student.append(classroom)
            print(f"Success : classroom Added {classroom.name}")
    
    def add_timetable(self, timetable):
            self.teacher.append(timetable)
            print(f"Succes : Timetable Added {timetable.name}")
            
    
        
