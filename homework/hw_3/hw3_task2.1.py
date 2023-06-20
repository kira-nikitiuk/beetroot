# task 2
# Make a program that checks if a string is in the right format for a phone number. The program should check that the string contains only numerical characters and is only 10 characters long. Print a suitable message depending on the outcome of the string evaluation.
phone_number= input("your phone number: ")
if not phone_number.isdigit():
  print("it is not a phone number, phone number include only numerical characters")
elif len(phone_number) != 10:
  print("it is not a phone number, phone number must include 10 characters long")
else:
  print("it is the correct phone number")