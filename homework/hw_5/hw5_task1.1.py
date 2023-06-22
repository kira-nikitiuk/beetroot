# Task 1 (варіант 1)
# The greatest number
# Write a Python program to get the largest number from a list of random numbers with the length of 10
# Constraints: use only while loop and random module to generate numbers

from random import randint

N = 10
arr = []
while len(arr) < 10:
    arr.append(randint(1, 99))
print(arr)

i = 0
while i < N - 1:
    m = i
    j = i + 1
    while j < N:
        if arr[j] < arr[m]:
            m = j
        j += 1

    arr[i], arr[m] = arr[m], arr[i]

    i += 1

print(arr)   