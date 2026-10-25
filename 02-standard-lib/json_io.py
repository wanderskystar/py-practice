"""
@File:  json_io.py
@Desc:  json模块读写练习
任务:   构造字典  写入data.json    再读取json文件到程序
知识点:          json.dump 保存   json.load 加载
"""
import json
# 1. 定义本地字典数据
data_dict = { 
    "name": "python练习",
    "author": "student",
    "hobby": ["coding", "data structure"],
    "score": 95
}
# 2. 将字典保存输出到 data.json
with open("data.json","w",encoding="utf-8") as f:
    json.dump(data_dict,f,ensure_ascii=False,indent=4)
print("字典写入json成功!")
# 3. 把 data.json 读回程序里面
with open("data.json","r",encoding="utf-8") as f:
    load_data = json.load(f)

print("json文件读写:")
print(load_data)
print(type(load_data))
