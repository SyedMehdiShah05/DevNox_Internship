class Student:
    def __init__(self, name, student_id, grade):
        self.name = name
        self.student_id = student_id
        self.grade = grade

    def display(self):
        return f"ID: {self.student_id} | Name: {self.name} | Grade: {self.grade}"

    def display_info(self):
        return f"Student ID: {self.student_id}, Name: {self.name}, Grade: {self.grade}"