#!/usr/bin/env python
# _*_ coding:utf-8 _*_

class Parent:
	"模拟父类演示类"
	initCount = 0;

	def __init__(self,name,age):
		self.name=name;
		self.age=age;
		Parent.initCount += 1;

	def _displayCount(self):
		print("Total Created Parent %d" % Parent.initCount)

	def showName(self):
		print("My Name: %s" % self.name);
parent = Parent("chenxiao",13);
parent._displayCount();
parent.showName();