# робить з AMD Ryzen -> AMD Ryzen 2

import json

with open('file1.json', 'r') as file:
    json_read = file.read()

data = json.loads(json_read)

for i in data:
    if "processor" in i:
        i["processor"] = "AMD Ryzen 2"

updated_json_data = json.dumps(data)

with open('file1.json', 'w') as file:
    file.write(updated_json_data)