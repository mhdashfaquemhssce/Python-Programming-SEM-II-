'''
# **Student Enrollment Manager** *:
Create a Python code to demonstrate the use of sets and
perform set operations (union, intersection,difference)
to manage student enrollments in multiple courses / appearing for
multiple entrance exams like CET, JEE, NEET etc.
Name: Mohd Ashfaque Shaikh
College: M.H. Saboo Siddik College of Engineering

'''
# Accept student enrollments for different entrance exams
cet_students = set(input("Enter CET students (comma-separated): ").split(","))
jee_students = set(input("Enter JEE students (comma-separated): ").split(","))
neet_students = set(input("Enter NEET students (comma-separated): ").split(","))

while True:
    print("\n1. View Enrollments  2. Union  3. Intersection  4. Difference  5. Exit")
    choice = input("Enter choice: ")

    if choice == "1":  # View all enrollments
        print("CET Students:", cet_students)
        print("JEE Students:", jee_students)
        print("NEET Students:", neet_students)

    elif choice == "2":  # Union of sets
        print("Students appearing for any exam:", cet_students | jee_students | neet_students)

    elif choice == "3":  # Intersection of sets
        print("Students appearing for both CET and JEE:", cet_students & jee_students)
        print("Students appearing for both JEE and NEET:", jee_students & neet_students)
        print("Students appearing for both CET and NEET:", cet_students & neet_students)

    elif choice == "4":  # Difference of sets
        print("Students in CET but not in JEE:", cet_students - jee_students)
        print("Students in JEE but not in CET:", jee_students - cet_students)
        print("Students in NEET but not in JEE:", neet_students - jee_students)

    elif choice == "5":  # Exit
        print("Exiting...")
        break

    else:
        print("Invalid choice.")
