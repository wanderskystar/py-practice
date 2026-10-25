import re
def extract_num():
    input_file = "note.txt"
    output_file = "numbers_result.txt"
    content = ""#提前初始化变量，解决UnboundLocalError
    try:
        with open(input_file,"r",encoding="utf-8") as f:
            content = f.read()
    except FileNotFoundError:
        print(f"错误：找不到文件{input_file},请把txt放到脚本同目录!")
        return  # 找不到文件直接退出函数，不再往下执行
    #编译正则表达式
    pattern = re.compile(r"\d+")

    num_list = pattern.findall(content)

    #写入新文件一行放一个数字
    with open(output_file,"w",encoding="utf-8") as f:
        for num in num_list:
            f.write(num+"\n")

    print(f"提取完成！一共找到 {len(num_list)} 组数字，结果保存在 {output_file}")

if __name__ == "__main__":
    extract_num()