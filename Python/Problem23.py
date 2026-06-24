word = input("Enter a word: ")

def is_pallindrome(word):
    return word == word[::-1]

print(is_pallindrome(word))