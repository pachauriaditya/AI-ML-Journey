list1 = list(map( int , input("Enter the numbers separated by space: ").split()))
list2 = list(map( int , input("Enter numbers separated by space: ").split()))

if set(list1).isdisjoint(set(list2)):
    print("The two lists have no common elements.")
else:
    print("The two lists have common elements.")