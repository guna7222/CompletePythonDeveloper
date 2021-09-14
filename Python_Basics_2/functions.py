# Functions
# A function is a block of code which will execute when a function is called def keyword is used to define a function
def my_function(a, b):
    return a + b


print(my_function(12, 12))


# function example
def greetings(user_first_name, user_second_name):
    print(user_first_name + ' ' + user_second_name)


user_first_name = input("Please enter your first name:- ")
user_second_name = input("please enter your second name:- ")
greetings(user_first_name, user_second_name)
