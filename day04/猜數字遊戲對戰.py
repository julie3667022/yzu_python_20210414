# -*- coding:UTF-8 -*-
'''
# 0~100之間(猜一數字,不含0與100)
遊戲進行 ...
'''

# ans = 47 #指定答案

# 隨機挑選
import random as r
ans = r.randint(1, 99)
min = 0
max = 100
count = 5

while count > 0:
    guess = int(input('Please input %d ~ %d:' % (min, max)))
    #檢查guess的資料是否在min與max之間?
    if guess <= min or guess >= max:
        print("xxx This number is out of range xxx")
        continue
    #將 count - 1
    count = count - 1
    # 判定結果
    if guess > ans:
        max = guess
    elif guess < ans:
        min = guess
    else:
        print("Congratulation!You got the right answer!!")
        break