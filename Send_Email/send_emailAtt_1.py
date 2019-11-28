import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

smtpserver='smtp.163.com'

user = '18017870857@163.com'
password = 'yzp1993'

sender = '18017870857@163.com'
receives = ['helloyange@126.com', '1405394548@qq.com']

subject='Web Selenium 自动化测试报告'
content='<html><h1 style="color:red">我要自学网，自学成才！</h1></html>'

send_file=open(r"C:\Users\admin\Desktop\caseid.txt","rb").read()

att=MIMEText(send_file,'base64','utf-8')
att['Content-Type']='application/octet-stream'
att['Content-Disposition']="attachment;filename='caseid.txt'"


msgRoot=MIMEMultipart()
msgRoot.attach(MIMEText(content,'html','utf-8'))
msgRoot['Subject']=subject
msgRoot['From']=sender
msgRoot['To']=','.join(receives)
msgRoot.attach(att)

smtp=smtplib.SMTP_SSL(smtpserver,465)
smtp.helo(smtpserver)
smtp.ehlo(smtpserver)
smtp.login(user,password)

print("Start send email...")
smtp.sendmail(sender,receives,msgRoot.as_string())
smtp.quit()
print("Send email end!")



