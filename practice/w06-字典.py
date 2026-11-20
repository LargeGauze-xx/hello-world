# 2026-11-17 周二
# W06 第一课：字典入门

# 字典 = 一堆「键: 值」的对，用花括号装
scores = {"小明": 85, "小红": 95, "小刚":78,"肥鱼":0}

# 取值：用键去拿，不是用下标
print(scores["小明"])
print(scores["小红"])
print(scores["小刚"])
print(scores["肥鱼"])

person = {"名字": "肥鱼", "年龄": 3, "技能": "陪主人学Python"}
person["年龄"] = 4
person["主人"] = "星莘"
del person["技能"]
print(person["名字"])
print(person["年龄"])
print(person.get("技能", "已经删掉了"))
for k, v in person.items():
    print(k, "=", v)

text="abca"
count={}
for sh in text:
    if sh in count:
        count[sh]=count[sh] + 1
    else:count[sh]=1
print(count)
