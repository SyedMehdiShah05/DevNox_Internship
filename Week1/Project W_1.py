# Week 1 Mini Project: Student Grade Calculator
# Command-line Student Grade Calculator — takes marks as input, computes grade using functions and conditionals,
# and handles invalid input gracefully with exceptions.	Mini Project

def calculate_percentage(marks):
    return sum(marks) / len(marks)


def calculate_grade(percentage):
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 50:
        return "D"
    else:
        return "F"


marks = []

subjects = 5

print("Enter marks out of 100")

for i in range(subjects):

    while True:

        try:
            mark = float(input(f"Subject {i+1}: "))

            if 0 <= mark <= 100:
                marks.append(mark)
                break
            else:
                print("Marks must be between 0 and 100.")

        except ValueError:
            print("Please enter a valid number.")

percentage = calculate_percentage(marks)
grade = calculate_grade(percentage)

print("\n----- Result -----")
print("Marks:", marks)
print(f"Percentage: {percentage:.2f}%")
print("Grade:", grade)

#also calculate gpa
def calculate_gpa(grade):
    grade_points = {
        "A+": 4.0,
        "A": 4.0,
        "B": 3.0,
        "C": 2.0,
        "D": 1.0,
        "F": 0.0
    }
    return grade_points.get(grade, 0.0) 

gpa = calculate_gpa(grade)
print(f"GPA: {gpa:.2f}")
