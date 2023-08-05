# Task 4
# Custom exception
# Create your custom exception named 'CustomException', you can inherit from base Exception class,
# but extend its functionality to log every error message to a file named 'logs.txt'. 
# Tips: Use __init__ method to extend functionality for saving messages to file

# '''
# class CustomException(Exception):
# def __init__(self, msg):
# '''


class CustomException(Exception):
    def __init__(self, msg):
        super().__init__(msg)
        self.log_error(msg)

    def log_error(self, msg):
        with open('C:\\Users\\Asus\\Desktop\\beetroot\\homework_class\\hw_16\\logs.txt', 'a') as file:
            file.write(f'помилка: {msg}\n')

try:
    raise CustomException("це користувацьке виключення")
except CustomException as e:
    print("виклячення:", e)
           

