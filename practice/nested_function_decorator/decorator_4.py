# 4. Напишіть декоратор, який перевіряє типи аргументів, переданих до функції, та виводить повідомлення про помилку, якщо типи не відповідають очікуваним

def decorator(func):
    def wrapper(*args):
        _list = [int, float, str]
        for i in args:
            if type(i) not in _list:
                print(f"Аргумент '{i}', не є одним з цих типів данних: int, float, str!")
            else:
                print(f"Аргумент: '{i}', відповідає певним типам данних!")

    return wrapper


@decorator
def function(*args):
    print(args)


function(True, 5, "23", "k", 7.9)
