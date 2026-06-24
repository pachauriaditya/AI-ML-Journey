list = list(map(int , input("Enter the numbers separated by space: ").split()))

for i in range(len(list)):
    count = 0

    for j in range(len(list)):
        if list[i] == list[j]:
            count += 1
    
    if count > 1 and list[i] not in list[:i]:
        print(f"{list[i]} occurs {count} times")