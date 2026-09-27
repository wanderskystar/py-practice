from pathlib import Path

# #假设单前路径 包装成Path对象.获取绝对完整路径(把相对路径、`../`这类简写全部展开).=父目录
# p = Path(__file__).resolve().parent

# # 常用属性
# print(p.name)      # 当前文件夹/文件名
# print(p.suffix)    # 后缀名（如 .py, .txt）
# print(p.parent)    # 上一级目录
# print(p.exists())  # 是否存在
#1.设定你要遍历的目标文件夹
#此处假设为脚本所在的文件夹
target_dir = Path(__file__).resolve().parent
print(f"正在遍历文件夹：{target_dir}")
#2.用iterdir遍历文件夹下的内容
for item in target_dir.iterdir():
    #item是一个Path对象

    #3.区分文件和文件夹
    if item.is_file():
        print(f"[文件]{item.name}")
    elif item.is_dir():
        print(f"[文件夹]{item.name}")
        