# For Loops
# Nested Loops
# For loop is used for iterating over a sequence( list, tuple, sets, dict, strings)

for item in "Hello Python":
    print(item)

# nested for loops
for item in [1,2,3,4,5]:
    for string in ['a', 'b']:
        print(item, string)

# dict
cars = {
    'name': 'Bmw',
    'color': 'black',
    'price': 250000
}
for i in cars.items():
    print(i)