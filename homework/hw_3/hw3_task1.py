# task 1
# Write a Python program to get a string made of the first 2 and the last 2 chars from a given string. If the string length is less than 2, return instead of the empty string.
string1 = input("your string: ")
if len(string1) <= 1:
  print(" ")
elif len(string1) == 2:
  print(string1*2)
else:
  first_two_chars = string1[:2]
  last_two_chars = string1[-2:]
  print(first_two_chars + last_two_chars)