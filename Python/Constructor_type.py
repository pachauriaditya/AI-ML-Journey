class Student:
    def __init__(self,name,cgpa):
        self.name = name
        self.cgpa = cgpa
    
    def get_cgpa(self):
        return self.cgpa

stu1 = Student("Virat", 10.0)
stu2 = Student("Rajat", 7.5)
stu3 = Student("Rahul", 9.0)

print(f"{stu1.name} has cgpa of {stu1.get_cgpa()}")
print(f"{stu2.name} has cgpa of {stu2.get_cgpa()}")
print(f"{stu3.name} has cgpa of {stu3.get_cgpa()}")