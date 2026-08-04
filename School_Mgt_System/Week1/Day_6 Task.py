#Task 6	Write exception-safe code that keeps asking for input until a valid integer is entered.

while True:

    try:
        number = int(input("Enter an integer: "))
        print("You entered:", number)
        break

    except ValueError:
        print("Invalid input! Please enter a valid integer.")

    

# Task 6: Simple To-Do List app (add/remove/view tasks) using functions and a list.

tasks = []


def add_task():
    task = input("Enter a new task: ")
    tasks.append(task)
    print("Task added successfully.\n")


def remove_task():
    if not tasks:
        print("No tasks available.\n")
        return

    view_tasks()

    try:
        index = int(input("Enter task number to remove: "))

        if 1 <= index <= len(tasks):
            removed = tasks.pop(index - 1)
            print(f"'{removed}' removed successfully.\n")
        else:
            print("Invalid task number.\n")

    except ValueError:
        print("Please enter a valid number.\n")


def view_tasks():
    if not tasks:
        print("No tasks available.\n")
    else:
        print("\n----- TO-DO LIST -----")

        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

        print()


while True:

    print("===== TO-DO LIST MENU =====")
    print("1. Add Task")
    print("2. Remove Task")
    print("3. View Tasks")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_task()

    elif choice == "2":
        remove_task()

    elif choice == "3":
        view_tasks()

    elif choice == "4":
        print("Thank you for using the To-Do List.")
        break

    else:
        print("Invalid choice. Please try again.\n")