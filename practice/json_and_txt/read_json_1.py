# робить з AMD Ryzen -> AMD Ryzen 2

import json


with open("file1.json", "r+") as jfile:
    data = json.load(jfile)
    # p = data["processor"]
    for i in data:
        print(i["processor"])
        if i["processor"] == 'AMD Ryzen':
            i["processor"] = 'AMD Ryzen 2'
    #for i in data



    for x in data:
        print(x)
    # json.dump(data, jfile)

with open("file1.json", "w+") as jfile:
    json.dump(data, jfile)       
     
