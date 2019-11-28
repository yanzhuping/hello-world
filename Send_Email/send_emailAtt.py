#发送带附件的邮件

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


smtpserver="smtp.163.com"

user='18017870857@163.com'
password='yzp1993'

sender="18017870857@163.com"
receiver=['1405394548@qq.com','helloyange@126.com']
# receiver="1405394548@qq.com"

subject='上班的安排，请知悉'
content='<html><h1 style="color:red">请大家明天7点准时到公司，因为明天要开早会，不要迟到,面向全体员工</h1></html>'

send_file=open(r"C:\Users\admin\Desktop\caseid.txt","rb").read()

att=MIMEText(send_file,"base64","utf-8")
att['Content-Type']='application/octet-stream'
att['Content-Disposition']="attachment;filename='caseid.txt'"

msgRoot=MIMEMultipart()
msgRoot.attach(MIMEText(content,'html','utf-8'))
msgRoot['Subject']=subject
msgRoot['From']=sender
msgRoot['To']=','.join(receiver)
# msgRoot['To']=receiver
msgRoot.attach(att)

smtp=smtplib.SMTP_SSL(smtpserver,465)
smtp.helo(smtpserver)
smtp.ehlo(smtpserver)
smtp.login(user,password)

print("start send email")
smtp.sendmail(sender,receiver,msgRoot.as_string())
smtp.quit()
print("send email end")


