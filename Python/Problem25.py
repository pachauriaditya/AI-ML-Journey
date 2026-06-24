list1 = list(map(int , input("Enter the numbers separated by space: ").split()))
list2 = list(map(int , input("Enter numbers separated by space: ").split()))

merge_list = list1 + list2
merge_list.sort()

print("Merged and sorted list:", merge_list)