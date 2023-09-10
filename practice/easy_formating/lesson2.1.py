#Реалізуйте функціонал генерування пошт для компанії "kobzar.com", де користувач повинен самостійно вводити своє ім'я і прізвище з терміналу.
name= input("your name:")
surname= input("your surname:")
adress="@kobzar.com"
print(f"{name}.{surname}{adress}")
print(f"{name[0]}.{surname}{adress}")
print(f"{name[0:3]}.{surname[0:3]}{adress}")