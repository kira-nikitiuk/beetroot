# Task 3
# Fraction
# Створіть клас Fraction, який буде представляти всю базову арифметичну логіку для дробів (+, -, /, *) з належною перевіркою й обробкою помилок. Потрібно додати магічні методи для математичних операцій та операції порівняння між об'єктами класу Fraction

# class Fraction:
#     pass

# if __name__ == "__main__":
#     x = Fraction(1, 2)
#     y = Fraction(1, 4)
#     x + y == Fraction(3, 4)

class Fraction:
    def __init__(self, numerator, denominator):
        if denominator == 0:
            raise ValueError("Denominator cannot be 0")
        
        greatest_common_divisor = self.compute_greatest_common_divisor(numerator, denominator)
        self.numerator = numerator // greatest_common_divisor
        self.denominator = denominator // greatest_common_divisor


    def compute_greatest_common_divisor(self, a, b):
        while b:
            a, b = b, a % b
        return a
    
    def __add__(self, other):
        new_numerator = self.numerator * other.denominator + other.numerator * self.denominator
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)
    
    def __sub__(self, other):
        new_numerator = self.numerator * other.denominator - other.numerator * self.denominator
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)

    def __mul__(self, other):
        new_numerator = self.numerator * other.numerator
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)

    def __truediv__(self, other):
        if other.numerator == 0:
            raise ValueError("Cannot divide by 0")
        new_numerator = self.numerator * other.denominator
        new_denominator = self.denominator * other.numerator
        return Fraction(new_numerator, new_denominator)
    
    def __eq__(self, other):
        return self.numerator == other.numerator and self.denominator == other.denominator

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"
    
    
if __name__ == "__main__":
    x = Fraction(1, 2)
    y = Fraction(1, 4)
    
    result = x + y
    print(result) 
    print(result == Fraction(3, 4)) 