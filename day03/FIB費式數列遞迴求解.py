# -*- coding:UTF-8 -*-
def f(n):
    if n == 0 or n == 1:
        return n


    return f(n - 1) + f(n - 2)

n = 30
value = f(n)
print(n, value)


# 課堂測試
n = 3*1**3
print(n)
n = 9//2
print(n)
x = 6/2*(1 + 2)
print(x)

x = True
y = False
z = False
if not x or y:
    print(1)
elif not x or not y and z:
    print(2)
elif not x or y or not y and x:
    print(3)
else:
    print(4)

# 雞兔同籠:雞加兔子共有 83 隻,雞的腳加上兔子的腳
# 共有 240 隻腳,求雞與兔子各有幾隻?
def getChickenAndRabbit(sum, feet):
    if feet/4 <= sum <= feet/2:
        rabbit = (feet - sum * 2)/2
        chicken = sum - rabbit
        return chicken, rabbit
    else:
        print('無法計算')
        return 0, 0

print(getChickenAndRabbit(83, 240))
c, r = getChickenAndRabbit(83, 240)
print(c, r)





