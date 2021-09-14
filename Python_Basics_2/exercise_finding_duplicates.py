# Finding duplicates in a list
my_list = [1, 2, 3, 4, 1, 2, 5, 6, 7, 8, 9]
duplicates = []
for values in my_list:
    if my_list.count(values) > 1:
        if values not in duplicates:
            duplicates.append(values)
print(duplicates)

# Remove duplicates in a list
my_list = [1, 2, 3, 4, 1, 2, 5, 6, 7, 8, 9]
unique = set(my_list)
print(unique)

# Remove duplicates in a list using dictionaries
my_list = [1, 2, 3, 4, 1, 2, 5, 6, 7, 8, 9]
unique = list(dict.fromkeys(my_list))
print(unique)

# Remove duplicates from a list
my_list = [1, 2, 3, 4, 1, 2, 5, 6, 7, 8, 9]
unique = []
for values in my_list:
    if values not in unique:
        unique.append(values)
print(unique)