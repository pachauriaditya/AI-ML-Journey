# Problem: Accessing Object Attributes in a Student Class

# Approach:
# 1. Create a Student class with a parameterized constructor.
# 2. Initialize the name and CGPA of each student.
# 3. Create multiple Student objects.
# 4. Access and print the object's attributes directly using the dot (.) operator.

# New Keywords/Concepts:
# - Attribute: A variable that belongs to an object (e.g., name, cgpa).
# - Dot (.) Operator: Used to access an object's attributes and methods.
# - self: Refers to the current object being created.
# - __init__: Constructor that is automatically called when an object is created.

# Time Complexity: O(1)
# Space Complexity: O(1)

class Student:

    # Parameterized constructor
    def __init__(self, name, cgpa):
        self.name = name      # Initialize student's name
        self.cgpa = cgpa      # Initialize student's CGPA

# Creating Student objects
stu1 = Student("Virat", 10.0)
stu2 = Student("Rajat", 7.5)
stu3 = Student("Rahul", 9.0)

# Accessing and printing student names
print(stu1.name)
print(stu2.name)
print(stu3.name)

# Accessing and printing student CGPAs
print(stu1.cgpa)
print(stu2.cgpa)
print(stu3.cgpa)