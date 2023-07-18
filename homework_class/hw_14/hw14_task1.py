# Task 1
# Write a decorator that prints a function with arguments passed to it.
# NO TE! It should print the function, not the result of its execution!

import inspect

def decorator(func):
    def wrapper(*args, **kwargs):
        code = inspect.getsource(func)
        print(code)
        return func(*args, **kwargs)
    return wrapper


@decorator
def function(*args, **kwargs):
    print(args, kwargs)

function(1, 2, a=3, b=4)


    