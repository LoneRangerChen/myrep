#!/usr/bin/env python
# _*_ coding:utf-8 _*_

tup1 = 'a',1,5,'nbn'
print(tup1)

tup2 = ('中国','new world')
tup3 = tup1+tup2
print(tup3,id(tup1),id(tup3))

print(max(tup2))