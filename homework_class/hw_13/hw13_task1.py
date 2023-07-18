# Task 1
# Write a Python program to detect the number of local variables declared in a function.

import inspect

def local_variables(func):
    code = inspect.getsource(func)
    new_code = code.split("\n")
    variable = "="
    element_to_skip = "=="
    counter = 0
    for line in new_code:
        line = line.strip()
        if variable in line and element_to_skip not in line:
             counter += 1
      
    return counter

def test():
    x = 1
    y = 2
    z = 3
    z == 3

    return x + y 

counted_function = local_variables(test)
print(counted_function)



