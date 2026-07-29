from pathlib import Path
import csv

# Red csv file 
print("\nReading CSv")

students = []

csv_path = Path(__file__).parent / "students.csv"
with csv_path.open(newline='') as file:
    reader = csv.DictReader(file)
    for row in reader:
        row["Age"] = int(row["Age"])
        row["Marks"] = int(row["Marks"])
        students.append(row)


# display 1st five row
print("\n first five student")

for student in students[:5]:
    print(student)

# CSV Statistics

print("\nStudents statistics")

total_students = len(students)
total_marks = sum(student["Marks"] for student in students)

average_marks = total_marks/total_students
higest = max(student["Marks"] for student in students)
lowest = min(student["Marks"] for student in students)

print(f"Total Students : {total_students}")
print(f"Average Marks : {average_marks:.2f}")
print(f"Higest Marks : {higest}")
print(f"Lowest Marks :{lowest}")

# Read JSON File
print("\n Reading JSON File")

import json
json_path = Path(__file__).parent / "employee.json"
with json_path.open() as file:
    employees = json.load(file)

print("\nLoaded employee data")
print(employees)

#    Employee with salary > 50000
print("\nEmployees with Salary > 50000\n")

for employee in employees:
    if employee["salary"] > 50000:
        print(employee)

# Json Statistics

print("\nEmployee Statistics")

total_employees = len(employees)

average_salary = sum(emp["salary"] for emp in employees) / total_employees

highest_salary = max(emp["salary"] for emp in employees)

lowest_salary = min(emp["salary"] for emp in employees)

print(f"Total Employees : {total_employees}")
print(f"Average Salary  : {average_salary:.2f}")
print(f"Highest Salary  : {highest_salary}")
print(f"Lowest Salary   : {lowest_salary}")

print("\nTask Completed Successfully!")