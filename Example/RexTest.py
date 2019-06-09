#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import  re

print(re.match("aaa",'aaaabbbccc').span())

print(re.search("aaa",' aaaabbbccc').span())

line = "Cats are smarter than dogs"

matchObj = re.match(r'(.*) are (.*?) .*', line, re.M | re.I)
if matchObj:
   print("matchObj.group() : ", matchObj.group())
   print("matchObj.group(1) : ", matchObj.group(1))
   print("matchObj.group(2) : ", matchObj.group(2))
else:
   print ("No match!!")


