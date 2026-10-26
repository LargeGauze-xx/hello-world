fruits=["苹果","香蕉","橙子"]
print(fruits[0])
print(fruits[-1])
print(len(fruits))

fruits.append("葡萄")
print(fruits)
fruits[0]="西瓜"
print(fruits)
fruits.remove("香蕉")
print(fruits)

fruits=["苹果","香蕉","橙子"]
for fruit in fruits:
    print(fruit)
print("香蕉" in fruits)
print("西瓜" in fruits)

fruits=["苹果", "香蕉", "橙子", "葡萄"]
print(fruits[1:3])
print(fruits[:2])
print(fruits[-2:])

numbers=[5,2,8,1,9]
numbers.sort()
print(numbers)