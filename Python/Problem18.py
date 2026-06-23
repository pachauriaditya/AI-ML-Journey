# Positive, Negative, or Zero Number Checker
#
# Problem:
# Continuously accept numbers from the user and
# determine whether each number is positive,
# negative, or zero.
# Stop the program when the user enters "Quit".
#
# Approach:
# 1. Use an infinite loop to continuously take input.
# 2. Check if the user entered "Quit".
# 3. Convert the input to a float.
# 4. Determine whether the number is positive,
#    negative, or zero.
# 5. Print the result and continue until "Quit"
#    is entered.
#
# Time Complexity: O(1) per input
# Space Complexity: O(1)

while True:
    n = input("Enter a number (or Quit to exit): ")

    if n == "Quit":
        break

    n = float(n)

    if n > 0:
        print("The number is positive")
    elif n < 0:
        print("The number is negative")
    else:
        print("The number is zero")