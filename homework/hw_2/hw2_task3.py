# task 3
#Make a program with 2 numbers saved in separate variables a and b, then print the result for each of the following:
'''
Addition
Subtraction
Division
Multiplication
Exponent (Power)
Modulus
Floor division'''

a = int(input("print first number:"))
b = int(input("print second number:"))
print(f"{a} + {b} = ", a+b)
print(f"{a} - {b} = ", a-b)
print(f"{a} * {b} = ", a*b)
print(f"{a} / {b} = ", a/b)
print(f"{a} % {b} = ", a%b, f"залишок від ділення")
print(f"{a} // {b} = ", a//b, f"цілочисельне ділення")
print(f"{a} ^ {b} = ", a**b, f"піднесення до степеня варіант 1") # піднесення до степеня варіант 1
print(f"{a} ^ {b} = ", pow(a,b), f"піднесення до степеня варіант 2") # піднесення до степеня варіант 2
print(f"|{b}| = ", abs(b))
print(f"|{a}| = ", abs(a))