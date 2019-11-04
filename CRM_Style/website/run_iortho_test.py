from CRM_Style.website.test_case.CreateCRM import *
from CRM_Style.website.test_case.model.config import *
import datetime

#提示输入值的格式：x_x_x
#第一个数字：0代表双膜，1代表单膜
#第二个数字：1代表设计阶段，2代表中期1,3代表中期2
#第三个数字：1代表当前阶段的第一个方案，2代表当前阶段的第2个方案
#输入：0_1_1,代表创建的是双膜矫治器的设计阶段的第一个方案，以此类推

#输入：新建硅胶，则创建线下新病例硅胶，需要传入患者名
#输入：新建口内照，则创建线下新病例口内照，需要传入患者名
#输入：中期硅胶，则创建线下中期病例硅胶，需要传入病例序号
#输入：中期口内照，则创建线下中期病例口内照，需要传入病例序号


#输入：质检合格，则创建质检合格报告，需要传入病例序号
#输入：质检不合格，则创建质检不合格报告，需要传入病例序号
#输入：不收治，则创建不收治报告，需要传入病例序号
#输入：文字方案，则创建文字方案报告，需要传入病例序号


#输入：结束阶段，则仅仅只是结束当前病例的阶段

#输入：q ，停止执行


#传参，可以传多个,以英文逗号分隔，如["C1111111","C2222222","C333333333"]

caseid=["C01001254574"]

patientname=["线下request"]    #只有创建新病例阶段的线下病例才需要在此处传参


start_time=datetime.datetime.now()
print("开始时间："+str(start_time))
run(sit_crm_username,sit_crm_password,sit_crm_url,institutions,doctorname,caseid,patientname)
end_time=datetime.datetime.now()
print("结束时间："+str(end_time))
print("运行共耗时(s)："+str((end_time-start_time).seconds))