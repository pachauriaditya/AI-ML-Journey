"""
Problem: Palindrome Checker

Description:
A palindrome is a word, phrase, number, or sequence that reads the same
forward and backward. This program checks whether the given word is a
palindrome or not.

Approach:
1. Take a word as input from the user.
2. Reverse the word using Python slicing (word[::-1]).
3. Compare the original word with the reversed word.
4. Return True if both are equal, otherwise return False.

Time Complexity: O(n)
Space Complexity: O(n)
"""

word = input("Enter a word: ")

def is_pallindrome(word):
    return word == word[::-1]

print(is_pallindrome(word))