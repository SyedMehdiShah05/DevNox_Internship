from school import School
from student import Student
from teacher import Teacher
from classroom import Classroom
from timetable import Timetable

def main():
    my_school = School("Hazara Public School", "Dhodial Mansehra")
    print(f"Welcome to {my_school.name}")

    while True:
        print("\nMain Menu:")
        print("1. Add Student")
        print("2. Add Teacher")
        print("3. Add Classroom")
        print("4. Add Timetable")
        print("5. View All Data")
        print("6. Exit")
        choice = input("Enter your choice: (1-6): ")

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
            for student in my_school.student: print(student.display_info())
                
            print("\nTeachers:")
            for teacher in my_school.teacher: print(teacher.display_info())
                
            print("\nClassrooms:")
            for classroom in my_school.classroom: print(classroom.display_info())
          
            print("\nTimetables:")
            for timetable in my_school.timetable: print(timetable.display_info())

        elif choice == '6':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()