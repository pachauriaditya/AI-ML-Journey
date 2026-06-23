# Extract Integer and Fractional Parts of a Decimal Number
#
# Problem:
# Take a decimal number as input and display
# its integer part and fractional part separately.
#
# Approach:
# 1. Input a decimal number as a float.
# 2. Convert it to an integer to get the integer part.
# 3. Subtract the integer part from the original number
#    to get the fractional part.
# 4. Print both values.
#
# Time Complexity: O(1)
# Space Complexity: O(1)

num = float(input("Enter a number: "))

intgeral_part = int(num)
fractional_part = num - intgeral_part

print("Integral part:", intgeral_part)
print("Fractional part:", fractional_part)