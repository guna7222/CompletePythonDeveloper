# *args vs **kwargs
# arguments vs keyword arguments
def super_function(*args):
    print(args)
    return sum(args)


print(super_function(1, 2, 3, 4))


# **kwargs
def another_function(**kwargs):
    print(kwargs)


print(another_function(name='gunasekhar', age=22))


# Another Example
def final_example(*args, **kwargs):
    total = 0
    for items in kwargs.values():
        total = total + items
    return sum(args) + total


print(final_example(1, 2, 3, 4, 5, num1=5, num2=12))
# Rule: parameter, *args, default parameter, **kwargs
