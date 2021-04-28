# -*- coding:UTF-8 -*-
import random as r # 給r一個別名
n = r.randint(1, 99)
result = "偶數" if n % 2 == 0 else "奇數" #如果n/2餘數是0，其餘奇數
print(n, result)
print(str(n) + "是" + result)

