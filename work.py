from CRM_Style.website.test_case.CreateCRM_1 import *
import sys

t_opt=get_opt(sys.argv[1:])
g_config=get_golobal_config(t_opt.get("env"))

run(g_config.get('username'),g_config.get('password'),
    g_config.get('url'),g_config.get('institutions'),
    g_config.get('doctorname'))

#命令
'''
双膜的第1阶段的第1个方案：python work.py --env=iortho_sit --caseid=C01001265453 --num=3d --dir=1
单膜的第1阶段的第1个方案：python work.py --env=iortho_sit --caseid=C12345678901 --num=3d

python work.py --env=iortho_sit --caseid=Cxxxxxxx --num=质检不合格
python work.py --env=iortho_sit --caseid=Cxxxxxxx --num=质检合格
python work.py --env=iortho_sit --caseid=Cxxxxxxx --num=不收治
python work.py --env=iortho_sit --caseid=Cxxxxxxx --num=文字方案
python work.py --env=iortho_sit --caseid=Cxxxxxxx --num=结束阶段

python work.py --env=iortho_sit --patientname=yanzp --num=新建硅胶
python work.py --env=iortho_sit --patientname=yanzp --num=新建口内照

注意：
如果是iortho_sit环境，可以不传入env参数，默认使用该环境
  即：python work.py --caseid=C12345678901 --num=3d --dir=1
  
如果是创建单膜3D方案，可以不传入dir参数，默认创建单膜
  即：python work.py --caseid=C12345678901 --num=3d
  
创建线下病例，也可以不传入patientname参数，默认使用 线下+5位随机数 作为患者姓名
  即：python work.py --num=新建硅胶
'''
