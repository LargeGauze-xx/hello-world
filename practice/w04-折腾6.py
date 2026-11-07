low = 1
high = 100
count = 0

while low <= high:
    mid = (low + high) // 2
    count += 1
    print(f"第 {count} 次，我猜：{mid}")
    ans = input("大了输1，小了输2，对了输3：")

    if ans == "3":
        print(f"猜中啦！用了 {count} 次")
        break
    elif ans == "1":      # 我猜大了 → 答案比 mid 小
        high = mid - 1
    else:                 # 我猜小了 → 答案比 mid 大
        low = mid + 1