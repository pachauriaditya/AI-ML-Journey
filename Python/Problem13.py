# Average of Three Numbers Using Lambda Function
#
# Problem:
# Create a lambda function to calculate the
# average of three numbers.
#
# Approach:
# 1. Define a lambda function with three parameters.
# 2. Add the three numbers.
# 3. Divide the sum by 3 to get the average.
# 4. Print the returned result.
#
# Time Complexity: O(1)
# Space Complexity: O(1)

# Lambda function to calculate average of three numbers
avg = lambda a, b, c: (a + b + c) / 3

print(avg(10, 20, 30))