# Data structures is the way to organize data.
dictionary = {
    'name': 'gunasekhar',
    'age': 22
}
print(dictionary['age'])

# A Dictionary is a collection which is ordered, changeable and won't allow duplicate values.
dictionary = {
    'names': ['guna', 'thrilok', 'hemanth'],
    'job': True,
    'salary': 12.2
}
print(dictionary['names'][1])

# dict keys must be immutable

data = {
    'car': ['bmw', 'audi'],
    123: 123,
    True: 'False',
    (1, 2, 3) : 'hey you'
}
print(True)
print(123)
print((1,2,3))

# dict methods
# get()
dic = {
    'name': 'guna',
    'age': 23,
    'language': 'English'
}
print(dic.get('python', 'yes'))

# another way of creating dict
another_way = dict(name = 'gunasekhar')
print(another_way)

# value()
dic = {
    'name': 'guna',
    'age': 23,
    'language': 'English'
}
print('guna' in dic.values())

# keys()
# items()
# clear()
# copy()
# pop(key)
# popitem()
# update()


