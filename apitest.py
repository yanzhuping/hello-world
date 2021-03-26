import unittest
import  time
from iorthoAPI.common.HTMLTestRunner import HTMLTestRunner
import os
from crm_style.function import *
import sys

def run(pattern):
    case_dir = os.path.join(get_fileBasePath(), 'iorthoAPI', 'testcase') #测试用例的路径
    print(case_dir)
    discover = unittest.defaultTestLoader.discover(case_dir, pattern=pattern, top_level_dir=None)
    # current_time = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
    # report_path =os.path.join(get_fileBasePath(), 'iorthoAPI', 'report') +"\\"+ current_time+".html" # 生成测试报告的路径
    report_path =os.path.join(get_fileBasePath(), 'iorthoAPI', 'report',"testreport.html")
    fp = open(report_path, "wb")
    runner = HTMLTestRunner(stream=fp, title=u"自动化测试报告", description=u'接口测试',verbosity=2)
    runner.run(discover)
    fp.close()


run(get_pattern())

"""
执行命令
python apitest.py --pattern=test*.py
python apitest.py --pattern=test_image.py
python apitest.py --pattern=test_personal_center.py
python apitest.py --pattern=test_assistant.py
python apitest.py --pattern=test_makeit.py
"""