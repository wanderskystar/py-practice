#文件名：prac_pathlib.py
#功能：pathlib路径库示例，        遍历文件夹，            批量给文件添加前缀重命名，        支持预览模式
#学习点：Path对象(自带一堆方法)、   iterdir遍历、      with_name修改路径、rename重命名、     dry_run预览思想





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
def batch_rename(dry_run=True):
    """
    dry_run = True:预览只打印不改名(默认开启)
    dry_run = False:真正执行重命名
    """
    
    #1.设定目标文件夹(脚本所在文件夹)
    target_dir = Path(__file__).resolve().parent
    prefix = "new_" #加的前缀
    print(f"正在遍历文件夹：{target_dir}")
    if dry_run:
        print("====【预览模式】====")
    print(f"---开始重命名：{target_dir}---")

    #2.用iterdir遍历文件夹下的内容
    for item in target_dir.iterdir():
        #3.只处理文件，跳过文件夹和脚本本省
        if item.is_file() and item.name != "prac_pathlib.py":

            #4.构造新名字
            #item.name获取原文件名(如a.txt),加上前缀(备好名字文本)
            new_name = prefix+item.name
            #5.生成新的path对象(用.with_name(新名字)正式改成新名字)
            new_path = item.with_name(new_name)

            if new_path.exists():
                print(f"!跳过：{item.name}->{new_name},目标文件已存在")
                continue

            print(f"{item.name}->{new_name}")
            #6.执行重命名操作
            if not dry_run:
                item.rename(new_path)
    if dry_run:
        print("\n=====预览结束，上面只是计划，没有改动文件=====")
    else:
        print("---批量重命名完成---")

if __name__ == "__main__":
    batch_rename(dry_run=True)#此为预览
