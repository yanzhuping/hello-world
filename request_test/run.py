import unittest
from BSTestRunner import BSTestRunner
import time

test_dir="./test_case"
report_dir="./reports"

#加载测试用例
discover=unittest.defaultTestLoader.discover(test_dir,pattern="weather_api_unittest.py")

#运行测试用例并生成报告
now=time.strftime("%Y-%m-%d %H_%M_%S")
report_name=report_dir+"/"+now+"_test_report.html"
with open(report_name,"wb")as f:
    runner = BSTestRunner(stream=f,title="weather api test report",description="China weather test report")

    runner.run(discover)