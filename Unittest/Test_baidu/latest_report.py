#找出最新（日期最近）的报告
import os
report_dir="./test_report"
lists=os.listdir(report_dir)    #返回一个文件列表
print(lists)

lists.sort(key=lambda fn:os.path.getatime(report_dir+"\\"+fn))  #将返回的列表排序

print("the latest report is "+lists[-1])

file=os.path.join(report_dir,lists[-1])
print(file)

