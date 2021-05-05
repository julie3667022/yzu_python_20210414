# -*- coding:UTF-8 -*-

str = ' she sell sea shell on the sea shore '
print(str)
#除去左右空白
str = str.strip()
str = str.lstrip() #去除左邊空白
str = str.rstrip() #去除右邊空白
print(str)
print("string length:",len(str))
print("how many s:", str.count("s"))
print("is there on word", str.find('on'))
print("is there off word", str.find('off'))
print("is there sea word:", "yes" if str.find("sea") >= 0 else "no")
print("is there land word:", "yes" if str.find("land") >= 0 else "no")
print('how many letters:', str.count('') + 1)
#是否都是英文字(a-zA-Z)
#小技巧: 先利用 replace 將中間的空白去除
print('Are they English word:', str.replace(' ', '').isalpha())
print(str[2])
print(str[0:3]) #取出0~3位置的字串(不包含3)
path = 'c:\temp\nba\score.py'
print('URL', path)
#加上r就會顯示原始路徑
path = r'c:\temp\nba\score.py'
print('URL', path)




