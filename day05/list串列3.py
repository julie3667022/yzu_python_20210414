# -*- coding:UTF-8 -*-
#append, insert, extend
scores = [20, 30, 10]
scores.append(50)
print(scores)
scores.insert(0, 10)
print(scores)
scores.append([70, 75, 79]) #用append會變持二維值
print(scores[5][0])
scores.extend([80, 82]) #用extend才會是一維值(直接在後面增加數值)
print(scores)
