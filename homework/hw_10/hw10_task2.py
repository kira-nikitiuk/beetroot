# Task 2
#Write a function that takes in two numbers from the user via input(), call the numbers a and b, and then returns the value of squared a divided by b, construct a try-except block which raises an exception if the two values given by the input function were not numbers, and if value b was zero (cannot divide by zero).    

def division():

    try:
        a = int(input("ввведіть значення a:"))
        b = int(input("ввведіть значення b:"))
        c = (a**2) / b
        return c
    except ValueError:
        raise ValueError ("your input is not intrger!")

    except ZeroDivisionError:
        raise ZeroDivisionError ("oh, no! its division by zero! Error!!! ")


try:
    result = division()
    print("result: ", result)
except ValueError as e:
    print("error: ", str(e))
except ZeroDivisionError as e:
    print("error: ", str(e))

