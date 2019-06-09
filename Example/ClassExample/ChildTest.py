#!/usr/bin/env python
# _*_ coding:utf-8 _*_
from ClassExample.ParentChilds import Parent
import  re

class ChildTest(Parent):
	"模拟子类演示"

	def __showAge(self):
		print("我的年龄是个秘密，但是因为是你，我可以告诉你，我刚好：%s"%self.age);

	def showBoyFriend(self):
		print("你好！");
		self.__showAge();

child = ChildTest('chengr',1);
child.showBoyFriend();
child._ChildTest__showAge()
child._displayCount();
print(Parent.initCount,ChildTest.__doc__);

print(re.match('aa','cccaabb').span())

