# -*- coding:UTF-8 -*-
# x*y=z
# 1*1=1 1*2=2 ... 1*9=9
# 2*1=2 2*2=4 ... 2*9=18
# ...
# 9*1=9 9*2=18 ... 9*9=81

n = int(input('please input nine tables size: ')) + 1 # 加上一因為(1, n)不包含n
for x in range(1, n):
    for y in range(1, n):
        z = x * y
        print("%2d*%-2d=%3d" % (x, y, z), end=" ")
    print()
