# Print Even Numbers in a Given Range
#
# Problem:
# Write a function that prints all even numbers
# within a given range (inclusive).
#
# Approach:
# 1. Define a function that takes the start and end
#    of the range as input.
# 2. Traverse all numbers from a to b.
# 3. Check if the current number is divisible by 2.
# 4. If divisible, print the number.
#
# Time Complexity: O(n)
# Space Complexity: O(1)

def printEven(a, b):
    for i in range(a, b + 1):
        if i % 2 == 0:
            print(i)

printEven(1, 10)