"""
Problem: Find Duplicate Elements and Their Frequency in a List

Description:
Given a list of integers, find the elements that appear more than once
and display how many times each duplicate element occurs.

Approach:
1. Take a list of integers as input from the user.
2. Traverse each element of the list.
3. Count the frequency of the current element by comparing it with all
   elements of the list.
4. If the count is greater than 1 and the element is not already checked,
   print the element and its frequency.
5. Avoid printing duplicate results using list slicing.

Time Complexity: O(n²)
Space Complexity: O(1)

Where:
n = number of elements in the list
"""

list = list(map(int, input("Enter the numbers separated by space: ").split()))

for i in range(len(list)):
    count = 0

    for j in range(len(list)):
        if list[i] == list[j]:
            count += 1

    if count > 1 and list[i] not in list[:i]:
        print(f"{list[i]} occurs {count} times")