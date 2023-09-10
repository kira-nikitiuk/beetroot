while True:
  reply = input("enter two strings and math jperation, if you want to quit:")
  if reply.lower() == "q":
    break
  elif len(reply.split(" "))!=3:
    print("add more digits")
    continue


  else:
    my_list = reply.split(" ")
    if (my_list[0].isdigit() and my_list[1].isdigit()):
      #print(f"{int(my_list[0])}{int(my_list[1])}")
      if my_list[2]=="+":
         print(int(my_list[0]) + int(my_list[1]))
      elif my_list[2]=="-":
         print(int(my_list[0]) - int(my_list[1]))
      elif my_list[2]=="*":
         print(int(my_list[0]) * int(my_list[1]))
      elif my_list[2]=="/":
          try:
            print(int(my_list[0]) / int(my_list[1]))
          except ZeroDivisionError:
            print("на 0 ділити не можна")

              
         
      else:
        print("invalid operation")

def calculator_2(num_1, num_2, operator):
    if operator == "+":
        return f"Your answer is: {num_1 + num_2}"
    elif operator == "-":
        return f"Your answer is: {num_1 - num_2}"
    elif operator == "*":
        return f"Your answer is: {num_1 * num_2}"
    elif operator == "/":
        try:
            return f"Your answer is: {num_1 / num_2}"
        except ZeroDivisionError:
            return "You can't divide by zero!"


# print(calculator(int(input("Please enter the first number: ")),
#                  int(input("Please enter the second number: ")),
#                  input("Please enter an operator(+, -, *, /) to solve 2 numbers: ")))
  