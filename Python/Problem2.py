# Basic Arithmetic Operations Calculator
#
# Problem:
# Take two numbers as input and perform addition,
# subtraction, multiplication, and division.
# Handle the case where division by zero is attempted.
#
# Approach:
# 1. Input two integers from the user.
# 2. Print their sum, difference, and product.
# 3. Check if the second number is not zero.
# 4. If valid, perform division and print the quotient.
# 5. Otherwise, display an error message.
#
# Time Complexity: O(1)
# Space Complexity: O(1)

num1 = int(input("Enter First number : "))
num2 = int(input("Enter Second number : "))

print("Sum of two number is :", num1 + num2)
print("Difference of two number is :", num1 - num2)
print("Multiplication of two number is :", num1 * num2)

if num2 != 0:
    print("Quotient of two number is :", num1 / num2)
else:
    print("Cannot divide by zero")