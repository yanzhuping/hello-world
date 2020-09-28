import unittest
import  time
from iorthoAPI.common.HTMLTestRunner import HTMLTestRunner
# from iorthoAPI.sendEmail.send_email import *
import os


def run_case(dir = "testcase"):
    case_dir = os.getcwd() + "\\" + dir
    print(case_dir)
    test_case = unittest.TestSuite()
    # discover = unittest.defaultTestLoader.discover(case_dir,pattern="testcase1.py",top_level_dir=None)
    discover = unittest.defaultTestLoader.discover(case_dir,pattern="test*.py",top_level_dir=None)
    return discover


if __name__ == '__main__':
    current_time = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
    report_path =os.getcwd() + "\\report\\" + current_time + '.html'  # 生成测试报告的路径
    print(report_path)
    fp = open(report_path, "wb")
    runner = HTMLTestRunner(stream=fp, title=u"自动化测试报告", description=u'接口测试',verbosity=2)
    runner.run(run_case())
    fp.close()

    # time.sleep(1)
    #
    # e_server = 'smtp.126.com'  # 邮件发送协议，测试邮箱是网易126邮箱
    #
    # e_user = 'helloyange@126.com'
    #
    # e_password = 'test123'  # 客户端授权码
    #
    # e_sender = 'helloyange@126.com'
    #
    # e_receives = ['1405394548@qq.com']  # 接收者，可以传入多个
    #
    # print("find latest report")
    # latest_report = latest_report(report_path)
    #
    # print("send email report..")
    # # send_mail(latest_report,e_server,e_user,e_password,e_sender,e_receives)
    #
    # send_mail_attachment(latest_report,e_server, e_user, e_password, e_sender, e_receives)  # 发送带附件的邮件
    #
    # print("Test end")