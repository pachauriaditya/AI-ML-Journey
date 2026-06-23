# Number Guessing Game
#
# Problem:
# Create a simple guessing game where the user
# tries to guess a secret number.
#
# Approach:
# 1. Store a predefined secret number.
# 2. Take the user's guess as input.
# 3. Compare the guessed number with the secret number.
# 4. If the guess is correct, display a success message.
# 5. If the guess is smaller, suggest a bigger number.
# 6. If the guess is larger, suggest a smaller number.
#
# Time Complexity: O(1)
# Space Complexity: O(1)

secret_num = 18

guessed_num = int(input("Guess a number : "))

if guessed_num == secret_num:
    print("You guessed it right!")

if guessed_num < secret_num:
    print("You guessed it wrong! Try a bigger number")

if guessed_num > secret_num:
    print("You guessed it wrong! Try a smaller number")