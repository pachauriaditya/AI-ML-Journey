# Simple Interest Calculator
#
# Problem:
# Take the principal amount, rate of interest,
# and time period as input and calculate the
# simple interest.
#
# Approach:
# 1. Input principal amount (P).
# 2. Input rate of interest (R).
# 3. Input time period (T).
# 4. Apply the formula:
#    SI = (P * R * T) / 100
# 5. Print the calculated simple interest.
#
# Time Complexity: O(1)
# Space Complexity: O(1)

P = float(input("Enter the principal amount: "))
R = float(input("Enter the rate of interest: "))
T = float(input("Enter the time period: "))

SI = (P * R * T) / 100

print("Simple Interest:", SI)