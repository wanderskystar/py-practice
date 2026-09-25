from pathlib import Path

#假设单前路径 包装成Path对象.获取绝对完整路径(把相对路径、`../`这类简写全部展开).=父目录
p = Path(__file__).resolve().parent

# 常用属性
print(p.name)      # 当前文件夹/文件名
print(p.suffix)    # 后缀名（如 .py, .txt）
print(p.parent)    # 上一级目录
print(p.exists())  # 是否存在