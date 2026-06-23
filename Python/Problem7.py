# Celsius to Fahrenheit Converter
#
# Problem:
# Take a temperature in Celsius as input and
# convert it to Fahrenheit.
#
# Approach:
# 1. Input the temperature in Celsius.
# 2. Convert the input to a float.
# 3. Apply the conversion formula:
#    Fahrenheit = (Celsius * 9/5) + 32
# 4. Print the temperature in Fahrenheit.
#
# Time Complexity: O(1)
# Space Complexity: O(1)

celsius_temp = input("Enter a temperature: ")
temp = float(celsius_temp)

fahrenheit_temp = (temp * 9/5) + 32

print("Temperature in Fahrenheit:", fahrenheit_temp)