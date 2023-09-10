# Напишіть декоратор, який записує в файл час, коли була викликана функція

import time

def data_time(func):
    def wrapper(_time):
        with open(r"C:\\Users\\Asus\\Desktop\\beetroot\\practice\\nested_function_decorator\\time_dec\\data_time.txt", "a") as file:
            file.write(f"час коли була викликана функція: {_time}\n")
        return func(_time)
    return wrapper 

@data_time
def function(_time):
    return _time

print(function(time.strftime("%Y-%m-%d %H:%M:%S")))


