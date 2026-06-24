"""
Problem: Find Unique Characters in a String

Description:
Given a string, find all the characters that appear for the first time
and count the total number of unique characters present in the string.

Approach:
1. Take a string as input from the user.
2. Create an empty string to store unique characters.
3. Traverse each character of the original string.
4. Check if the character is not already present in the unique string.
5. Add the character to the unique string.
6. Print the unique characters and their count.

Time Complexity: O(n²)
Space Complexity: O(n)

Where:
n = length of the string
"""

string = input("Enter a string: ")

unique = ""

for ch in string:
    if ch not in unique:
        unique += ch

print("Unique characters in the string are:", unique)
print("Number of unique characters in the string are:", len(unique))