import smtplib                         #发送邮件模块
from email.mime.text import MIMEText   #定义邮件内容
from email.header import Header        #定义邮件标题

smtpserver="smtp.126.com"
user="helloyange@126.com"
password="test123"

sender="helloyange@126.com"
receive="1405394548@qq.com"

subject="时代天使中秋节放假通知"
content='<html><h1 style="color:red">放假时间为2019年9月10号，共3天，请各位吃好玩好</h1></html>'

msg=MIMEText(content,'html','utf-8')
msg['Subject']=Header(subject,'utf-8')
msg['From']=sender
msg['To']=receive

smtp=smtplib.SMTP_SSL(smtpserver,465)
smtp.helo(smtpserver)
smtp.ehlo(smtpserver)
smtp.login(user,password)

print("Stard send Email.......")
smtp.sendmail(sender,receive,msg.as_string())
smtp.quit()
print("Send Email End!!!")