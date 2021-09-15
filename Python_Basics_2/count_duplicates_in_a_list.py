# count duplicates in a list
my_list = [1, 2, 1, 1, 1, 2, 3, 5, 4]
duplicates = []
for values in my_list:
    if my_list.count(values) > 1:
        duplicates.append(values)

print(len(duplicates))  # here len function is used to count the duplicates
