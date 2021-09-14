# return
# The return keyword is to exit a function and return a value.
# functions should return something
# should do one thing really one.
def addition(num1, num2):
    return num1 + num2


total = addition(10, 5)

print(addition(total, 100))

print(addition(15, addition(2, 12)))

# nested functions
def sum(num1, num2):
    def another_function(n1, n2):
        return n1 + n2
    return another_function(num1, num2)

total = sum(12, 12)
print(total)