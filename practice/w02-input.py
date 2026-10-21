# input() 会停下来等你打字，返回的永远是字符串
name=input("你叫什么名字？")
# 年龄要拿来算数，所以用 int() 把字符串转成整数
age=int(input("你多大了？"))
# f-string：f 是开关，{} 是插槽，里面会换成变量的值
print(f"你好，{name}！你今年{age}岁。")
print(f"明年你就{age+1}岁了")
