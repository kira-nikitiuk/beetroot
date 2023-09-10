import json


greeting = "hi beetroot"
with open("file3.json", "r+") as file:
    data = json.load(file)
    #data.append(greeting)
    data.insert(0, greeting)

    print(data)

with open("file3.json", "w+") as file:
    json.dump(data, file)    