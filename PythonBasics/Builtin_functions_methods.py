# Built-in Functions and methods

greet = 'hai how are you'
print(greet[0:len(greet)])
print(greet[:])

# len() function is used to get the length of the string.

# upper() method

name = 'gunasekhar'
print(name.upper()) # Converts string into upper case

# capitalize()
print(name.capitalize()) # Converts the first character to upper case

# lower()
print(name.lower()) # converts the string into lower case

# find(start, stop, end)
print(name.find('se')) # find method returns the index of the first occurrence of the specified value.

# replace()
print(name.replace('g', 'GG'))

