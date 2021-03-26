import os
import smtplib
from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def latest_report(report_dir):
    lists = os.listdir(report_dir)
    print(lists)

    lists.sort(key=lambda fn: os.path.getatime(report_dir + '\\' + fn))

    print("the latest report is " + lists[-2])

    file = os.path.join(report_dir, lists[-2])

    return file


def send_mail_attachment(latest_report,e_server,e_user,e_password,e_sender,e_receives):

    smtpserver = e_server

    user = e_user
    password = e_password #这是客户端授权码，根据自己邮箱密码来设置

    sender = e_sender
    receives = e_receives

    subject = 'Web Selenium 自动化测试报告'   #邮件标题

    f = open(latest_report, 'rb')
    mail_content = f.read()        #需要发送的正文
    f.close()

    send_file=open(latest_report,'rb').read()  #需要发送的附件

    att=MIMEText(send_file,'base64','utf-8')
    att['Content-Type']='application/octet-stream'
    att['Content-Disposition'] = "attachment;filename='%s'"%(latest_report)

    msgRoot = MIMEMultipart()
    msgRoot.attach(MIMEText(mail_content, 'html', 'utf-8'))
    msgRoot['Subject'] = subject
    msgRoot['From'] = sender
    msgRoot['To'] = ','.join(receives)
    msgRoot.attach(att)


    smtp = smtplib.SMTP_SSL(smtpserver, 465)
    smtp.helo(smtpserver)
    smtp.ehlo(smtpserver)
    smtp.login(user, password)

    print("Start send email...")
    smtp.sendmail(sender, receives, msgRoot.as_string())
    smtp.quit()
    print("Send email end!")