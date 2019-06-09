#!/usr/bin/env python
# _*_ coding:utf-8 _*_
class MailInfo:
	"邮件信息主体"
	def __init__(self,mailSubject,maildesc,revicer=[],atts=[],msgImages=[]):
		self.mailSubject=mailSubject;
		self.revicer=revicer;
		self.maildesc=maildesc;
		self.atts=atts;
		self.msgImages=msgImages;
	def __str__(self):
		isAtts = '无'
		if len(self.atts) > 0:
			isAtts = '有'
		str = "邮件的标题：%s；接收人：%s；邮件内容：%s；是否有附件：%s" % (self.mailSubject,self.revicer,self.maildesc,isAtts)
		return str;