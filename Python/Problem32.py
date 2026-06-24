string = input("Enter a string: ")
unique = ""
for ch in string:
    if ch not in unique:
        unique += ch
print("Unique characters in the string are:", unique)
print("Number of unique characters in the string are:", len(unique))