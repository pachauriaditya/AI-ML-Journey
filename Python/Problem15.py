# Print Digits and Count Digits of a Number
#
# Problem:
# Write a function that prints each digit of a number
# separately and returns the total count of digits.
#
# Approach:
# 1. Convert the number to a string.
# 2. Traverse each character (digit) in the string.
# 3. Print each digit on a new line.
# 4. Increment a counter for every digit.
# 5. Return the total count.
#
# Time Complexity: O(d)
# Space Complexity: O(1)

def print_digits(n):
    count = 0

    for digit in str(n):
        print(digit)
        count += 1

    return count

n = int(input("Enter a number: "))

print("Number of digits:", print_digits(n))