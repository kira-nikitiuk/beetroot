# удаляет москву

# import json

# with open("file2.json", "r") as file:
#     data = json.load(file)

# if "location" in data:
#     del data["location"]

# updated_json_data = json.dumps(data)

# with open('file2.json', 'w') as file:
#     file.write(updated_json_data)

import json

with open("file2.json", "r") as file:
    data = json.load(file)

    index_to_remove = 0
    for i, item in enumerate(data):
        if "location" in item and item["location"] == "Moscow, Russia Data Tower":
            index_to_remove = i
            break

    if index_to_remove != 0:
        del data[index_to_remove]

with open("file2.json", "w") as file:
    json.dump(data, file)