# Task 4
# Створити лист із днями тижня.
# В один рядок (ну або як завжди) створити словник виду: {1: “Monday”, 2:...

list_1 = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")

dict_1 = {}
num_1 = 1

for i in list_1:
    dict_1.update({i : num_1})
    num_1 += 1

print(f"first dictionary (type day:number) :  {dict_1}")    


#Також в один рядок або як вдасться створити зворотний словник {“Monday”: 1,    

dict_2 = {}
num_2 = 1

for j in list_1:
    dict_2.update({num_2 : j})
    num_2 += 1

print(f"second dictionary (type number:day) :   {dict_2}")  