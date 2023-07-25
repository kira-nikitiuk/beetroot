# Реалізувати функцію, яка буде загорнута в декілька декораторів (декоратори потрібно написати самим)
def decoranor_1(func):
    def wrapper(arg):
        if len(arg) > 10:
            print("argument more then 10")
            return func(arg)
        else:
            print(f"your argument {arg} less then 10")
            return func(arg)
    return wrapper    
        
def decoranor_2(func):
    def wrapper(arg):
        try:
            arg == str(arg)
        except ValueError:
            print("your argument isnt a string") 
            return func(arg)   

        if str(arg).isalpha():
            print("your arguments hes only letters")
            return func(arg)
        else:
            print("your arguments hes not only letters")
            return func(arg) 
    return wrapper



@decoranor_1
@decoranor_2

def function(arg):
    print(arg)


function("2222222222222222222")

