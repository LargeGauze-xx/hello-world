# 2026-11-06 周五
# W04 第二课：参数 + return

# ---------- 一、参数：把东西传进去 ----------
def greet(name):
    print("你好，" + name)

greet("主人")
greet("肥鱼")


# ---------- 二、return：把结果递回来 ----------
def add(a, b):
    return a + b

result = add(3, 5)
print(result)


# ---------- 三、练习 ----------
# 写一个函数 max_of(a, b)，返回两个数里较大的那个。
# 在这里写：
def max_of(a,b):
    if a>b:
        return a
    else:
        return b
number=max_of(1,9)
print(number)

def max_of3(a,b,c):
    first=max_of(a,b)
    biggest=max_of(first,c)
    return biggest
print(max_of3(3,6,9))

def square(n):
    return n*n
print(square(4))

def area(w,h):   
    return w*h
print(area(3,5))   