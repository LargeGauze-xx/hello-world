#  成绩等级：elif 是 else if 的缩写，三个分支互斥
score = int(input("输入成绩："))
if score >= 90:
    print("优秀")
elif score >= 60:
    print("及格")
else:
    print("不及格")