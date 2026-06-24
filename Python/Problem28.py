"""
Problem: Create Dictionary with Words and Their Lengths

Description:
Given a list of words, create a dictionary where each word is stored
as a key and its length is stored as the corresponding value.

Approach:
1. Create a list containing multiple words.
2. Use dictionary comprehension to iterate through each word.
3. Calculate the length of each word using len().
4. Store the word as a key and its length as a value in the dictionary.
5. Print the generated dictionary.

Time Complexity: O(n * m)
Space Complexity: O(n)

Where:
n = number of words
m = average length of each word
"""

words = ["apple", "banana", "kiwi", "'cherry", "mango"]

dict = {word: len(word) for word in words}

print(dict)