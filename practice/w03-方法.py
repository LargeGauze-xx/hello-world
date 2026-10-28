# 2026-10-28 周三
# 练习：倒序 / 去重 / 找第二大

scores = [85, 92, 78, 90, 88]
scores.sort(reverse=True)
print(scores)

nums=[3,1,3,2,1]
result=[]
for num in nums:
    if not num in result:
        result.append(num)
print(result)

scores = [85, 92, 78, 92, 88]
temp_score=[]
for score in scores:
    if not score in temp_score:
        temp_score.append(score)
temp_score.sort()
print(temp_score[-2])