# Income Tax Rate Calculator
#
# Problem:
# Take a user's salary as input and determine
# the applicable tax rate based on salary brackets.
#
# Tax Slabs:
# - Salary < 30,000      -> 5% Tax
# - 30,000 <= Salary < 70,000 -> 15% Tax
# - Salary >= 70,000     -> 25% Tax
#
# Approach:
# 1. Input the salary.
# 2. Check which salary range it falls into.
# 3. Print the corresponding tax rate.
#
# Time Complexity: O(1)
# Space Complexity: O(1)

salary = int(input("Enter your salary: "))

if salary < 30000:
    print("Final Rate tax is 5%")

if salary >= 30000 and salary < 70000:
    print("Final Rate tax is 15%")

if salary >= 70000:
    print("Final Rate tax is 25%")