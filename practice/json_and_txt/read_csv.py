'''Реалізувати функціонал вичитки, апдейту і видалення даних з цього файлу.
Потім реалізувати функціонал запису своїх даних у інший csv-файл.
Як додаткове завдання - реалізувати функціонал запису діктів у csv-файл'''
# 1. Обгорнути весь функціонал у окремі функції
import csv
csv_filename = 'Work_with_files/nestle_employee.csv'
# Simple way
# with open(csv_filename) as csv_file:
#     reader = csv.reader(csv_file)
#     lst_from_csv_file = list(reader)
# print(lst_from_csv_file)
# One-liner method
#import csv; lst_from_csv_file=list(csv.reader(open(csv_filename))); print(lst_from_csv_file)
# Pandas method # Pandas module must be installed
# import pandas as pd
# read_from_pandas = pd.read_csv(csv_filename, header=None)
# list_from_csv_file = read_from_pandas.values.tolist()
# print(list_from_csv_file)
# Raw Python No Dependency
# with open(csv_filename) as f:
#     lines = f.readlines()
#     lst = [line.strip().split(',') for line in lines]
#     print(lst)
# 2. Додати функціонал на перевірку наявності файлу та відловити виняткові ситуації,
# якщо файл відсутній або має неправильний формат.
try:
    with open(csv_filename, 'r') as file:
        csv_reader = csv.reader(file)
        list_from_csv_file = []
        for row in csv_reader:
            list_from_csv_file.append(row)
    #print(list_from_csv_file)
except FileNotFoundError:
    print('File Not Found!')
except AttributeError:
    print('module "csv" has no attribute "open"!')
except TypeError:
    print('File of the wrong type!')
# 3. Записати вміст файлу в інший файл
with open('Work_with_files/duplicate_nestle_employee.csv', 'w', newline='') as file:
    csv_writer = csv.writer(file)
    csv_writer.writerows(list_from_csv_file)
# 4. Записати у файл дані, які введе користувач з терміналу.
# Передбачити можливість запису в файли різних форматів - txt/json/csv
input_from_the_user = list_from_csv_file
# Write to txt
with open('Work_with_files/input_to_txt_nestle_employee.txt', 'w') as file:
    file.write(str(input_from_the_user))
# Write to json
import json
turn_list_to_dict = {}
i = 0
while i < len(list_from_csv_file):
    turn_list_to_dict[i] = list_from_csv_file[i]
    i += 1
print(turn_list_to_dict)
with open('Work_with_files/input_to_txt_nestle_employee.json', 'w') as file:
    json.dump(turn_list_to_dict, file)
# Write to csv is similar to section 3