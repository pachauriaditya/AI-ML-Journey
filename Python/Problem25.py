"""
Problem: Merge and Sort Two Lists

Description:
Given two lists of integers, merge them into a single list and
sort the merged list in ascending order.

Approach:
1. Take two lists as input from the user.
2. Merge both lists using the '+' operator.
3. Sort the merged list using the sort() method.
4. Print the merged and sorted list.

Time Complexity: O((n + m) log(n + m))
Space Complexity: O(n + m)

Where:
n = size of first list
m = size of second list
"""

list1 = list(map(int, input("Enter the numbers separated by space: ").split()))
list2 = list(map(int, input("Enter numbers separated by space: ").split()))

merge_list = list1 + list2
merge_list.sort()

print("Merged and sorted list:", merge_list)