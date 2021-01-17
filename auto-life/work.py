from crm_style.create_crm import *
import sys

t_opt=get_opt(sys.argv[1:])
g_config=get_golobal_config(t_opt.get("env"))

run(g_config.get('username'),g_config.get('password'),g_config.get('url'),
    g_config.get('institutions'),g_config.get('doctorname'),
    g_config.get('i_username'),g_config.get('i_password'),g_config.get('i_url'),
    g_config.get('c_username'),g_config.get('c_password'),g_config.get('c_url'),
    g_config)


#参数来自于crm_style/config_1.ini,自己按需配置
#命令
'''

普通单膜方案：
python work.py --env=iortho_adv --caseid=BC01000032139 --num=3d

普通双膜方案：
python work.py --env=iortho_sit --caseid=C01004535625 --num=3d --dir=0

双膜拔多牙：
python work.py --env=iortho_sit --caseid=C01004163194 --num=3d --dir=1

双膜拔单牙：
python work.py --env=iortho_sit --caseid=C01001338005 --num=3d --dir=2


双膜不拔牙：
python work.py --env=iortho_sit --caseid=C01004163194 --num=3d --dir=5


完整双膜拔牙，符合多重情况：
python work.py --env=iortho_sit --caseid=C01001353046 --num=3d --dir=6

单膜有乳牙
python work.py --env=iortho_sit --caseid=BC01000032106 --num=3d --dir=7

单膜拔多牙：
python work.py --env=iortho_sit --caseid=BC01000032106 --num=3d --dir=3

单膜拔单牙：
python work.py --env=iortho_sit --caseid=C01001351640 --num=3d --dir=4

普通单膜方案：
python work.py --env=iortho_sit --caseid=C01001351640 --num=3d



python work.py --env=iortho_sit --caseid=BC01000032139 --num=质检不合格
python work.py --env=iortho_sit --caseid=C01001352102 --num=质检合格
python work.py --env=iortho_sit --caseid=C01001351639 --num=不收治
python work.py --env=iortho_sit --caseid=C01001321614 --num=文字方案
python work.py --env=iortho_sit --caseid=BC01000031981 --num=结束阶段

python work.py --env=iortho_sit --patientname=yanzp --num=新建硅胶
python work.py --env=iortho_sit --patientname=yanzp --num=新建口内照
python work.py --env=iortho_sit --caseid=C01001341313 --num=中期硅胶
python work.py --env=iortho_sit --caseid=BC01000032139 --num=中期口内照
python work.py --env=iortho_sit --caseid=BC01000032139 --num=病例照片不合格


单膜发货：
python work.py --env=iortho_sit --caseid=BC01000032274 --num=3d --dir=8
#发货之前需要先3D方案且已经批准，单膜发货建议先运行单膜发货创建3D并批准
python work.py --env=iortho_sit --caseid=BC01000032274 --num=发货

python work.py --env=iortho_sit --num=冠军A6本阶段
python work.py --env=iortho_sit --num=冠军A6后续阶段
python work.py --env=iortho_sit --num=冠军非A6
python work.py --env=iortho_sit --num=标准
python work.py --env=iortho_sit --num=儿童
python work.py --env=iortho_sit --num=儿童A6
python work.py --env=iortho_sit --num=儿童加冠军
python work.py --env=iortho_sit --num=儿童加冠军A6

python work.py --env=comfos_sit --num=北京病例



注意：
如果是iortho_sit环境，可以不传入env参数，默认使用该环境
  即：python work.py --caseid=C12345678901 --num=3d --dir=1
  
如果是创建iortho_sit单膜3D方案，可以不传入dir参数，默认创建单膜
  即：python work.py --caseid=C01001261718 --num=3d
  
创建iortho_sit线下病例，也可以不传入patientname参数，默认使用 线下+5位随机数 作为患者姓名
  即：python work.py --num=新建硅胶
'''
