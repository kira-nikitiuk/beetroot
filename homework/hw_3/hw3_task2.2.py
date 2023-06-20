# task 2 (варіант 2)
phone_number= input("your phone number(+380__): ")
if not phone_number.isdigit():
  print("it is not a phone number, phone number include only numerical characters")
elif len(phone_number) != 9:
  print("it is not a phone number, phone number must include 10 characters long")
else:
  full_phone_number = "+380" + phone_number
  print("your phone number is correct:", full_phone_number)