text = input()
def text_clean(text):
    #text.split() 按空白的字符拆分，忽略掉空串
    #去除掉了多余空格后就直接用一个空白字符拼接 
    clean_text = " ".join(text.split())
    num_list = [char for char in clean_text if char.isdigit()]
    all_nums = ' '.join(num_list)

    return clean_text,all_nums

if __name__ == "__main__":
     raw_text = input("请输入一段文本")
     cleaned_str,digits = text_clean(raw_text)
     print("===== 清洗后文本 =====")
     print(cleaned_str)
     print("===== 提取到的所有数字 =====")
     print(digits)