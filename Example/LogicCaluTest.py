#!/usr/bin/env python
# _*_ coding:utf-8 _*_

a = 123
b = 5
c = 0

print(a%b)
print(a//b)
print(a**c)

print(a != b)
b**=c
print(b)

if a and b :
	print("两者成立！！")
if not(a or b) :
	print("任何都不能算成立！！")
else:
	print("chengl!!!")

str = 'abcdefg'
list = ['111',19.99,'222']

if 'a' in str or 'b' not in list :
	print('判断通过！！')
elif 'a' not in str :
	print('你说的算')


print('aa'  is not 'aca')
