# is vs ==
print(True == 1)
print([] == 1)
print(''== 1)
print(10 == 10.0)
print([] == [])

# is
# is Identity operator is bit convention for strings and integers because they store in same location in the memory
print(True is True)
print("1" is "1")
print([] is []) # False
print([1,2] is [1,2]) # False

a = [1,2,3]
b = [1,2,3]
print(a is b) # False
c = a
print(c is a) # True