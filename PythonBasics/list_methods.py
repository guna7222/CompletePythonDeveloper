# List methods
# A method is a action that belongs to specific data type

# append() method is used to add the value at the end of the list

num = [1, 2, 3, 4, 5, 6] # Adds an element at the end of the list
print(num)

# insert(index, object) is used to add the value at specified index
names = ['python', 'docker', 'git']
names.insert(0, 'linux')
print(names)

# extend()
fruits = ['apple', 'grapes', 'mango']
fruits.extend(['pineapple', 'guvva'])
print(fruits)

# pop() removes the last item of the list ( note)
# pop(1) removes the specified index value

programming_languages = ['python', 'c']
new = programming_languages.pop()
print(new)
print(programming_languages)

# remove()
bikes = ['yamaha', 'royal en-field', 'triumph']
bikes.remove('yamaha')
print(bikes)

# clear()
cars = ['bmw', 'audi', 'range rover']
cars.clear()
print(cars)

# index(value, start, stop) ( remember)
cars = ['bmw', 'audi', 'range rover']
new = cars.index('bmw')
print(new)
print(cars)

# count() ( remember)
cars = ['bmw', 'audi', 'range rover', 'bmw']
new_cars = cars.count('bmw')
print(new_cars)
print(cars)

# sort()
cars = ['bmw', 'audi', 'range rover', 'bmw']
cars.sort()
print(cars)

# reverse()
cars = ['bmw', 'audi', 'range rover', 'bmw']
cars.reverse()
print(cars)

"""
append()	Adds an element at the end of the list
clear()	Removes all the elements from the list
copy()	Returns a copy of the list
count()	Returns the number of elements with the specified value
extend()	Add the elements of a list (or any iterable), to the end of the current list
index()	Returns the index of the first element with the specified value
insert()	Adds an element at the specified position
pop()	Removes the element at the specified position
remove()	Removes the item with the specified value
reverse()	Reverses the order of the list
sort()	Sorts the list
"""

# A method is a function that “belongs to” an object.
