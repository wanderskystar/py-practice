def count_text_file(file_path:str):
    line_count = 0
    chinese_count  = 0
    try:
        #with自动关闭文件
        with open(file_path,"r",encoding="utf-8") as  f:
            for line in f:
                line_count +=1
                #遍历每个字符
                for char in  line:
                    #汉字范围
                    if  '\u4e00' <= char <='\u9fff':
                        chinese_count+=1
        print(f"总文件行数：{line_count}")
        print(f"汉字总个数：{chinese_count}")
    except FileNotFoundError:
        print(f"错误！找不到文件{file_path}")
    except Exception as e:
        print(f"发生异常{e}")
    
if  __name__ == "__main__":
    count_text_file(r"D:\code\py-practice\python-threeweek-pra\First-week\test.txt")