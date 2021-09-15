"""
Docstrings are not actually comments, but, they are documentation strings.
These docstrings are within triple quotes.
They are not assigned to any variable and therefore, at times, serve the purpose of comments as well.
"""


#  by using the docstrings you can comment inside the function
def simple(a):
    """
    Info:- this functions prints and returns
    """
    print(a)


help(simple)
simple('!!!!')
print(simple.__doc__)
