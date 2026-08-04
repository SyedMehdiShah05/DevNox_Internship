# ----------------------------------------------------
# Week 1 Mini Project: Student Grade Calculator
# This program:
# 1. Takes marks for 5 subjects from the user.
# 2. Validates the input using exception handling.
# 3. Calculates the percentage.
# 4. Determines the grade.
# 5. Converts the grade into GPA.
# ----------------------------------------------------


# Function to calculate the average percentage
def calculate_percentage(marks):
    # sum(marks) adds all marks together
    # len(marks) returns the total number of subjects
    # Dividing gives the average percentage
    return sum(marks) / len(marks)


# Function to calculate the grade based on percentage
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


# Create an empty list to store marks
marks = []

# Total number of subjects
subjects = 5

# Display instructions to the user
print("Enter marks out of 100")


# Loop runs once for each subject
for i in range(subjects):

    # Keep asking until a valid mark is entered
    while True:

        try:
            # Take marks as decimal numbers
            mark = float(input(f"Subject {i+1}: "))

            # Check whether marks are between 0 and 100
            if 0 <= mark <= 100:

                # Store valid marks in the list
                marks.append(mark)

                # Exit the while loop
                break

            else:
                # Display error if marks are outside the valid range
                print("Marks must be between 0 and 100.")

        # Handle invalid input like letters or symbols
        except ValueError:
            print("Please enter a valid number.")


# Calculate the overall percentage
percentage = calculate_percentage(marks)

# Calculate the grade using the percentage
grade = calculate_grade(percentage)


# Display the result heading
print("\n----- Result -----")

# Display all entered marks
print("Marks:", marks)

# Display percentage with two decimal places
print(f"Percentage: {percentage:.2f}%")

# Display final grade
print("Grade:", grade)


# ----------------------------------------------------
# Function to calculate GPA from the grade
# ----------------------------------------------------
def calculate_gpa(grade):

    # Dictionary stores grade-to-GPA mapping
    grade_points = {
        "A+": 4.0,
        "A": 4.0,
        "B": 3.0,
        "C": 2.0,
        "D": 1.0,
        "F": 0.0
    }

    # Return GPA corresponding to the grade
    # If grade is not found, return 0.0
    return grade_points.get(grade, 0.0)


# Calculate GPA using the obtained grade
gpa = calculate_gpa(grade)

# Display GPA with two decimal places
print(f"GPA: {gpa:.2f}")