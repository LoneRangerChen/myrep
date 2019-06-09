#!/usr/bin/env python
# _*_ coding:utf-8 _*_

# fileoi = open('test.txt',"r",encoding="utf-8")
# print(fileoi.name)
# print(fileoi.mode)
# fileoi.write("你好吗大本打\n");
# fileoi.write("aaaani\n");
# fileoi.flush();
with open('test.txt',"r",encoding="utf-8") as fileoi:
	while True :
		line = fileoi.readline();
		if not line :
			break;
		print(line);

# if not fileoi.closed :
# 	fileoi.close();

try:
	fh = open("testfile", "r")
	try:
		fh.write("这是一个测试文件，用于测试异常!!")
	finally:
		print("关闭文件")
		fh.close()
except IOError as arg1:
	print("Error: 没有找到文件或读取文件失败",arg1);
else:
    print ("内容写入文件成功")
    fh.close();
finally:
	fh.close();

# def testException(index):
# 	if(not index):
# 		raise Exception("错误呜呜呜威威",index);
#
# testException('')