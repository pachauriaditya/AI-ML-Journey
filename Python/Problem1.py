# User Greeting Program
#
# Problem:
# Take the user's name and age as input and display
# a personalized greeting message.
#
# Approach:
# 1. Input the user's name.
# 2. Input the user's age and convert it to an integer.
# 3. Print a greeting message using the entered details.
#
# Time Complexity: O(1)
# Space Complexity: O(1)

name = input("Enter Your Name : ")
age = int(input("Enter Your Age : "))

print("Hello", name, ", you are", age, "years old")