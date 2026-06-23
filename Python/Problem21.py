# Prime Number Checker Using Function
#
# Problem:
# Determine whether a given number is prime or not.
# A prime number has exactly two factors:
# 1 and itself.
#
# Approach:
# 1. If n <= 1, return False.
# 2. Check divisibility from 2 to n - 1.
# 3. If any number divides n completely,
#    return False.
# 4. Otherwise, return True.
# 5. Print the result.
#
# Time Complexity: O(n)
# Space Complexity: O(1)

def isPrime(n):
    if n <= 1:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True

n = int(input("Enter a number: "))

if isPrime(n):
    print(f"{n} is a prime number.")
else:
    print(f"{n} is not a prime number.")