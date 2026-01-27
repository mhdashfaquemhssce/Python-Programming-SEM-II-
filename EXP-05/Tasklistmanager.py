'''
*Task List Manager ****:Develop a Python program to manage a task list
using lists and tuples, including adding, removing, updating,
and sorting tasks. **

Name: Shaikh Mohd Ashfaque
'''
# Initialize an empty task list
tasks = []

while True:
    print("\nTask Manager")
    print("1. Add Task")
    print("2. Remove Task")
    print("3. Update Task")
    print("4. View Tasks")
    print("5. Sort Tasks")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":  # Add Task
        task = input("Enter task name: ")
        priority = input("Enter priority (High/Medium/Low): ")
        tasks.append((task, priority))  # Store task as a tuple in list
        print("Task added successfully.")

    elif choice == "2":  # Remove Task
        if tasks:
            for i, (task, priority) in enumerate(tasks):
                print(f"{i+1}. {task} ({priority})")
            index = int(input("Enter task number to remove: ")) - 1
            if 0 <= index < len(tasks):
                removed_task = tasks.pop(index)
                print(f"Task '{removed_task[0]}' removed successfully.")
            else:
                print("Invalid task number.")
        else:
            print("No tasks available.")

    elif choice == "3":  # Update Task
        if tasks:
            for i, (task, priority) in enumerate(tasks):
                print(f"{i+1}. {task} ({priority})")
            index = int(input("Enter task number to update: ")) - 1
            if 0 <= index < len(tasks):
                new_task = input("Enter new task name: ")
                new_priority = input("Enter new priority (High/Medium/Low): ")
                tasks[index] = (new_task, new_priority)
                print("Task updated successfully.")
            else:
                print("Invalid task number.")
        else:
            print("No tasks available.")

    elif choice == "4":  # View Tasks
        if tasks:
            print("\nTask List:")
            for i, (task, priority) in enumerate(tasks):
                print(f"{i+1}. {task} ({priority})")
        else:
            print("No tasks available.")

    elif choice == "5":  # Sort Tasks by Name
        if tasks:
            tasks.sort()  # Sort by task name (default tuple sorting)
            print("Tasks sorted successfully.")
        else:
            print("No tasks available.")

    elif choice == "6":  # Exit
        print("Exiting Task Manager.")
        break

    else:
        print("Invalid choice! Please enter a number between 1 and 6.")
