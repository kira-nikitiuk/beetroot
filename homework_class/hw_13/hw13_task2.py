# Task 2
# Write a Python program to access a function inside a function (Tips: use function, which returns another function)

def first_func():
    def srcond_func():
        print("hi")

    return srcond_func()

first_func()



    

    