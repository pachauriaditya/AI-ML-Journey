students ={}

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