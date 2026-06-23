"""
Problem:
Given a list of (student, course) pairs:

1. Print the names of all students enrolled in the English course.
2. Find all unique courses available.
3. Create a mapping of each student to the set of courses they are enrolled in.

Approach:
1. Store student-course data as a list of tuples.
2. Traverse the list once:
   - Add each course to a set to collect unique courses.
   - Print the student's name if the course is "English".
3. Traverse the list again:
   - Use a dictionary where:
     Key   -> Student Name
     Value -> Set of Courses
   - If the student is not present in the dictionary,
     create a new empty set for that student.
   - Add the course to the student's set.
4. Print the final dictionary containing student-course mappings.

Time Complexity:
O(n)

Space Complexity:
O(n)

where n is the number of student-course records.
"""

info = [
    ("Aditya","Maths"),
    ("Virat","Science"),
    ("Rohit","Science"),
    ("Dhoni","Maths"),
    ("Sachin","Maths"),
    ("Rahul","English"),
    ("Rajat ","English"),
]
course_set = set()

for name , course in info:
    course_set.add(course)
    if(course == "English"):
        print(name)

print(course_set)

dict = {}

for name , course in info:
    if( dict.get(name) == None):
        dict.update({name: set()})
        dict[name].add(course)
    else:
        dict[name].add(course)
print(dict)