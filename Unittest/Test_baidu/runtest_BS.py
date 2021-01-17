from BSTestRunner import BSTestRunner
import unittest
import time

test_dir="./test_case"
discovery=unittest.defaultTestLoader.discover(test_dir,pattern="test*.py")

if __name__ == '__main__':
    report_dir="./test_report"
    now=time.strftime("%Y-%m-%d %H_%M_%S")
    report_name=report_dir+"/"+now+"_result.html"

    with open(report_name,"wb")as f:
        runner=BSTestRunner(stream=f,title="Test report",description="test case report")
        runner.run(discovery)
    f.close()