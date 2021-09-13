# break
"""
Break keyword is used to break out of for loop for while loop
Break statement in python terminates the current loop and resumes execution at the next statement
"""
n = 'guna'
for i in n:
    if i == 'u':
        print(i)
        break

# Continue statement instruct a loop to continue to the next iteration
for i in range(1, 20):
    if i == 3:
        print(i)
        continue

# pass statement is a null operations, nothing happens when it executes
for i in range(1, 10):
    pass