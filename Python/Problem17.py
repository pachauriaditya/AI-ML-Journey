# Print Numbers Divisible by Both 3 and 5 in a Range
#
# Problem:
# Write a function that prints all numbers within
# a given range that are divisible by both 3 and 5.
#
# Approach:
# 1. Define a function that takes the start and end
#    of the range as input.
# 2. Traverse all numbers from a to b.
# 3. Check if the number is divisible by both 3 and 5.
# 4. If true, print the number.
#
# Time Complexity: O(n)
# Space Complexity: O(1)

def print_num(a, b):
    for i in range(a, b + 1):
        if i % 3 == 0 and i % 5 == 0:
            print(i)

print_num(1, 100)