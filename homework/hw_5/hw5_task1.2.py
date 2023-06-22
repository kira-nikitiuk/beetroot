# Task 1 (варіант 2)
# The greatest number
# Write a Python program to get the largest number from a list of random numbers with the length of 10
# Constraints: use only while loop and random module to generate numbers
import random 

def selection_sort(list1):

    for i in range(len(list1)):
        minimum = i

        for j in range(i + 1, len(list1)):
            if list1[j] < list1[minimum]:
                minimum = j

        list1[minimum], list1[i] = list1[i], list1[minimum]

    return list1

list1 = []

while len(list1)<10:
   random_number = random.randint(1,100)
   list1.append(random_number)
   
print("Original list:", list1)
sorted_list = selection_sort(list1)
print("Sorted list:", sorted_list) 