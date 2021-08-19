# Formatted Strings
"""
A python formatted method takes the passed arguments, format them and place them in the strings
where the placeholders are.

"""
name = 'gunasekhar'
age = 23
print(f'My name is {name} and i\'m {age} year old.')

print('My name is {} and i\'m {} year old'.format(name, age))

print('My name is {name} and i\'m {age} year old'.format(name='guna', age=23))

