# task 3
#Words combination
#Create a program that reads an input string and then creates and prints 5 random strings from characters of the input string.
#For example, the program obtained the word ‘hello’, so it should print 5 random strings(words) that combine characters
#'h', 'e', 'l', 'l', 'o' -> 'hlelo', 'olelh', 'loleh' …
#Tips: Use random module to get random char from string)

import random

string1 = input("your five letter word:")
splited_string = list(string1)
print(splited_string)
for i in range(5):
  random_string = ''.join(random.choice(string1) for i in range(len(string1)))
  print(random_string)