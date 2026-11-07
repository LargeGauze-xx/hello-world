# 2026-11-07 周六
# W04 项目：猜数字游戏（第一段：只猜一次）

import random

# 让电脑随便想一个 1 到 100 之间的数
secret = random.randint(1, 100)
count=0
# 你来猜一个
while True:
    if count >=7:
        print("次数用完了，答案是",secret)
        break
    guess = int(input("猜一个："))
    count = count + 1
    if guess > secret:
        print("大了")
    elif guess < secret:
        print("小了")
    else:
        print("猜对了！")
        break
