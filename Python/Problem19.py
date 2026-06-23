# Simple Calculator Using Functions
#
# Problem:
# Create a calculator function that performs
# addition, subtraction, multiplication, and
# division based on the operation provided.
#
# Approach:
# 1. Define a function with two numbers and an
#    operation as parameters.
# 2. Check the operation using conditional statements.
# 3. Perform the corresponding arithmetic operation.
# 4. Handle division by zero separately.
# 5. Return the result or an error message.
#
# Time Complexity: O(1)
# Space Complexity: O(1)

def calculator(a, b, operation):
    if operation == 'add':
        return a + b
    elif operation == 'subtract':
        return a - b
    elif operation == 'multiply':
        return a * b
    elif operation == 'divide':
        if b != 0:
            return a / b
        else:
            return "Error: Division by zero"
    else:
        return "Error: Invalid operation"

print(calculator(10, 5, 'add'))