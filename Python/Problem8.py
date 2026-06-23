# Area of a Circle
#
# Problem:
# Take the radius of a circle as input and
# calculate its area.
#
# Approach:
# 1. Input the radius of the circle.
# 2. Apply the formula:
#    Area = π × r × r
# 3. Print the calculated area.
#
# Time Complexity: O(1)
# Space Complexity: O(1)

r = float(input("Enter the radius of the circle: "))

area = 3.14 * r * r

print("Area of the circle:", area)