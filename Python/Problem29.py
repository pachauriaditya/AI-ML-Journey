"""
Problem: Count Spaces in a String

Description:
Given a string, count the total number of spaces present in the string.

Approach:
1. Take a string as input from the user.
2. Traverse each character of the string using a loop.
3. Check if the current character is a space.
4. Increment the counter whenever a space is found.
5. Print the total number of spaces.

Time Complexity: O(n)
Space Complexity: O(1)

Where:
n = length of the string
"""

string = input("Enter a string: ")

count = 0

for ch in string:
    if ch == ' ':
        count += 1

print(f"Number of spaces in the string: {count}")