#这是sit环境的运行文件



from Auto_iortho.driver import HTMLTestRunner
from Auto_iortho.website.test_case.test_case import *
from time import strftime

print("start test..")

input_name=readDataFromMySQL(host,mysqluser,mysqlpasswd,dbName,tableName)


suite = unittest.TestSuite()
suite.addTest(
    ParametrizedTestCase.parametrize(
        standard_process,param=input_name,param1=username,
        param2=password,param3=url,param4=crm_username,param5=crm_password,param6=crmurl))


report_dir='./test_report'

now = strftime("%Y-%m-%d %H_%M_%S")
report_name=report_dir+'/'+now+'result.html'

print("start write report..")
f=open(report_name,'wb')
runner=HTMLTestRunner.HTMLTestRunner(stream=f,title="Test Report")

runner.run(suite)
f.close()

# sleep(1)
#
# print("find latest report")
# latest_report=latest_report(report_dir)
#
# print("send email report..")
# send_mail(latest_report,e_server,e_user,e_password,e_sender,e_receives)

# send_mail_attachment(latest_report,e_server,e_user,e_password,e_sender,e_receives)  #发送带附件的邮件

print("Test end")
