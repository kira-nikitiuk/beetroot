# Task 3
# Write a class TypeDecorators which has several methods for converting results of functions 
# to a specified type (if it's possible):
# methods:
# to_int
# to_str
# to_bool
# to_float
# Don't forget to use @wraps
# '''
# class TypeDecorators:
#     pass
# @TypeDecorators.to_int
# def do_nothing(string: str):
#     return string
# @TypeDecorators.to_bool
# def do_something(string: str):
#     return string
# assert do_nothing('25') == 25
# assert do_something('True') is True
# '''

from functools import wraps

class TypeDecorators:
    @staticmethod
    def to_int(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            try:
                return int(result)
            except ValueError:
                return result
        return wrapper

    @staticmethod
    def to_str(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            return str(result)
        return wrapper

    @staticmethod
    def to_bool(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            return bool(result)
        return wrapper

    @staticmethod
    def to_float(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            try:
                return float(result)
            except ValueError:
                return result
        return wrapper

if __name__ == "__main__":
    @TypeDecorators.to_int
    def do_nothing(string: str):
        return string

    @TypeDecorators.to_bool
    def do_something(string: str):
        return string
    
    result1 = do_nothing('7')
    print("do_nothing result:", result1)  
    result2 = do_something('T')
    print("do_something result:", result2)  

    
