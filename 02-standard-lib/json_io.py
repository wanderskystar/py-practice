import json


data_dict = { 
    "name": "python练习",
    "author": "student",
    "hobby": ["coding", "data structure"],
    "score": 95
}

with open("data.json","w",encoding="utf-8") as f:
    json.dump(data_dict,f,ensure_ascii=False,indent=4)
print("字典写入json成功!")

with open("data.json","r",encoding="utf-8") as f:
    load_data = json.load(f)

print("json文件读写:")
print(load_data)
print(type(load_data))
