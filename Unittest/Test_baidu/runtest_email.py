import unittest
from BSTestRunner import BSTestRunner
import time
import smtplib
from email.mime.text import MIMEText
from email.header import Header
import os

def send_mail(latest_report):
    f=open(latest_report,'rb')
    mail_content=f.read()
    f.close()

    smtpserver = 'smtp.163.com'

    user = '18017870857@163.com'
    password = 'yzp1993'

    sender = '18017870857@163.com'
    receives = ['helloyange@126.com', '1405394548@qq.com']

    subject = 'Web Selenium 结果周报'
    # content = '<html><h1 style="color:red">我要自学网，自学成才！</h1></html>'

    msg = MIMEText(mail_content, 'html', 'utf-8')
    msg['Subject'] = Header(subject, 'utf-8')
    msg['From'] = sender
    msg['To'] = ','.join(receives)

    smtp = smtplib.SMTP_SSL(smtpserver, 465)
    smtp.helo(smtpserver)
    smtp.ehlo(smtpserver)
    smtp.login(user, password)

    print("Start send email...")
    smtp.sendmail(sender, receives, msg.as_string())
    smtp.quit()
    print("Send email end!")

def latest_report(report_dir):
    lists = os.listdir(report_dir)
    print(lists)

    lists.sort(key=lambda fn: os.path.getatime(report_dir + '\\' + fn))

    print("the latest report is " + lists[-1])

    file = os.path.join(report_dir, lists[-1])
    print(file)
    return file

if __name__ == '__main__':
    report_dir='./test_report'
    test_dir = './test_case'

    discover = unittest.defaultTestLoader.discover(test_dir, pattern="test*.py")
    now=time.strftime("%Y-%m-%d %H_%M_%S")
    report_name=report_dir+'/'+now+'result.html'

    with open(report_name,'wb') as f:
        runner=BSTestRunner(stream=f,title="Test Report",description="baidu search")
        runner.run(discover)
    f.close()

    latest_report=latest_report(report_dir)
    send_mail(latest_report)