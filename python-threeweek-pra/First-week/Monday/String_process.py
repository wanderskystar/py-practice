text = input()
def clean_text(text):
    #text.split() 按空白的字符拆分，忽略掉空串
    #去除掉了多余空格后就直接用一个空白字符拼接 
    text = " ".join(text.split())
    