# 判断奇偶数：% 是取余数，== 0 说明除得尽
num=int(input("输入一个数字"))
if num%2==0:
    print(f"{num}是偶数")
else:
    print(f"{num}是奇数")

# 嵌套示例：外层 if 成立后，里面再判断
x=15
if x > 0:
    print("正数")    
    if x > 10:    # ← 这个 if 整个都属于外层 if 的「子代码」     
        print("很大")