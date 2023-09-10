# Task 1
# Practice asynchronous code
# Create a separate asynchronous code to calculate Fibonacci, factorial, squares and cubic for an input number. 
# Schedule the execution of this code using asyncio.gather for a list of integers from 1 to 10. 
# You need to get four lists of results from corresponding functions.
# Rewrite the code to use simple functions to get the same results but using a multiprocessing library. 
# Time the execution of both realizations, explore the results, what realization is more effective, 
# why did you get a result like this.

import multiprocessing
import time

def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
    

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
    

def squares(n):
    return n * n


def cubic(n):
    return n ** 3

def main():
    numbers = list(range(1, 11))

    start = time.time()

    with multiprocessing.Pool() as pool:
        fibonacci_r = pool.map(fibonacci, numbers)
        factorial_r = pool.map(factorial, numbers)
        squares_r = pool.map(squares, numbers)
        cubic_r = pool.map(cubic, numbers)

    end = time.time()

    print("\ntime: ", end - start)

    print("\nFibonacci: ", fibonacci_r)
    print("factorial: ", factorial_r)
    print("squares: ", squares_r)
    print("cubic: ", cubic_r)    

if __name__ == "__main__":
    main()