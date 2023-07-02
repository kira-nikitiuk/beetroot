# Task 3 (схоже на попереднє, але з діленням та n-ю кількістю чисел)
# A simple calculator.
# Create a function called make_operation, which takes in a simple arithmetic operator as a first parameter (to keep things simple let it only be ‘+’, ‘-’ or ‘*’) and an arbitrary number of arguments (only numbers) as the second parameter. Then return the sum or product of all the numbers in the arbitrary parameter. For example:

# the call make_operation(‘+’, 7, 7, 2) should return 16
# the call make_operation(‘-’, 5, 5, -10, -20) should return 30
# the call make_operation(‘*’, 7, 6) should return 42  

def make_operation(arithmetic_operator, *args):
    result = args[0]
    if arithmetic_operator == "+":
        for i in args[1:]:
            result += i
    if arithmetic_operator == "-":
        for i in args[1:]:
            result -= i
    if arithmetic_operator == "*":
        for i in args[1:]:
            result *= i
    if arithmetic_operator == "/":
        for i in args[1:]:
            try:
                return f"Your answer is: {result / i}"
            except ZeroDivisionError:
                return "You can't divide by zero!"     

    return result        

print(make_operation("+", 4, 5))  
print(make_operation("-", 5, 5, -10, -20)) 
print(make_operation("*", 7, 6))
print(make_operation("/", 8, 2))
print(make_operation("/", 8, 0))