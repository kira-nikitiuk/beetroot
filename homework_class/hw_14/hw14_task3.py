def arg_rules(type_: type, max_length: int, contains: list):
    def decorator(func):
        def wrapper(*args, **kwargs):
           
           
            if not isinstance(args[0], type_):
                raise TypeError(f"Error: Argument type should be {type_.__name__}")
            
            
            if len(args[0]) > max_length:
                raise ValueError(f"Error: Argument length should be at most {max_length}")
            
           
            for symbol in contains:
                if symbol not in args[0]:
                    raise ValueError(f"Error: Argument should contain the symbol '{symbol}'")
            

            return func(*args, **kwargs)
        return wrapper
    return decorator

@arg_rules(type_ = str, max_length = 15, contains = ['05', '@'])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"

try:
    create_slogan('johndoe05@gmail.com')
except Exception as e:
    print(e) 

result = create_slogan('S@SH05')
print(result) 
