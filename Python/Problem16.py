# Sum of Digits of a Number
#
# Problem:
# Write a function that takes a number as input
# and returns the sum of all its digits.
#
# Approach:
# 1. Initialize a variable sum as 0.
# 2. Convert the number to a string.
# 3. Traverse each digit in the string.
# 4. Convert the digit to an integer and add it to sum.
# 5. Return the final sum.
#
# Time Complexity: O(d)
# Space Complexity: O(1)

def sum_of_digits(n):
    sum = 0

    for digit in str(n):
        sum += int(digit)

    return sum

print(sum_of_digits(5464))