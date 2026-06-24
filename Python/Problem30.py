"""
Problem: Check Common Elements Between Two Lists

Description:
Given two lists of integers, determine whether they have any common
elements or not.

Approach:
1. Take two lists as input from the user.
2. Convert both lists into sets.
3. Use the isdisjoint() method to check whether the sets have no common
   elements.
4. If sets are disjoint, print that there are no common elements.
5. Otherwise, print that common elements exist.

Time Complexity: O(n + m)
Space Complexity: O(n + m)

Where:
n = size of first list
m = size of second list
"""

list1 = list(map(int, input("Enter the numbers separated by space: ").split()))
list2 = list(map(int, input("Enter numbers separated by space: ").split()))

if set(list1).isdisjoint(set(list2)):
    print("The two lists have no common elements.")
else:
    print("The two lists have common elements.")