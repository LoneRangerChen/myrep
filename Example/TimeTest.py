#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import time
import calendar
import datetime

localtime = time.localtime(time.time())
print(localtime)

print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime()))

print(calendar.month(2030,1))

print(time.timezone)

print(calendar.firstweekday())

print(calendar.isleap(2012),calendar.calendar(2018,w=2,l=1,c=6))

print(calendar.month(2018,6,w=2))

print(calendar.monthcalendar(2019,6))

print(time.gmtime(),calendar.timegm(time.gmtime()))
currntTime = time.gmtime()
print(calendar.weekday(currntTime.tm_year,currntTime.tm_mon,currntTime.tm_mday))

print(type(datetime.datetime.now()))

print(type((datetime.date(2019,5,6)+datetime.timedelta(days=-6)).strftime('%Y-%m-%d %H:%M:%S')))
