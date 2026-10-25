#文件名：time_demo.py
#功能:    datetime时间库示例，获取当前时间、计算两个日期相差天数、格式化输出日志样式时间
#学习点：  datetime.now()       datetime(年,月,日)相减      %Y-%m-%d %H:%M:%S

from datetime import  datetime
def time_demo():
    now_time = datetime.now()
    print(f"当前时间{now_time}")

    date_1 = datetime(2008,1,8)
    date_2 = datetime(2029,7,1)

    delta = date_2-date_1
    print(f"相差{delta.days}天")
    log_str = now_time.strftime("%Y-%m-%d %H:%M:%S")
    print("日志格式时间：", log_str)


if __name__ == "__main__":
    time_demo()
