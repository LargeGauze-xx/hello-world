scores=[85,92,78,90,88]
total=0
for s in scores:
    total=total+s
scores1=total
scores2=total/len(scores)
scores.sort()
scores3=scores[-1]
print(f"总分:{scores1}")
print(f"平均分:{scores2}")
print(f"最高分:{scores3}")
