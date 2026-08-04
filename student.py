class Student:
    def __init__(self, name, student_id, grade):
        self.name = name
        self.student_id = student_id
        self.grade = grade

    def display(self):
        return f" Name : {self.name} | Student_ID: {self.student_id}  | Grade : {self.grade}"

    #def display(self):
       #print(f"Name : {self.name}")
       #print(f"ID : {self.student_id}")
       #print(f"Grade : {self.grade}")