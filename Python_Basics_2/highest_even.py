# Highest Even

def heightEven(even):
    evens = []
    for items in even:
        if items % 2 == 0:
            evens.append(items)
    return max(evens)


print(heightEven([1, 2, 3, 4, 11, 12, 90, 22]))
