# -*- coding:UTF-8 -*-
import random as r
while True:
    n = r.randint(1, 100)
    if n % 3 == 0:
        print(n)
        continue # 繼續執行下個迴圈(剩下的程式碼不會執行)
    if n == 50:
        print("exit loop, n=", n)
        break #強制跳離迴圈

