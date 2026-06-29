class Student:
    def __init__(self,name,cgpa):
        self.name = name
        self.cgpa = cgpa

stu1 = Student("Virat", 10.0)
stu2 = Student("Rajat", 7.5)
stu3 = Student("Rahul", 9.0)

print(stu1.name)
print(stu2.name)
print(stu3.name)

print(stu1.cgpa)
print(stu2.cgpa)
print(stu3.cgpa)