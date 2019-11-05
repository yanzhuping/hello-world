from CRM_Style.website.test_case.CreateCRM_1 import *
import sys

t_opt=get_opt(sys.argv[1:])
g_config=get_golobal_config(t_opt.get("env"))

run(g_config.get('username'),g_config.get('password'),g_config.get('url'),g_config.get('institutions'),g_config.get('doctorname'))




#命令
'''
双膜的第1阶段的第1个方案：python main.py --env=iortho_sit --caseid=['xxxxx'] --num=0_1_1
单膜的第1阶段的第1个方案：python main.py --env=iortho_sit --caseid=['xxxxx'] --num=1_1_1

python main.py --env=iortho_sit --caseid=Cxxxxxxx --num=质检不合格
python main.py --env=iortho_sit --caseid=Cxxxxxxx --num=质检合格
python main.py --env=iortho_sit --caseid=Cxxxxxxx --num=不收治
python main.py --env=iortho_sit --caseid=Cxxxxxxx --num=文字方案
python main.py --env=iortho_sit --caseid=Cxxxxxxx --num=结束阶段

python main.py --env=iortho_sit --patientname=yanzp --num=新建硅胶
python main.py --env=iortho_sit --patientname=yanzp --num=新建口内照

注意：
如果是iortho_sit环境，可以不传入env参数，默认使用该环境
创建线下病例，也可以不传入patientname参数，会使用 线下+5位随机数 作为患者姓名
如果是创建双膜的第一阶段的第一个病例，也不用传入num参数 ，默认创建双膜设计阶段第一个3D方案

'''
