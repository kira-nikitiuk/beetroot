# Task 1
# Imports practice
#  Make a directory with 2 modules; make a function in one of them; then import this function in the other module and use that in your script of choice.

from hw9_task1_functoin import comparison

def comparison_2 ():
    your_name = input("Enter your name: ")
    capitalized_name = your_name.capitalize()
    print(f"Hi {capitalized_name}! Let's study comparison!")
    first_num = int(input("enter first number: "))
    second_num = int(input("enter second number: " ))
    result = comparison(first_num, second_num)
    return result

test = comparison_2()
print(test)




