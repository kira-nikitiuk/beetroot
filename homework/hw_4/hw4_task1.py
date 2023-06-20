# Task 1
#The Guessing Game.
#Write a program that generates a random number between 1 and 10 and lets the user guess what number was generated. The result should be sent back to the user via a print statement.

import random

random_number = random.randrange(1,10)
your_number = int(input("your number: "))
print(your_number)
if your_number == random_number:
  print(f"random number = {random_number}, your number = {your_number}, {random_number} = {your_number}, you win!")
else:
  print(f"random number = {random_number}, but your number = {your_number}, you are a loser")