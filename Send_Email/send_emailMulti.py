#给多人发送邮件

import smtplib                          #发送邮件模块
from email.mime.text import MIMEText    #定义邮件内容
from email.header import  Header        #定义邮件标题

smtpserver="smtp.163.com"

user='18017870857@163.com'
password='yzp1993'

sender="18017870857@163.com"
receiver=['1405394548@qq.com','helloyange@126.com']

subject='生日聚会邀请函'
content='<html><h1 style="color:red">本人于下月27号举行生日宴会，地点为上海中心，届时请各位光临</h1></html>'

msg=MIMEText(content,'html','utf-8')
msg['Subject']=Header(subject,'utf-8')
msg['From']=sender
msg['To']=','.join(receiver)  #给多人发送邮件写法

smtp=smtplib.SMTP_SSL(smtpserver,465)
smtp.helo(smtpserver)
smtp.ehlo(smtpserver)
smtp.login(user,password)

print("start send email")
smtp.sendmail(sender,receiver,msg.as_string())
smtp.quit()
print("send email end")
