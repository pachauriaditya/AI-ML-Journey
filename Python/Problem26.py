"""
Problem: Separate Even and Odd Numbers from a Tuple

Description:
Given a tuple of integers, separate the even and odd numbers into
two different tuples and display them.

Approach:
1. Take multiple integers as input and store them in a tuple.
2. Traverse each element of the tuple.
3. If the number is divisible by 2, add it to the even list.
4. Otherwise, add it to the odd list.
5. Convert both lists into tuples.
6. Print the even and odd tuples.

Time Complexity: O(n)
Space Complexity: O(n)

Where:
n = number of elements in the tuple
"""

nums = tuple(map(int, input("Enter numbers separated by space: ").split()))

even = []
odd = []

for i in nums:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)

even = tuple(even)
odd = tuple(odd)

print("Even numbers:", even)
print("Odd numbers:", odd)