#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import smtplib
from email.header import Header
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import formataddr

from ClassExample.MailInfo import MailInfo


class MailSend:
	"邮件发送脚本"
	server_name,ser_pass = 'chen.fei@sunyard.com','Fei823666'

	#发送邮件（SMTP协议）
	def sendSMTPMail(self,mailInfo,server_addr='smtp.sunyard.com',post=465):
		ret = True;
		try:
			if not mailInfo.mailSubject:
				print("邮件标题为空，非法发送")
				return
			msgRoot = MIMEMultipart('related')
			msgRoot['From'] = Header(MailSend.server_name, 'utf-8')
			msgRoot['From'] = formataddr(["PTruboot", MailSend.server_name]);
			msgRoot['To'] = formataddr(['FK', mailInfo.revicer.__str__()]);
			subject = mailInfo.mailSubject
			msgRoot['Subject'] = Header(subject, 'utf-8')

			msgAlternative = MIMEMultipart('alternative')
			msgRoot.attach(msgAlternative)

			mail_info = mailInfo.maildesc
			msgAlternative.attach(MIMEText(mail_info, 'html', 'utf-8'))

			self.sendMsg(mailInfo.msgImages,msgRoot)

			self.sendAttrs(mailInfo.atts,msgRoot)

			#SMTP邮件发送
			server = smtplib.SMTP_SSL(server_addr, post);
			server.login(MailSend.server_name, MailSend.ser_pass);

			if len(mailInfo.revicer)<=0:
				print("邮件接受人为空，无法发送")
				return
			server.sendmail(MailSend.server_name, mailInfo.revicer, msgRoot.as_string())
			server.quit();
			mailInfo.__str__();
		except Exception as evt:
			print(evt)
			print(mailInfo.__str__())
			ret = False;
		return ret;

	#添加图片
	def sendMsg(self,mailMsgs,msgRoot):
		if mailMsgs and len(mailMsgs)>0:

			for index in range(len(mailMsgs)):
				msg = mailMsgs[index]

				# 指定图片为当前目录
				fp = open( 'E:\\我的女王\\'+msg , 'rb')
				msgImage = MIMEImage(fp.read())
				fp.close()

				# 定义图片 ID，在 HTML 文本中引用
				msgImage.add_header('Content-ID', '<%s>'% ('msg'+str(index)))
				msgRoot.attach(msgImage)
				del msg

	#添加附件
	def sendAttrs(self,atts,msgRoot):
		if atts and len(atts)>0:
			for att in atts :
				# 构造附件1，传送当前目录下的 test.txt 文件
				fb=open('E:\\我的女王\\' + att, 'rb')
				att1 = MIMEText(fb.read(), 'base64', 'utf-8')
				fb.close()
				att1["Content-Type"] = 'application/octet-stream'
				# 这里的filename可以任意写，写什么名字，邮件中显示什么名字
				att1["Content-Disposition"] = 'attachment; filename="%s"'%att
				msgRoot.attach(att1)

maildesc = '''
		<p>Python 邮件发送测试...</p>
		<p>图片演示：</p>
		<p><img src="cid:msg0"></p>
'''
mailInfo=MailInfo("Python测试发送邮件",maildesc,['1017352852@qq.com',],['IMG_20160314_171031.jpg','IMG_20160314_153910.jpg'],['IMG_20160314_171031.jpg',])

mail = MailSend()
ret = mail.sendSMTPMail(mailInfo)
if ret:
	print("邮件发送成功！")
else:
	print("邮件发送失败！")
