# 2. Написати декоратор, який обмежує кількість разів виклику функції та видає помилку, якщо ліміт перевищено.
# not ready

def decorator(func):
    calls = 0
    def wrapper(name_1, name_2):
        nonlocal calls #+= 1
        while calls < 6:
            print("you can call function")
    return wrapper        

@decorator
def function(name_1, name_2):
    return f"hello {name_1} and {name_2}\n"


# num = 3
# print(function("Maxim", "Kira")*num)


