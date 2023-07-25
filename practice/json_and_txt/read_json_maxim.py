# Тепер реалізуйте функціонал видалення дікта з джсон-файлу
#Умовно, у вас є в дікті значення росія москва - видаліть цей запис
import json
with open("json_file_2.json", "r+") as file:
    data = json.load(file)
    dict_index = 0
    for i in data:
        if i["location"] == "Moscow, Russia Data Tower":
            i.pop("location")
with open("json_file_2.json", "w+") as file:
    json.dump(data, file)