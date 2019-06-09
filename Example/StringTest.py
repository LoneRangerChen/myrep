#!/usr/bin/env python
# _*_ coding:utf-8 _*_

str = r'大江东去浪淘尽\n'\
	'千古江山无尽游'
print(str)

class AssignValue(object):
    def __init__(self, value):
        self.value = value
my_value = AssignValue(6)
print('value 为: {0.value}'.format(my_value))

print("你的名字：%s;性别：%s;年龄：%d"%('勃朗特','女',101))

site = {"name": "111", "url": "www.11.com"}
print("网站名：{name}, 地址 {url}".format(**site))

print('{:a<5d}'.format(10))

print(u'Hello\u0020World !')

print('jey'.capitalize().center(20))

print('列夫托尔斯泰'.encode(encoding='GBK',errors='strict'))

astr = '列夫托尔斯泰'.encode(encoding='GBK',errors='strict')
print(astr.decode(encoding='GBK',errors='strict').find('泰'))

print("aqq 22".isalnum())

print('adasdsadas1'.isalpha())

print('a,b,223,ddd,55'.split(','))

print('welcome to china'.title().lower().replace(' ','').upper().rjust(100))





