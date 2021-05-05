# -*- coding:UTF-8 -*-
import random as r
ans = r.randint(1, 99)
min = 0
max = 100
count = 5

# 判定結果變成一個方法
def check(guess, who):
    global min, max
    if guess > ans:
        max = guess
    elif guess < ans:
        min = guess
    else:
        print('%s right answer' % who)
        return True

    return False

while count > 0:
    # 使用者猜
    guess = int(input('(%d). PLEASE INPUT %d ~ %d : ' % (count, min, max)))
    # 檢查 guess 的資料是否在 min 與 max 之間 ?
    if guess <= min or guess >= max:
        print('WRONG NUMBER RANGE')
        continue

    # 判定結果
    if check(guess, "user"):
        break

    # 電腦猜
    guess = r.randint(min+1, max-1)
    print('(%d). PC GUESS %d ~ %d : %d' % (count, min, max, guess))
    # 判定結果
    if check(guess, "PC"):
        break

    # 將 count 減去一次
    count = count - 1