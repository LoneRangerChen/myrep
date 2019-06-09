#!/usr/bin/env python
# _*_ coding:utf-8 _*_
x = 10
expr = """
list1 = []
list1.append('aaa')
list1.append(12.33)
print(list1)

del list1[1]
print(len(list1))

other = ['ss',19.99]

list1+=other
print(len(list1))

for index in list1 :
	print('数值：{0}'.format(index))
at = (111,'222','444')
alist = list(at)
print(id(alist),id(list(at)),alist)
alist.reverse();
print(alist)

bList = ['dadad','daasda','fffs']
bList.sort()
print(bList)
"""

exec(expr)