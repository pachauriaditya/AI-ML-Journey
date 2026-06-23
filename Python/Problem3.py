# Average of Three Numbers
#
# Problem:
# Take three numbers as input and calculate their average.
#
# Approach:
# 1. Input two integers and one floating-point number.
# 2. Add all three numbers.
# 3. Divide the sum by 3 to get the average.
# 4. Print the result.
#
# Time Complexity: O(1)
# Space Complexity: O(1)

num1 = int(input("Enter First Number : "))
num2 = int(input("Enter Second Number : "))
num3 = float(input("Enter Third Number : "))

average = (float(num1) + float(num2) + num3) / 3

print("Average of Three Number is :", average)