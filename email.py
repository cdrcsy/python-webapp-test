#!/usr/bin/env python
# coding:utf-8


from email.Header import Header
from email.MIMEText import MIMEText
from email.utils import parseaddr, formataddr
import smtplib


to_list = ['363733368@qq.com']
stmp_server = "smtp.126.com"
from_addr = "maycn_126@126.com"
stmp_pass = 'maycn_18981925006'


msg = MIMEText('hello,send by Python...', 'plain', 'utf-8')

msg['From'] = Header(u'Python爱好者 <%s>'% from_addr ,'utf-8')
msg['To'] = Header(u'管理员<%s>'% to_list ,'utf-8')
msg['Subject'] = Header(u'来自smtp的问候....','utf-8').encode()

server = smtplib.SMTP(stmp_server,25)
server.set_debuglevel(1)
server.login(from_addr,stmp_pass)
server.sendmail(from_addr,[to_list],msg.as_string())
server.quit()

