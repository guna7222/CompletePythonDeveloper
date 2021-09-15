def is_even(num):
    """
    to check even number or odd
    """
    if num % 2 == 0:
        return True
    elif num % 2 != 0:  # here we can else instead of elif to clean up code
        return False


print(is_even(12))


# clean code example

def is_even(num):
    """
    to check even number or odd
    """
    if num % 2 == 0:
        return True
    return False


is_even(23)


# clean code final example

def is_even(num):
    return num % 2 == 0


print(is_even(22))
