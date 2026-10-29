from datetime import datetime

def write_log(event_msg:str):

    now = datetime.now().strftime("%Y-%m-%d: %H-%M-%S")
    log_line = f"[{now}]: [{event_msg}]"

    with open("log_txt","w",encoding="utf-8") as f:
        f.write(log_line)
    
print("✅ 日志已经写入：", log_line.strip())

if __name__ == "__main__":
    # 脚本启动时自动记录【脚本启动事件】
    write_log("脚本开始运行")

    # 示例：
    write_log("执行读取文件操作")
    write_log("数据处理完成")

    # 脚本结束记录
    write_log("脚本执行结束\n")