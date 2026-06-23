# Data Type Conversion
#
# Problem:
# Take a number as input in string format and convert it
# to integer, float, and string types.
# Print each value along with its data type.
#
# Approach:
# 1. Read the input as a string.
# 2. Convert it to an integer using int().
# 3. Convert it to a float using float().
# 4. Convert it back to a string using str().
# 5. Print all values and their corresponding data types.
#
# Time Complexity: O(1)
# Space Complexity: O(1)

num = input("Enter a number: ")

integer_value = int(num)
float_value = float(num)
string_value = str(num)

print(integer_value, type(integer_value))
print(float_value, type(float_value))
print(string_value, type(string_value))