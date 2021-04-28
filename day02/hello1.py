# -*- coding:UTF-8 -*-
import keyword

print(keyword.kwlist)


print("我是中文")





score = 40
if score >= 60:
    print(score, '及格')
else:
    print(score, '不及格')

#整數8, 10, 16進位
a = 12  # 10進位
b = 0o12  # 8進位
c = 0x12  # 16進位
print(a, b, c)

# 浮點數
a = 3.14
b = 3.14e2  #科學記號: 3.14e2 -> * 10**2(二次方)
c = 1000e-2  #科學記號: 3.14e2 -> * 1/10**2(二次方)
print(a, b, c)

# 賦質(=)
name, h, w, age, isPass= 'John', 170.5, 60, 18, True
print(name, h, w, age, isPass)

#資料型態(type)
print(name, type(name))
print(h, type(h))
print(w, type(w))
print(age, type(age))
print(isPass, type(isPass))

# 刪除變數
money = 1000000
print(money)
del money
print(money)
