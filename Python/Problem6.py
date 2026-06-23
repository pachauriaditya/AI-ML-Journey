# Swap Two Numbers Using a Temporary Variable
#
# Problem:
# Take two numbers as input and swap their values
# using a temporary variable.
#
# Approach:
# 1. Input two integers from the user.
# 2. Store the first number in a temporary variable.
# 3. Assign the second number to the first number.
# 4. Assign the temporary value to the second number.
# 5. Print the swapped values.
#
# Time Complexity: O(1)
# Space Complexity: O(1)

num1 = int(input("Enter First Number : "))
num2 = int(input("Enter Second Number : "))

temp = num1
num1 = num2
num2 = temp

print("After swapping:")
print("First Number :", num1)
print("Second Number :", num2)