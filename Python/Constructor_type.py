# Problem: Student Class using Parameterized Constructor

# Approach:
# 1. Create a Student class with a parameterized constructor.
# 2. Initialize each student's name and CGPA using the constructor.
# 3. Create a method to return the student's CGPA.
# 4. Create multiple student objects and display their details.

# New Keywords/Concepts:
# - __init__: Special constructor method that is automatically called when an object is created.
# - self: Refers to the current object of the class.
# - Parameterized Constructor: A constructor that accepts values while creating an object.
# - Object: An instance of a class.
# - f-string: A formatted string used to insert variables directly inside a string using {}.

# Time Complexity: O(1)
# Space Complexity: O(1)

# In Python, only one constructor (__init__) can exist in a class.
# If multiple __init__ methods are written, the last one overrides the previous ones.

class Student:

    '''
    # Default constructor (example)
    def __init__(self):
        print("This is default constructor")
    '''

    # Parameterized constructor
    def __init__(self, name, cgpa):
        self.name = name      # Store student's name
        self.cgpa = cgpa      # Store student's CGPA
    
    # Method to return the student's CGPA
    def get_cgpa(self):
        return self.cgpa

# Creating Student objects
stu1 = Student("Virat", 10.0)
stu2 = Student("Rajat", 7.5)
stu3 = Student("Rahul", 9.0)

# Displaying student details
print(f"{stu1.name} has cgpa of {stu1.get_cgpa()}")
print(f"{stu2.name} has cgpa of {stu2.get_cgpa()}")
print(f"{stu3.name} has cgpa of {stu3.get_cgpa()}")