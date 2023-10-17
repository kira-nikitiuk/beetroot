# Task 1
# Practice asynchronous code
# Create a separate asynchronous code to calculate Fibonacci, factorial, squares and cubic for an input number. 
# Schedule the execution of this code using asyncio.gather for a list of integers from 1 to 10. 
# You need to get four lists of results from corresponding functions.
# Rewrite the code to use simple functions to get the same results but using a multiprocessing library. 
# Time the execution of both realizations, explore the results, what realization is more effective, 
# why did you get a result like this.

import asyncio

async def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return await fibonacci(n - 1) + await fibonacci(n - 2)
    

async def factorial(n):
    if n == 0:
        return 1
    else:
        return n * await factorial(n - 1)
    

async def squares(n):
    return n * n


async def cubic(n):
    return n ** 3


async def main():
    numbers = list(range(1, 11))
    fibonacci_ = [fibonacci(n) for n in numbers]
    factorial_ = [factorial(n) for n in numbers]
    squares_ = [squares(n) for n in numbers]
    cubic_ = [cubic(n) for n in numbers]

    fibonacci_r, factorial_r, squares_r, cubic_r = await asyncio.gather(
        asyncio.gather(*fibonacci_),
        asyncio.gather(*factorial_),
        asyncio.gather(*squares_),
        asyncio.gather(*cubic_ )
    ) 

    print("Fibonacci: ", fibonacci_r)
    print("factorial: ", factorial_r)
    print("squares: ", squares_r)
    print("cubic: ", cubic_r)

if __name__ == "__main__":
    asyncio.run(main()) 
    