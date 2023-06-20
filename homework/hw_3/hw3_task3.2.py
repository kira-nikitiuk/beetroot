import random

def randomaizer(a,b):

  if a<75 and b>20:
    print(f"{a}-{b}=")
    expected_result = a - b
  elif a<75 and b<20:
    print(f"{a}+{b}=")
    expected_result = a + b
  elif a>=75 and b<20:
    print(f"{a}*{b}=")
    expected_result = a * b
  else:
    print(f"{a}/{b}=")
    expected_result = a / b

  return expected_result

a = random.randrange(50,100)
b = random.randrange(0,49)
expected_result = randomaizer(a,b)
answer = input("your answer: ")


if answer.isdigit():
  answer = float(answer)
  if answer == expected_result:
    print("WELL DONE!")
  else:
    print("you are bad at math...")
else:
  print("error: answer is not a number!!!")