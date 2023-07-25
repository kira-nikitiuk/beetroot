#1. Реалізувати декоратор, який перевіряє, чи є аргумент функції числом та виводить повідомлення про помилку, якщо це не так.

#способ 1
def decorator(func):

    def wrapper(num):
        if not isinstance(num, (int, float)):
            return "ні, інпут не є числом"
        return func(num)
    return wrapper        

@decorator
def some_func(num):
    return f"your number{num}"

print(some_func(5))
print(some_func("a"))


#способ 2
def decorator(func):
    def wrapper(num):
        if type(num) == int or type(num) == float:
            return "Твій інпут є числом"
        else:
            return "Твій інпут не є числом"
    return wrapper

@decorator
def some_func(num):
    return num

print(some_func(-1))

