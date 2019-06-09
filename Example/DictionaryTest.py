#!/usr/bin/env python
# _*_ coding:utf-8 _*_
dict1 = {'Name': 'Zara', 'Age': 7};
dict2 = {'Name': 'Mahnaz', 'Age': 27};
dict3 = {'Name': 'Abid', 'Age': 27};
dict4 = {'Name': 'Zara', 'Age': 7};
print ("Return Value : %d" %  dict1.__eq__(dict2))

print(str(dict1.copy()))

dict1 = {"name":dict2,"old":dict3,"other":{"name":dict2,"se1":dict4,"oit":{'ot':dict4}}}
print(len(dict1))
print(dict1.copy())

