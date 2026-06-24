"""
Problem: Student Record Management System

Description:
Create a menu-driven program to manage student records using a dictionary.
The program allows users to add students, update marks, search for a student,
display all student records, and exit the program.

Approach:
1. Create an empty dictionary to store student names and their marks.
2. Display a menu repeatedly using a while loop.
3. Perform operations based on the user's choice:
   - Add a new student and marks.
   - Update marks of an existing student.
   - Search for a student by name.
   - Display all students and their marks.
   - Exit the program.
4. Use dictionary operations for efficient storage and retrieval.
5. Continue until the user chooses to exit.

Time Complexity:
- Add Student: O(1)
- Update Marks: O(1)
- Search Student: O(1)
- Display All Students: O(n)

Space Complexity: O(n)

Where:
n = number of students stored in the dictionary
"""

students = {}

while True:
    print("A - Add a student")
    print("B - Update marks")
    print("C - Search for a student")
    print("D - Display all students and marks")
    print("E - Exit")

    choice = input("Enter your choice: ").upper()

    if choice == "A":
        name = input("Enter the student's name: ")
        age = int(input("Enter the student's Marks: "))
        students[name] = age

    elif choice == "B":
        name = input("Enter the student name : ")
        if name in students:
            marks = int(input("Enter the new marks: "))
            students[name] = marks
            print("Student marks updated successfully.")
        else:
            print("Student not found.")

    elif choice == "C":
        name = input("Enter the student's name to search: ")
        if name in students:
            print(f"Student found. Marks: {students[name]}")
        else:
            print("Student not found.")

    elif choice == "D":
        if students:
            print("All students and their marks:")
            for name, marks in students.items():
                print(f"{name}: {marks}")
        else:
            print("No students found.")

    elif choice == "E":
        print("Program terminated.")
        break

    else:
        print("Invalid choice. Please try again.")