'''
Student Record Keeper
Name: Shaikh Mohd Ashfque

This program allows the user to add, update, view, and remove
student records using a dictionary.
'''

# Dictionary to store all student records
# Key   → Roll Number
# Value → Dictionary containing Name, Grade, and Attendance
students = {}

# Infinite loop to keep the program running until the user exits
while True:
    
    # Display menu options
    print("\n1. Add Student")
    print("2. Update Student")
    print("3. View Students")
    print("4. Remove Student")
    print("5. Exit")
    
    # Take user choice
    choice = input("Enter choice: ")

    # -------------------- ADD STUDENT --------------------
    if choice == "1":
        
        # Take student details as input
        roll_no = input("Enter Roll Number: ")
        name = input("Enter Name: ")
        grade = input("Enter Grade: ")
        attendance = input("Enter Attendance (%): ")
        
        # Store student details in the dictionary
        students[roll_no] = {
            "Name": name,
            "Grade": grade,
            "Attendance": attendance
        }
        
        print("Student added successfully.")

    # -------------------- UPDATE STUDENT --------------------
    elif choice == "2":
        
        # Ask for roll number to update
        roll_no = input("Enter Roll Number to update: ")
        
        # Check if student exists
        if roll_no in students:
            
            # Display current record
            print("Current Record:", students[roll_no])
            
            # Take new values (press Enter to keep old value)
            grade = input("Enter new Grade (or press Enter to keep unchanged): ")
            attendance = input("Enter new Attendance (or press Enter to keep unchanged): ")
            
            # Update grade if provided
            if grade:
                students[roll_no]["Grade"] = grade
            
            # Update attendance if provided
            if attendance:
                students[roll_no]["Attendance"] = attendance
            
            print("Record updated successfully.")
        else:
            print("Student not found.")

    # -------------------- VIEW STUDENTS --------------------
    elif choice == "3":
        
        # Check if dictionary is not empty
        if students:

            # Why .items() is used? Because it allows access to both key and value at the same time.
            # Loop through all student records
            for roll_no, info in students.items():
                
                # Display student details
                print(
                    f"Roll No: {roll_no}, "
                    f"Name: {info['Name']}, "
                    f"Grade: {info['Grade']}, "
                    f"Attendance: {info['Attendance']}%"
                )
        else:
            print("No student records available.")

    # -------------------- REMOVE STUDENT --------------------
    elif choice == "4":
        
        # Ask for roll number to remove
        roll_no = input("Enter Roll Number to remove: ")
        
        # Check if student exists
        if roll_no in students:
            
            # Delete student record
            del students[roll_no]
            print("Student record removed.")
        else:
            print("Student not found.")

    # -------------------- EXIT PROGRAM --------------------
    elif choice == "5":
        
        # Exit the loop and program
        print("Exiting program...")
        break

    # -------------------- INVALID INPUT --------------------
    else:
        print("Invalid choice. Please enter a number from 1 to 5.")
