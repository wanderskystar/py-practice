import os
while  True:
    print("-----备忘录系统-----");
    print("1.新增备忘录");
    print("2.查看全部备忘录");
    print("3.退出程序");
    #print("请选择您要进行的功能：")
    choice = input("请输入您的选择(1/2/3) \n")
    script_dir =  os.path.dirname(os.path.abspath(__file__))
    parent_dir = os.path.dirname(script_dir)
    file_path = os.path.join(parent_dir,"memofile")
    if choice  ==  "3":
        break
    elif choice == "2":
        try:
            with open(file_path,"r",encoding = "utf-8") as f:
                all_text = f.read()     
                print("\n------历史备忘录")
                print(all_text)
        except FileNotFoundError:
            print("备忘录还未创建")
    elif choice == "1":
        content = input("请输入您要保存的内容：\n")
        with open(file_path,"a",encoding="utf-8") as f:
            f.write(content+"\n")
            print("保存成功！\n")
    
