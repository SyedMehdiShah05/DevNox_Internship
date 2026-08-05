from school import School
from student import Student
from teacher import Teacher
from classroom import Classroom
from timetable import Timetable as AbstractTimetable


def _make_timetable_method(method_name):
    def generic_method(self, *args, **kwargs):
        if method_name == "display_info":
            day = getattr(self, "day", "Unknown day")
            timing = getattr(self, "timing", getattr(self, "time", "Unknown time"))
            subject = getattr(self, "subject", "Unknown subject")
            return f"{day} at {timing} - {subject}"
        if method_name in ("to_dict", "as_dict"):
            return {
                "day": getattr(self, "day", None),
                "timing": getattr(self, "timing", getattr(self, "time", None)),
                "subject": getattr(self, "subject", None),
            }
        if method_name in ("get_schedule", "get_details", "get_info", "info"):
            return self.display_info()
        return f"Method '{method_name}' executed for timetable."
    return generic_method


def _timetable_init(self, day, time, subject):
    self.day = day
    self.timing = time
    self.subject = subject

abstract_methods = getattr(AbstractTimetable, "__abstractmethods__", frozenset())
implemented_methods = {"__init__": _timetable_init, "__str__": lambda self: self.display_info()}
for method_name in abstract_methods:
    if method_name not in implemented_methods:
        implemented_methods[method_name] = _make_timetable_method(method_name)

Timetable = type("Timetable", (AbstractTimetable,), implemented_methods)

def main():
    my_school = School("Hazara Public School", "Dhodial Mansehra")
    print(f"\nWelcome to {my_school.name}")

    while True:
        print("\nMain Menu:")
        print("1. Add Student")
        print("2. Add Teacher")
        print("3. Add Classroom")
        print("4. Add Timetable")
        print("5. View All Data")
        print("6. Delete Student/Teacher/Classroom/Timetable")
        print("7. Exit")
        choice = input("Enter your choice: (1-7): ")

        if choice == '1':
            name = input("Enter student name: ")
            s_id = input("Enter student ID: ")
            grade = int(input("Enter student grade: "))
            new_student = Student(name, s_id, grade)
            my_school.add_student(new_student)

        elif choice == '2':
            name = input("Enter teacher name: ")
            spec = input("Enter teacher specialization: ")
            contact = input("Enter teacher contact number: ")
            new_teacher = Teacher(name, spec, contact)
            my_school.add_teacher(new_teacher)

        elif choice == '3':
            c_id = input("Enter classroom ID: ")
            cap = input("Enter classroom capacity: ")
            rtype = input("Enter classroom type (Lab/Lecture): ")
            new_room = Classroom(c_id, cap, rtype)
            my_school.add_classroom(new_room)

        elif choice == '4':
            day = input("Enter day : ")
            time = input("Enter time (H:M): ")
            subject = input("Enter subject: ")
            new_time = Timetable(day, time, subject)
            my_school.add_timetable(new_time)

        elif choice == '5':
            print("\nStudents:")
            for student in my_school.students: print(student.display_info())
                
            print("\nTeachers:")
            for teacher in my_school.teachers: print(teacher.display_info())
                
            print("\nClassrooms:")
            for classroom in my_school.classrooms: print(classroom.display_info())
          
            print("\nTimetables:")
            for timetable in my_school.timetables: print(timetable.display_info())

        elif choice == '6':
            del_choice = input("Delete (1) Student, (2) Teacher, (3) Classroom, (4) Timetable: ")
            if del_choice == '1':
                s_id = input("Enter student ID to delete: ")
                my_school.delete_student(s_id)
            elif del_choice == '2':
                t_name = input("Enter teacher name to delete: ")
                my_school.delete_teacher(t_name)
            elif del_choice == '3':
                c_id = input("Enter classroom ID to delete: ")
                my_school.delete_classroom(c_id)
            elif del_choice == '4':
                day = input("Enter timetable day to delete: ")
                time = input("Enter timetable time to delete: ")
                my_school.delete_timetable(day, time)
            else:
                print("Invalid choice for deletion.")

        elif choice == '7':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

    try:
        import psycopg2
    except ModuleNotFoundError:
        print("Warning: psycopg2 is not installed. Skipping database connection.")
    else:
        try:
            # Connecting to the Aiven PostgreSQL database
            connection = psycopg2.connect(
                host="pg-17c55422-mehdiiims05-10be.a.aivencloud.com",
                database="defaultdb",
                user="avnadmin",
                #password="AVNS_1tS7zBS6pi4U5MNH53g",
                port="21182",
                sslmode="require"
            )
            
            # The cursor allows Python code to execute PostgreSQL command in a database session
            cursor = connection.cursor()
            connection.commit()
            print("Successfully connected to the School Management System Database!")
 
        except Exception as error:
            print(f"Error connecting to database: {error}")
