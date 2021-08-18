"""
Fundamental Data Types,
Custom Data Types:- we can create our own custom data types by using classes
specialized data types:- modules, packages
"""
a = 10
b = 20
print(a + b)

# A data type is a values in Python

'''
To store a floating point number we need more memory comparing with int 
'''

print(5 ** 5)  # Exponentiation(**)

print(2 // 4)  # floor division (//)

print(4 % 5)  # Modulo (%) will return an reminder

# math functions
print(round(2.5))  # round()

print(abs(-12))  # abs() returns absolute value of the argument

# operator precedence
print((12 - 2) - 2)
'''
()
**
* /
+ -

'''
print(bin(5))
print(int('0b101', 2))

'''
Note:-  A programs is all about storing, retrieving, manipulating data.

a program is a simply instructions that tells computer what to do
'''
# variables:- are containers for storing data types.
my_name = 'gunasekhar'
print(my_name)

print(len(my_name))

# Many values to Multiple Variables
a, b, c = 12, 12, 12
print(a)
print(b)
print(c)

# isinstance() function returns True if a specified object is of the specified data type
a = 12
if isinstance(a, str):
    print('int')
else:
    print('no')

PI = 3.14  # To show constants

# Expression vs Statements
a = 10  # statement
b = 10 / 2  # 10/2 is called expression because it produces the value (and entire line is called statement).

'''
Statement:- A statement represents an action or command e.g:- print statement, assignment statement 
expression:- expression is a combination of variables, operators and values that yields a result values.
'''

# augmented assignment operator (is called short-hand)
addition = 10
addition += 100
print(addition)

# string concatenation
first_name = 'guna '
second_name = 'sekhar'
print(first_name + second_name)

# Type conversion:- Type conversion refers to the conversion of one data type into another data type.
print(type(int(str(100))))

# Escape sequence
print('it\'s sunny today')

print("it's a kind of \"sunny Today\" and some more ")

print('\t hello world \n hello Python')

'''
formatted strings:- format method takes the passed arguments, formats them and place them in the strings where 
the placeholders are 
'''
name = 'gunasekhar'
age = 23
print(f'my name is {name} and im {age} years old')
