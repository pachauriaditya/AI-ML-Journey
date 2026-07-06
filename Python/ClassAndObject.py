# Class Attributes
# Shared by all objects of the class.

class Student:

    # Class Attributes
    subject = "Python"
    college = "UIT"
    year = 2026


# Object Creation
stu1 = Student()
stu2 = Student()

# Accessing Class Attributes through objects
print(stu1.subject)
print(stu2.college)

# We can also access them using the class name:
# print(Student.subject)
# print(Student.college)