# Task 2
# Exclusive common numbers.
# Generate 2 lists with the length of 10 with random integers from 1 to 10, and make a third list containing the common integers between the 2 initial lists without any duplicates.
# Constraints: use only while loop and random module to generate numbers

import random

list1 = []   #list1 = random.sample(range(1, 11), 10)
i = 0

while i < 10:
    list1.append(random.randint(1, 10))
    i += 1
print(list1)

list2 = []  #list2 = random.sample(range(1, 11), 10)
j = 0
while j < 10:
    list2.append(random.randint(1, 10))
    j += 1
print(list2)

common_numbers = list(set(list1) & set(list2))
print(common_numbers)
