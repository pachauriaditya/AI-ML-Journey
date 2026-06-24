"""
Problem: Calculate Average of Numbers in a List

Description:
Given a list of numbers, find the average (mean) of all elements present
in the list.

Approach:
1. Initialize a variable to store the sum of all elements.
2. Traverse the list using a loop and add each element to the sum.
3. Divide the total sum by the number of elements in the list.
4. Print the calculated average.

Time Complexity: O(n)
Space Complexity: O(1)
"""

numbers = [-8, -6, -5, -4, 0, 1, 2, 3, 4, 5]

sum = 0
for i in numbers:
    sum += i

average = sum / len(numbers)

print(average)