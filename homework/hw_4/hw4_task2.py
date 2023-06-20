#Task 2
#The birthday greeting program.
#Write a program that takes your name as input, and then your age as input and greets you with the following:
#“Hello <name>, on your next birthday you’ll be <age+1> years”

name = input("your name is: ")
age = int(input("your age is: "))
new_age = age+1
print(f"Hello {name.capitalize()}, on your next birthday you’ll be {new_age} years")