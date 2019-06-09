#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import time


def printTime(str):
	#打印时间
	print(time.localtime());
	if str != None :
		print("您传入的值为：{}".format(str))
	return str;

printTime('222');


def printMoreStr(name,age,desc=None):
	print("{}的年龄：{}，家庭地址：{}".format(name,age,desc));
	return ;
printMoreStr("张晓梅","22","杭州")

printMoreStr(age="22",name="李磊");

def functionArgs(arg1,*varArgs):
	print(arg1);
	for var in varArgs:
		print(var);
	return ;

functionArgs("zhang",4,56,7,7,8);


newFunction = lambda a,b:a+b;
print(newFunction(1,2))

