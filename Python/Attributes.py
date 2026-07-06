'''
Class Attributes vs Instance Attributes

-> Class attributes are shared by all objects.
-> Instance attributes are unique for each object.
-> If both class and instance have an attribute with the same name,
   Python gives priority to the instance attribute.
'''

class Student:

    # Class Attributes (Shared by all objects)
    college_name = "UIT"
    PI = 3.14

    # Constructor
    def __init__(self, name, gpa):
        # Instance Attributes (Unique for each object)
        self.name = name
        self.gpa = gpa

        # Instance attribute with the same name as class attribute
        self.PI = 3.14


# Object Creation
stu1 = Student("Virat", 9.2)

# Accessing Instance Attribute
print(stu1.name)

# Accessing Class Attribute
print(Student.college_name)

# Accessing PI
# Since PI exists as both class and instance attribute,
# Python gives priority to the instance attribute.
print(stu1.PI)

# To access the class attribute explicitly:
# print(Student.PI)