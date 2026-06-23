# Sum of First N Natural Numbers
#
# Problem:
# Take a positive integer n as input and calculate
# the sum of the first n natural numbers.
#
# Approach:
# 1. Input the value of n.
# 2. Initialize sum as 0.
# 3. Traverse from 1 to n using a loop.
# 4. Add each number to sum.
# 5. Print the final sum.
#
# Time Complexity: O(n)
# Space Complexity: O(1)

n = int(input("Enter a number : "))

sum = 0

for i in range(1, n + 1):
    sum += i

print("sum", sum)