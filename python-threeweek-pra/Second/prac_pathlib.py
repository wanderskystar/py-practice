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

#批量修改文件名
#1.设定目标文件夹(脚本所在文件夹)
target_dir = Path(__file__).resolve().parent
prefix = "new_" #加的前缀
print(f"---开始重命名：{target_dir}---")
#2.遍历文件夹
for item in target_dir.iterdir():
    #3.只处理文件，跳过文件夹和脚本本省
    if item.is_file() and item.name != "prac_pathlib.py":

        #4.构造新名字
        #item.name获取原文件名(如a.txt),加上前缀
        new_name = prefix+item.name

        #5.生成新的path对象(保留原目录，自改名字)
        new_path = item.with_name(new_name)

        #6.执行重命名操作
        item.rename(new_path)

print("---批量重命名完成---")