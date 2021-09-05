# sets
# set is a unordered collection of unique values
# add()
hello = {1,2,3,4}
hello.add(5)
print(hello)

# difference()
my_set = {1, 2, 3}
your_set = {4,5,6, 3}
print(my_set.difference(your_set))

# discard()
my_set.discard(2)
print(my_set)

# intersection
print(my_set.intersection(your_set))

# difference_update()
my_set.difference_update(your_set)
print(my_set)

# isdisjoint()
first_set = {1,2,3}
second_set = {4,5,6,3}
print(first_set.isdisjoint(second_set))

# union()
first_set = {1,2,3}
second_set = {4,5,6,3}
print(first_set.union(second_set))
print(first_set | second_set)

# issubset()
third_set = {1,2,3}
fourth_set = {1,2,4,5,6, 3}
print(third_set.issubset(fourth_set))

# issuperset()
print(fourth_set.issuperset(third_set))