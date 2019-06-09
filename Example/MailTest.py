#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr

my_sender = 'chen.fei@sunyard.com'
my_passwd = 'Fei823666'
my_revicer = '1017352852@qq.com'

def baseMail():
	ret = True;
	try:
		msg = MIMEText('你好，我是PT机器人！','plain','utf-8');
		msg['From'] = formataddr(["PTruboot",my_sender]);
		msg['To'] = formataddr(['FK',my_revicer]);
		msg['Subject'] = "Python测试发送邮件"

		server = smtplib.SMTP_SSL('smtp.sunyard.com',465);
		server.login(my_sender, my_passwd);
		server.sendmail(my_sender, [my_revicer, ], msg.as_string())
		server.quit();
	except Exception:
		ret = False;
	return ret;
ret = baseMail();
if ret:
	print("邮件发送成功！")
else:
	print("邮件发送失败！")

