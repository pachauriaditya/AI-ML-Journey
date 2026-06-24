nums = tuple(map(int, input("Enter numbers separated by space: ").split()))
even = []
odd =[]

for i in nums:
    if i%2 == 0:
        even.append(i)
    else:
        odd.append(i)

even = tuple(even)
odd = tuple(odd)

print("Even numbers:", even)
print("Odd numbers:", odd)