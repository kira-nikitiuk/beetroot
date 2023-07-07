# Task 1
# Imports practice
# Make a directory with 2 modules; make a function in one of them; then import this function in the other module and use that in your script of choice.


def comparison(first_num, second_num):
    if first_num > second_num:
        final_number = first_num - second_num 
        return f" перше число = {first_num}, друге число = {second_num}, перше число більше за друге на {final_number} "
    elif second_num > first_num:
        final_number = second_num - first_num
        return f" перше число = {first_num}, друге число = {second_num}, перше число менше за друге на {final_number} "
    else:
        return f" перше число = другому числу ( {second_num} = {first_num} )"
     
